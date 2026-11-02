"""Current R14 semantic/design checks; no real appointment or platform-control claim."""
from pathlib import Path
from copy import deepcopy
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL = {'docs/reform-evidence.md', 'docs/readiness-v1-1.md', 'docs/usability-v1-2.md', 'docs/migration-report.md'}

def check_coverage(model):
    assert model['ratified'] is False and model['actual_appointments_verified'] is False
    for n, people in model['models'].items():
        ids = {p['id']: p for p in people}
        apps = model['office_appointments'][n]
        holders = {a['person'] for a in apps}
        assert len(holders) == len(apps), 'Office workload combined without explicit model'
        for a in apps:
            p = ids[a['person']]
            assert a['actual_adopted'] is False
            assert p['office_hours'] == a['hours']
            assert p['office_hours'] + p['delivery_hours'] <= 6, 'Unfunded Office hours'
            assert p['grade'] >= (4 if a['role'] == 'Planning Lead' else 5)
            assert p['home'] != 'oversight', 'Protected/operating role combination'
            if not a['concurrent']: assert p['manager'] == 'coo'
        for p in people:
            if p['role'] in ('Division Head', 'Technical Lead'):
                assert p['manager'] == 'coo', 'Hidden Office reporting intermediary'
        assert not holders.intersection(model['council']), 'Office voting seat'
        s = model['succession'][n]
        assert not s['actual_signed'] and s['primary'] != s['reserve']
        for key in ['primary', 'reserve']:
            assert 'acting COO scenario assessment' in ids[s[key]]['qualifications']
        assert len(set(model['adjudicator_pools'][n])) >= 2
        for pid in model['adjudicator_pools'][n]:
            assert 'senior adjudication scenario assessment' in ids[pid]['qualifications']

def acting_allowed(*, adopted, signed_before_absence, accepted, qualified, available, conflicted, days, authorization_valid):
    return all([adopted, signed_before_absence, accepted, qualified, available, not conflicted,
                authorization_valid, 0 <= days < 30])

def can_decide(*, adopted, mandate_active, domain, permitted_domains, conflicted, reserved, technical_safe):
    return all([adopted, mandate_active, domain in permitted_domains, not conflicted, not reserved, technical_safe])

def case_allowed(investigator, adjudicator, appeal, assessor, subject):
    roles = [investigator, adjudicator, appeal, assessor]
    return len(set(roles)) == 4 and subject not in roles

def queue(demands, capacity):
    backlog = 0
    result = []
    for demand in demands:
        backlog = max(0, backlog + demand - capacity)
        result.append(backlog)
    return result

def check_workload(work):
    for w in work['weeks'].values():
        assert sum(w['allocation']) == w['baseline'], 'Work disappeared'
        assert len(w['allocation']) == len(w['overhead']) == 5
        assert min(w['allocation'] + w['overhead']) >= 0
        assert sum(w['allocation']) + sum(w['overhead']) >= w['baseline']
    assert queue([11]*4, 8) == [3,6,9,12]
    assert queue([4.5]*4, 4) == [.5,1,1.5,2]
    assert queue([4.5,6,5,4.75], 4) == [.5,2.5,3.5,4.25]
    assert queue([11,16,13,11], 12) == [0,4,5,4]
    assert queue([4.5,6,5,4.75], 8) == [0,0,0,0]

def semantic_errors(pages):
    errors = []
    for name, text in pages.items():
        if '/proposals/' in name or name in HISTORICAL or name == 'docs/governance/current-authority.md':
            continue
        if re.search(r'executive-directors|An ED owns|If an ED office|executive portfolio or COO|Portfolio leadership reviews', text):
            errors.append(name + ': obsolete active route')
        # A legacy anchor must attach to a substantive heading and content, not an empty tail.
        lines = text.splitlines()
        fenced = False
        for i, line in enumerate(lines):
            if line.startswith('```'): fenced = not fenced
            if fenced or not re.fullmatch(r'<a id="[^"]+"></a>', line): continue
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or re.fullmatch(r'<a id="[^"]+"></a>', lines[j])): j += 1
            if j >= len(lines) or not lines[j].startswith('## '):
                errors.append(name + ': empty/unattached legacy anchor ' + line)
                continue
            k = j + 1
            content = []
            while k < len(lines) and not lines[k].startswith('#') and not lines[k].startswith('<a id='):
                content.append(lines[k]); k += 1
            if len(' '.join(content).strip()) < 60:
                errors.append(name + ': insubstantial legacy section ' + line)
    return errors

