# v1.4 executive workload, staffing and comparative readiness

**Project version:** 1.5.0 · **Release date:** 2026-11-02 · **Status:** Official release.

**Historical R14 simulation.** Current whole-person data and corrected data-derived mixed queue are in [R15 evidence](capacity-readiness-v1-5.md). The old 4.25h mixed-sequence prose incorrectly used governance demand for the last busy week; actual JSON sequence yields 4.0h at 4h availability. This note corrects interpretation without erasing historical evidence.

**Repository-only implementation evidence.** All people, skills, availability, signatures and outcomes in table tops are hypothetical. No actual adoption, qualified reserve, acceptance, appointment or security test is verified. The independent audit supplied in the conversation is the input; no standalone audit file is fabricated. This report is not public handbook policy.

## Method and baseline

Compared v1.2 commit cf094e4993658ceaa453eb18c3744684072aeb47, v1.3 commit 4125b7eb260acf7a93e69b04d7550a750cf613b8, and the selected pending R14 target. Same underlying work, qualifications and accepted windows are used in paired traces; Office allocation displaces delivery rather than creating free staff. Earlier 18-manager v1.2 fixture is audit evidence, not a current measured roster. Baseline COO demand is the supplied 6/11/16/13/10-hour model. Numerical workloads are design assumptions, not measured improvements.

## Reproducible executive workload

Role order: COO / Integration / CoS / Planning / Heads. Allocation sums to baseline exactly. Added interface overhead covers reading/transferring scoped decisions, not a mandatory meeting. Eliminated work = 0, duplicated work assumed = 0, deferred work = 0 only if every recipient can accept the modeled allocation. Real duplication, absence or conflict adds demand; service reduction must be counted as reduced output, not efficiency.

| Week | Baseline | Reassigned allocation | Added overhead | Final role demand | Total |
|---|---|---|---|---|---|
| normal | 6h | 2.75, 1.25, 1, 0.25, 0.75 | 0.25, 0.25, 0, 0, 0 | 3.0, 1.5, 1, 0.25, 0.75 | 6.5h |
| high | 11h | 4, 3, 1.5, 1, 1.5 | 0.5, 0.25, 0.25, 0, 0 | 4.5, 3.25, 1.75, 1, 1.5 | 12.0h |
| incident | 16h | 5.5, 4, 2, 1, 3.5 | 0.5, 0.5, 0.5, 0, 0 | 6.0, 4.5, 2.5, 1, 3.5 | 17.5h |
| shortage | 13h | 4.5, 3.5, 1.5, 1, 2.5 | 0.5, 0.25, 0.25, 0, 0 | 5.0, 3.75, 1.75, 1, 2.5 | 14.0h |
| governance | 10h | 4.5, 1.5, 2.5, 0.5, 1 | 0.25, 0.25, 0.25, 0, 0 | 4.75, 1.75, 2.75, 0.5, 1 | 10.75h |

At 60, illustrative Office support budgets are Integration 6h, CoS 4h, Planning 2h; added Heads work consumes existing Head capacity and is NOT free. COO sensitivity uses 4/8/12h; none is an obligation. Without Planning appointment its analytical allocation moves explicitly to accepted CoS/Head capacity or is deferred.

| Week | Old COO demand | New COO demand | New load at 4 / 8 / 12h | New one-week COO backlog at 4 / 8 / 12h |
|---|---|---|---|---|
| normal | 6 | 3.0 | 75% / 38% / 25% | 0 / 0 / 0h |
| high | 11 | 4.5 | 112% / 56% / 38% | 0.5 / 0 / 0h |
| incident | 16 | 6.0 | 150% / 75% / 50% | 2.0 / 0 / 0h |
| shortage | 13 | 5.0 | 125% / 62% / 42% | 1.0 / 0 / 0h |
| governance | 10 | 4.75 | 119% / 59% / 40% | 0.75 / 0 / 0h |

Backlog recurrence: B(t) = max(0, B(t-1) + demand(t) - capacity(t)); unused earlier capacity is not banked. Work can wait in this idealized queue; urgent fairness/safety still needs immediate qualified coverage or reduced service. Half-hour equivalents are not case counts.

| Sequence / COO capacity | Old weekly backlog (h) | New weekly backlog (h) |
|---|---|---|
| high / 4 | [7, 14, 21, 28] | [0.5, 1.0, 1.5, 2.0] |
| high / 8 | [3, 6, 9, 12] | [0, 0, 0, 0] |
| high / 12 | [0, 0, 0, 0] | [0, 0, 0, 0] |
| mixed / 4 | [7, 19, 28, 35] | [0.5, 2.5, 3.5, 4.0] |
| mixed / 8 | [3, 11, 16, 19] | [0, 0, 0, 0] |
| mixed / 12 | [0, 4, 5, 4] | [0, 0, 0, 0] |

