# ER:LC Organization — Operating System & Structure

**Version:** 3.2.2 — full edition, integrated organizational ranks and appointments  
**Date:** 2 November 2026  
**Status:** Proposed full-structure edition for an independently operated ER:LC Discord/Roblox community; builds on v3.2.1 without changing its governance or reporting design  
**Scope:** Governance, personnel, directorates, team assignments, career progression, recruitment, oversight, staff experience, player participation, authority, and day-to-day operations.

> **Design objective:** Create a sizeable, professional community organization whose routine work can continue without the Owner's intervention. Authority comes from a defined assignment and mandate, not simply from having a more impressive Discord role.
>
> **Not a roleplay corporation:** These structures exist to improve member experience and accountability. A position should not exist purely to give someone a title.

---

## 1. Executive summary — the decisions made

The organization uses **six operating directorates**, **two executive portfolios**, **one five-seat Governance Council**, **one independent oversight office containing three protected functions**, and flexible functional teams. The Council sets cross-organization policy within its charter; the COO remains responsible for daily operations, and the Owner/CEO retains defined reserved powers. A person may serve in multiple teams while retaining **one home team and one permanent people manager**. Secondary team leads can assign work within the agreed scope but cannot independently promote, discipline, or reassign that person.

The old universal **Associate / Officer / Specialist / Principal / Distinguished** ladder and the separate **In Training / Qualified / Experienced / Senior / Expert** career-stage ladder are **retired**. Their replacement is one recognizable, eight-level **organizational rank hierarchy**, integrated with real jobs and management appointments:

`01 Staff Member → 02 Moderator → 03 Senior Moderator → 04 Administrator → 05 Senior Administrator → 06 Director → 07 Executive → 08 Owner / Chief Executive`

This is **one hierarchy of standing and appointment eligibility**, not eight successive jobs everyone must hold. The top three levels are **appointment-linked**: Directors hold grade 06, the COO and Oversight Commissioner hold grade 07, and the actual Owner/CEO holds grade 08. Grade 06 includes both Executive Directors and Directorate Directors; their reporting relationship still determines their actual managerial remit. There are **two direct executive reports to the Owner**—the COO and the Oversight Commissioner—with independent, non-interchangeable mandates. The Governance Council is a collective policy body, **not** another rank.

Each person has four separate records:

1. **Organizational rank** — one grade, used for standing and some eligibility thresholds, without blanket command power.
2. **Functional job title** — e.g. Game Enforcement Officer, Session Host, Investigator, Technical Lead.
3. **Appointment, if any** — e.g. Team Lead, Operations Manager, Director, Chief of Staff, Commissioner.
4. **Qualifications and delegated authority** — e.g. session command, enforcement certification, case review, evidence access, or a narrow technical permission.

**Design constraint:** Staff in non-moderation functions do **not** need to become moderators first to qualify for management. Subject-matter expertise remains a viable non-managerial career path. Rank requirements are either **directly linked to an appointment/job** or **a minimum eligibility threshold**; neither creates universal access across unrelated teams. See Section 6 for the full mapping and exception rules.

**Operating principles**

- One home team; one accountable people manager.
- Multiple approved work assignments are possible; conflicting orders are not.
- One decision owner for each important decision or project; the Governance Council is the single collective approver only for matters specifically assigned to it.
- Organization-wide rules receive cross-functional review without requiring CEO or COO approval for every routine decision.
- Authority is limited to the holder's remit, even for executives.
- Specialists can develop without being forced into management or into unrelated Moderator ranks.
- Ranks govern standing and eligibility; job appointments and case-specific qualifications govern actual command.
- Team sizes follow workload, not identical organizational charts.
- One independent oversight office coordinates Internal Affairs, Appeals & Member Advocacy, and Standards & Assurance, with strict separation of case decisions and evidence access.
- Staff well-being, meaningful volunteer participation, and player feedback are core operational responsibilities, not optional extras.
- Positions have an explicit mandate, appointment process, alternate, and termination/review rule.
- Qualifications grant specific capabilities; Discord technical access grants only what the person needs.

---

## 2. Organization chart and lines of accountability

```text
OWNER / CEO  [08 — Owner / Chief Executive]
│  Ownership and constitutional reserved powers
│
├── GOVERNANCE COUNCIL  [policy flow: CEO → Council → COO]
│   │  5 voting members: CEO, COO, both Executive Directors, Staff Representative
│   │  Chief of Staff = non-voting Council Secretary
│   └── APPROVED ORGANIZATION-WIDE POLICY ───────────────┐
│                                                      │ (implementation)
├── CHIEF OPERATING OFFICER (COO) [07 — Executive] ◄─────┘
│   │  Reports directly to CEO; remains operating superior of both portfolios
│   │
│   ├── CHIEF OF STAFF  [05+ — Senior Administrator; DIRECT report to COO]
│   │   Executive coordination, cross-directorate follow-through,
│   │   Council agendas/minutes and policy implementation tracking
│   │   (supports portfolios; no line authority over directorates)
│   │
│   ├── EXECUTIVE DIRECTOR — OPERATIONS [06 — Director]
│   │   ├── Trust & Safety Directorate
│   │   ├── Live Operations Directorate
│   │   └── Roleplay Programs Directorate
│   │
│   └── EXECUTIVE DIRECTOR — COMMUNITY & SERVICES [06 — Director]
│       ├── Community Experience Directorate
│       ├── People & Culture Directorate
│       └── Technology & Systems Directorate
│
└── OFFICE OF INDEPENDENT OVERSIGHT  [DIRECT to CEO; outside COO/Council]
    └── Oversight Commissioner [07 — Executive]
        ├── Internal Affairs & Investigations
        ├── Appeals & Member Advocacy
        └── Standards & Assurance
```

**Rank overlay on the organization chart:** All six Directorate Directors also hold **06 — Director**; their supervising Executive Director holds the **same organizational grade 06**, but possesses a **different, portfolio-level appointment**. The reporting arrow—not the shared grade—determines supervisory authority. The Chief of Staff normally holds **05 — Senior Administrator** and is **not** a superior of any Director. The Oversight Commissioner shares grade 07 with the COO but is **not** in the COO's command chain. The Owner alone holds grade 08. Rank labels are a secondary overlay, not extra boxes or fictional staff positions.

**Two different relationships must be drawn in Atlas:**

- **Policy/decision flow:** `CEO → Governance Council → COO → operating directorates`. This is why the Council is positioned **visually between CEO and COO** and connected to both. The arrow from Council to COO means *approved policy is implemented by the COO*, **not** that the Council is the COO's line manager.
- **People/reporting flow:** `CEO → COO → Executive Directors → six Directors`; also `COO → Chief of Staff`. The CEO also appoints the **Oversight Commissioner**, whose office is separate from COO/Council command. The Chief of Staff has **one supervisor (COO)** and acts as non-voting Council Secretary.

**Visualization rule:** Never render the Governance Council as a floating unconnected node. Show its policy connections with a **distinct dotted or labeled edge**; use solid edges for reporting lines. Likewise, show the Chief of Staff as a **direct COO report** with support links to executive portfolios and a secretary link to the Council. A support link must not imply supervisory authority.

### 2.1 Governance Council — charter and participants

**Official name:** Governance Council (GC). **Purpose:** Provide a small, accountable body for establishing and maintaining **organization-wide** rules, rather than requiring the Owner/CEO or COO to design and approve every policy alone. It is a governing forum with delegated collective decisions, **not** a board of corporate directors, a separate directorate, or an additional rung in the staff command ladder. **Atlas placement:** Visually place the Council on the policy path between the CEO and COO, connect its policy outputs to the COO, and preserve the COO’s direct reporting line to the CEO.

#### Membership — five voting seats

| Seat | How the seat is filled | Contribution and responsibility | Boundaries |
|---|---|---|---|
| **Owner / Chief Executive Officer (CEO)** | Ex officio: the server Owner, or the person formally designated by the Owner to exercise this seat; ownership-reserved actions remain with the actual Owner | Sets strategic direction, identifies constitutional/ownership issues, ensures the Council's policy work supports the community, ratifies reserved changes | Cannot use a Council vote to remove the Discord Owner's actual technical control; should not bypass published governance rules casually |
| **Chief Operating Officer (COO)** | Ex officio by appointment as COO; **chairs ordinary meetings** | Brings operational problems, tests feasibility and staffing impact, assigns implementation ownership, ensures cross-directorate decisions are put into practice | Does not gain extra votes as chair; retains ordinary executive authority for routine operations without consulting the Council |
| **Executive Director — Operations** | Ex officio while holding that portfolio | Represents Trust & Safety, Live Operations and Roleplay Programs; evaluates enforcement, session delivery, RP consequences and operational risks | Must consult the affected directors; does not personally replace their routine decision authority |
| **Executive Director — Community & Services** | Ex officio while holding that portfolio | Represents Community Experience, People & Culture and Technology & Systems; tests personnel, member-experience, technical, access and resource implications | Cannot grant privileged Discord access by Council vote alone or bypass technical-access approval |
| **Staff Representative** | Elected by **non-executive organizational staff** for a six-month term; the electorate and eligibility list are published before the ballot | Brings frontline workload, fairness, clarity and volunteer-retention concerns to policy debates; can introduce proposals, request consultations and **casts one equal vote** | Represents staff perspectives rather than acting as their personnel manager; receives no extra moderator, investigator or administrator permissions |

**Staff Representative selection and accountability:** Rank alone does not determine Council voting eligibility or the strength of a vote. Candidates must be active organizational staff, outside the CEO/COO/Executive Director and independent oversight-head positions, with sufficient service to understand operations (suggested: **60 days**). Staff elect one representative by confidential ballot, using one vote per eligible staff member; most votes wins, with a runoff for a tie. The representative keeps their normal Home Team, People Manager and primary work. They serve **six months**, may seek re-election, and should collect feedback across *all* directorates, not just their own. If the seat becomes vacant, run a replacement election for the remainder of the term. Define an objective misconduct/removal procedure and independent appeal before the first election; the COO must not be able to dismiss an inconvenient representative unilaterally.

#### Non-voting participants and advisers

| Participant | When present | Contribution | Restrictions |
|---|---|---|---|
| **Chief of Staff — Council Secretary** | All ordinary meetings, or an authorized alternate; administratively reports to COO | Sets agendas with the chair; circulates drafts; tracks consultations, attendance, votes, minutes, implementation owners and review dates | **No vote, no casting vote, no automatic policy-approval authority**; is not an extra executive superior |
| **Oversight Commissioner** | Invited for changes affecting independent oversight, its charter, budgets or structural safeguards | Explains office-wide risks, coordination requirements and conflicts; may submit a written objection | **No vote**; may not disclose confidential case information or trade case outcomes for policy concessions |
| **Internal Affairs lead / investigator** | Invited when proposals affect staff-misconduct investigations or evidence integrity | Advises on investigation independence, recusal and evidence handling | **No vote**; participates only on relevant policy, never on the outcome of a pending case |
| **Appeals & Member Advocacy lead / reviewer** | Invited when proposals affect appeals, discipline or due process | Advises on fair process, appeal rights and review consistency | **No vote**; individual appeals remain outside Council control |
| **Standards & Assurance lead / assessor** | Invited for systemic audit, quality or permission-control proposals | Advises on policy coherence, auditability, risk controls and systemic failures | **No vote**; cannot become the policy's executive implementer and then audit their own work |
| **Affected director, specialist or member representative** | Invited only for a relevant agenda item | Explains operational effects, offers expertise or submits feedback | **No vote**; attendance creates no permanent Council office or new chain of command |

Advisers may submit a **written dissent or risk note** for the policy register. The Council must consider material concerns, but advisory status does not make the Office of Independent Oversight subordinate. **The Oversight Commissioner and all three functional leads are non-voting**; they do not approve systems they will later investigate, hear on appeal, or audit. The relevant functional expert—not automatically the Commissioner—should advise where specialist independence matters.

#### Delegated authority: what the Council decides

**Council approval required for:**

