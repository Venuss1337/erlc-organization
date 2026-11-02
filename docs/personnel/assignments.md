<a id="staff-assignments-and-reporting"></a>
# Staff assignments and reporting

**Project version:** 1.1.0 · **Release date:** 2026-11-02 · **Status:** Official release.

Canonical home for home-team reporting, cross-team allocation, capacity and assignment conflicts. Use [the rank framework](ranks-and-appointments.md) for grades and [OIO safeguards](../oversight/independent-oversight.md) for independent case conflicts.

<a id="the-permanent-reporting-rule"></a>
## The permanent reporting rule

Every organizational staff member has:

- **Exactly one Home Team** — the administrative unit to which they belong.
- **Exactly one People Manager** — normally their Home Team Lead or, in a one-person team, their director/manager.
- **One Primary Assignment** — their usual operating job, commonly in the home team.
- **Zero or more approved Secondary Assignments** — explicit roles in other teams or standing rotations.
- **One Task Lead per active assignment** — may differ from the People Manager.
- **An Assignment Coordinator** — an administrative contact in People & Culture for workload visibility, not a superior in the chain of command.

**Practical default:** one primary + one secondary team. A second light secondary assignment can be allowed by exception; ongoing commitments across four or five teams should generally be refused because they make availability and accountability unreliable.

<a id="who-is-responsible-for-what"></a>
## Who is responsible for what?

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

<a id="concrete-example"></a>
## Concrete example

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

<a id="an-allocation-agreement"></a>
## An allocation agreement

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

<a id="priorities-when-assignments-collide"></a>
## Priorities when assignments collide

1. **Immediate safety/security emergency** under a designated Incident Commander — temporary, documented and narrowly scoped.
2. **Previously accepted live duty** (e.g. scheduled session or active investigation) — don't abandon it without handoff.
3. **Approved primary commitments**.
4. **Approved secondary commitments**.
5. **Optional/ad hoc tasks**.

A supervisor cannot manufacture an “emergency” to defeat someone's existing commitments. If it is not time-critical, reschedule it.

---

<a id="secondary-assignment-workflow"></a>
## Secondary assignment workflow

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

<a id="capacity-exclusivity-and-conflicts"></a>
## Capacity, exclusivity and conflicts

- **Assignment capacity:** Apply [the permanent reporting rule](assignments.md#the-permanent-reporting-rule) and its exception process above.
- **Internal Affairs investigators** cannot investigate teams/cases in which they are personally involved; some assignments should be restricted outright.
- Appeals reviewers cannot review their own enforcement actions, those of close collaborators without recusal, or cases on which they advised the initial decision.
- Technical privileged-access administrators are not permitted to use those permissions to obtain IA case material without authorization.
- A Team Lead responsible for an applicant's assessment should disclose personal relationships or conflicts and recuse where needed.
- Inactivity is addressed through the **Staff Experience & Retention Framework**: private check-in, opt-in leave or reduced duties, and published readiness/administrative status rules before punitive action; this is a volunteer community.

## Coverage, leave and continuity dependencies

Use the [capacity/service checks](../operations/operating-practices.md#capacity-and-service-levels) to set real service availability and the [continuity procedure](../operations/continuity.md) for temporary mandates. They do not expand compulsory volunteer hours or create a second permanent manager. An emergency allocation uses [incident command](../operations/incident-response.md) within a qualified, logged scope; a new secondary request still needs consent and the existing home/host approval. If an ED office is inactive, unresolved conflicts go directly to COO. Managers first resolve workload clashes rather than sending every routine change through every layer.

<a id="example-a--cross-team-staff-member"></a>
## Example A — Cross-team staff member

**Taylor** is a Game Enforcement Officer (**Moderator, grade 02**; home team), a certified Session Controller (secondary), and an occasional incident responder. Their single People Manager is the Game Enforcement Team Lead. Their Session Commander directs live session tasks only while Taylor serves an accepted shift. An Assignment Coordinator maintains the record. Neither team may silently change Taylor's availability.

<a id="person--assignment-record"></a>
## Person / assignment record

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

---

[Documentation index](../../README.md) · [Status and review register](../proposals/review-register.md)
