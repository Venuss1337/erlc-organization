"""R15 fixed-roster, capacity, independence and negative validation."""
from pathlib import Path
from copy import deepcopy
import json
from capacity_model import demand, backlog, sequence, task_buckets, transition, reserve_allowed, overlap_hours

ROOT=Path(__file__).resolve().parents[1]

def validate(model, capacity):
    assert model['version']==capacity['version']=='1.5.0'
    assert model['ratified'] is False and not model['actual_appointments_verified']
    for size, block in capacity['models'].items():
        people={p['id']:p for p in model['models'][size]}
        assert len(people)==int(size) and set(people)==set(block['people'])
        for p in people.values():
            assert p['manager'] is None if p['id']=='owner' else isinstance(p['manager'],str) and p['manager'] in people
            seen=set();at=p
            while at['manager'] is not None:
                assert at['id'] not in seen;seen.add(at['id']);at=people[at['manager']]
        for function,pid in model['functional_owners'][size].items():
            assert pid in people
            assert function+' functional scenario assessment' in people[pid]['qualifications']
        records=block['people']
        for rec in records.values():
            for key in ['before_busy','after_busy']:
                assert set(rec[key])==set(capacity['categories'])
                assert min(rec[key].values())>=0
            assert rec['accepted_hours']>0 and rec['windows']
            for w,v in rec['weeks'].items():
                assert abs(rec['ready_hours'][w]+rec['blocked_allocation_hours'][w]-sum(v.values()))<1e-6
            assert all(abs(rec['weeks']['busy'][k]-rec['after_busy'][k])<1e-6 for k in capacity['categories'])
            for weeks in capacity['sequences'].values():
                for level in capacity['capacity_levels']:
                    actual=sequence(rec,weeks,level)
                    # Independent cumulative recurrence; no expected sequence is copied from a narrative.
                    b=0
                    for i,w in enumerate(weeks):
                        b=max(0,b+rec['ready_hours'][w]-level)
                        assert abs(actual[i]-b)<1e-6
        before=sum(sum(r['before_busy'].values()) for r in records.values())
        after=sum(sum(r['after_busy'].values()) for r in records.values())
        deferred=sum(x['hours'] for x in block['deferred_delivery'])
        assert abs(after-before+deferred-block['extra_coordination'])<1e-6, 'Unaccounted work disappearance/addition'
        for f in block['flows']:
            assert f['from'] in people and f['to'] in people and f['hours']>=0
        for r in model['reserve_pool'][size]:
            assert r['person'] in people and r['category'] in ['investigation','appeal','assurance']
            assert not r['actual_authorized'] and not r['actual_accepted'] and not r['actual_access_verified'], 'Fabricated actual readiness'
            assert not any(a['person']==r['person'] for a in model['office_appointments'][size])
            assert records[r['person']]['after_busy']['casework']==r['case_hours']
        task_buckets(block['dependency_examples'])

def run():
    model=json.loads((ROOT/'docs/structure-model.json').read_text(encoding='utf-8'))
    data=json.loads((ROOT/'docs/management-capacity.json').read_text(encoding='utf-8'))
    validate(model,data)
    negatives=0
    for mutation in ['double-manager','cycle','free-hours','qualified','ready']:
        m=deepcopy(model);d=deepcopy(data)
        if mutation=='double-manager':m['models']['20'][2]['manager']=['coo','owner']
        if mutation=='cycle':m['models']['20'][1]['manager']='safety-head'
        if mutation=='free-hours':d['models']['20']['people']['game-head']['after_busy']['executive']+=5
        if mutation=='qualified':m['models']['20'][3]['qualifications']=[]
        if mutation=='ready':m['reserve_pool']['20'][0]['actual_accepted']=True
        try:validate(m,d)
        except (AssertionError,TypeError,KeyError):negatives+=1
        else:raise AssertionError('Invalid capacity model accepted: '+mutation)
    r=model['reserve_pool']['60'][0]
    good=dict(adopted=True,registered=True,consent=True,case_mandate=True,safe_access=True,compatible_window=True,hypothetical=True,required_hours=1,released_case_hours=1.5,access_days=30,candidate_windows=['Sat 16:00-19:00 UTC'],case_windows=['Sat 17:00-18:00 UTC'])
    assert reserve_allowed(model,'60',r,'investigation','safety-head',[],good)
    for key,value in [('adopted',False),('registered',False),('consent',False),('case_mandate',False),('safe_access',False),('compatible_window',False),('required_hours',2),('access_days',31),('special_external_required',True),('hypothetical',False),('case_windows',['Tue 17:00-18:00 UTC'])]:
        bad=dict(good);bad[key]=value
        assert not reserve_allowed(model,'60',r,'investigation','safety-head',[],bad);negatives+=1
    assert not reserve_allowed(model,'60',r,'appeal','safety-head',[],good);negatives+=1
    assert not reserve_allowed(model,'60',r,'investigation',r['person'],[],good);negatives+=1
    assert not reserve_allowed(model,'60',r,'investigation','game-head',[],good);negatives+=1
    assert not reserve_allowed(model,'60',r,'investigation','safety-head',[r['person']],good);negatives+=1
    bad=dict(good);bad['personal_conflicts']=[r['person']]
    assert not reserve_allowed(model,'60',r,'investigation','safety-head',[],bad);negatives+=1
    for subject in ['owner','coo','commissioner','ia','appeals']:
        assert not reserve_allowed(model,'60',r,'investigation',subject,[],good);negatives+=1
    wrong=dict(good);wrong['appointor']='safety-head'
    assert not reserve_allowed(model,'60',r,'investigation','safety-head',[],wrong);negatives+=1
    assurance=model['reserve_pool']['60'][2]
    wrong=dict(good);wrong['audited_home']='safety'
    assert not reserve_allowed(model,'60',assurance,'assurance','game-head',[],wrong);negatives+=1
    tasks=deepcopy(data['models']['60']['dependency_examples'])
    total=sum(task_buckets(tasks).values())
    try:transition(tasks,'reserve-case','ready')
    except AssertionError:negatives+=1
    else:raise AssertionError('Blocked authority ignored')
    transition(tasks,'reserve-case','ready',True)
    assert sum(task_buckets(tasks).values())==total
    try:task_buckets(tasks+[deepcopy(tasks[0])])
    except AssertionError:negatives+=1
    else:raise AssertionError('Duplicate labor accepted')
    # Fix prior mixed sequence from actual executive data; no hardcoded role demand list.
    old=json.loads((ROOT/'docs/executive-workload.json').read_text())
    keys=old['sequences']['mixed']
    demands=[old['weeks'][k]['allocation'][0]+old['weeks'][k]['overhead'][0] for k in keys]
    result=backlog(demands,[4]*len(keys))
    assert result[-1]==max(0,sum(demands)-4*len(keys))
    assert overlap_hours(['Sat 16:00-19:00 UTC'],['Sat 17:00-18:00 UTC'])==1
    assert overlap_hours(['Sat 16:00-19:00 UTC'],['Sun 16:00-19:00 UTC'])==0
    print('PASS: R15 whole-role accounting, fixed rosters, workload conservation, dependency states and category reserves; '+str(negatives)+' negative cases.')
    print('PASS: data-derived executive mixed backlog at 4h = '+str(result)+'. No actual readiness is certified.')

if __name__=='__main__':run()