1. Organization-wide staff conduct, recruitment, promotion, training, participation and discipline **frameworks** (not decisions about an individual person).
2. Policies applying to multiple directorates, including cross-team authority, information handling, major member-facing standards and escalation procedures.
3. Material restructuring of operating directorates, recurring changes to executive reporting arrangements, or new cross-organizational governance functions, **subject to Owner-reserved powers**.
4. Organization-wide adoption or retirement of policy systems, and periodic review of policies already approved by the Council.
5. Significant unresolved *policy* disagreements between portfolios after executive-level attempts to reconcile them.

**Outside the Council's remit:** Routine session scheduling, ordinary moderation decisions, individual RP promotions, team-level procedures consistent with existing policy, daily hiring within approved vacancies, technical execution of Discord roles, personnel management, individual investigations, individual appeals and emergency incident command. These continue under their designated decision owners. The Council cannot order IA to close a case, overturn an independent appeal, access private evidence as a group, or interfere with an active investigation. Council members who hold separate case authority exercise it only through that separate role and its safeguards.

**Owner-reserved matters:** The Owner/CEO retains actual ownership and technical control; appointment/removal of the COO and Oversight Commissioner; transfer of ownership; and any constitutional change to these reserved powers or the Office of Independent Oversight charter. The Council can **recommend** such changes, but they require both the specified enhanced Council vote and explicit Owner ratification. The Owner can technically act without the Council, but departures from the agreed governance process should be exceptional, logged with reasons and reviewed transparently insofar as confidentiality permits.

#### Meetings, voting and conflicts

- **Ordinary meeting:** Once a month, with extra meetings when a substantive cross-organization issue warrants one. Async deliberation/voting is valid if the same notice, quorum and recordkeeping requirements are met. Avoid meetings just to announce routine actions.
- **Agenda and consultation:** A proposal names one Driver, a policy owner, the problem, intended effect, affected groups, foreseeable costs/risks, implementation date and planned review date. Share the draft with affected directors and the Staff Representative, normally allowing **at least 48 hours** for feedback before a final vote. The Chief of Staff keeps the record.
- **Quorum:** **Four of the five voting seats**, including at least one of CEO/COO and one Executive Director. An absent seat is not silently reassigned. If an Executive Director position has not yet been activated, the Owner must formally adopt an interim Council membership/quorum charter; do not pretend an empty seat cast a vote.
- **Normal organization-wide policy:** At least **three affirmative votes** from the five voting seats, with quorum met. Abstentions are not approvals; a tie or insufficient affirmative votes means no adoption. The chair has **no casting vote**.
- **Major structural changes:** At least **four affirmative votes** from the five seats, with quorum met. Changes to the constitution, Owner-reserved authority or the Office of Independent Oversight charter also require **explicit Owner ratification** and consultation with the Oversight Commissioner and affected functional leads.
- **Conflicts and recusal:** A member with a personal conflict declares it and does not vote on that item. If too few unconflicted members remain to meet quorum, defer the vote or follow a documented Owner-reserved conflict-resolution process with independent advice; do not manufacture substitute votes. Policies must never be used to determine the outcome of a named person's pending case.
- **Recording and publication:** Record attendance, conflict declarations, draft version, summary of consultation, votes (including abstentions), objections, final text, effective date, implementation owner and review date. Publish non-sensitive rules and decision summaries in an accessible Discord channel or policy registry; keep genuinely sensitive details in a restricted register.
- **Temporary urgent policy:** During a genuine time-sensitive safety or platform-security issue, the COO may impose a narrowly scoped **temporary operating measure** for up to **seven days**, notify the Council promptly and submit it for review. Extending it beyond seven days requires Council approval unless actual Owner/platform obligations necessitate immediate protective action; log any Owner exception. This does not let the COO or Council seize control of individual IA/appeal cases.

#### Example policy lifecycle

```text
Staff / director / oversight adviser raises an organization-wide issue
     ↓
Named Driver drafts proposal; relevant directors and Staff Representative review
     ↓
Independent oversight adviser consulted if their remit is affected
     ↓
Governance Council debates and votes under its published thresholds
     ↓
Owner ratifies only if the decision touches reserved constitutional powers
     ↓
COO designates implementation owner; directorates publish and train
     ↓
Chief of Staff tracks effective date, feedback and periodic policy review
```

**Who is accountable afterward?** The **Council** is responsible for the collective *policy decision*; the **COO** is accountable for cross-directorate execution; the assigned **Director** owns delivery inside their portfolio; **Standards & Assurance** may later audit compliance independently. The Council does not replace their chain of command.

### 2.2 Why add these leadership positions?

| Appointment | Actual responsibility | What it cannot do |
|---|---|---|
| **Governance Council (collective body)** | Approves cross-organization rules, major operating restructures and designated governance standards by a documented vote | Direct staff as a new managerial layer; decide individual cases; take over daily operations |
| **COO** | Runs daily operations, resolves portfolio conflicts, executes approved cross-organizational policy, oversees executive directors | Suppress independent investigations; unilaterally change the constitution |
| **Executive Director — Operations** | Supervises three high-activity directors; balances moderation, sessions and RP staffing; manages cross-functional incidents | Override an Internal Affairs finding or member appeal |
| **Executive Director — Community & Services** | Supervises community, personnel and technical services; balances support, hiring and platform priorities | Grant self-approved technical privileges; overrule independent oversight |
| **Chief of Staff** | Grade 05+; direct report to COO; coordinates executive priorities, follows up on directorate action owners, prepares Council agendas and minutes as its non-voting Secretary | Become a second COO, command directors, discipline staff, independently approve policy or overrule their decisions |
| **Oversight Commissioner** | Leads one independent office, maintains conflict/recusal rules, assigns intake to protected functions and reports systemic risks to the Owner | Direct an investigation's findings, reverse an appeal on personal preference, adjudicate their own conduct or demand blanket case access |
| **Internal Affairs lead** | Oversees independent staff-misconduct investigations and evidence integrity within the office | Serve as the sole disciplinary adjudicator or hear an appeal of their own investigation |
| **Appeals & Member Advocacy lead** | Oversees independent reviews of contested enforcement/personnel decisions and fair-process concerns | Review their own earlier action or secretly rewrite disciplinary records |
| **Standards & Assurance lead** | Reviews systemic policy, training, governance and access-control weaknesses | Retake routine moderation decisions or audit their own implementation work |

**Important:** Only the **Oversight Commissioner** is an independent office head reporting directly to the Owner, not to the COO or Governance Council. The three functional leads work inside that office, but the Commissioner cannot command findings, appeal outcomes or audit conclusions. Cases involving the Commissioner or a conflicted functional lead go to an **Owner-appointed, unconflicted external reviewer** under a prepublished recusal procedure—not to the accused person's subordinate. Where the Owner is the subject of a dispute, an advisory independent review panel may publish findings, but a Discord server Owner retains ultimate technical control; absolute independence from ownership cannot be guaranteed.

### 2.3 Chief of Staff — reporting and exact mandate

**Reports to:** COO (direct, permanent administrative supervisor). **Organizational rank:** Senior Administrator (05) minimum, without a Director appointment or supervisory control over directors. **Council connection:** Non-voting secretary to the Governance Council. **Works with:** Both Executive Directors and the six Directorate Directors through *coordination requests*, not their personnel reporting lines.

| Chief of Staff is responsible for | Chief of Staff is **not** authorized to do |
|---|---|
| Maintain COO's weekly executive priorities, action register, deadlines and issue log | Replace the COO or act as a superior to Executive Directors by title |
| Prepare the COO's briefings, track work promised by portfolio leaders, flag unresolved blockers to COO | Order a director to alter operational priorities without a COO decision |
| Prepare Council agendas, circulate policy drafts, log votes, publish non-sensitive decisions | Vote on the Council, veto policies or decide an individual case |
| Track the named implementer of approved Council policies and request progress updates | Give investigations, appeals or assurance findings instructions |

**Escalation:** If a director does not provide a requested status update or disputes an action, the Chief of Staff records the blocker and asks the **COO** for a decision. They do not issue their own disciplinary or managerial order. **Staffing:** one Chief of Staff, not a standalone directorate, with no mandatory assistants.

**Lean operation:** Governance Council seats are **appointments held concurrently with existing work**, not five new full-time positions. Executive Director appointments activate when the COO genuinely needs an intermediate manager (for example, numerous active directors and frequent cross-directorate conflicts). Until then, each director may report directly to the COO. The chart shows the **target organization**, not mandatory bureaucracy at launch.

---

## 3. The six operating directorates

The staff ranges below are **illustrative planning bands**, not minimum headcounts or evidence-based universal industry standards. One coordinator can own a low-volume function; high-volume teams can split into multiple staffed squads.

### 3.1 Trust & Safety Directorate

**Director:** Director of Trust & Safety (grade 06 — Director)  
**Reports to:** Executive Director — Operations (grade 06 — Director; portfolio appointment)  
**Mandate:** Consistent, fair enforcement of community and in-game rules; case quality; safety response.

| Team or function | Roles and hierarchy | Staffing pattern |
|---|---|---|
| **Discord Moderation** | Discord Moderation Lead → Senior Discord Moderators → Discord Moderators; trainee placement if needed | One or multiple coverage teams; approx. 5–10 total to start scaling |
| **Game Enforcement** | Game Enforcement Manager → Game Enforcement Team Leads → Senior Enforcement Officers / Enforcement Officers | Often the largest enforcement function; scale by session coverage; approx. 6–14+ |
| **Case Operations** | Case Coordinator → Case Reviewers / Evidence Custodians | Compact expert team; approx. 1–4 |
| **Critical Incident Response** | Duty Incident Commander + cross-trained responders from existing teams | **Rotation**, not necessarily a permanent extra team |

**Owns:** Warnings, routine discipline, evidence review, game and chat enforcement, incident escalation and enforcement playbooks.  
**Does not own:** Police department promotions, scheduling ordinary sessions, independent appeals, hiring decisions outside its own positions.

**Separation:** Case Operations handles evidence and internal quality checks; allegations of staff misconduct go to **Internal Affairs within the Office of Independent Oversight**. Ordinary moderation appeals go to its **Appeals & Member Advocacy** function, not to the deciding moderator or Case Operations. Trust & Safety Case Operations audits its own evidence quality, not staff integrity or independent appeal outcomes.

### 3.2 Live Operations Directorate

**Director:** Director of Live Operations (grade 06 — Director)  
**Reports to:** Executive Director — Operations (grade 06 — Director; portfolio appointment)  
**Mandate:** Reliable, well-staffed and enjoyable ER:LC sessions.

| Team or function | Roles and hierarchy | Staffing pattern |
|---|---|---|
| **Scheduling & Dispatch** | Dispatch Coordinator → Schedulers / Dispatch Officers | Compact: approx. 1–4 |
| **Session Operations** | Session Operations Manager → Squad Commanders → Session Controllers / Session Hosts | **Multiple active squads**, each with roughly 4–7 people when full |
| **Session Quality & Readiness** | Quality Coordinator → Session Reviewers / Readiness Coaches | Approx. 1–4; part-time reviewers possible |

**How squads work:** Team Alpha, Bravo, Charlie, etc. have their own Squad Commander and can run assigned session blocks independently. The Operations Manager owns overall performance; each Squad Commander controls the live session they have been assigned. A staff member can be a primary Session Host in Alpha and a secondary trainer or enforcement responder elsewhere.

**Owns:** SSU/SSD scheduling and execution, host readiness, session coverage, live operations quality.  
**Does not own:** Permanent bans, personnel disciplinary judgments, roleplay department membership policies.

**Boundary with independent oversight:** Session Quality & Readiness checks host preparation, session procedures and immediate coaching. It does **not** independently investigate staff abuse or audit the whole organization; those issues are referred to the relevant Office of Independent Oversight function.

**Operational emergency exception:** A Session Commander may use specifically qualified, time-limited safety actions (e.g. temporary removal of an active disruptor) within written rules; lasting enforcement action remains with Trust & Safety.

### 3.3 Roleplay Programs Directorate

**Director:** Director of Roleplay Programs (grade 06 — Director)  
**Reports to:** Executive Director — Operations (grade 06 — Director; portfolio appointment)  
**Mandate:** Department programs, player-facing RP opportunities, coordinated standards.