At 4h, four busy weeks still leave 2h COO backlog; mixed weeks leave 4.25h. At 8/12h the modeled COO queue clears, conditional on other roles and Heads actually absorbing work. This is redistribution, not measured speed. A missing Integration Director pushes unaccepted decisions to a valid alternate/COO or deferral; no magical queue reset.

## Scale, spans and opportunity cost

All delivery budgets in this new fixture use a six-hour illustrative ceiling, including supervision and Office work. This replaces the earlier broad 3–6 band only as a simulation assumption. People may volunteer less; then services shrink.

| Size | Unique staff / People Managers | COO permanent reports | Office hours within fixed roster | Displaced delivery / limits |
|---|---|---|---|---|
| 20 | 20 / 7 | 4 | Integration Director=2h, Chief of Staff=1.5h | 3.5h removed from previous delivery/other duties; max People span 4 |
| 30 | 30 / 8 | 4 | Integration Director=4h, Chief of Staff=2h | 6h removed from previous delivery/other duties; max People span 7 |
| 60 | 60 / 13 | 7 | Integration Director=6h, Chief of Staff=4h, Planning Lead=2h | 12h removed from previous delivery/other duties; max People span 9 |

20: Integration is concurrent Game Head (2h of its 6h), CoS concurrent Personnel contributor (1.5h). No Planning appointment. Game-related contested arbitration conflicts the Integration holder; a named unconflicted alternate/COO must decide or cancel. Under the identical busy demand, Integration exceeds 2h by 1.25h; CoS plus absent Planning work demands 2.75h against 1.5h (1.25h gap). This small model cannot promise the full busy service; defer optional work and resolve conflict rather than imply success.

30: Integration is a Game specialist with 4h Office + 2h primary quality work, CoS 2h Office + 4h Personnel; no Planning appointment. Busy CoS plus planning demand 2.75h exceeds 2h by .75h; assign accepted aggregate analysis to an existing Head or defer it. Integration retains 4h capacity but incident-week demand 4.5h exceeds that. No permanent deputy or extra volunteer is added.

60: former Game contributor 6 becomes dedicated Integration, Community contributor 5 dedicated CoS, Community contributor 6 conditional Planning. Their remaining 2h/4h are explicitly consented secondary Member Services support under Community task scope, retaining COO as sole permanent manager; no private-record access is inherited. Those three people leave their former contributor allocation; a 12h Office budget displaces delivery. Two Community People Leads remain, with fewer reports; Game still has a nine-report Lead. Broader Head coaching risk is not solved by Office charts.

## Full unique fictional rosters

The following rows list every person at all sizes, with role, grade, home, one permanent manager, primary/secondary work, qualification and voluntary availability. Qualifications added for R14 are fictional scenario assessments; actual implementation remains unavailable. No outside reviewer is counted.

### 20 staff

| ID / fictional identity | Role / grade | Home / permanent manager | Primary and secondary assignment | Scenario qualification | Voluntary availability |
|---|---|---|---|---|---|
| owner / Alex Rowan | Owner / 8 | ownership / None | ownership | actual ownership | 2–4 voluntary hours/week |
| coo / Beth Calder | COO / 7 | executive / owner | integration | operational management | 5–8 voluntary hours/week |
| safety-head / Safety Volunteer 1 | Division Head / 6 | safety / coo | Discord/game enforcement | current enforcement, acting COO scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-1 / Safety Volunteer 2 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-2 / Safety Volunteer 3 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-3 / Safety Volunteer 4 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement, incident command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-head / Game Volunteer 1 | Division Head / 6 | game / coo | session or RP delivery; concurrent Integration Director | session/program qualification, integration arbitration, delegation limits, acting COO scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-1 / Game Volunteer 2 | Contributor / 1 | game / game-head | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-2 / Game Volunteer 3 | Contributor / 1 | game / game-head | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-3 / Game Volunteer 4 | Contributor / 1 | game / game-head | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-4 / Game Volunteer 5 | Contributor / 1 | game / game-head | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-head / Community Volunteer 1 | Division Head / 6 | community / coo | support or People function | support/personnel confidentiality, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-1 / Community Volunteer 2 | Contributor / 5 | community / community-head | Personnel coordinator; CoS concurrent only if qualified; concurrent Chief of Staff | support/personnel confidentiality, executive coordination, executive coordination, Council secretariat | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-2 / Community Volunteer 3 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-3 / Community Volunteer 4 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-head / Technology Volunteer 1 | Technical Lead / 5 | technology / coo | engineering/access | technical and access handling, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-1 / Technology Volunteer 2 | Contributor / 1 | technology / technology-head | engineering/access | technical and access handling | 6 voluntary hours/week; illustrative accepted windows, not quota |
| commissioner / Galen Price | Commissioner / 7 | oversight / owner | Commissioner | oversight administration | 2–4 voluntary hours/week |
| ia / Hazel Rowe | Investigator / 1 | oversight / commissioner | Investigator | investigation/evidence | 2–4 voluntary hours/week |
| appeals / Idris Snow | Appeals Reviewer / 1 | oversight / commissioner | Appeals Reviewer | independent case review | 2–4 voluntary hours/week |

