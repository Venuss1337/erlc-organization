"""Validate proposed staffing, ownership and governance; no live implementation claim."""
import json
from pathlib import Path
from collections import Counter
from copy import deepcopy

def validate(model):
    assert model['status'] == 'proposed' and model['ratified'] is False, 'Unauthorized adoption'
    assert len(set(model['case_separation'].values())) == 4, 'Self-review'
    assert set(model['divisions']) == {'safety', 'game', 'community'}
    assert len(model['functions']) == 26 and set(model['functions'].values()) <= {'safety','game','community','technology','oversight'}
    for count, people in model['models'].items():
        ids = {p['id']: p for p in people}
        assert len(ids) == len(people) == int(count)
        assert len({p['name'] for p in people}) == len(people)
        for p in people:
            assert p['role'] not in ['Executive Director','Unit Manager']
            assert p['id'] == 'owner' or p['manager'] in ids, 'Missing supervisor'
            assert not isinstance(p['manager'], list), 'Multiple People Managers'
            assert p['qualifications'] and p['availability'] and p['assignment']
            if p['role'] == 'Division Head': assert p['grade'] == 6 and p['manager'] == 'coo'
            if p['role'] == 'Technical Lead': assert p['grade'] == 5 and p['manager'] == 'coo'
            if p['home'] == 'oversight': assert p['manager'] == ('owner' if p['id']=='commissioner' else 'commissioner')
            seen = set()
            at = p
            while at['manager'] is not None:
                assert at['id'] not in seen, 'Reporting cycle'
                seen.add(at['id'])
                at = ids[at['manager']]
        council = [ids[x] for x in model['council']]
        assert len({p['id'] for p in council}) == 5
        assert council[2]['home'] != council[3]['home']
        managers = Counter(p['manager'] for p in people if p['manager'])
        assert council[4]['id'] not in managers and all(p['home']!='oversight' for p in council)
        print(count, 'staff;', len(managers), 'People Managers; max span', max(managers.values()))

if __name__ == '__main__':
    model = json.loads(Path('docs/structure-model.json').read_text(encoding='utf-8'))
    validate(model)
    for mutation in ['cycle','missing','adoption','ownership','double','self-review']:
        bad = deepcopy(model)
        if mutation=='cycle': bad['models']['20'][0]['manager']='coo'
        if mutation=='missing': bad['models']['20'][1]['manager']='retired-ed'
        if mutation=='adoption': bad['ratified']=True
        if mutation=='ownership': bad['functions']['IA']='unowned'
        if mutation=='self-review': bad['case_separation']['appeal']='ia'
        if mutation=='double': bad['models']['20'][2]['manager']=['coo','owner']
        try:
            validate(bad)
        except (AssertionError, TypeError, KeyError):
            print('PASS negative:', mutation)
        else:
            raise AssertionError('Negative case accepted: '+mutation)
    print('PASS proposed reporting, ownership, grades, Council, roots and negative cases. Case separation also requires procedural review.')
