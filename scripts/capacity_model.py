"""Dependency-free whole-person workload and protected reserve simulation. No live authority."""
from collections import defaultdict

def demand(record, week, before=False):
    return sum(record['before_busy'].values()) if before else sum(record['weeks'][week].values())

def backlog(demands, capacities):
    outstanding = 0.0
    values = []
    for new, capacity in zip(demands, capacities):
        assert new >= 0 and capacity >= 0
        outstanding = max(0.0, outstanding + new - capacity)
        values.append(round(outstanding, 4))
    return values

def sequence(record, weeks, capacity, absent_weeks=()):
    return backlog([record.get('ready_hours',{}).get(w,demand(record,w)) for w in weeks], [0 if i in absent_weeks else capacity for i in range(len(weeks))])

def task_buckets(tasks):
    ids = set()
    buckets = defaultdict(float)
    for t in tasks:
        assert t['id'] not in ids, 'Duplicate dependency/labor task'
        ids.add(t['id'])
        assert t['hours'] >= 0
        assert t['state'] in ['ready','blocked-decision','blocked-qualification','blocked-authority','deferred-service']
        buckets[t['state']] += t['hours']
    return dict(buckets)

def transition(tasks, task_id, destination, requirements_verified=False):
    assert destination in ['ready','blocked-decision','blocked-qualification','blocked-authority','deferred-service']
    found = [t for t in tasks if t['id']==task_id]
    assert len(found)==1
    if destination=='ready' and found[0]['state']!='ready': assert requirements_verified, 'Blocked work cannot become qualified/authorized through spare hours'
    found[0]['state']=destination
    return task_buckets(tasks)

def reserve_allowed(model, size, reserve, category, subject, participants, context):
    people={p['id']:p for p in model['models'][size]}
    pid=reserve['person']
    if pid not in people or category != reserve['category']:return False
    if context.get('special_external_required'):return False
    if subject in people and (subject in ['owner','coo'] or people[subject]['home']=='oversight'):return False
    if context.get('appointor','commissioner')==subject:return False
    if pid==subject or pid in participants or pid in context.get('personal_conflicts',[]):return False
    if any(a['person']==pid for a in model['office_appointments'][size]):return False
    if 'reserve '+category+' synthetic assessment' not in people[pid]['qualifications']:return False
    at=people[pid]
    while at['manager'] is not None:
        if at['manager']==subject:return False
        at=people[at['manager']]
    if category=='assurance' and context.get('audited_home')==people[pid]['home']:return False
    if not all(context.get(k,False) for k in ['adopted','registered','consent','case_mandate','safe_access','compatible_window']):return False
    if overlap_hours(context.get('candidate_windows',[]),context.get('case_windows',[])) < .25:return False
    if context.get('required_hours',0)>context.get('released_case_hours',0):return False
    if context.get('access_days',31)>30:return False
    if not context.get('hypothetical',False):
        if not all(reserve.get(k,False) for k in ['actual_authorized','actual_accepted','actual_access_verified']):return False
    return True


def overlap_hours(left, right):
    import re
    def parse(window):
        m=re.fullmatch(r'(\w+) (\d+):(\d+)-(\d+):(\d+) UTC',window)
        assert m, 'Unspecified timezone/window'
        day,a,b,c,d=m.groups();return day,int(a)*60+int(b),int(c)*60+int(d)
    total=0
    for x in left:
        dx,sx,ex=parse(x)
        for y in right:
            dy,sy,ey=parse(y)
            if dx==dy: total+=max(0,min(ex,ey)-max(sx,sy))
    return total/60