### 30 staff

| ID / fictional identity | Role / grade | Home / permanent manager | Primary and secondary assignment | Scenario qualification | Voluntary availability |
|---|---|---|---|---|---|
| owner / Alex Rowan | Owner / 8 | ownership / None | ownership | actual ownership | 2–4 voluntary hours/week |
| coo / Beth Calder | COO / 7 | executive / owner | integration | operational management | 5–8 voluntary hours/week |
| safety-head / Safety Volunteer 1 | Division Head / 6 | safety / coo | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-1 / Safety Volunteer 2 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-2 / Safety Volunteer 3 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-3 / Safety Volunteer 4 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement, incident command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-4 / Safety Volunteer 5 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-5 / Safety Volunteer 6 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-6 / Safety Volunteer 7 | Contributor / 2 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-head / Game Volunteer 1 | Division Head / 6 | game / coo | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-1 / Game Volunteer 2 | People Lead / 4 | game / game-head | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-2 / Game Volunteer 3 | Contributor / 1 | game / game-1 | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-3 / Game Volunteer 4 | Contributor / 1 | game / game-1 | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-4 / Game Volunteer 5 | Contributor / 1 | game / game-1 | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-5 / Game Volunteer 6 | Contributor / 5 | game / game-1 | session or RP delivery; concurrent Integration Director | session/program qualification, integration arbitration, delegation limits, acting COO scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-6 / Game Volunteer 7 | Contributor / 1 | game / game-1 | Law Enforcement program coordination/training | session/program qualification, Law Enforcement program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-7 / Game Volunteer 8 | Contributor / 1 | game / game-1 | Fire & EMS program coordination/training | session/program qualification, Fire & EMS program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-8 / Game Volunteer 9 | Contributor / 1 | game / game-1 | DOT program coordination/training | session/program qualification, DOT program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-head / Community Volunteer 1 | Division Head / 6 | community / coo | support or People function | support/personnel confidentiality, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-1 / Community Volunteer 2 | Contributor / 5 | community / community-head | Personnel coordinator; CoS concurrent only if qualified; concurrent Chief of Staff | support/personnel confidentiality, executive coordination, executive coordination, Council secretariat | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-2 / Community Volunteer 3 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-3 / Community Volunteer 4 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-4 / Community Volunteer 5 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-5 / Community Volunteer 6 | Contributor / 1 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-head / Technology Volunteer 1 | Technical Lead / 5 | technology / coo | engineering/access | technical and access handling, acting COO scenario assessment, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-1 / Technology Volunteer 2 | Contributor / 1 | technology / technology-head | engineering/access | technical and access handling | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-2 / Technology Volunteer 3 | Contributor / 1 | technology / technology-head | engineering/access | technical and access handling | 6 voluntary hours/week; illustrative accepted windows, not quota |
| commissioner / Galen Price | Commissioner / 7 | oversight / owner | Commissioner | oversight administration | 2–4 voluntary hours/week |
| ia / Hazel Rowe | Investigator / 1 | oversight / commissioner | Investigator | investigation/evidence | 2–4 voluntary hours/week |
| appeals / Idris Snow | Appeals Reviewer / 1 | oversight / commissioner | Appeals Reviewer | independent case review | 2–4 voluntary hours/week |

### 60 staff