| Program | Structure | Staffing pattern |
|---|---|---|
| **Law Enforcement Program** | Program Commander → Deputies / Unit Supervisors → RP personnel | Expandable large roster |
| **Fire & EMS Program** | Program Commander → Deputies / Unit Supervisors → RP personnel | Expandable large roster |
| **Transportation / DOT Program** | DOT Program Coordinator → Supervisors / RP personnel | Coordinator-led until growth |
| **Civilian RP Program** | Civilian Program Lead → RP Coordinators / participants | Flexible |
| **Roleplay Standards** | RP Standards Lead or Coordinator → Evaluators / Trainers | Compact: approx. 1–3 |

**Crucial distinction:** Roleplay department members are generally **players**, not automatically organizational staff. A police department's roleplay rank is separate from a Discord staff qualification, team membership, or personnel authority.

**Owns:** Department standards, membership systems, departmental qualifications, internal RP promotions and RP programming.  
**Does not own:** General Discord moderation, global bans, server infrastructure, or independent staff-misconduct investigations. **Roleplay Standards** sets RP-specific vehicle, uniform, conduct and qualification rules; independent Standards & Assurance examines systemic compliance and governance failures rather than running RP standards day-to-day.

### 3.4 Community Experience Directorate

**Director:** Director of Community Experience (grade 06 — Director)  
**Reports to:** Executive Director — Community & Services (grade 06 — Director; portfolio appointment)  
**Mandate:** Member experience, onboarding, support, community culture and healthy growth.

| Team | Roles | Staffing pattern |
|---|---|---|
| **Member Services** | Support Manager or Lead → Support Officers / Onboarding Assistants | Can scale to shifts; approx. 3–8 |
| **Community Engagement** | Engagement Lead → Events Coordinators / Communications Officers | Combined event and communications function; approx. 2–5 |
| **Player Voice & Improvements** | Player Feedback Coordinator (may be an existing Engagement/Support officer) → rotating topic owners | **Standing function, not automatically another team**; approx. 1 coordinator plus existing contributors |
| **Partnerships & Growth** | Partnerships Coordinator → Outreach Officers | One-person function until needed; approx. 1–3 |

**Owns:** Questions, member onboarding, ticket intake, announcements, events, partnerships, **player feedback intake, community consultation and the public improvements register**.  
**Does not own:** Final punishment appeals, private investigations or unilateral policy changes. Support forwards confidential complaints to the appropriate enforcement or independent oversight function.

#### 3.4.1 Player Voice & Public Improvement Framework

**Accountable owner:** Director of Community Experience. **Day-to-day Driver:** Player Feedback Coordinator, ordinarily an existing Community Engagement or Member Services contributor. **Decision owners:** The directorate responsible for each suggestion; the Governance Council only when a proposed change is organization-wide. This is a **process**, not an additional Council seat or mandatory managerial layer.

1. **Continuous intake:** Offer one accessible suggestion channel/form with categories for session experience, RP programs, Discord usability, events and general ideas. Allow private feedback when needed; send reports of abuse, bans and sensitive complaints to the proper case/appeal route instead of posting them publicly.
2. **Triage and ownership:** Merge duplicates, remove harassment/private data, distinguish bugs from ideas, assign one responsible directorate and record the next review point. Aim to acknowledge actionable submissions within **seven days when staffed**; this is a service target, not an enforceable promise.
3. **Monthly open consultation:** Run a short town-hall thread, voice Q&A, structured poll or equivalent on **one or two concrete topics**, with an asynchronous option for players who cannot attend. Publish the question, relevant constraints and a brief summary of arguments. Polls inform decisions; they do not automatically override safety rules or leadership authority.
4. **Quarterly pulse survey:** Ask a few repeatable questions about session quality, accessibility of activities, fairness, onboarding and priorities. Separate staff experience surveys from player surveys. Do not collect real names or unnecessary identifying data; use aggregated results and acknowledge selection bias.
5. **Public improvement tracker:** Publish a readable issue, description, responsible team, last update and status: `Received → Reviewing → Planned → In Progress → Implemented`, or `Declined / Not Now` with a concise reason. Not every suggestion becomes a promise. Sensitive abuse reports, evidence and personnel matters **never** appear on the public tracker.
6. **Close the loop:** Review open items at least **monthly**, publish a short `You said / We did / Why not` update, and link implemented changes to the original feedback. When multiple directorates or organization-wide policy are affected, submit a properly scoped proposal to the Governance Council.

**Fairness rule:** Players may criticize policies without retaliation. Moderation remains available for harassment, spam and private-information exposure. Do not publish individual disciplinary outcomes as proof that feedback was acted on.

**Success signals:** Number of actionable themes addressed, implementation/update timeliness, repeat player concerns, survey response coverage and player-reported experience; **not** raw suggestion counts or promises to fulfill every request. Public summaries must be understandable without internal management terminology.

### 3.5 People & Culture Directorate

**Director:** Director of People & Culture (grade 06 — Director)  
**Reports to:** Executive Director — Community & Services (grade 06 — Director; portfolio appointment)  
**Mandate:** Fair staffing processes, capability development, workforce allocation, retention, volunteer well-being and records.

| Team | Roles | Staffing pattern |
|---|---|---|
| **Talent Acquisition** | Recruitment Lead / Coordinator → Recruiting Officers and Assessors | Approx. 1–4 |
| **Learning & Development** | Training Lead → Trainers / Qualification Assessors | Approx. 2–5 |
| **Personnel Operations** | Personnel Manager → **Workforce / Assignment Coordinator**, Records Coordinator | Approx. 1–4 |
| **Staff Experience & Retention** | Staff Experience Coordinator / existing Personnel Operations lead; trained peer mentors when available | **Dedicated responsibility**, initially combined with Personnel Operations rather than automatically adding headcount |

**The Workforce / Assignment Coordinator is a new key role.** They maintain the shared capacity calendar, map primary and secondary assignments, flag over-allocation and facilitate handoffs. They do not become a second boss for everybody and cannot override operational team leads.

**Owns:** Vacancy process, recruitment administration, onboarding records, approved assignments, career framework, training coordination, allocation consistency, **staff experience, retention and voluntary-availability safeguards**.  
**Does not own:** Operational task priorities within another team, unilateral appointments of every directorate's specialists, individual independent appeals or disciplinary findings.

#### 3.5.1 Staff Experience & Retention Framework

**Accountable owner:** Director of People & Culture. **Process owner:** Staff Experience Coordinator (may initially be the Personnel Operations Manager). **Personal support:** Each staff member's **one Home People Manager**. **Independent challenge:** The elected Staff Representative may raise systemic issues to the Governance Council; suspected abuse of authority goes to Internal Affairs, not to a manager implicated in the report.

| Stage / cadence | Practical action | Responsible party | Constraint |
|---|---|---|---|
| **Joining / first two weeks** | Clear job expectations, accessible SOPs, named mentor/contact, initial supported tasks and an opt-in availability discussion | Receiving team + Learning & Development | No invented mandatory weekly hours |
| **Around day 30 and day 90** | Short private check-in on workload, training, belonging, friction and role fit | Home People Manager | Staff may request a different unconflicted contact through People & Culture |
| **Quarterly** | Optional lightweight staff pulse survey and manager check-in; summarize themes and propose fixes | Staff Experience Coordinator | Publish aggregates, never identifiable individual responses |
| **Continuously** | Flexible leave/break process, respectful re-entry after absence, optional peer mentoring and constructive recognition | Home People Manager + Staff Experience | Never require medical explanations or public disclosure of personal difficulties |
| **When work changes** | Review primary/secondary duties, cover gaps, and reduce or pause commitments when someone becomes overloaded | Workforce Coordinator + relevant leads | Previously accepted live duty gets a safe handoff, not guilt-based pressure |
| **Leaving / transfer** | Optional non-punitive exit feedback, clean access removal and alumni/rejoin pathway where suitable | Personnel Operations | Do not turn a voluntary exit into a misconduct record |

**Core standards**

- **Volunteer-first expectations:** Publish what *each role actually needs* (for example, availability for a scheduled session), distinguish opt-in commitments from enforceable platform-safety obligations, and never treat a hobby as an employment contract. The default remains **one primary and one active secondary assignment**; exceptions need consent and workload review.
- **Recognition and advancement:** Highlight meaningful contributions, mentoring, reliability and improvements to player experience—not punishment counts, message volume or hours online. Offer specialist development and lateral moves instead of pressuring everyone into management.
- **Support and burnout prevention:** Make it easy to request a pause, reduced scope, training help, conflict mediation or a manager change without public embarrassment. Ask what support the volunteer wants; do not require disclosure of health or private circumstances.
- **Inactive roster handling:** Contact someone privately, clarify whether they wish to remain active, offer leave or reassignment, and use a published administrative inactive-status process if no response follows. Repeated missed *accepted* duties can trigger a fair readiness review; mere low activity is not automatically misconduct.
- **Manager accountability:** People & Culture coaches managers and checks for unreasonable demands. It does **not** create a second line manager or overrule a qualified host lead mid-session. Formal misconduct allegations go to the independent office; routine disagreements use normal management and personnel procedures.
- **Confidentiality:** Store individual feedback and availability narrowly; restrict access to the Home People Manager and authorized People & Culture staff on a need-to-know basis. Publish only sufficiently aggregated trends; small groups where staff can be identified should be combined or omitted.

**Quarterly review indicators:** Voluntary retention by cohort/team, departures and stated reasons where voluntarily supplied, coverage reliability, time-to-qualification, use of leave/breaks, unresolved workload concerns, and pulse-survey themes. Treat these as **signals for improvement**, not quotas or grounds for ranking individual volunteers. People & Culture shares a short anonymized summary with the COO and Governance Council and owns the follow-through.

### 3.6 Technology & Systems Directorate

**Director:** Director of Technology & Systems (grade 06 — Director)  
**Reports to:** Executive Director — Community & Services (grade 06 — Director; portfolio appointment)  
**Mandate:** Dependable Discord platform, bot automation, data reporting and access implementation.

| Team or function | Roles | Staffing pattern |
|---|---|---|
| **Platform Engineering** | Technical Lead → Bot Developer / Systems Developer | Approx. 1–4 |
| **Infrastructure & Access** | Systems Administrator / Access Coordinator | Approx. 1–2 |
| **Operational Analytics** | Data & Reporting Analyst | One person initially; approx. 1–2 |

These may share one lead when compact. Technical security implementation belongs here; **independent audit of security controls** belongs to the Office of Independent Oversight’s Standards & Assurance function.

**Owns:** Bots, integrations, roles/channels configuration, permission execution, server reliability, data/reporting tools.  
**Does not own:** Changing organizational policy by editing Discord permissions; unreviewed acquisition of broad case evidence.

---

## 4. Office of Independent Oversight — one office, three protected functions

**Official name:** Office of Independent Oversight (OIO). **Reports to:** Owner/CEO, outside the COO and Governance Council command chain. **Office head:** Oversight Commissioner (**grade 07 — Executive**, by appointment), appointed by the Owner under a published eligibility, conflict and removal procedure. The Office consolidates governance support and intake; it does **not** merge investigation, appeal adjudication and systemic audit into one person's authority.

### 4.1 Internal organization, appointments and staffing

```text
OWNER / CEO  [appoints Commissioner; cannot guarantee technical independence]
    │
    └── OFFICE OF INDEPENDENT OVERSIGHT
        ├── Oversight Commissioner  [administration, routing, safeguards]
        ├── Internal Affairs & Investigations
        │   └── IA Lead / Investigator(s)  [independent fact-finding]
        ├── Appeals & Member Advocacy
        │   └── Appeals Lead / Reviewer(s)  [independent case review]
        └── Standards & Assurance
            └── Assurance Lead / Assessor(s)  [systemic audits]
```

| Function | Accountable role | Does | Does not |
|---|---|---|---|
| **Office coordination** | **Oversight Commissioner** | Maintains common intake/triage, staffing, recusals, secure registers, deadlines and aggregate reporting; appoints a case lead **only if unconflicted** | Choose guilt, dictate findings, veto appeal outcomes, audit own decisions or automatically open every confidential file |
| **Internal Affairs & Investigations (IA)** | IA Lead / appointed investigator | Investigates alleged organizational staff abuse, corruption, retaliation and serious conflicts; produces documented factual findings and recommendations | Impose the final disciplinary sanction as sole investigator and judge; review appeals of its own investigations |
| **Appeals & Member Advocacy** | Appeals Lead / appointed reviewer | Independently reviews contested enforcement/personnel outcomes and procedural fairness; recommends or orders remedies **within the approved appeal charter** | Re-investigate staff misconduct as IA, hear a case in which they participated, or change records without a logged authorization |
| **Standards & Assurance** | Assurance Lead / assessor | Audits systemic process, training standards, recurring defects, records practices and access controls; publishes corrective recommendations | Manage sessions, replace RP/Session Quality staff, adjudicate individual cases or investigate misconduct as the ordinary case owner |

