# v1.1.0 readiness, validation and tabletop record

**Project version:** 1.4.0 · **Release date:** 2026-11-02 · **Status:** Official release.

**Historical reference; not the selected target.** [R14 adoption package](proposals/v1-4-ratification.md) is the sole selected reform. Earlier proposals remain unratified unless actual evidence is supplied; retained office names describe their historical context.

**Historical pre-reform record.** Target organization and current approval dependencies are in [R13 reform](proposals/v1-3-reform.md). Earlier office names and staffing figures below describe the previous design, not active target positions.

Repository-only engineering evidence. This is not an active policy, appointment record, independent re-audit or evidence of operational adoption. The user commissioned implementation of the prior audit findings; no independent audit artifact was found in this working repository or the inspected nearby files. The supplied audit findings and preceding audit conversation are the assessment input. No proposal is ratified by this report.

## Scope and change authority

Read README, AGENTS, contribution/release rules, every maintained policy/review page, source map, original examples/templates, publication generator, deployment configuration and validators before editing. Reviewed current dependencies/configuration without changing framework versions. Original architecture remains: eight ranks, six directorates, CEO/COO, two conditional executive portfolios, CoS, Council, OIO and its three protected functions, one permanent People Manager and primary/secondary assignments.

The implementation commission authorizes a **released specification**. GOV-01–04 in the [ratification package](proposals/v1-1-ratification.md) distinguish required formal adoption from engineering authorization. Exact existing-text supersessions are recorded in `policy_amendments` in the [source map](source-map.json), with before/after hashes, reason and authority. Original baseline/range hashes remain unchanged. New paragraphs do not exempt original tables, fences or worked examples. Existing Phase 1 ED seating and simultaneous-activation guidance are superseded deliberately; historical open questions remain clearly framed as baseline evidence.

## Audit finding to implementation traceability