| ID / fictional identity | Role / grade | Home / permanent manager | Primary and secondary assignment | Scenario qualification | Voluntary availability |
|---|---|---|---|---|---|
| owner / Alex Rowan | Owner / 8 | ownership / None | ownership | actual ownership | 2–4 voluntary hours/week |
| coo / Beth Calder | COO / 7 | executive / owner | integration | operational management | 5–8 voluntary hours/week |
| safety-head / Safety Volunteer 1 | Division Head / 6 | safety / coo | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-1 / Safety Volunteer 2 | People Lead / 3 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-2 / Safety Volunteer 3 | People Lead / 3 | safety / safety-head | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-3 / Safety Volunteer 4 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement, incident command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-4 / Safety Volunteer 5 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-5 / Safety Volunteer 6 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-6 / Safety Volunteer 7 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-7 / Safety Volunteer 8 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-8 / Safety Volunteer 9 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-9 / Safety Volunteer 10 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-10 / Safety Volunteer 11 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-11 / Safety Volunteer 12 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-12 / Safety Volunteer 13 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-13 / Safety Volunteer 14 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-14 / Safety Volunteer 15 | Contributor / 2 | safety / safety-1 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| safety-15 / Safety Volunteer 16 | Contributor / 2 | safety / safety-2 | Discord/game enforcement | current enforcement | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-head / Game Volunteer 1 | Division Head / 6 | game / coo | session or RP delivery | session/program qualification, acting COO scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-1 / Game Volunteer 2 | People Lead / 4 | game / game-head | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-2 / Game Volunteer 3 | People Lead / 4 | game / game-head | session or RP delivery | session/program qualification | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-3 / Game Volunteer 4 | Contributor / 1 | game / game-2 | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-4 / Game Volunteer 5 | Contributor / 1 | game / game-1 | qualified Session Commander | session command | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-5 / Game Volunteer 6 | Integration Director / 5 | executive / coo | Integration Director | session/program qualification, integration arbitration, delegation limits, acting COO scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-6 / Game Volunteer 7 | Contributor / 1 | game / game-1 | Law Enforcement program coordination/training | session/program qualification, Law Enforcement program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-7 / Game Volunteer 8 | Contributor / 1 | game / game-2 | Fire & EMS program coordination/training | session/program qualification, Fire & EMS program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-8 / Game Volunteer 9 | Contributor / 1 | game / game-1 | DOT program coordination/training | session/program qualification, DOT program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-9 / Game Volunteer 10 | Contributor / 1 | game / game-2 | Civilian RP program coordination/training | session/program qualification, Civilian RP program scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-10 / Game Volunteer 11 | Contributor / 1 | game / game-1 | Scheduling and dispatch | session/program qualification, dispatch/readiness assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-11 / Game Volunteer 12 | Contributor / 1 | game / game-2 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-12 / Game Volunteer 13 | Contributor / 1 | game / game-1 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-13 / Game Volunteer 14 | Contributor / 1 | game / game-2 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-14 / Game Volunteer 15 | Contributor / 1 | game / game-1 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-15 / Game Volunteer 16 | Contributor / 1 | game / game-2 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-16 / Game Volunteer 17 | Contributor / 1 | game / game-1 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-17 / Game Volunteer 18 | Contributor / 1 | game / game-2 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-18 / Game Volunteer 19 | Contributor / 1 | game / game-1 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-19 / Game Volunteer 20 | Contributor / 1 | game / game-2 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| game-20 / Game Volunteer 21 | Contributor / 1 | game / game-1 | Session hosting/control | session/program qualification, hosting/control assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-head / Community Volunteer 1 | Division Head / 6 | community / coo | support or People function | support/personnel confidentiality, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-1 / Community Volunteer 2 | People Lead / 5 | community / community-head | Personnel coordination and coaching; no Office appointment | support/personnel confidentiality, executive coordination | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-2 / Community Volunteer 3 | People Lead / 4 | community / community-head | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-3 / Community Volunteer 4 | Contributor / 1 | community / community-2 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-4 / Community Volunteer 5 | Chief of Staff / 5 | executive / coo | Chief of Staff; accepted secondary Member Services support (2h) | support/personnel confidentiality, executive coordination, Council secretariat | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-5 / Community Volunteer 6 | Planning Lead / 4 | executive / coo | Planning Lead; accepted secondary Member Services support (4h) | support/personnel confidentiality, capacity analysis, privacy-safe aggregate reporting | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-6 / Community Volunteer 7 | Contributor / 1 | community / community-1 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-7 / Community Volunteer 8 | Contributor / 1 | community / community-2 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-8 / Community Volunteer 9 | Contributor / 1 | community / community-1 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-9 / Community Volunteer 10 | Contributor / 1 | community / community-2 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-10 / Community Volunteer 11 | Contributor / 1 | community / community-1 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-11 / Community Volunteer 12 | Contributor / 1 | community / community-2 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-12 / Community Volunteer 13 | Contributor / 1 | community / community-1 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-13 / Community Volunteer 14 | Contributor / 1 | community / community-2 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| community-14 / Community Volunteer 15 | Contributor / 1 | community / community-1 | support or People function | support/personnel confidentiality | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-head / Technology Volunteer 1 | Technical Lead / 5 | technology / coo | engineering/access | technical and access handling, senior adjudication scenario assessment | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-1 / Technology Volunteer 2 | Contributor / 1 | technology / technology-head | engineering/access | technical and access handling | 6 voluntary hours/week; illustrative accepted windows, not quota |
| technology-2 / Technology Volunteer 3 | Contributor / 1 | technology / technology-head | engineering/access | technical and access handling | 6 voluntary hours/week; illustrative accepted windows, not quota |
| commissioner / Galen Price | Commissioner / 7 | oversight / owner | Commissioner | oversight administration | 2–4 voluntary hours/week |
| ia / Hazel Rowe | Investigator / 1 | oversight / commissioner | Investigator | investigation/evidence | 2–4 voluntary hours/week |
| appeals / Idris Snow | Appeals Reviewer / 1 | oversight / commissioner | Appeals Reviewer | independent case review | 2–4 voluntary hours/week |