**Staffing for approximately 60 organizational staff:** Start with **three unique OIO personnel if capacity permits**: (1) Commissioner who also performs *limited* systemic assurance work, (2) IA investigator/lead, (3) Appeals reviewer/lead. This preserves the blueprint's illustrative three-person oversight allocation. The Commissioner **must not audit the Commissioner's own work**, and any Commissioner-related audit requires an unconflicted independent assessor. For a sustained caseload, add a distinct Assurance Lead (fourth position) or qualified alternate reviewers. A unit may be a **function with one qualified specialist**, not a manager plus a fictional team. Multiple roles in one person are allowed only when there is no conflict within an individual case and a documented independent alternate exists. If that cannot be guaranteed, pause/refer the case rather than claim it received independent review.

The Commissioner is the **single accountable administrative head**. Functional leads have protected professional discretion in their own cases: the Commissioner can enforce procedure and request documented correction of process errors, but may not secretly rewrite findings, order a desired outcome or deny appeal intake to protect executives. Serious interference is reportable directly to the Owner under the independent reviewer protocol.

### 4.2 One intake, one case owner — jurisdiction and referrals

A single OIO intake route may accept confidential complaints, appeals and systemic reports. **Triage classifies and routes** them without giving a general triage volunteer unrestricted access to all underlying evidence. An incident may generate separate linked records with different scopes; one unit remains the **primary case owner for each question**.

| Incoming matter | Primary owner | Other participants / referral boundary |
|---|---|---|
| Ordinary Discord/game rule violation, player warning or ban | **Trust & Safety** | Case Operations checks evidence/process internally; an appeal can be filed with OIO Appeals |
| Appeal of a warning, ban or personnel outcome | **OIO — Appeals & Member Advocacy** | Original decision owner provides record; reviewer was uninvolved and is not under the initial decision-maker's direction |
| Alleged staff abuse, corruption, retaliation or fabricated evidence | **OIO — Internal Affairs** | An authorized **unconflicted adjudicator outside the IA fact-finding role** decides disciplinary action; appeal goes to a different reviewer |
| Session host readiness, quality coaching or ordinary session procedure | **Live Operations — Session Quality & Readiness** | Refer systemic breakdown to OIO Assurance; possible staff abuse to IA |
| Police/Fire/DOT/Civilian RP uniforms, vehicles, training or program criteria | **Roleplay Programs — Roleplay Standards** | OIO Assurance reviews repeated governance failures, not day-to-day RP standards decisions |
| Repeated policy inconsistency, data-access risk or quality-control failure | **OIO — Standards & Assurance** | May recommend corrections to director/COO/GC; suspected staff misconduct gets a separate IA referral |
| Community ideas, polls, experience concerns without misconduct claims | **Community Experience — Player Voice & Improvements** | Track publicly only nonsensitive issues; organization-wide policy proposals go to the Governance Council |
| Staff workload, mentoring, leave or ordinary conflict over assignments | **People & Culture — Staff Experience & Retention** | Separate personnel route; report coercion/retaliation to IA, not a conflicted manager |

**Anti-duplication rule:** When a referral crosses units, record `(a) the owner for each question, (b) what evidence can be shared, (c) why a linked record is needed, and (d) which outcome each unit may decide`. Do not launch three full investigations for one ordinary case. A misconduct report and the appeal of the underlying player ban can proceed separately if their decision questions differ; coordinate only as confidentiality and fairness permit.

### 4.3 Decision integrity and safeguards

- **Separation of duties:** IA investigates facts; an independently authorized and unconflicted adjudicator determines consequences. Appeals reviews the original decision and may refer newly discovered misconduct to IA. Assurance audits **systems**, not individual guilt. The Commissioner cannot be investigator, initial disciplinary decision-maker and appeals reviewer for one matter.
- **Recusals and alternate reviewers:** Every assigned reviewer discloses conflicts. A reviewer who took the original enforcement action, participated in the IA inquiry, or is closely involved with the subject cannot be the final appeal reviewer. If insufficient independent members remain, the Owner appoints a temporary outside reviewer under written rules, with no stake in the matter.
- **Cases concerning office leadership:** Allegations against the Commissioner go directly to the Owner/designated unconflicted intake and external reviewer. Allegations against an IA/Appeals/Assurance lead are assigned outside that lead's authority. The Commissioner cannot screen out complaints about their own conduct.
- **Confidentiality and data minimization:** Separate access groups and case registers for IA, Appeals and Assurance; role titles do not grant blanket visibility. Share only the minimum relevant record across functions; define retention periods, audit access, and prohibit public case details.
- **Independent reporting:** The Office gives anonymized trend/quality reports to the Owner and non-case-specific advice to the Governance Council. It may raise a charter or interference concern directly with the Owner; the COO and Council cannot block intake, close a named case or edit findings.
- **Office self-review:** Systemic reviews of OIO processes use an unconflicted assessor, independent of the work under audit. OIO cannot declare its own disputed decisions finally validated solely by internal agreement.
- **Realistic limit:** As the Discord Owner keeps ultimate technical control, the Office's independence is **procedural and organizational**, not an absolute legal or technical guarantee. Owner-involved allegations may require an advisory outside panel and public procedural transparency to the extent permitted.

### 4.4 What happens after a finding?

An IA finding is sent to the predesignated **unconflicted disciplinary authority** (normally the authorized management/Owner level under the sanction policy; never the subject or investigating officer). The appeal reviewer is chosen independently of both that authority and the investigation. An Assurance finding names a corrective **operational owner** and a review date; the relevant director/COO implements it, with Governance Council approval only when an organization-wide policy change is necessary. An Appeals determination uses the published remedy charter, not an informal request for the initial moderator to approve their own reversal.

**Design choice:** One office and shared administration reduce bureaucracy; three clearly separated functions protect members from a single unchecked integrity team.

---

## 5. Multi-team membership: one coordinator, several work leads

### 5.1 The permanent reporting rule

Every organizational staff member has:

- **Exactly one Home Team** — the administrative unit to which they belong.
- **Exactly one People Manager** — normally their Home Team Lead or, in a one-person team, their director/manager.
- **One Primary Assignment** — their usual operating job, commonly in the home team.
- **Zero or more approved Secondary Assignments** — explicit roles in other teams or standing rotations.
- **One Task Lead per active assignment** — may differ from the People Manager.
- **An Assignment Coordinator** — an administrative contact in People & Culture for workload visibility, not a superior in the chain of command.

**Practical default:** one primary + one secondary team. A second light secondary assignment can be allowed by exception; ongoing commitments across four or five teams should generally be refused because they make availability and accountability unreliable.

### 5.2 Who is responsible for what?

| Responsibility | Authority |
|---|---|
| Career coaching, general performance assessment, leave/availability, welfare, long-term development | **Home People Manager** |
| Day-to-day work instructions during an assigned shift or project | **Host Team Lead / Task Lead** |
| Task prioritization inside a host team | **Host Team Lead**, constrained by the approved allocation |
| Changing the person's permanent home team | Receiving director + releasing director; Personnel records; escalations by portfolio executives |
| Approving a normal secondary assignment | Home People Manager + receiving Team Lead/Manager; recorded by Personnel Operations |
| Balancing overall workload and spotting conflicts | **Workforce / Assignment Coordinator** (facilitates, does not impose) |
| Resolving conflicting work across teams/directorates | Relevant managers first → respective directors → portfolio executive(s) → COO |
| Feedback from secondary service | Host Team Lead provides documented input to Home People Manager |
| Formal performance action or removal from staff | Authorized Home line management + People & Culture procedure; independent appeal available |

**No double-boss rule:** A secondary Team Lead is not the person's general supervisor. They direct tasks only during the person's agreed assignment and cannot independently alter their career status, discipline them outside emergency authority, or silently demand availability beyond the allocation.

### 5.3 Concrete example

> **Person:** Avery (illustrative)  
> **Home Team:** Game Enforcement  
> **People Manager:** Game Enforcement Team Lead  
> **Primary job:** Game Enforcement Officer  
> **Secondary job:** Session Controller, Team Bravo  
> **Rotation:** Critical Incident Response, qualified responder  
> **Assignment Coordinator:** Personnel Operations' Workforce Coordinator

- During an enforcement patrol, the Game Enforcement Lead directs the work.
- During an approved Bravo session shift, Bravo's Session Commander has **session-scoped** authority over the person's assigned session duties.
- If both need Avery at the same time, **the previously approved roster / primary allocation wins unless a documented emergency override applies**. A new request is negotiated; neither lead can simply seize the person's time.
- Bravo provides shift feedback to Avery's Home People Manager, who combines that input into the overall review.
- The Workforce Coordinator records the overlap, recommends options and confirms the resulting schedule.
- If the leads cannot resolve it, the directors decide; the executive portfolio or COO resolves inter-directorate deadlocks.

### 5.4 An allocation agreement

Every standing cross-team assignment should have this short record:

```yaml
member: example-user-id
home_team: game-enforcement
people_manager: game-enforcement-team-lead
primary_assignment:
  team: game-enforcement
  title: enforcement-officer
  priority: standard-primary
secondary_assignments:
  - team: session-bravo
    title: session-controller
    estimated_share_of_available_time: 20%
    approved_by_home: true
    approved_by_host: true
    qualification: session-controller
    review_date: 2026-12-01
  - team: incident-response-rotation
    title: qualified-responder
    activation_only: true
conflict_route: managers > directors > executive-directors > COO
```

Time shares are **planning estimates of voluntary availability**, not work quotas, contracts or mandatory weekly hours. People can change their availability. Record expected duty windows, not invented obligations.

### 5.5 Priorities when assignments collide

1. **Immediate safety/security emergency** under a designated Incident Commander — temporary, documented and narrowly scoped.
2. **Previously accepted live duty** (e.g. scheduled session or active investigation) — don't abandon it without handoff.
3. **Approved primary commitments**.
4. **Approved secondary commitments**.
5. **Optional/ad hoc tasks**.

A supervisor cannot manufacture an “emergency” to defeat someone's existing commitments. If it is not time-critical, reschedule it.

---

## 6. Integrated career and organizational rank framework

### 6.1 The eight-level organizational hierarchy

This is a **hybrid corporate–community** model. Ranks provide understandable organizational standing and eligibility, while functional titles identify people's work. The former public Associate/Specialist/Principal ladder and the independent five-stage capability ladder are **not retained as parallel rank systems**. `Trainee`, `qualified`, `senior specialist` or `expert` may still describe a **training state, job title or qualification**, but they are not competing universal ranks.

| Grade | Public rank | Primary purpose | Award/eligibility rule | Automatic authority? |
|---|---|---|---|---|
| **08** | **Owner / Chief Executive** | Sole ownership and constitutional reserved powers | Exclusively the actual Owner/CEO; not an earned promotion | Only actual ownership and specifically reserved charter authority |
| **07** | **Executive** | Two direct executive offices accountable to Owner | Appointment as **COO** or **Oversight Commissioner** | Only the holder's executive or protected oversight mandate; the offices are not interchangeable |
| **06** | **Director** | Directorate or executive-portfolio leadership | Appointment as one of **six Directorate Directors** or **two Executive Directors** | Only appointment-defined directorate or portfolio scope |
| **05** | **Senior Administrator** | Senior organizational management and executive coordination | Approved senior management responsibility or exceptional assessed organizational competence | No blanket management or technical access |
| **04** | **Administrator** | Management of teams/functions and significant delegated operational responsibility | Qualified appointment or documented management-equivalent assessment | No blanket enforcement or technical access |
| **03** | **Senior Moderator** | Advanced community/game enforcement, mentoring, frontline moderation leadership | Senior moderation/enforcement assessment and track record | Only specifically qualified enforcement permissions |
| **02** | **Moderator** | Independent community/game moderation and enforcement | Approval as independently qualified Discord Moderator / Game Enforcement Officer | Only approved moderation/enforcement scope |
| **01** | **Staff Member** | General entry standing for staff in any function | Approved staff recruitment or transfer; trainees may hold limited access | None without relevant job qualification |