| Original finding | Canonical implementation | Remaining dependency |
|---|---|---|
| Incomplete investigation/adjudication/sanction/appeal machinery | [Case lifecycle, matrix, proof and remedies](oversight/case-handling.md) | GOV-02 plus actual qualified separated officers |
| No reliable reserve / recusal capacity | [Alternates and external mandates](oversight/case-handling.md#alternates-and-external-reviewers) | Consenting screened reserves; confidentiality/storage |
| Council fails with inactive EDs | [GOV-01 interim elections and fallback](proposals/v1-1-ratification.md#gov-01--interim-five-seat-council) | Actual Owner interim adoption/elections; permanent enhanced ratification |
| Owner independence limits | [Owner panel and non-cooperation](proposals/v1-1-ratification.md#owner-related-review-and-non-cooperation) | External people, safe channels and Owner cooperation; no compulsory remedy |
| Privileged containment/evidence/recovery | [Technical procedure](operations/discord-permissions.md#security-containment-and-recovery) | Real custody/access tests; Owner/application-owner availability |
| Serious platform safety incidents | [Safety escalation](operations/incident-response.md#serious-safety-and-platform-escalation) | Available responder; platform/emergency authorities decide external action |
| Emergency activation/transfer/stand-down | [Incident response](operations/incident-response.md) | GOV-04, domain qualification and actual permissions |
| Succession/temporary mandates | [Continuity](operations/continuity.md) | Reserved appointor decisions, qualified consenting backups |
| Roster disconnected from capacity | [Capability/service checks](operations/operating-practices.md#capacity-and-service-levels) | Actual accepted windows, service reduction decisions |
| Executive relays/report duplication | [Activation](governance/structure.md#activation-and-direct-reporting), [single register](operations/operating-practices.md#one-action-and-exception-register) | COO/Owner workload evidence and use of one record |
| Poor management not necessarily misconduct | [Capability review](personnel/management-and-development.md) | Coaching, appointor and independent challenge capacity |
| Specialist standing / 04–05 assessment | [Rank assessment](personnel/ranks-and-appointments.md#assessment-criteria-and-specialist-access) | Published functional tests, GOV-03, fair assessors |
| Appeals triage/overload | [Case targets/capacity](oversight/case-handling.md#triage-capacity-and-service-targets) | Capacity visibility and unconflicted reserves |
| Unresolved decisions invisible | [Current register](proposals/review-register.md#current-approval-and-implementation-register) | Actual status updates backed by real evidence |

## Research and design basis

Retrieved 2026-11-02 from primary sources; Context7 used for official Discord API and Starlight documentation. These practices inform a bespoke design, not external endorsement or proof of effectiveness. Policy time periods and staffing examples are local design judgments, not claimed research findings.

| Source / date where available | Supported practice and application | Limits of transfer |
|---|---|---|
| [Acas Code](https://www.acas.org.uk/acas-code-of-practice-on-disciplinary-and-grievance-procedures/html), 2015 code | Investigate facts, allow response and use impartial appeal; different investigation/hearing officers where practicable. Supports role separation and reasons | Employment code is not automatically the law governing these volunteers; no employment contract/hearing bureaucracy imported |
| [Google SRE Workbook, incident response](https://sre.google/workbook/incident-response/), 2018 | Explicit command, communication, handover and exercises inform the short incident flow | Paid technical on-call coverage and Google's resources do not exist here; no 24/7 promise |
| [Discord permission reference](https://github.com/discord/discord-api-docs/blob/main/developers/topics/permissions.mdx), living | Role-position restrictions and Administrator overwrite bypass constrain real access and containment | Organizational policy cannot remove native Owner power or manufacture bot privileges |
| [Discord audit-log reference](https://github.com/discord/discord-api-docs/blob/main/developers/resources/audit-log.mdx), living | 45-day audit-log retention and View Audit Log permission require timely lawful collection | Logs are not a complete message archive or tested backup |
| [Discord token reset](https://support-dev.discord.com/hc/en-us/articles/6470840524311-Why-can-t-I-copy-my-bot-s-token), updated 2025-05-27 | Developer Portal reset and trusted redeployment support token-compromise containment | A server moderator may not own the application or host; custody must be verified |
| [Discord parent/guardian reporting](https://support.discord.com/hc/en-us/articles/360000291932-How-to-Contact-Discord-Safety-for-Parents-and-Guardians), 2024-04-04 | Specific message reporting, appropriate emergency escalation, no misleading/mass reports | Internal volunteers cannot replace platform safety or emergency services |
| [Roblox reporting/blocking](https://about.roblox.com/reporting-and-blocking), living | Report relevant experience/content through platform tools | ER:LC staff cannot act as Roblox platform adjudicators |
| [NCVO volunteer role descriptions](https://www.ncvo.org.uk/help-and-guidance/involving-volunteers/planning-for-volunteers/writing-volunteer-role-descriptions/), living | Clear responsibilities/boundaries and balanced, flexible volunteering inform coverage and capability review | UK guidance is not a universal legal conclusion; no mandatory hours or employee discipline imported |
| [Starlight frontmatter](https://starlight.astro.build/reference/frontmatter/) and [sidebar](https://starlight.astro.build/guides/sidebar/), living | Sidebar order controls navigation; hidden removes a sidebar entry, not necessarily the underlying published page | Explicit source generation remains the publication boundary; no proposal staged merely with hidden metadata |

No live server/account inspection, actual case review or technical penetration test was authorized or performed. No legal compliance certification, safeguarding qualification or reliable external reviewer availability is claimed.

## Tabletop method and fixtures

Fifteen new traces below evaluate the new specification rather than importing old audit outcomes. Fictional officers consent only to the listed scenario duties. Assumptions do not establish real appointments or required working hours. **As of this release all new policy gates are unverified.** The statuses below apply to present readiness, with a separate explanation of how the designed path works after stated adoption. “Executable under documented rules” is used only for existing valid routine authority; “Conditional” requires staffing/implementation/adoption; “Blocked” has a specific unmet requirement that cannot be safely bypassed.

**Counts:** A = distinct authorizing/outcome decisions in the modeled path (not notifications, evidence collection, observer advice or mechanical execution). H = meaningful transfers between responsible functions shown by arrows; reporter-to-intake and routine notices excluded. Counts are scenario-specific, not claims that every case has an identical number of approvals. When the same person holds compatible roles no new headcount is added. Elapsed response periods are service targets, not measured duration.

**20-person fixture:** Owner Ada; COO Ben; T&S Cora (Director), Dev (qualified senior enforcement/IC), Eli and Faye (officers), Gus (moderator); Live Ops Hana (Director/qualified commander), Ivo (commander), Jae and Kit (hosts); RP Lia (coordinator), Mo (trainer); Community Nia (Director), Oren (support/elected representative); P&C Pia (coordinator); Tech Quin (maintainer); OIO Rosa (Commissioner), Sol (IA), Tavi (Appeals). Exactly 20 including Owner; no ED/CoS. Existing retained grades follow valid assignments, not invented promotions. Non-moderators retain specialist eligibility. Elected portfolio delegates require actual ballot; Cora and Nia are illustrative candidates, not appointments. Quin is the only technician, so independent technical recovery is a known gap. No external reserve is counted as an available staff member.

**30-person fixture:** Same 20 plus three T&S officers, three Live Ops controllers/hosts, one RP trainer, one Community supporter, one P&C assessor and one technical backup = 30. Assume the backup passes a fictional recovery exercise for a named bot; this is not a real test. EDs/CoS still inactive. No one is assumed always online. One session can use Hana/Dev; a second requires Ivo plus a separate available qualified officer, not Dev twice.

**60-person fixture:** Owner 1; executive office 4 (COO Ben, Ops ED Uma, Services ED Vik, CoS Wren); T&S 15, Live Ops 15, RP 9, Community 6, P&C 4, Tech 3, OIO 3 = 60. Every allocation includes its Director/lead; no extra Council staff. Council: Ada, Ben, Uma, Vik and Oren (existing Community staff); Wren non-voting. Rosa/Sol/Tavi retain distinct OIO roles. Della is fictional Technology Director, Emil a recovery maintainer and Freya a backup; Cora/Hana remain their Directors. For specific traces external X1 investigator, X2 adjudicator, X3 appeal reviewer are only assumed where explicitly stated; they are temporary independent volunteers, outside the 60 staff count, not permanent offices or guaranteed reserves.

## Fifteen scenario traces

### T01 — 20 staff; both Executive Directors inactive

**Rules:** GOV-01, existing Council quorum and direct COO reporting. Existing full charter has only Ada, Ben and Oren, so no policy vote. Ada may actually adopt the 90-day interim charter under the existing interim power; Pia administers nomination/ballot with unconflicted OIO process observation. Staff elect consenting Cora/Nia and alternates; no rank is created. Five seated people then test four-person quorum including executive, portfolio and frontline representation; ordinary three yes, major four yes plus reserved ratification.

Path: Owner interim decision → election administration → seated Council → recorded implementation. **A3** (interim adoption, electoral authorization, subsequent policy vote), **H3**. If no candidates/Owner signature, no adoption; Ben still runs routine services and may cancel unsafe sessions. **Outcome: Conditional; currently blocked for new Council policy.** The procedure resolves the design contradiction after real adoption, not by counting empty seats.

### T02 — 30 staff; demand exceeds volunteered coverage

**Rules:** service capability checks, accepted-duty priority and one register. Hana sees three requested sessions but coverage for only two independent commander/responder pairs. She publishes two windows, pauses the third and asks Pia to recruit for the missing capability rather than an ED. Quin/backup postpone optional maintenance during accepted session support. Cora/Hana negotiate the overlap; if unresolved Ben decides the service priority, with no CoS/empty ED relay.

Path: service lead → Workforce coordination → service lead final roster. **A1** service commitment decision, **H2**; an unresolved cross-directorate deadlock adds one COO decision/handoff. Complaints about fewer sessions are legitimate service feedback, not a duty to conscript hosts. **Outcome: Executable for existing voluntary service reduction; new measured coverage routine conditional on GOV-03/04 and real availability.** It does not make three sessions possible.

### T03 — 60 staff; all directorates active

**Rules:** conditional portfolio activation, delegated decisions, Council five seats. Assume actual appointment/qualification records and GOV-03 activation for this tabletop. Ben uses one month of exception records to justify Uma's and Vik's separate remits, Owner appoints, Wren coordinates one shared register. Hana changes an ordinary session roster directly; Uma handles a substantive staffing tradeoff, not every roster edit. Council considers only a cross-organization rule, outside this routine path.

Path: host scheduling → Hana decision → dispatch execution. **A1, H2**. No further executive approval is inserted. Existing model allows routine delegation; staffing still cannot guarantee continuous service or reserve independence. **Outcome: Conditional for full fixture/activation; routine mandate is executable under existing rules.** The model no longer needs executive activation purely for seats.

### T04 — ordinary staff abuse, initial adjudication and appeal

**Rules:** case lifecycle, ordinary-staff matrix, balance of probabilities, 14-day appeal. In the 60 fixture a T&S Senior Administrator is accused of fabricating removal notes. Rosa screens officers; Sol investigates, Cora (unconflicted Director) decides after notice/response, Tavi independently hears factual/proportionality challenge, Personnel/technical executor applies final remedy. Assume Tavi had no prior advice and is not under Cora's direction. Evidence is sufficient for warning/retraining, not deliberate fabrication; Tavi corrects an overstated finding and records propagation.

Path: Rosa assignment → Sol facts → Cora decision → Tavi appeal → executor. **A3** assignment/initial/appeal, **H4**. If Cora is implicated use external/cross-director fallback, not T&S self-review. **Outcome: Conditional on GOV-02 and safe records; designed path executable with these officers.** No guarantee the appeal agrees with IA, and no new penalty applied before adoption.

### T05 — IA investigator conflict

**Rules:** conflict screen, alternate mandate, separate appeal. Sol discloses a close collaboration with subject Dev before opening evidence. Rosa excludes Sol, checks a consenting trained reserve X1, gives a 30-day scoped mandate; Cora adjudicates if unconflicted and Tavi remains separate. X1 cannot later hear the appeal. If X1 is unavailable no qualified internal replacement is assumed.

Path: conflict screening → Rosa alternate mandate → X1 investigation → Cora adjudication. **A2** assignment and initial decision, **H3**, before any appeal. **Outcome: Conditional if screened X1 exists; otherwise Blocked.** Existing protective measures receive independent review rather than indefinite restriction while Sol investigates a friend.

### T06 — complaint against COO

**Rules:** senior-office matrix and Owner-reserved removal. Sol receives the complaint safely; unconflicted Rosa coordinates Owner appointment of external X1 and a different external appeal reviewer X3. X1 investigates, Ada decides initial consequence, X3 reviews. Ben cannot block intake or set evidence access; Wren cannot route case evidence through the executive register. Assume X1/X3 consent and are unconflicted; no invented capacity from the three-person OIO.

Path: Rosa coordination → Owner assignment → X1 findings → Ada decision → X3 appeal → Owner execution. **A3** external assignment, initial, appeal; **H5**. Reserved removal recommendation needs actual Ada action even if appeal is otherwise authoritative. **Outcome: Conditional on GOV-02, external people and Owner cooperation; refusal leaves remedy unresolved.** No absolute independence claim.

### T07 — credible complaint against Owner

**Rules:** GOV-02 independent selectors/panel and platform reporting. Sol, Tavi and Oren screen/select X1/X2/X3 with at least two unconflicted selectors. X1 investigates available lawful material; X2 issues advisory reasons after Ada responds; X3 independently handles challenge. Ada refuses the recommendation and removes a channel. Panel cannot compel logs or reverse ownership. Functional leads can state the obstruction safely through available authorized channels and offer platform referrals; no secret evidence archive.

Path: unconflicted selectors → X1 → X2 → X3 → Owner accepts/refuses execution. **A4** panel selection, initial advice, appeal advice, reserved execution choice; **H4**. Missing panel or lawful records blocks even advisory completeness. **Outcome: Blocked for guaranteed enforcement against hostile Owner; conditional advisory review only.** This remaining structural limit is explicit, not solved by text.

### T08 — overloaded Appeals

**Rules:** triage, consolidation, independence, target updates. Twelve appeals arrive about one enforcement action; two also concern distinct personal evidence. Tavi groups common questions but preserves distinct submissions. Fictional estimated remaining review effort is nine hours; Tavi volunteers two before next review and no reserve accepts. Rosa tells parties the capacity limit, prioritizes active restrictions, requests screened alternates and releases optional assurance commitments; officers may decline. Repeated messages do not become twelve full investigations.

Path: Appeals intake → Rosa capacity action → Tavi scoped priority review. **A1** capacity/service decision, **H2**; no final merits decision counted because backlog remains. **Outcome: Conditional for fair partial service, Blocked for full timely clearance.** Targets are missed transparently, appeal eligibility stays open and conflicted shortcuts are prohibited.

### T09 — Council quorum failure and urgent measure

**Rules:** existing urgent seven-day COO power; GOV-01 elected recusal substitutes after adoption. Assume interim charter actually adopted. Cora and Nia recuse on an item affecting a personal financial interest; only one elected unconflicted substitute exists. Four seats can still meet if required representation remains, but a major item needs four yes; a further absence leaves three and no vote. Secretary records no adoption. Ben may impose a genuine narrowly necessary security measure for seven days, not constitutional change. Elect/seat a valid alternate or let measure expire; no rolling reissue.

Path for failure: Secretary conflict/quorum check → deferred Council record. **A0, H1**. Urgent path: Ben temporary measure → Secretary notice/review register. **A1, H1**. **Outcome: Executable for existing bounded urgent protection; major policy Blocked until legitimate quorum.** Deadlock is sometimes the legitimate result, not a defect to evade.

### T10 — unexpected Director resignation

**Rules:** continuity, retained grade, access revocation. Della resigns immediately. Ben assesses willing Emil, with a work-relevant leadership assessment/P&C check; appoints acting Technology Director for 30 days if qualified and not separately Owner-reserved. Freya executes/checks approved scoped access; named custodian removes Della's access. If Emil only wants specialist work, Ben retains essential decisions and cuts optional service; do not coerce a promotion.

Path: COO acting appointment → Personnel record → access execution → accepted handover. **A2** appointment and distinct privilege approval (if needed), **H3**. No permanent deputy or Council vote. **Outcome: Conditional on real appointor, qualifications and recovery access; loss of sole application-owner control remains Blocked.** Returning officer/replacement must have explicit resumption/reversion.

### T11 — major session incident

**Rules:** incident activation, distinct domains and safe coverage. Ivo commands a session, Dev is separately qualified/available Duty IC; Faye enforces within certification. Coordinated disruption overwhelms routine operations. Ivo pauses session, Dev declares S2 and accepts command, Faye applies qualified temporary removals, technical maintainer investigates bot misuse without case access. Wren receives status only. Dev logs/communicates objectives and transfers explicitly to qualified relief or ends service if no relief.

Path: Ivo alert/pause → Dev command → Faye containment → normal T&S lasting-action review. **A4** session pause, command activation, scoped enforcement decision, later lasting decision; **H3**. These are domain decisions, not four advance approvals: no preapproval by Director/ED/COO to pause. Stand-down requires technical/enforcement readiness checks, not an all-powerful IC signoff. **Outcome: Conditional on GOV-04, qualification and access; safe pause executable under existing session mandate.** Abuse concerns go separately to IA.

### T12 — compromised privileged Discord bot

**Rules:** native role hierarchy, emergency revocation, Developer Portal custody, independent restoration approval. Freya is preauthorized maintainer but bot highest role is above hers. She cannot kick/demote it merely because organizational rank permits investigation. She alerts actual higher-role Owner custodian and pauses affected functions. Assume Ada reachable: Ada removes server access, application custodian Emil resets token, Freya collects safe audit facts, Della/valid acting authority approves restricted restoration only after clean host/permission tests. Removing the bot alone does not revoke its token globally.

Path: Freya alert → actual higher-role custodian containment → application custodian rotation → technical restoration approver → executor. **A3** server containment, token revocation and restoration approval, **H4**. Preauthorized containment/revocation needs no fresh advance approval; restoration does. Separate application/host custody may add real blockers. **Outcome: Conditional with reachable custodians and successful tests; Blocked if Owner/application custody unavailable.** No test or recovery success actually demonstrated by this tabletop.

### T13 — Administrator or Director promotion dispute

**Rules:** 04/05 evidence, combined appointment, relevant qualifications, fair selection and remedy limits. Emil wants technical leadership without moderation history. Structured assessment demonstrates substantive function management; Director/P&C may combine 04 with a real appointment. For Director, Ben uses published criteria and unconflicted technical assessment then directly appoints 06, preserving prior validated grade; no forced 02/03/05 detour. Another applicant alleges favoritism: Tavi reviews records independently, orders reassessment with a different assessor if a material conflict existed, not automatic promotion.

Path: functional assessment → appointor decision → Personnel → independent challenge → reassessment owner. **A2** appointment and appeal, **H4**; P&C check is not a second substantive promotion committee. **Outcome: Conditional on GOV-03/GOV-02; non-moderator route already explicit and executable in baseline.** No new universal specialist ladder; a declined vacancy does not lower earned standing.

### T14 — multiple volunteers unavailable

**Rules:** consent, capacity checks, assignment priority, leave and continuity. In 30 fixture Ivo, Faye, Quin and Pia become unavailable without private explanation. Hana reassesses actual windows; no second commander/responder pair, so consolidates to one session or cancels if first pair also absent. Backup technician handles preauthorized containment only; optional release deferred. Oren publishes reduced support notice if affected. Managers arrange handoff when able, no coercive hours or automatic IA.

Path: availability notice → service leads reduce accepted work → Workforce/acting record → published service notice. **A1 per affected service** (modeled two: sessions and technical work), **H3**. If no Workforce contact, leads record the change directly and notify COO; no mandatory coordinator bottleneck. **Outcome: Executable for existing leave/service reduction; conditional for new continuity powers.** Less service is the legitimate outcome; roster headcount cannot repair lost availability.

### T15 — Chief of Staff versus Executive Director

**Rules:** CoS coordination-only mandate, direct COO report and one register. Wren asks Uma to rewrite current action updates into a new daily slide deck and countermand Hana's roster. Uma points to the existing entry, declines the extra managerial order and explains the live commitment. Wren records a scope disagreement; Ben decides the substantive priority and removes the duplicate reporting request. Any alleged retaliation goes independently to IA, not a CoS disciplinary note.

Path: CoS coordination request → ED scope response → COO decision → CoS shared-register update. **A1, H3**. No Council or Owner signoff. **Outcome: Executable under existing CoS boundaries; register simplification conditional on GOV-03.** A COO who informally rewards overreach remains a human implementation risk, not a formal authority gap.

## Residual risks and adoption checklist

| Gate | Required evidence before claiming operational readiness | Present state |
|---|---|---|
| Governance legitimacy | Actual full/interim charter decision, electorate/ballot/seat records, quorum and ratification records | Not verified |
| Fair case machinery | Trained separated case officers, usable external reserves/panel, written delegated powers and independent challenge | Not verified |
| Privacy/security | Real storage/access/deletion capability, privileged custody, negative permission tests and recovery exercise | Not verified |
| Service continuity | Consented coverage, qualified backups/acting records and safe reduced-service notices | Not verified |
| Policy communication | Effective dates, understandable training, safe complaint routes and acknowledgement of limits | Not verified |
| Owner accountability | Actual cooperation with transparent reasons and external recommendations | Cannot be guaranteed technically |

Minimum adoption order: (1) legitimate Council mode; (2) ratify GOV-02 and protected safeguards; (3) staff/test confidential records and reviewer mandates; (4) ratify/implement GOV-03/04 with actual coverage/access exercises; (5) launch only verified safe services and review after 90 days. A major safety report can always go directly to platforms/emergency authorities; it must not wait for this sequence.

## Updated readiness assessment

Same category weights and 0–10 anchors as the audit: 0 absent, 2 fundamentally broken, 4 partial, 6 coherent but material gaps, 8 implementable with realistic safeguards, 10 exceptional and evidenced. These are author judgments about the **released specification**, not an independent validated performance measurement. Approval, staffing and control evidence are still absent, so actual operational readiness cannot be rated as deployed or improved empirically.

| Category | Weight | Prior | Revised specification | Weighted points | Basis and remaining weakness |
|---|---|---|---|---|---|
| Clarity/coherence | 12 | 8 | 8 | 9.60 | Canonical scopes and status gates clearer; more procedural material needs training |
| Authority/delegation | 12 | 7 | 8 | 9.60 | Named adjudicators/acting authority/limits; reserved ratification still external |
| Efficiency/bureaucracy | 12 | 5 | 6.5 | 7.80 | One register and conditional portfolios; full architecture still expensive at small scale |
| Staffing/resource realism | 11 | 4 | 6 | 6.60 | Capability-based reductions and honest blocked cases; independent reserves remain scarce |
| Scalability/adaptability | 10 | 6 | 7 | 7.00 | Interim/full modes and individual activation; elections/real capacity still required |
| Oversight/accountability | 10 | 6 | 7 | 7.00 | Separated decision machinery and external scope; hostile Owner cannot be compelled |
| Personnel/fairness/retention | 9 | 7 | 8 | 7.20 | Non-punitive coaching and job-relevant advancement; assessor quality untested |
| Incident/resilience | 9 | 4 | 6.5 | 5.85 | Activation, transfer and expiry; qualified backups/access may be missing |
| Technical implementation | 8 | 5 | 6 | 4.80 | Real native constraints and recovery procedure; no live test evidence |
| Documentation/implementability | 7 | 6 | 8 | 5.60 | Runnable decision paths, compact templates, preservation and build checks; adoption still needed |
| **Total** | **100** | **58.5/100** | — | **71.05/100** | **Specification assessment only; no operational uplift claimed** |

Calculation: sum(weight × score / 10). Separate conceptual quality 8/10; conditional operational practicality 6.5/10; expected efficiency 6/10; resilience 6/10. Confidence medium in textual coherence, low in real-world capability. Do not use these scores as an adoption gate; use the evidence checklist. More text earns no credit by itself: staffing, Owner control and untested access deliberately constrain the result.

## Repository validation record

Validation commands: `bun install --frozen-lockfile`, `bun run validate:docs`, `bun run check`, `bun run build`, `git diff --check`. Build includes output routes, base-path links/assets/fragments, publication list, sidebar groups, license notices, search assets and workflow checks. Negative preservation checks must still reject an unrelated original-policy change and tampered amendment hash; restored files must pass afterward.

Actual command results and any warnings are reported in the implementation delivery. This record does not certify controls on Discord, Roblox or external case-storage systems. LICENSE and v1.0.0 history are checked against Git before committing. No release tag, push or deployment is authorized.

### Checks performed on 2026-11-02

- Frozen Bun installation passed without dependency/lockfile changes.
- Markdown validator passed: 28 Markdown files, 346 relative links/fragments, all 1,158 original lines in 48 ranges; two exact authorized supersessions reversed successfully for baseline comparison. All 22 tables, 14 fences and nine original worked examples remain intact.
- Preservation negative controls passed: an unrelated original one-manager rule mutation failed validation, and a tampered amendment hash failed validation. Both files were restored exactly afterward. This checks meaningful failure behavior, not merely a successful build.
- Original source-map provenance/ranges/editorial records, LICENSE bytes, README licensing section and complete v1.0.0 changelog entry match pre-change Git content. All original explicit section anchors still precede their original subject headings.
- Astro check passed with zero errors, warnings or hints. Production build passed with 22 routes and 1,319 local links/assets/fragments; base path, sidebar, specification notices, canonical URLs, license notice, search assets and workflow configuration passed automated verification.
- Build retains the pre-existing nonfatal Starlight `/404` route-priority warning; the expected `404.html` is emitted and checked. No dependency upgrade or unrelated 404 redesign was introduced.

These are repository/build checks, not a live Discord permission test, external-reviewer qualification test or governance approval. The final post-edit validation and clean committed state are reported at delivery.