## Comparative adversarial stress tests

P = fresh substantive authorizations; H = meaningful handoffs on the explicitly stated path, excluding notifications/recording. Outcomes distinguish current reality (all new powers unapproved) from conditional tabletop after a real instrument. Inputs are identical per row in A=v1.2 active portfolios at 60, B=v1.3, C=v1.4. At 20/30 A portfolios are inactive, so ordinary cross-functional escalation reaches COO. No model gains free qualified backups. R14-specific acting/decision assessments are extra preparation and consume displaced delivery; baseline people do not magically receive them.

| Test / same fictional input | A: v1.2 | B: v1.3 | C: v1.4 proposed path and outcome | P/H and scale limitations |
|---|---|---|---|---|
| 1 Routine day; two sessions requested | Commanders act without executive launch approval | Same | G04/G05 + two separate qualified responders use accepted windows; support resolves ordinary tickets | Executive P0/H0 all sizes; missing overlap cancels a session in all models |
| 2 High week; six shared resource questions | EDs absorb portfolio scope at 60, COO at small scales | COO owns residual exceptions | Domain owners settle agreements; mandated unconflicted Integration decides residual, COO reserved work | One decision, not Office vote; disputed path Heads→Integration P1/H1 versus B Heads→COO P1/H1; capacity gaps at 20/30 remain |
| 3 Four busy weeks | ED hours displace delivery; COO not automatically absent-proof | At 8h COO backlog 3/6/9/12h | New modeled 4.5h COO demand; 8h queue 0/0/0/0 if support coverage holds | 4h still .5/1/1.5/2h; Office/Head shortfalls counted separately, not reset |
| 4 COO absent two weeks, no handover | Existing ED portfolios continue; Owner replacement still needed | Heads continue; fresh acting dependency | PRE-SIGNED conditional primary accepts trigger, records actual scope and displaced work; otherwise blocked | Activation P0 new appointments/H1 records transfer; Owner preauthorization is one prior approval, not free. At 20 acting Game Head needs valid Game relief or reduced service |
| 5 COO and Owner absent | Local work, reserved/ownership blocked | Same | Valid prior conditional appointment can activate; no new Owner power, extensions or ownership recovery | Conditional on actual signature, validity and person; absent signature remains blocked at every size |
| 6 Game Head resigns immediately | Separate Live/RP Directors limit scope; ED can integrate | COO selects acting broad Head | Existing written qualified Head alternate activates, or valid acting/incumbent COO appoints; Personnel/access execute | P1/H2 for new appointment plus separate access if needed. No qualified replacement in fixture assumed; core sessions only, RP work may pause |
| 7 Cross-division deadlock over coverage | At 60 Ops ED P1/H2; small COO | COO P1/H1 | Integration P1/H1 within envelope, no COO reapproval; conflict routes to named unconflicted alternate | At 20 Game Head/Integration personally involved: recusal, .5h arbitration shifts to COO or defer; no invented neutral |
| 8 Session disruption + security + misconduct + coverage + Council vote | Two portfolios can split integration, OIO separate | COO receives residual integration/preparation | S04 IC, technical custodian containment, Hazel IA, valid pool judge later, Integration resource choice, CoS Council preparation, Planning safe aggregates; COO reserved decisions | Containment P0; restoration P1 separate. Single S04 and absent real custodian/reviewer can still block; busy/incident support deficits at 20/30 require service cuts |
| 9 Manager underperformance, not abuse | Six-stage capability procedure present | Detailed procedure missing | Supervisor understands/supports/reviews, original appointor decides with response, independent challenge and handover | Initial coaching P0; adverse appointment decision P1 then appeal separately; all sizes conditional GOV-03/02 for new powers |
| 10 Head alleged abuse | IA→unconflicted ED→appeal at 60 | IA→COO→external appeal | Commissioner screens; actual Owner-approved qualified pool member receives case mandate, separate external appeal; actual appointor executes reserved removal | Assignment + adjudication + appeal P3/H4 through executor; no free saving of fairness stages. Missing external reviewer blocks full senior process |
| 11 Investigator recusal | Reserve required | Reserve required | Hazel recuses; unconflicted Commissioner seeks qualified investigator distinct from judge/appeal; pool adjudicator is not automatically investigator | Assignment attempt P1/H1; no investigator reserve in fixture → BLOCKED at all sizes, preserve/referral only |
| 12 Appeals overload: 9h work, reviewer accepts 2h | 7h remains | Same | Idris consolidates common questions, preserves individual evidence, Commissioner publishes safe capacity blocker and seeks screened help | P1 capacity action/H2; Office receives aggregate only; 7h remains, not solved by Planning |
| 13 Bot compromise beyond available custodian | Native hierarchy/application owner may block recovery | Same | Preauthorized maintainer contains what possible, actual custodian rotates, valid technical approver verifies restoration independently; no Integration override | P0 fresh containment, P1 restoration/H3; missing actual ownership/token custody → BLOCKED recovery all sizes |
| 14 Council quorum failure: 3 valid voters | No policy adoption; old ED vacancy may cause failure | No adoption; new elected seats help after ratification | Chair/minute fallback records deferral; explicit acting COO seat only after charter + actual appointment; no sixth Office vote | P0 adoption/H1 record. Even 60 staff cannot invent votes or actual Owner ratification |
| 15 Thirty percent inactive, losses concentrated in COO/IC/review/recovery | Portfolios help only if actually available | Broad executive/capability losses | 20: six inactive COO/S04/G04/T02/Hazel/C02. 30: add G05/C03/S02 = nine. 60: eighteen including COO/Integration/CoS/Planning/Game Head/both Game Leads/S04/G04/G05/T01/T02/Hazel/Idris + four contributors | Existing qualified mandates only. 20 one Commander, no explicit IC/IA; 30 no Commander; 60 loss of primary and reserve acting candidate plus both Commanders blocks executive coverage/live sessions; no perfect succession claim |