**No mandatory rank-by-rank climb.** Someone can progress from Staff Member to Administrator through a legitimate technical, operational or people-management appointment without first being a Moderator or Senior Moderator. Grades 02 and 03 are meaningful **enforcement standing**, not universal prerequisites for every directorate. Grade 01 can also be held by highly skilled independent specialists: their **professional expertise, senior functional titles and specific remit** are shown in their job and qualification records, rather than forcing them through unrelated moderator promotions.

**Top-level consistency:** The Owner (08) has exactly **two direct Executive-grade reports** in this design: COO (07) and Oversight Commissioner (07). Both Executive Directors (despite the word *Executive* in their **job title**) occupy the **Director grade 06** and report to the COO. All six Directorate Directors also occupy grade 06; **the Executive Director appointment carries portfolio supervisory authority even over an equal-grade Directorate Director**. No new management layer is added.

### 6.2 Three rank-to-position relationships

| Relationship | Definition | Example | Consequence |
|---|---|---|---|
| **Direct correlation** | Appointment to a designated job confers a defined grade (or a grade floor if the member already holds higher valid standing) | `Discord Moderator = 02`; `Senior Discord Moderator = 03`; `Director of Live Operations = 06` | Grade is assigned under the approved process; no automatic downgrade when the job is a lower-grade secondary assignment |
| **Minimum rank** | A role requires at least a defined grade *plus* separate qualifications and selection | `Game Enforcement Team Lead: 03 minimum`; `Chief of Staff: 05 minimum` | Meeting the grade alone does **not** grant the position |
| **Qualification-gated, no general minimum beyond Staff Member** | Case-specific expertise, not broad organizational rank, controls eligibility | Session Commander, trained Investigator, Systems Developer | Passing the relevant specialist assessment matters more than a moderator title |

**Appointment-linked grades:** Grades 06–08 are reserved for their corresponding live appointments; grade 07 is not awarded for general “seniority.” A person leaving a Director/Executive appointment immediately loses that rank and related appointment powers, reverting to their **previous retained standing**, usually grade 04 or 05 (or another validated prior grade). The Owner grade is not delegated or reassigned through a routine personnel action. Acting appointments must explicitly state their temporary grade, scope and expiry; no silent permanent promotion.

**One-current-grade rule for multiple assignments:** A person holds **one active organizational grade**, based on their highest valid standing or current appointment. A higher, appointment-linked grade 06/07 takes precedence while that appointment lasts; the prior earned grade is retained for reversion. A person serving as both **Director (06)** and a qualified Discord Moderator does **not** also display grade 02, and a Senior Administrator (05) serving a support shift does not become Staff Member (01). A directly correlated lower-grade role is thus a *minimum floor*, not a forced downgrade. No assignment confers permissions unrelated to that assignment.

**Promotion-linked jobs:** Moderators and Senior Moderators earn grade 02/03 through the corresponding enforcement qualification and appointment. A transferred former moderator may retain previously earned grade 02/03 under an **explicit good-standing retention decision**, but may **not** use enforcement powers without an active authorized enforcement assignment and current qualifications. A role requirement involving *current enforcement standing* also requires current authorization—historical grade alone is insufficient.

### 6.3 Position and eligibility matrix — all six directorates and oversight

These are **proposed default mappings**. A director may define stricter, job-relevant training prerequisites through the approved People & Culture framework, but cannot bypass appointment authority or create automatic Discord permissions. A minimum rank is not an entitlement to the position; recruitment must still assess the actual job.

| Function / position | Proposed grade relationship | Selection or qualification boundary |
|---|---|---|
| **Owner / CEO** | **08 — Owner / Chief Executive**, direct and exclusive | Actual Owner; reserved powers as chartered |
| **COO** | **07 — Executive**, direct | Owner appointment; executive management remit |
| **Oversight Commissioner** | **07 — Executive**, direct | Owner appointment, independence and conflict screening; cannot direct IA findings or appeals |
| **Executive Director — Operations / Community & Services** | **06 — Director**, direct | Owner appointment; portfolio scope, under COO |
| **Any of six Directorate Directors** | **06 — Director**, direct | COO appointment/confirmation as specified; one directorate remit |
| **Chief of Staff** | **05 — Senior Administrator minimum** | COO appointment; coordination only, no line authority over Directors |
| **Discord Moderator / Game Enforcement Officer** | **02 — Moderator**, direct | Function-specific training, evaluation and authorized assignment |
| **Senior Discord Moderator / Senior Enforcement Officer** | **03 — Senior Moderator**, direct | Advanced enforcement assessment and documented sound judgment |
| **Discord Moderation Lead / Game Enforcement Team Lead** | **03 — Senior Moderator minimum** | Real frontline management appointment and current enforcement competency |
| **Game Enforcement Manager** | **04 — Administrator minimum** | Unit management assessment and Trust & Safety appointment |
| **Case Coordinator / Case Reviewer / Evidence Custodian** | **01 — Staff Member baseline; 04 if appointed to substantive unit management** | Specific case/evidence handling qualifications; case independence maintained |
| **Critical Incident Duty Commander / responder** | **Qualification-gated; no automatic rank increase** | Time-limited incident delegation; qualification and logged activation |
| **Session Host / Session Controller / Scheduler / Dispatch Officer** | **01 — Staff Member baseline** | Appropriate hosting, controller or dispatch qualification |
| **Squad / Session Commander** | **01 baseline; assigned session-command authority** | Session Commander qualification and defined shift mandate; not automatically Administrator |
| **Session Operations Manager** | **04 — Administrator minimum** | Accountable for several session squads/coverage groups |
| **Session Quality Coordinator / Reviewer / Readiness Coach** | **01 baseline; 04 when a substantive management appointment exists** | Readiness review qualification, not general moderation powers |
| **RP Program Commander / Deputy / Unit Supervisor** | **01 baseline; 04 if appointed to an organizational management function** | RP program-specific authority, not automatically Discord administrative rank |
| **RP Standards Lead / Evaluator / Trainer** | **01 baseline; 04 if appointed unit manager** | Roleplay-program standards qualification |
| **Support Officer / Senior Support Officer / Onboarding Assistant** | **01 — Staff Member baseline** | Support skills, sensitive-ticket boundaries, optional functional senior title |
| **Member Services Support Lead / Manager** | **04 — Administrator minimum for substantive team management; Lead may remain 01 if coordinating a solo/light function** | Team-management appointment distinct from general support qualification |
| **Engagement / Events / Communications / Partnerships / Player Feedback Coordinator** | **01 baseline; 04 only for substantive managerial appointment** | Accountability for deliverables is not automatically personnel command |
| **Recruiter / Training Assessor / Trainer / Personnel or Workforce Coordinator** | **01 baseline; 04 if appointed to manage a real team** | Independent recruiting/training/personnel qualification and confidentiality |
| **Recruitment Lead / Training Lead / Personnel Manager** | **04 — Administrator minimum when supervising staff** | Management suitability and People & Culture appointment |
| **Developer / Systems Developer / Data Analyst / Access Coordinator** | **01 baseline; may earn 04 through assessed managerial-equivalent responsibilities** | Technical skills and least-privilege access; never required to moderate first |
| **Technical Lead / Systems Administrator (job title)** | **04 — Administrator if managing a technical function; otherwise 01 with specialist title** | Technical authority from an explicit access authorization, not organizational grade |
| **IA Investigator / Senior Investigator / Appeals Reviewer / Assurance Assessor** | **01 baseline; no Moderator prerequisite** | Protected selection, integrity/conflict checks, qualifications and separate case authority |
| **IA / Appeals / Assurance functional Lead** | **04 — Administrator normally when responsible for personnel or function; specialist-only lead may remain 01** | Appointment by appropriate OIO authority; professional findings remain protected |
| **Staff Representative on Governance Council** | **Retains existing grade (01–06 as eligible)** | Elected non-executive staff seat; equal vote, no grade promotion or enforcement powers |

**How to read the matrix:** `04 minimum` is a **managerial eligibility threshold**, not a command license. A Senior Moderator can apply for Game Enforcement Manager and receive grade 04 **as part of the same successful appointment**; no second, arbitrary promotion committee is needed. A technical or support specialist can similarly qualify for grade 04 **without ever holding grade 02/03**. Conversely, an Administrator who has never been certified to enforce rules is not magically qualified to ban players.

**Senior Administrator (05)** is reserved for genuinely senior cross-team/cross-directorate responsibility, the Chief of Staff appointment, or evidence-backed organizational leadership beyond ordinary unit management. It is not an automatic stepping stone before Director; someone appointed Director moves into grade 06 and reverts to their **documented retained grade** on departure. If a directorate has no work requiring grade 05, leave it unused there.

### 6.4 Promotions, appointments, transfers and reversions

1. **Earned enforcement promotion (01 → 02 → 03 when relevant):** Trust & Safety records training, supervised performance, judgment and authorization; the designated manager proposes the advancement, People & Culture confirms a consistent process, and the designated approving authority approves. No punishment quota or message-count target.
2. **Professional specialization:** An existing Staff Member becomes Senior Support Officer, qualified Session Commander or Senior Investigator by meeting the *functional* standard. These titles/qualifications do not force universal Moderator standing or technical permissions. Their work can still qualify them for an Administrator-grade management appointment later.
3. **Administrator / Senior Administrator progression:** Appointment or separately documented managerial-equivalent assessment must show **substantive delegated organizational responsibility**, sound decisions, integrity and scope—not expertise alone or honorary seniority. A manager can approve **combined appointment and rank elevation** rather than first creating an artificial vacant grade.
4. **Director / Executive appointment:** The authorized appointing body fills a real position and simultaneously assigns its **appointment-linked** grade. Exiting the office removes that grade and all appointment-specific access; retained grade and independent qualifications are reviewed separately.
5. **Cross-directorate move:** A staff member retains their duly awarded lower-grade standing unless a recorded review determines a specific qualification or appointment no longer applies. New teams provide any additional training before granting powers.
6. **Rank correction or demotion:** Never confuse a routine step-down, lapse of qualifications, inactivity, or voluntary leave with misconduct. Any adverse status reduction must state a fair reason, authorized decision maker, review route and appeal. Case findings use the OIO processes when misconduct is alleged.

**Default approval model:** Direct enforcement upgrades (02/03) are proposed by the receiving/owning Trust & Safety leadership and approved by its Director under People & Culture procedures; grade 04–05 promotions require the relevant Directorate Director, with portfolio/COO review for exceptional cross-directorate scope. Grade 06 Director appointments follow the existing COO-confirmation rule; Executive Director and Commissioner appointments are Owner-made; the COO is Owner-appointed. The Owner/CEO is not a promotion committee for every ordinary advancement. Any case with conflicted decision-makers uses the published recusal and appeal procedure.

**Temporary/acting assignment:** Record the acting appointment, start/end date, precise operational powers, and whether an *acting grade* is displayed. Temporary coverage is not a permanent grade increase; automatically expire access at the end unless affirmatively renewed.

### 6.5 Leadership appointment catalogue

| Appointment | Normal grade | Scope and limit |
|---|---|---|
| **Coordinator** | 01 baseline | Owns deliverables; no direct reports required |
| **Team Lead** | 03 minimum for enforcement; 04 when managing a broader organizational team; 01 possible for a solo/light coordinating title | Manages only assigned team and authorized tasks |
| **Unit / Operations Manager** | 04 minimum; 05 for a sustained senior multi-unit remit | Supervises assigned teams/coverage groups only |
| **Directorate Director** | 06, appointment-linked | Leads one of six operating directorates |
| **Executive Director** | 06, appointment-linked | Manages one of two three-directorate portfolios under COO |
| **Chief of Staff** | 05 minimum | Reports directly to COO; coordinates but cannot command directors |
| **COO** | 07, appointment-linked | Runs operating organization, excluding OIO command |
| **Oversight Commissioner** | 07, appointment-linked | Administrative head of protected independent oversight functions |
| **Owner / CEO** | 08, exclusive | Reserved ownership/constitutional powers |