def run():
    model = json.loads((ROOT/'docs/structure-model.json').read_text(encoding='utf-8'))
    work = json.loads((ROOT/'docs/executive-workload.json').read_text(encoding='utf-8'))
    check_coverage(model); check_workload(work)
    paths = subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','--','docs/*.md'], cwd=ROOT, text=True).splitlines()
    pages = {n:(ROOT/n).read_text(encoding='utf-8') for n in set(paths)}
    errors = semantic_errors(pages)
    assert not errors, '\n'.join(errors)
    expected_subjects = {
        'docs/personnel/ranks-and-appointments.md': {'management-appointment-template':'Appointment record', 'assessment-criteria-and-specialist-access':'Assessment and challenge'},
        'docs/governance/structure.md': {'directorate-staffing-assumptions':'Activation and scale'},
    }
    for name, mapping in expected_subjects.items():
        for anchor, title in mapping.items():
            tail = pages[name].split('<a id="'+anchor+'"></a>', 1)[1]
            heading = re.search(r'^## (.+)$', tail, re.M)
            assert heading and heading[1] == title, 'Semantic subject mismatch'
    review = pages['docs/personnel/management-and-development.md']
    for stage in ['Understand','Support','Review','Decide','Challenge','Close and hand over']:
        assert '**'+stage+':' in review or '**'+stage+'**' in review or '**'+stage+':**' in review
    assert 'separate' in pages['docs/oversight/case-handling.md']
    authority = pages['docs/operations/authority-and-escalation.md']
    for category in ['Routine divisional staffing','Unresolved cross-division','Technical maintenance','Senior misconduct','Acting COO','Seven-day emergency']:
        assert category in authority
    assert 'no routine COO reapproval' in authority or 'routine COO reapproval' in authority
    assert 'R14' in pages['docs/proposals/v1-4-ratification.md']
    base = dict(adopted=True, signed_before_absence=True, accepted=True, qualified=True,
                available=True, conflicted=False, days=1, authorization_valid=True)
    assert acting_allowed(**base)
    negatives = 0
    for field, value in [('adopted',False),('signed_before_absence',False),('accepted',False),('qualified',False),('available',False),('conflicted',True),('days',30),('authorization_valid',False)]:
        bad = dict(base); bad[field] = value
        assert not acting_allowed(**bad); negatives += 1
    decision = dict(adopted=True, mandate_active=True, domain='shared scheduling', permitted_domains=['shared scheduling'], conflicted=False, reserved=False, technical_safe=True)
    assert can_decide(**decision)
    for field,value in [('adopted',False),('mandate_active',False),('domain','dismiss Head'),('conflicted',True),('reserved',True),('technical_safe',False)]:
        bad=dict(decision); bad[field]=value
        assert not can_decide(**bad); negatives += 1
    assert case_allowed('i','j','a','s','subject')
    assert not case_allowed('i','i','a','s','subject'); negatives += 1
    assert not case_allowed('i','subject','a','s','subject'); negatives += 1
    for mutation in ['reporting','hours','vote']:
        bad=deepcopy(model)
        if mutation=='reporting': bad['models']['60'][2]['manager']='game-5'
        if mutation=='hours': bad['office_appointments']['60'][0]['hours']=40
        if mutation=='vote': bad['council'][4]='community-4'
        try: check_coverage(bad)
        except AssertionError: negatives += 1
        else: raise AssertionError('Bad model accepted: '+mutation)
    bad=deepcopy(work);bad['weeks']['high']['allocation'][0]-=1
    try:check_workload(bad)
    except AssertionError:negatives+=1
    else:raise AssertionError('Disappearing work accepted')
    assert semantic_errors({'docs/test.md':'# Test\n\n<a id="role-profiles"></a>\n'})
    assert semantic_errors({'docs/test.md':'# Test\n\nAn ED owns the active portfolio.'})
    negatives += 2
    print(f'PASS: R14 semantic references, Office allocations, domain/case/succession gates; {negatives} negative checks.')
    print('PASS: workload conservation and cumulative backlog. Hypothetical gates do not certify actual appointments or controls.')

if __name__ == '__main__': run()