At 20 the Office improves normal administration but conflict-heavy demand can be WORSE: the same Head is Integration and cannot arbitrate their own resources. At 30 analysis/support work may exceed combined CoS allocation. At 60 seven permanent COO reports (four delivery plus three Office) increase coaching demands; the modeled overhead includes some executive review, but actual complexity could exceed it. All models retain outside operational OIO and scarce independent review. A larger Office does not repair platform ownership or create a second IA investigator.

## Detailed absence traces

Assume only for the positive branch that R14 is lawfully adopted, actual Owner signed the stated prior conditional appointment, the candidate accepted and is currently qualified/available, and records/access exist. The real repository proves none of these. Negative branch deliberately removes one condition.

| Absence | Participants / path / scope | Approvals and meaningful handoffs | Outcome and remaining blocker |
|---|---|---|---|
| COO 48h | CoS/records alternate logs agreed trigger; primary accepts existing conditional appointment; Heads keep routine mandates | One PRIOR Owner appointment; activation no fresh approval/H1. Existing Office domains continue | Conditional; without signature/available candidate executive exceptions defer, ordinary work continues |
| COO two weeks | Same, reconstruct shared exceptions; acting holder narrows primary duties and takes only authorized powers | No new appointment on valid activation; separate technical access approval/execution if needed | Acting 30-day/authorization expiry caps apply; 20/30 candidate loses original delivery capacity; not continuous staffing |
| COO resigns | Verified notice activates only expressly covered preexisting instrument; Owner starts normal permanent selection | Prior appointment plus later actual permanent appointment; Personnel/access handoffs | Term expiry without lawful renewal/replacement ends executive authority; no indefinite acting extension |
| COO and Owner | Prior signed mandate, no emergency self-appointment | P0 new/H1; no new Owner reserved powers | Conditional; native Owner control, ratification and extension remain blocked |
| Integration absent | Heads/domain owners continue, named unconflicted mandate alternate handles covered residual | Prior named delegation; P1 for actual arbitration/H1 | No named qualified alternate → COO/defer, modeled workload returns rather than disappears |
| CoS absent | Existing record owners maintain entries; Council chair names non-voting minute-taker | Administrative designation not policy approval; H1 | No compulsory extra reports; missed optional preparation can defer policy, no CoS acting-COO assumption |
| Planning absent | Heads read own accepted capacity; CoS can compile only accepted aggregate work | No fresh operating approval/H0–1 | Defer noncritical analysis if no capacity; no private-file access as shortcut |
| COO and Integration absent | Preauthorized reserve accepts only if actually qualified/unconflicted/available | One prior Owner conditional appointment; H1 | 20 reserve Safety Head, 30 Technical Lead, 60 Game Head are hypothetical assessed candidates; lose original duties, reduce services. Neither available → blocked executive-only work |
| Head and COO absent | Existing scoped Head coverage, or preauthorized acting COO appoints qualified acting Head | New Head appointment P1/H2 incl Personnel; access separate | No named qualified Head backup is asserted in fixture; local delegated tasks continue, consequential Head decisions may block |