**Public-facing naming rule:** Prefer meaningful functional titles and concise grade tags: `Game Enforcement Team Lead · Senior Moderator (03)`, `Director of Trust & Safety · Director (06)`, `Oversight Commissioner · Executive (07)`, `Session Commander · Staff Member (01)`. Do not overwrite someone's job with a vague “Expert” title or create separate public grades for every training certificate. Internal systems retain the full record.

### 6.6 What rank does *not* mean

- **Rank is not universal command:** A grade-05 Senior Administrator in People & Culture cannot command grade-03 enforcement staff in an active incident unless separately assigned that mandate.
- **Equal rank does not mean equal appointment:** An Executive Director (06) directs the Directors (06) in that portfolio; the reporting structure is unambiguous.
- **Oversight stays independent:** Grade-07 Commissioner is not the COO's deputy; investigators and reviewers can examine higher-grade staff under the published case rules, without becoming those people's line managers.
- **Council votes are not weighted by rank:** The elected Staff Representative's vote equals every other voting seat; the Council does not confer a new rank.
- **Discord `Administrator` permission is separate:** The organizational rank **Administrator (04)**, Senior Administrator (05), Director (06), Executive (07) or Owner (08) does not by itself grant technical permissions, except those actually inseparable from Discord ownership. See Sections 8 and 10.

---

## 7. Recruiting and assigning staff

### 7.1 Three entry paths, not one blanket application

| Route | When to use | Example |
|---|---|---|
| **General Staff Intake** | New people want to join but have no specialized training | Staff candidate chooses interest areas; initial screening |
| **Role-Specific Recruitment** | A team has an actual vacancy that requires capabilities | Game Enforcement Officer, Session Host, Support Officer |
| **Internal Transfer / Secondment** | Existing qualified staff want another assignment | Moderator becomes a part-time Session Controller |

**Default recommendation:** Use **role-specific recruitment for operational vacancies**, with a short general staff interest form available year-round. Every vacancy lists whether its rank is directly linked, a minimum eligibility threshold, or qualification-gated only. Don't recruit 25 undirected “staff” and then invent jobs for them.

### 7.2 Hiring workflow

1. **Team Lead identifies a staffing need** using volume, coverage gaps, or specialist requirement — not vanity headcount.
2. **Director (or delegated Unit Manager) approves a position request**, its mandate, vacancy count, proposed organizational grade relationship, and training requirements. Portfolio leadership reviews large changes in capacity.
3. **Talent Acquisition posts the vacancy**, manages forms, consistent screening and applicant communication.
4. **Host team conducts a work-relevant assessment** — e.g. sample moderation scenario, mock session plan, support ticket response, short technical exercise.
5. **Host hiring authority selects the candidate** from qualified applicants. People & Culture verifies standards, grade eligibility and any justified grade transition, and records the decision; it is not an alternate shadow director.
6. **Learning & Development handles qualification** and the receiving team handles supervised onboarding.
7. **Personnel Operations assigns a Home Team, People Manager, functional job title and one organizational grade**, registers the grade basis (earned, direct correlation, appointment-linked or acting), retained prior standing, qualifications and access requests; Technology provisions limited permissions after approval.
8. **An initial review** checks actual readiness and fit; unsuccessful candidates get a documented, appropriate exit or reassignment path.

**Leadership roles** follow a higher standard: published responsibilities, grade eligibility or combined appointment-promotion review, evidence of judgment, panel assessment or structured interview, conflict-of-interest screening, and the specified appointing authority. A qualified non-moderator may obtain an Administrator-level appointment without first working as a Moderator. Director appointments are confirmed by the COO (and, if designated as owner-reserved, the Owner). Executive Directors and the Oversight Commissioner are appointed by the Owner; the COO is appointed by the Owner.

### 7.3 Secondary assignment workflow

```text
Staff member expresses interest OR host team publishes vacancy
    ↓
Host lead checks capability, suitability and available slots
    ↓
Home manager reviews load, schedule and possible conflicts
    ↓
Host lead + home manager approve scope and duty windows
    ↓
Personnel Operations records secondary assignment and review date
    ↓
Training / qualifications checked; minimum necessary access granted
    ↓
Secondary lead directs tasks only within this assignment
    ↓
Home manager receives periodic feedback; both review continuation
```

A secondary assignment **must not require resignation from the primary team** unless the work is genuinely incompatible, confidentially conflicting, or exceeds available capacity.

### 7.4 Capacity, exclusivity and conflicts

- Default maximum: **one primary and one active secondary**; a third light rotation requires documented approval.
- **Internal Affairs investigators** cannot investigate teams/cases in which they are personally involved; some assignments should be restricted outright.
- Appeals reviewers cannot review their own enforcement actions, those of close collaborators without recusal, or cases on which they advised the initial decision.
- Technical privileged-access administrators are not permitted to use those permissions to obtain IA case material without authorization.
- A Team Lead responsible for an applicant's assessment should disclose personal relationships or conflicts and recuse where needed.
- Inactivity is addressed through the **Staff Experience & Retention Framework**: private check-in, opt-in leave or reduced duties, and published readiness/administrative status rules before punitive action; this is a volunteer community.

### 7.5 A position-request template

```markdown
## Position request
Team / directorate:
Requested title:
Rank relationship: direct | minimum | qualification-only
Required/assigned organizational grade (01–08, if applicable):
Justification for grade requirement / exception:
Vacancies:
Reason for opening:
Expected outcomes / coverage:
Core tasks:
Required qualifications:
Access needed:
People Manager:
Host Team Lead:
Primary or secondary assignment allowed?:
Training / probation process:
Rank granted upon appointment (if any), prior retained rank and exit/reversion plan:
Success criteria after initial review:
Approved by:
```

---

## 8. Authority, escalations and decision ownership

### 8.1 Four separate forms of authority

1. **Governance authority:** A documented Council vote on policies within its collective mandate, or an Owner-reserved constitutional decision.
2. **Personnel authority:** Assigned line management over a defined set of staff.
3. **Operational authority:** A qualified person's authority during a defined incident, case, shift or project.
4. **Technical authority:** Actual Discord/Roblox permissions required to execute an approved action.

Possessing one does not imply the others. **Organizational grade is a fifth, descriptive personnel attribute—not an additional source of authority.** It determines standing and some appointment eligibility but does not displace any of the four scoped authorities above. A higher grade is **not** a universal management appointment; an executive title is **not** automatically the Discord `Administrator` permission. Director-to-Director reporting and COO-to-OIO independence follow their actual appointments, not a numerical comparison.

### 8.2 Delegated decision matrix

| Decision | Default accountable authority | Required consultation / check |
|---|---|---|
| Routine chat violation | Qualified Discord Moderator | Follow published enforcement policy |
| In-game player violation | Qualified Game Enforcement Officer | Evidence and appeal route |
| Start/end assigned session | Qualified Session Commander | Published session standards |
| Temporary disruptive-player removal during live session | Qualified emergency actor | Log for Safety follow-up when needed |
| Permanent player ban | Authorized Trust & Safety role | Evidence; independent appeal available |
| RP department internal promotion | Authorized Program Commander | Roleplay Programs criteria |
| Recruit into approved staff vacancy | Authorized hiring manager in receiving team | People & Culture verification, role-to-grade mapping and qualifications |
| Promote to Moderator (02) or Senior Moderator (03) | Trust & Safety Director or delegated authorized promotion approver | Enforcement qualification, documented evaluation and Personnel records |
| Award Administrator (04) or Senior Administrator (05) | Directorate Director under documented approval rules | Real managerial responsibility or assessed equivalent; People & Culture check; non-moderator pathway available |
| Assign Director (06), Executive (07), Owner/CEO (08) standing | Authorized appointment / actual ownership | No separate prestige promotion; appointment-linked grade and automatic reversion upon exit |
| Add secondary assignment | Home manager + host manager | Personnel Operations records and capacity check |
| Change permanent Home Team | Releasing + receiving directors | Workforce Coordinator facilitates; escalation if disputed |
| Appoint Team Lead | Directorate Director | People & Culture process; portfolio as needed |
| Appoint Directorate Director | COO | Owner confirmation where reserved |
| Appoint Executive Director / Oversight Commissioner | Owner | Screening and recusal procedures; OIO functional leads have protected case discretion |
| Adopt organization-wide staff or member policy | Governance Council (3 affirmative votes of 5; quorum required) | Affected directorates and Staff Representative consulted; oversight adviser where relevant |
| Approve major operating restructuring | Governance Council (4 affirmative votes of 5; quorum required) | COO implementation plan; Owner ratification if reserved powers are implicated |
| Issue temporary urgent operating measure (max. 7 days) | COO | Prompt notice to Council; longer continuation needs Council approval; Owner/platform exception documented |
| Audit operating policy or systemic controls | OIO — Standards & Assurance qualified assessor | Commissioner coordinates resources, not findings; affected directorate responds |
| Investigate alleged staff misconduct | OIO — Internal Affairs unconflicted investigator | Separate disciplinary adjudicator; protected evidence access |
| Hear independent appeal | OIO — Appeals & Member Advocacy unconflicted reviewer | Initial actor and IA investigator excluded from final review |
| Resolve cross-directorate conflict | Portfolio Executive Director(s), then COO | Stakeholders heard; decision documented |
| Handle staff retention or voluntary leave process | Home People Manager + People & Culture Staff Experience function | No forced quotas; independent IA route for alleged abuse |
| Prioritize player-feedback improvement | Responsible operating directorate | Community Experience maintains public tracker; Council only for cross-organization policy |
| Route mixed enforcement / staff misconduct / systemic complaint | OIO intake assigns an owner **for each question** | Separate records and access; no duplicate case ownership |
| Change constitutional distribution of power | Governance Council proposal (4 affirmative votes of 5) **and Owner ratification** | Consult affected leaders and the Office of Independent Oversight; publish changes |

### 8.3 Single decision owner: DRI / DACI

For major initiatives, record:

- **Driver:** Person responsible for progressing the work.
- **Approver:** One named decision-maker with formal authority.
- **Contributors:** Experts/teams supplying relevant input.
- **Informed:** People who need the outcome.

For Council-governed policies, name the **Governance Council as the single collective Approver** and separately identify the COO/director who will implement the result. For routine work, keep one individual Approver. This prevents two directors from assuming they're both final approvers and protects specialist teams from unannounced interference. The Approver's mandate still has to be valid: no project form can create powers they don't possess.

### 8.4 Escalation rules

```text
Within a team's mandate       → Team Lead
Across teams, same directorate → Unit Manager / Director
Across directorates           → Executive Director(s)
Across executive portfolios   → COO (routine operational resolution)
Cross-organization rule change → Governance Council (after executive consultation)
Owner-reserved policy         → Council recommendation + Owner ratification
Misconduct / abuse complaint  → OIO / Internal Affairs
Contested enforcement action  → OIO / Appeals & Member Advocacy
Systemic policy/control fault → OIO / Standards & Assurance
Staff support / workload       → People & Culture / Staff Experience
Player suggestions / experience→ Community Experience / Player Voice
```

Urgent safety events use the active Incident Command protocol, **not** a slow series of approvals. Each emergency action gets reviewed afterward.

---

## 9. Performance, accountability and meeting rhythm

### Daily: teams operate

- Session squads handle assigned shifts and record concise outcomes.
- Moderators enforce their rules with sufficient case notes.
- Support handles ordinary requests and routes specialty cases.
- Managers resolve routine resource conflicts before escalating them.

### Weekly: managers coordinate

- Team Leads: short update on demand, blockers, staffing and quality.
- Directors: consolidate only material exceptions, risks and improvement actions.
- Chief of Staff: maintains organization-wide issue/decision log and asks owners of overdue tasks for updates.
- Workforce Coordinator: checks uncovered shifts and excessive secondary assignments.
- Staff Experience Coordinator: follows up on consented workload/leave concerns and optional mentor support without collecting intrusive personal details.
- Player Feedback Coordinator: routes public suggestions to one owning team and updates overdue tracker items.

### Monthly: Governance Council policy review

