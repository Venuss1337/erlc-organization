# Proposal status, references and review register

**Project version:** 1.4.0 · **Release date:** 2026-11-02 · **Status:** Official release.

**Historical pre-reform record.** Target organization and current approval dependencies are in [R13 reform](v1-3-reform.md). Earlier office names and staffing figures below describe the previous design, not active target positions.

Review material only. This register does not ratify the source or resolve open policy choices. [Council adoption rules](../governance/governance-council.md) govern policy changes; Owner-reserved decisions require the specified ratification.

<a id="current-approval-and-implementation-register"></a>
## Current R14 approval and implementation register

Use the [R14 issue register](v1-4-ratification.md#review-register) for live R14 status, [approval units](v1-4-ratification.md#approval-units) for exact authorities and [current authority](../governance/current-authority.md) before cutover. No ratification, appointments, reserves, elections or security tests are evidenced. R13 is superseded as a target, not recorded as adopted. The older tables below are historical traceability; unresolved dependencies remain carried into R14 unless explicitly superseded.

## Historical v1.1 approval and implementation register

Documentation release is authorized by the user's implementation commission. **No Council ratification, officer appointment, reviewer availability or technical test is evidenced.** Status categories below distinguish existing rules, released proposals, operational tasks and verified artifacts. See the [ratification package](v1-1-ratification.md) for exact text, authorities and bootstrap limits; see the [tabletop record](../readiness-v1-1.md) for simulation assumptions and validation evidence.

| ID | Current rule or gap | Proposed resolution / canonical owner | Approving authority | Dependencies | Status |
|---|---|---|---|---|---|
| REV-01 / GOV-01 | Inactive ED seats prevent full Council quorum; original implementation phases conflicted | Elected interim portfolio delegates and elected recusal substitutes; Phase 1 now references the gated interim procedure | Owner interim adoption under current charter; enhanced Council + Owner for permanent charter | Election, accepted seats, valid quorum | Proposed — Pending Required Approval |
| REV-02 / GOV-03 | Existing explicit good-standing retention of 02–03 also listed as open | Retain existing good-standing decision; specify record and no automatic enforcement access in rank assessment section | Council ordinary policy vote | P&C recording; appeal route GOV-02 | Clarification proposed; existing explicit retention rule unchanged |
| REV-03 / GOV-03 | Director approval and delegated 02–03 approver both mentioned | Written named T&S delegation with scope/expiry; otherwise Director remains approver | Council ordinary policy vote; T&S executes delegation | Qualification/evaluation and P&C check | Proposed — Pending Required Approval |
| GOV-02 | Sanctions/adjudicators/remedies, OIO appointments and external panel incomplete | Case lifecycle, authority matrix, proof, graduated sanctions, independent appeal and alternate mandates | Four Council yes + Owner ratification; protected-function consultation | Valid Council; trained officers; separate access | Proposed — Pending Required Approval |
| GOV-03 | Grade 04/05 criteria, promotion review and manager capability process incomplete | Functional assessment, combined appointment, fair reassessment and management review | Three Council yes; relevant directors/P&C | GOV-02 for binding appeal; actual assessors | Proposed — Pending Required Approval |
| GOV-04 | Incident activation, succession, technical custody and retention not executable | Incident, continuity and technical/privacy procedures | Three Council yes; Owner for reserved acting/recovery powers; GOV-02 for protected changes | Access tests, recovery custody, qualified backups | Proposed — Pending Required Approval |
| IMP-01 | No verified qualified independent reserve list | Screen/train willing investigators, adjudicators, appeal reviewers and assessors; special Owner panel reserve | Commissioner; special appointors under GOV-02 | GOV-02, safe records, real consent and capacity | Operational implementation task — not verified |
| IMP-02 | No evidence of restricted storage, deletion or access/recovery tests | Choose authorized existing tools, test least privilege/negative access, inventory custody and retention/deletion | Technology and OIO owners; Owner reserved privileges | GOV-04/GOV-02, actual system availability | Operational implementation task — not verified |
| IMP-03 | No verified safe duty coverage/acting roster | Capability checks, consenting duty windows, backups and reduced service plan | Service Directors / COO; Owner reserved appointments | GOV-03/GOV-04 and qualified available people | Operational implementation task — not verified |
| IMP-04 | Team-specific functional training remains unspecified | Publish work-relevant assessments and refreshers before independent duty; no universal moderation prerequisite | Relevant Director with P&C, protected OIO qualification owner | Actual trainers, sample assessment and supervised observation | Operational implementation task — not verified |
| IMP-05 | Some Director posts may be Owner-reserved; no designation supplied | Default remains COO appointment; record any existing reserved designation before a vacancy decision; prospective expansion requires constitutional adoption | Owner confirms existing instrument; Council enhanced + Owner for new reserved power | Published designation/decision reference | Unresolved external/approval dependency |
| IMP-06 | Appointment terms and ongoing layer value not reviewed consistently | 30-day acting terms; six-month appointment/layer review without automatic permanent expiry | GOV-03/GOV-04 appointors; GOV-02 Commissioner safeguard | Valid appointments and workload evidence | Proposed — Pending Required Approval |
| VER-01 | Repository artifacts can be checked independently of operations | Preservation ledger, Markdown links, Astro check, build and publication verification | Repository maintainer; not governance approval | Full Git baseline and installed Bun/Python | Verified repository artifacts — dated results in readiness report; no live-control claim |

To change a status to adopted/implemented/verified, record the actual decision or test reference, date, responsible owner, effective scope and limitations. Blank forms and hypothetical names are not evidence. No unresolved issue is closed solely because text exists.

## v1.2 editorial delivery and remaining usability dependencies

The [staff guide](../start-here/staff-guide.md), [everyday tasks](../operations/everyday-work.md), [reporting help](../oversight/get-help.md) and role profiles are instructional summaries authorized by the v1.2 implementation commission. They change no constitutional or case authority. The [usability evidence](../usability-v1-2.md) records the baseline and limitations. **GOV-01–04 above remain pending with the same approvers; no new governance amendment is proposed by v1.2.**

| ID | Gap / delivery | Resolution or owner | Authority / dependency | Status |
|---|---|---|---|---|
| UX-01 | Ordinary users had no task/role entry layer | Three guides, grouped role profiles and task sidebar; repository maintainer | Editorial instruction only; canonical policies control | Implemented documentation; validation recorded in usability evidence |
| UX-02 | No real supervisor/contact/playbook records in this handbook | Relevant Director/P&C supplies actual assignment contacts and local functional instructions outside Git | Actual appointments, current qualifications and approved local playbooks; existing IMP-04 | Operational dependency — not verified |
| UX-03 | No empirical newcomer evaluation | Invite consenting staff to test tasks and revise ambiguous language without collecting unnecessary personal data | Optional future user research, no new mandatory report | Recommended follow-up — not performed |
| UX-04 | Public versus repository-only could be mistaken for confidential | Explicit publication classification and output exclusions; no private records in either location | Repository/site maintainer; real storage/access remains IMP-02 | Publication rules implemented; live private storage not verified |

## Baseline design references and open questions (historical evidence)

The following v1.0.0 material is retained to show the original gaps and ambiguities. **It is not a second live decision register.** The table above and linked canonical specifications give current proposed resolutions and approval dependencies. “Open” in the preserved excerpts below refers to the baseline, not a claim that v1.1.0 lacks drafted procedures.

## Design references and limitations

These public references informed the underlying ideas. This document is a **bespoke organizational design**, not a claim that any of the named organizations endorses or directly operates an ER:LC server.

- GitLab Handbook — Directly Responsible Individuals and decision ownership: https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/
- Atlassian Team Playbook — DACI decision-making: https://www.atlassian.com/team-playbook/plays/daci
- Discord Support — Roles, hierarchy and Administrator permissions: https://support.discord.com/hc/en-us/articles/214836687-Discord-Roles-and-Permissions

**Governance framework in this release:** Five voting Council seats; monthly/async meetings; quorum of four; three affirmative votes for normal policies and four for major structural changes; Owner ratification for reserved changes; a six-month elected Staff Representative term. These charter rules are included in the official release; unresolved implementation decisions below remain open.

**Open governance decisions for the Owner to ratify:** precise criteria and any exceptional equivalencies for grades 04–05; grade/reversion appeals; whether grade 02–03 can be retained after leaving active enforcement; detailed Staff Representative removal/appeal process; Oversight Commissioner appointment/removal criteria; OIO external-reviewer selection and independent adjudicator rules; specific appointment terms; disciplinary penalty matrix; evidence retention schedule; which director appointments are owner-reserved; whether managerial positions are time-limited; incident commander activation rules; precise team-specific training requirements; interim Council membership if an Executive Director seat is vacant. The seven-day player-feedback acknowledgement is a suggested service target, not a binding SLA.

## Pre-existing ambiguities requiring review

The following tensions were found in the original document. Both source passages are retained; this repository makes no decision between them. These are review questions, not newly approved policies.

| ID | Source passages and current locations | Question for authorized review |
|---|---|---|
| REV-01 | Original §14 Phase 1 seats Executive Directors on the Council, while Phase 3 activates their appointments; [implementation phases](../operations/operating-practices.md#implementation-phases). Original §2.3 allows delayed activation; [lean operation](../governance/structure.md#chief-of-staff--reporting-and-exact-mandate). | Confirm when the executive appointments and Council seats become active. The existing [Council charter](../governance/governance-council.md#meetings-voting-and-conflicts) requires an Owner-adopted interim membership/quorum charter for an inactive Executive Director seat; no interim charter was supplied. |
| REV-02 | Original §6.2 permits retained grade 02–03 after an explicit good-standing decision; [rank relationships](../personnel/ranks-and-appointments.md#three-rank-to-position-relationships). Original §16 still lists whether that retention is allowed as an open decision (above). | Confirm whether retention is adopted in the proposed framework or remains an unresolved choice. Historical grade does not supply active enforcement authorization under either passage. |
| REV-03 | Original §6.4's default approval model names Trust & Safety Director approval, while original §8.2 also names a delegated authorized promotion approver; both are linked from [promotion approvals](../operations/authority-and-escalation.md#delegated-decision-matrix). | Confirm the permitted delegation of grade 02–03 approval and its documentation. Do not infer a new delegation or remove one during an editorial refactor. |

The other items in the source's open-decision list remain unspecified, including sanction rules, retention schedules and independent-reviewer procedures. Their absence is not permission to invent them. Use the [contribution process](../../CONTRIBUTING.md#proposing-and-approving-changes) and the original [Council proposal template](../governance/governance-council.md#governance-council-policy-proposal-template) to bring a concrete change to the appropriate decision owner.

---

[Documentation index](../../README.md) · [Status and review register](review-register.md)