## Structural comparison and decision counts

| Measure | A v1.2 | B v1.3 | C v1.4 |
|---|---|---|---|
| Delivery units | 6 directorates | 3 divisions + Office | Same consolidated delivery |
| Max intermediates contributor→COO | 4 with active ED/manager/lead | 2 | 2; no Office intermediary |
| 60-person unique permanent supervisors | 18 prior audit fixture | 13 | Computed current fixture; Office specialists have no invented reports |
| Cross-division owner | Active ED by portfolio, then COO | COO | Named domain first, then scoped Integration, COO reserved |
| Routine launch/moderation executive approvals | 0 | 0 | 0 |
| Former-boundary within-division transfer | 2 Director approvals | 1 Head | 1 Head; unchanged from B |
| Prepared succession | Nomination/actual appointor dependency | Same, no named coverage | Prior conditional appointment procedure and fictional assessed candidates, ACTUAL implementation unverified |
| Case separation | Required | Required | Required; qualified initial pool only after adoption, no stage removal |
| Council feasibility | Conditional ED seats/interim instrument | Proposed elected seats | Same elected seats with explicit acting-seat/chair rules; no Office seats |

## Findings addressed and remaining readiness

Critical corrections: bounded domain mandates remove covered COO decisions; Owner-preauthorized conditional succession avoids new appointment during Owner absence; senior pool removes default COO initial adjudication for Heads/Office; six-step performance process restored; obsolete target portfolio routes removed; legacy anchors point to meaningful content. None proves real availability. Consolidated functions, eight grades, one permanent manager, technical approval separation, protected case roles, volunteer consent and fair migration remain.

Five ranked residual risks: (1) legitimate ratification and actual Owner cooperation; (2) absent/overloaded qualified Office/acting coverage; (3) unstaffed independent investigators/external appeals/assurance; (4) native technical custody and confidential storage tests; (5) broad Head/working-Lead capacity and displaced delivery. No score uplift is assigned. A fresh auditor should challenge actual scope records, conflict rates, unresolved-decision age, candidate exercises, report duplication and real opportunity costs before claiming improved performance.

## Research and design basis

Reviewed 2026-11-02. These are published practices/guidance or research, not evidence this community achieved their outcomes.