- Review pending cross-directorate proposals, expiring temporary measures, policy implementation blockers, staff-representative feedback and relevant **aggregated player consultations**.
- Revisit approved policies at their scheduled review dates; involve relevant independent oversight advisers without giving them operational control.
- Chief of Staff publishes non-sensitive decisions and tracks who is implementing each approved measure.

### Monthly: executive performance review

The COO and executive directors examine:

- Session reliability, player satisfaction and coverage.
- Enforcement quality, fairness and timely resolution — **not punishment count**.
- Recruitment readiness, **voluntary retention, training completion, workload concerns and staff experience trends** without individual activity quotas.
- Ticket demand, support quality, **player feedback themes, published improvement-tracker updates and consultation outcomes**.
- Availability of essential bots/systems, access risks and incidents.
- Open audit recommendations and independent oversight summaries that can lawfully/appropriately be shared.

### Quarterly: staff experience and community voice

- People & Culture summarizes voluntary staff pulse feedback, retention/leave themes and the workload changes made in response, without identifying individuals in small teams.
- Community Experience runs a brief player pulse survey and publishes a `You said / We did / Why not` summary; suggestions remain traceable to an owning team without publishing private complainants.
- The COO reviews barriers that operational teams cannot resolve; organization-wide policy gaps go to the Governance Council rather than creating another executive working group.

### Periodic independent review

- **OIO / IA:** anonymized misconduct trends and process timeliness where feasible; no disclosure of active case identities.
- **OIO / Appeals:** overturns, errors and systemic fairness issues, without treating appeal reversal as a score to maximize/minimize.
- **OIO / Assurance:** sampled procedures, access control, training consistency, overlapping quality functions and root causes of significant failures. An unconflicted assessor checks OIO's own processes when necessary.

All performance metrics are diagnostic, not simplistic quotas. A staff member should not be rewarded for maximizing bans, ticket closures, or convictions.

---

## 10. Discord implementation and permission design

**Server role layers should be distinct:**

| Layer | Examples | Purpose |
|---|---|---|
| Identity / affiliation | `Staff`, `Police Program`, `Events Team` | Discoverability, notifications, channels |
| **Organizational grade (01–08)** | `Moderator [02]`, `Administrator [04]`, `Director [06]`, `Executive [07]` | Visible standing and appointment-eligibility metadata; **not a universal permission bundle** |
| Functional assignment | `Discord Moderation`, `Game Enforcement`, `Session Squad Bravo` | Membership and scoped workspace access |
| Qualified capabilities | `Approved Session Host`, `Ban Reviewer`, `Evidence Handler` | Capability record; technical access only if necessary |
| Organizational appointment | `Game Enforcement Lead`, `Director of Live Operations`, `COO`, `Oversight Commissioner` | Actual named remit/reporting authority; no universal technical admin |
| Governance affiliation (optional) | `Governance Council`, `Staff Representative` | Discoverability and a restricted policy workspace, **not** automatic administrator or enforcement power |
| Privileged technical roles | Restricted bot operator / server configuration maintainer | Actual Discord settings permission, closely controlled |

**Implementation preference:** Store the **canonical numeric grade** (01–08), its basis, current functional title and appointment separately in the personnel registry. If displaying grade roles in Discord, use one mutually exclusive current-grade role per person, supplemented by functional/team roles and temporary acting markers. Avoid giving every grade its own permission bundle; use actual work-role permission groups, or the minimum Discord native roles needed for moderation. During a temporary Director/Executive appointment, keep the prior earned grade as a *registry field*, not an extra active Discord grade role. The Owner remains the sole holder of grade 08.

**Discord-specific constraint:** Members generally cannot moderate users whose highest role is equal to or higher than their own. Publishing grades as stacked Discord roles can therefore obstruct authorized moderation: plan the actual Discord role order and bot/execution routes separately from personnel standing, and do not promise that a lower-grade investigator can natively sanction a higher-role target. The Discord `Administrator` permission bypasses channel permission restrictions. Consequently, a job title or matrix reporting diagram cannot by itself override Discord technical permissions. Give `Administrator` only where strictly justified; use a bot/dashboard for fine-grained workflows if necessary, but don't pretend it changes Discord's native hierarchy.

**Governance implementation:** Rank does not alter Council votes; the Staff Representative keeps their prior grade and still casts one equal vote. Maintain a dedicated policy proposal register, Council minutes/vote log, published rules and read-only staff feedback channel. A private Council discussion channel may exist, but final non-sensitive rules should not be hidden there. Council roles themselves grant no automatic `Administrator`, `Ban Members` or evidence-access permission.

**OIO and player voice implementation:** Provide one confidential OIO intake route with **separate private IA, Appeals and Assurance case permissions**; the Commissioner's general title does not automatically open all case attachments. Maintain a public player suggestions channel/form, periodic consultation announcements, a public non-sensitive improvement tracker and a monthly change summary. Never redirect confidential complaints into the public tracker.

**Operational suggestion:** Store grade and its basis, retained grade, real reporting and assignment data in a personnel registry/dashboard; keep Discord roles for visible affiliation, notifications and minimum practical access. Separate role-change approval from role-change execution, and log privileged actions.

**Privacy:** Staff complaint files, confidential staff well-being feedback, applicant data, appeals and investigation evidence need separated access controls, defined retention/deletion processes and a clear ban on sharing private information outside authorized casework. Minors may be present in ER:LC and Discord communities; take that into account when choosing channels, collection fields and reporting procedures.

---

## 11. How small or large units should grow

The organizational unit is **a responsibility**, not necessarily a team of four people.

| Actual headcount | Appropriate structure | Avoid |
|---|---|---|
| **1** | Coordinator/single specialist reports to director or manager | Inventing a manager and deputy above a solo contributor |
| **2–4** | Team Lead or Coordinator with contributors, depending on workload | Creating middle management for prestige |
| **5–8** | Stable team with Lead, named alternate, clear rotation | Team Lead supervising every task personally |
| **9–15** | Consider multiple shifts or squads, each with a Lead | One huge always-on roster without coverage ownership |
| **Several squads** | Unit/Operations Manager supervising Team Leads | Additional directors for one function |

**Split a team** when shift coverage, task specialization, workload or supervision quality requires it; do not split just to produce an impressive org chart. **Merge teams** when their work is infrequent, overlapping and better served by one accountable lead. All headcounts above are illustrative heuristics, not strict thresholds.

### Example 60-person staffing concept

A possible planning allocation, **not a universal target**: Trust & Safety 15; Live Operations 15; Roleplay Programs 10; Community Experience 6; People & Culture 4; Technology & Systems 3; Office of Independent Oversight 3 (Commissioner + IA + Appeals, with limited Assurance dual-hat and independent alternates); Executive Office 4 = **60**. The four executive positions are the COO, two Executive Directors and Chief of Staff. The Owner/CEO is counted separately from this illustrative **60 organizational staff** allocation; if the Owner is also counted as staff, adjust the totals accordingly. The Council reuses the COO and both Executive Directors, the Chief of Staff serves as a non-voting secretary, and the elected Staff Representative occupies an **existing staff seat** in one of the listed teams—**no five-person Council headcount is added**. Counts include leadership positions and are unique persons, not duplicate assignment slots. If people hold multiple team assignments, a team's seat count and organization-wide headcount must be reported separately. **Player Voice & Improvements** and **Staff Experience & Retention** are initially responsibilities of existing Community Experience and People & Culture staff, not extra persons in this illustration. Add a standalone OIO Assurance specialist only when justified by the workload and independence requirements, and rebalance the 60-person distribution accordingly.

**Growth trigger for executive layer:** Activate both Executive Directors if the COO regularly coordinates six directors, needs routine intervention across multiple functions, or cannot maintain direct management quality. Do not fill them merely to match the chart.

---

## 12. Worked examples

### Example A — Cross-team staff member

**Taylor** is a Game Enforcement Officer (**Moderator, grade 02**; home team), a certified Session Controller (secondary), and an occasional incident responder. Their single People Manager is the Game Enforcement Team Lead. Their Session Commander directs live session tasks only while Taylor serves an accepted shift. An Assignment Coordinator maintains the record. Neither team may silently change Taylor's availability.

### Example B — Solo specialist

**Morgan** is the Partnerships Coordinator (**Staff Member, grade 01**, with specialist responsibility), the only person in Partnerships & Growth. Morgan has no direct reports, owns partnership deliverables, and reports to the Community Experience Director (or another authorized manager). There is no empty “Partnerships Manager” rank.

### Example C — Cross-directorate new rule

Live Operations wants to update rules for sessions. The Session Quality Coordinator is **Driver**; Director of Live Operations is **Approver** for session-specific matters; Trust & Safety and RP Standards are **Contributors**; hosts are **Informed**. If the proposal changes organization-wide ban policy, the relevant enforcement authority contributes but **the Governance Council becomes the collective Approver**; the COO and Trust & Safety implement the approved rule. Neither the Council nor its members decide an individual pending ban appeal.

### Example D — New policy affecting all staff

Several directorates want to change staff inactivity and leave procedures. People & Culture drafts a proposal, the Staff Representative collects frontline concerns, and Live Operations tests the effect on session coverage. The OIO Standards & Assurance function gives independent procedural advice. The Governance Council votes; if approved, the COO assigns implementation to People & Culture and the Chief of Staff records the policy and review date. No executive obtains a new power to punish individual staff outside the existing personnel and appeals rules.

### Example E — Report against executive staff

A member reports the Executive Director — Operations (**Director, grade 06**). Member Services routes it to the OIO's **Internal Affairs** function; the subject's chain of command cannot block intake or alter evidence. An unconflicted investigator gathers facts. A separately authorized adjudicator determines action. Appeals, if applicable, goes to an independent reviewer. Serious findings reach the Owner through an OIO reporting channel. The Commissioner ensures assignment to an unconflicted reviewer but cannot choose the investigation's factual conclusions.

### Example F — Staffing a new squad

Live Operations reports recurring uncovered evening sessions. It proposes Squad Charlie with one qualified Commander, one Controller and three Hosts. The Operations executive approves capacity; Talent Acquisition opens a **Session Host** vacancy. Existing staff may request secondary placements. Personnel records homes and reporting lines; the squad launches only after qualification and coverage are confirmed.

---

### Example G — One incident, no duplicate investigations

A session host is accused of unfairly removing a player. The **ban/removal appeal** belongs to OIO Appeals, while **suspected staff abuse** (if factually alleged) belongs to OIO Internal Affairs. Live Operations may separately coach host readiness and OIO Assurance may later review a recurring systemic policy issue. Each question has a named case owner and a limited evidence-sharing record; four teams do **not** independently retry the same ban.

### Example H — Retaining a burned-out volunteer

A Game Enforcement Officer has missed several *optional* patrols but still wants to help. Their Home People Manager offers a private check-in; People & Culture discusses a temporary break or narrower availability and the Workforce Coordinator adjusts their secondary assignment. No misconduct case is opened simply for reduced activity. If an accepted live duty is affected, a documented handoff protects session coverage.

### Example I — Player feedback becomes a visible improvement

Players repeatedly report confusing SSU announcements. Community Experience categorizes the reports, assigns Live Operations as owner and lists the topic publicly as `Reviewing`. Live Operations tests a simpler announcement process, changes its own operating procedure within existing rules and marks the tracker `Implemented` with a brief explanation. If the change requires a cross-directorate notification policy, it becomes a Governance Council proposal; individual reports remain private when necessary.

---

## 13. Templates for immediate adoption

### 13.1 Person / assignment record

```yaml
member_id: "discord-or-internal-id"
status: active  # candidate | active | leave | inactive | alumni
organizational_grade: 2  # 01 staff, 02 moderator, 03 senior moderator, 04 administrator, 05 senior administrator, 06 director, 07 executive, 08 owner
rank_label: moderator
rank_basis: direct-job-correlation  # earned | direct-job-correlation | managerial-assessment | appointment-linked | acting
retained_grade_before_appointment: null  # populated for appointment-linked / acting grades; null for this permanent Moderator role
rank_decision_approved_by: "trust-safety-director-id"
rank_effective_date: 2026-11-02
rank_review_or_expiry: null
training_status: qualified  # candidate | trainee | qualified; not a second career ladder
home_team: game-enforcement
people_manager_id: "member-id"
functional_title: game-enforcement-officer
management_appointment: null
qualifications:
  - game-enforcement-level-2
  - session-controller
primary_assignment:
  team: game-enforcement
  host_lead_id: "member-id"
secondary_assignments:
  - team: session-bravo
    assignment_title: session-controller
    host_lead_id: "member-id"
    approved_home: true
    approved_host: true
    review_date: 2026-12-01
assignment_coordinator_id: "member-id"
access_profile: scoped-approved-roles
last_review: null
```