| Primary source / date | Mechanism used | Adaptation and limit |
|---|---|---|
| [GitLab Chief of Staff](https://handbook.gitlab.com/job-description-library/chief-executive-officer/chief-of-staff/), living | Executive Office support and directed/self-directed coordination | Separate executive follow-through from operating line authority; GitLab's paid remit is not copied wholesale |
| [GitLab DRI](https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/), living | Explicit accountable owner and contributors | Domain owner with actual mandate, not a universal permission or committee |
| [Atlassian DACI](https://www.atlassian.com/team-playbook/plays/daci), living | Distinct Driver, Approver, Contributors and Informed | One binding owner; consultation/notification are not repeated approvals; no mandatory workshop |
| [Amazon Day 1](https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/), living | Team ownership and different treatment of reversible/consequential decisions | Local reversible scheduling vs reserved constitutional/personnel power; no speed statistic or employee commitment imported |
| [Google incident response](https://sre.google/workbook/incident-response/), 2018 | Separate command, operations and communications; prepared handover | Domain containment independent of executive preapproval; volunteer coverage not paid on-call |
| [Council on Foundations succession](https://cof.org/content/planning-ceo-succession), date not established | Identify priority duties, candidates and acting authority before absence | Prior actual authorization and consent; no copied nonprofit board powers or ownership transfer |
| [Reitzig delayering](https://link.springer.com/article/10.1007/s41469-022-00109-7), 2022 | Delayering needs changed delegation/work practices | Explicit distributed decisions; no universal optimum or measured ER:LC result |
| [NCVO volunteer roles](https://www.ncvo.org.uk/help-and-guidance/involving-volunteers/planning-for-volunteers/writing-volunteer-role-descriptions/), living | Clear role boundaries and realistic unpaid participation | Accepted capacity, no quotas; UK guidance not a universal legal conclusion |

Context7 checked current official Starlight manual sidebar slug/link/collapsed configuration. Existing source allowlist remains the publication boundary; hidden navigation is not confidentiality. No dependencies, platform or dashboard are added.

## Preservation and validation scope

Earlier releases and LICENSE remain byte-preserved except maintained document metadata. Original provenance/line hashes and v1.3 history remain unchanged. A v1.4 exact before/after amendment ledger records every changed preexisting Markdown source and validates replacements; historical preservation alone is not semantic equivalence. Additional current semantic, graph, decision, succession, case and workload negative checks test the R14 design. Actual test results are recorded below after execution; no live Discord/control test is claimed.

## Additional A/B/C workload comparison

For the same baseline executive work, one illustrative 60-person A routing assigns the following COO / two EDs combined / CoS hours, including extra interfaces: normal 4 / 1.5 / 1.5 = 7; high 6.5 / 6 / 1.5 = 14; incident 9 / 7.5 / 2.5 = 19; shortage 8 / 5 / 2 = 15; governance 7 / 2 / 3 = 12. Those are routing assumptions, not empirical ED productivity. ED hours displace the same volunteers' other work; portfolios are inactive at 20/30, so A retains the baseline COO pressure there. B has baseline 6/11/16/13/10h at COO. C final allocation is tabulated above. No model gets extra people or more availability merely because it has a title.

At 8h COO availability four high weeks give A zero COO backlog only if EDs accept the six combined hours, B 12h backlog, C zero only if Office/Head allocations hold. Mixed sequence A COO demands 6.5/9/8/6.5 produce backlog 0/1/1/0; B 3/11/16/19; C 0/0/0/0. At 4h, A high-week backlog 2.5/5/7.5/10, B 7/14/21/28, C .5/1/1.5/2. At 12h all three COO queues clear for four high weeks; that does not prove frontline or independent review coverage. C pays 1h of added busy-week coordination overhead; A pays 3h under these assumptions, but could outperform C if mature portfolio relationships reduce actual interfaces.

Semantic review corrected legacy appointment-template, assessment, staffing and leadership anchors to their actual restored subject. A valid fragment alone was not accepted as sufficient. Current-authority substitute chair uncertainty remains explicit instead of inventing a pre-reform rule.

## Executed repository verification — 2026-11-02

- Frozen Bun installation: 433 installs checked across 508 packages, no changes.
- Astro check: eight files, zero errors, warnings or hints.
- Production build/output verifier: 28 routes (26 explicit public specifications, license, 404); 1,823 local links/assets/fragments in the first completed build. Pages base, canonical URLs, sidebar, search, deployment YAML and publication/staging exclusions passed. Final post-review rerun is reported in delivery.
- Python Markdown/preservation: 39 Markdown files, 399 relative links/fragments; all 1,158 original baseline lines/48 ranges accounted for, five official releases, immutable historical 22 tables/14 fences/nine examples checked. This is historical preservation, NOT a claim current target procedures are text-identical.
- Current structure: 20/30/60 people, respectively 7/8/13 unique People Managers; maximum spans 4/7/9. Six structural negative mutations rejected.
- Executive semantic/workload validator: 22 negative cases rejected for missing/expired/conflicted succession, unauthorized/out-of-scope decisions, case self-review, Office reporting/availability/voting defects, disappearing workload and empty/stale references. Positive cases are fictional logic checks, not actual signatures or controls.
- The existing nonfatal Starlight 404 route-priority warning remains; expected 404 output is emitted and verified. No dependency upgrade or unrelated route redesign was introduced.
- No actual Discord test, external reviewer availability test, user study, Council vote, Owner signature, push or deployment was performed.

## Scale comparison with reconstructed pre-reform small fixtures

| Size | A/B/C total people | A/B/C permanent People Managers | A/B/C COO permanent reports | A/B/C maximum intermediate managers below COO |
|---|---|---|---|---|
| 20 | 20 / 20 / 20 | 7 / 7 / 7 | 6 / 4 / 4 | 1 / 1 / 1 |
| 30 | 30 / 30 / 30 | 9 / 8 / 8 | 6 / 4 / 4 | 1 / 2 / 2 |
| 60 | 60 / 60 / 60 | 18 / 13 / 13 | 3 / 4 / 7 | 4 / 2 / 2 |

A20/30 counts are an analytical reconstruction of the historical readiness fixtures: Owner, COO, T&S/Live/RP/Community working supervisors and Commissioner = seven at 20; added P&C and Technical direct reports make their functional owners supervisors at 30 = nine. ED/CoS inactive at those sizes. Six functional owners/coordinators report to COO; not every owner is a grade-06 Director. The 60-person A count comes from the original audit fixture, not a current live roster. B/C counts are computed from JSON manager IDs. This comparison exposes a regression: the illustrative 30-person Game People Lead adds a reporting intermediate relative to that lean A fixture. Its coaching workload must justify it. Capabilities in paired incident/review tests remain the same explicit available subset, never extra qualified recovery/review people merely because C has more generic technical contributors.