### 13.2 Team mandate template

```markdown
# [Team name]
Directorate:
Reports to:
Accountable Team Lead / Coordinator:
Purpose:
Scope of authorized decisions:
Responsibilities and expected deliverables:
Explicit out-of-scope areas:
Roles/qualifications needed:
Primary and secondary assignments accepted?:
Grade relationship and minimum qualifications for each job:
How requests reach this team:
Escalation target and emergency exception:
Required records and data access:
Quality measures:
Acting lead / succession:
Review date:
```

### 13.3 Governance Council policy proposal template

```markdown
# Council policy proposal
Proposal ID / version:
Driver and originating team:
Policy owner:
Problem / evidence / objective:
Affected directorates and groups:
Staff Representative consultation:
Relevant OIO functional advice (if any):
Staff Experience / workload consultation (if affected):
Player Voice consultation summary (if member-facing):
Impact on volunteers, access and member experience:
Implementation burden and alternatives considered:
Proposed policy text:
Effective date / training or communication plan:
Implementation owner:
Review date:
Declared conflicts and recusal:
Quorum / votes / outcome:
Owner ratification required and obtained? (if reserved):
Publication / minutes link:
```

### 13.4 Staff Experience check-in record (restricted)

```markdown
# Voluntary staff check-in
Staff member / home team:
Home People Manager or unconflicted contact:
Date and consent to record a summary:
Role clarity or support requested:
Availability change or preferred break (optional):
Training / mentoring requested:
Agreed action, owner and review date:
Sensitive personal details intentionally excluded:
```

**Privacy:** Do not demand diagnoses, personal explanations or public disclosures. Record only what is necessary for the agreed action; do not reuse a support conversation as disciplinary evidence without a separate, justified process.

### 13.5 Public player improvement item

```markdown
# Player improvement item
Public issue ID / title:
Category / brief non-sensitive description:
Submitted / consolidated feedback theme:
Owning directorate and Driver:
Status: Received | Reviewing | Planned | In Progress | Implemented | Declined / Not Now
Reason / next action:
Last updated / next review:
Consultation or poll summary (optional):
Link to published change or rationale:
```

### 13.6 Oversight intake and routing record (restricted)

```markdown
# OIO intake routing
Restricted case ID / received date:
Initial classification: IA | Appeal | Assurance | multiple linked questions
Primary owner of each question:
Assigned unconflicted investigator/reviewer/assessor:
Declared recusal / alternate reviewer:
Linked case IDs (if needed):
Permitted evidence-sharing scope:
Initial authority / adjudicator (if IA sanction implicated):
Decision or action owner and review date:
Retention/access category:
```

### 13.7 Management appointment template

```markdown
# [Appointment title]
Appointed by:
Organizational grade: [01–08]
Grade relationship: direct | minimum | qualification-only
Prior retained grade and reversion terms:
Acting start/end date (if temporary):
Reports to:
Direct reports:
Functions owned:
Decisions authorized:
Decisions requiring additional approval:
Access allowed:
Conflicts / recusal requirements:
Reporting and review cadence:
Success measures:
Term or periodic review:
Acting replacement:
Removal and appeal procedure:
```

---

## 14. Implementation phases

### Phase 1 — Foundational governance

- Ratify six directorate mandates, **one Office of Independent Oversight charter with three protected functional mandates**, and the Governance Council charter (including voting thresholds, reserved powers and member recusals).
- Seat the CEO/Owner, COO and Executive Directors on the Council; elect a Staff Representative; designate the Chief of Staff as non-voting secretary.
- Establish the Council proposal/vote register and publish the first schedule of organization-wide policies.
- Assign an Owner, operations executive/COO, and interim directors as capacity allows.
- Publish the eight organizational grades and job-to-grade matrix (Section 6), including top-grade appointment conditions, non-moderation routes and reversion rules.
- Publish a minimal authority matrix and urgent incident procedure.
- Separate technical permissions from job titles.
- Appoint an Oversight Commissioner and identify qualified IA, Appeals and Assurance leads/alternates; publish recusal, adjudication and referral rules before accepting sensitive cases.
- Assign one existing Community Experience owner to Player Voice and publish a safe non-sensitive improvement tracker.

### Phase 2 — Personnel registry and assignments

- Record each person's one organizational grade, grade basis, retained prior grade where relevant, Home Team, People Manager, qualifications and assignment slots.
- Appoint a Workforce / Assignment Coordinator.
- Define team-specific applications, role grade thresholds, grade-promotion approvals and an internal secondment request.
- Train leads on cross-team task authority and conflict resolution.
- Assign a Staff Experience Coordinator within People & Culture, launch opt-in 30/90-day check-ins, leave/re-entry options and a quarterly aggregate pulse review.
- Implement OIO's separate case access/registers and single-intake triage; train Case Operations, Session Quality and RP Standards on the referral matrix.

### Phase 3 — Scale operations

- Create Session Operations squads based on coverage.
- Expand Game Enforcement and Member Services based on actual demand.
- Add specialist OIO reviewers/assessors where caseload or independence justifies additional unique staff; do not appoint extra heads merely for titles.
- Run a monthly player consultation and publish a `You said / We did / Why not` update; use quarterly player and staff pulses as feedback, not popularity contests.
- Activate the Executive Directors (grade 06) and a Chief of Staff (grade 05 minimum) once ongoing coordination work exists; do not create extra roles just to fill rank levels.

### Phase 4 — Continuous assurance

- Run periodic Governance Council policy reviews without giving the Council authority over individual IA or appeal outcomes.
- Run OIO practical audits and anonymized Appeals/IA trend reviews, including a conflict-safe review of OIO's own process.
- Review staff retention and voluntary workload signals and publicly report improvements delivered from player feedback without disclosing personal case data.
- Check management spans, vacant coverage and unnecessary managerial layers.
- Retire redundant positions, merge low-volume functions, and improve SOPs based on real problems.

---

## 15. Non-negotiable rules — proposed organizational charter

1. **One person, one home People Manager.** Multiple teams do not mean multiple general bosses.
2. **A secondary assignment grants only assignment-scoped task authority.** It does not change permanent reporting lines.
3. **Managers must coordinate staffing demands.** They may not silently compete for a person's time.
4. **All positions require work and a mandate.** A position can exist with one person or without a dedicated manager.
5. **Organizational rank, job title, technical access, and authority are separate.** Higher grade alone never grants command or the Discord `Administrator` permission; grades 06–08 track specific live appointments/ownership.
6. **The Office of Independent Oversight receives and routes cases without COO or Governance Council approval.** Its IA, Appeals and Assurance functions have protected case discretion, distinct access and recusal rules.
7. **No individual adjudicates their own misconduct or the appeal of a decision they made.** Unconflicted substitutes must be available.
8. **Recruit for specific capacity and capabilities.** General interest applications are an intake channel, not a reason to create empty positions.
9. **A member may develop as an expert without managing anyone or becoming a moderator.** Non-enforcement staff can qualify for managerial grades directly through relevant appointments; experts retain real functional titles and delegated qualifications.
10. **Routine decisions stay close to the work.** Only exceptional decisions should reach the Owner.
11. **The Governance Council owns organization-wide policy, not daily line management.** Its decisions follow documented quorum, voting, consultation, publication and conflict rules.
12. **Independent oversight remains outside Council voting.** The Commissioner and functional leads may advise on systemic matters, but neither the Commissioner nor Council may dictate findings, appeal outcomes or audit conclusions.
13. **The elected Staff Representative has an equal Council vote.** Representation does not confer disciplinary or technical authority; elections and removals must be fair and documented.
14. **Volunteers can request reasonable breaks, role adjustments and private support without automatic punishment.** People & Culture coordinates retention but never becomes everyone's second boss.
15. **Players have a transparent improvement channel.** Community Experience owns consultations and a public non-sensitive tracker; individual complaints and case evidence remain confidential.
16. **One question has one accountable case owner.** Overlapping teams refer and coordinate without duplicating investigations or reviewing their own actions.
17. **Two Executive-grade offices report directly to Owner, with separate mandates.** COO runs operations; Oversight Commissioner protects independent oversight. Neither commands the other.
18. **Director and Executive grades are appointment-linked, not permanent prestige ranks.** Leaving the appointment removes its grade and powers while preserving separately earned standing and qualifications as appropriate.

---

## 16. Design references and limitations

These public references informed the underlying ideas. This document is a **bespoke proposed design**, not a claim that any of the named organizations endorses or directly operates an ER:LC server.

- GitLab Handbook — Directly Responsible Individuals and decision ownership: https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/
- Atlassian Team Playbook — DACI decision-making: https://www.atlassian.com/team-playbook/plays/daci
- Discord Support — Roles, hierarchy and Administrator permissions: https://support.discord.com/hc/en-us/articles/214836687-Discord-Roles-and-Permissions

**Governance choices now proposed in this version:** Five voting Council seats; monthly/async meetings; quorum of four; three affirmative votes for normal policies and four for major structural changes; Owner ratification for reserved changes; a six-month elected Staff Representative term. These are **proposed charter rules**, not an assertion that they have already been formally adopted.

**Open governance decisions for the Owner to ratify:** precise criteria and any exceptional equivalencies for grades 04–05; grade/reversion appeals; whether grade 02–03 can be retained after leaving active enforcement; detailed Staff Representative removal/appeal process; Oversight Commissioner appointment/removal criteria; OIO external-reviewer selection and independent adjudicator rules; specific appointment terms; disciplinary penalty matrix; evidence retention schedule; which director appointments are owner-reserved; whether managerial positions are time-limited; incident commander activation rules; precise team-specific training requirements; interim Council membership if an Executive Director seat is vacant. The seven-day player-feedback acknowledgement is a suggested service target, not a binding SLA.

**v3.2 change summary:** The three independent offices were consolidated into **one Office of Independent Oversight** with protected Internal Affairs, Appeals & Member Advocacy, and Standards & Assurance functions; a clear jurisdiction/referral matrix addresses overlap with Case Operations, Session Quality and Roleplay Standards. **Staff Experience & Retention** is now a defined responsibility within People & Culture, with volunteer-first check-ins, leave/re-entry, support and aggregate review. **Player Voice & Improvements** is now a defined Community Experience function, with ongoing intake, monthly consultation, quarterly surveys and a public improvement tracker. Decision matrices, Council advisers, org charts, privacy rules, staffing assumptions, examples, templates and launch phases have been aligned. The Governance Council remains **five voting seats** and no new directorate is created.

**v3.2.1 clarification:** The Governance Council is visually connected between CEO and COO **for policy flow only** while the COO directly reports to CEO. The Chief of Staff is a direct COO report and non-voting Council Secretary with defined coordination, tracking and escalation boundaries. No staffing/titles/directorates from v3.2 were consolidated in this full edition.

**v3.2.2 integrated-rank change summary:** Added the agreed eight-level hybrid hierarchy **Staff Member (01) → Moderator (02) → Senior Moderator (03) → Administrator (04) → Senior Administrator (05) → Director (06) → Executive (07) → Owner / Chief Executive (08)**. Removed the stand-alone five-stage career classification as a universal ladder; preserved training statuses and specialist qualifications without treating them as grades. Added direct-linked, minimum-eligibility and qualification-only mappings across all six directorates and the OIO; made grade 06–08 appointment-linked; defined bypasses for non-moderation staff; retained the COO and Oversight Commissioner as the Owner's two independent Executive-grade reports. Updated recruitment, promotion authority, case/permission boundaries, Discord role design, sample records, appointment templates, implementation phases, examples and charter rules. The governance Council, six directorates, OIO independence and staffing totals are otherwise unchanged.

**Final principle:** Build an organization that serves the community. A large organizational chart can be useful for clarity and succession, but actual managerial layers, permissions and staffing must be justified by work. The goal is decentralization with accountability, not hierarchy for its own sake.
