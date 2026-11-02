<a id="discord-implementation-and-permissions"></a>
# Discord implementation and permissions

**Project version:** 1.1.0 · **Release date:** 2026-11-02 · **Status:** Official release.

Canonical home for Discord role design, least-privilege implementation and platform limits. [Personnel grades](../personnel/ranks-and-appointments.md), [Council rights](../governance/governance-council.md) and [case access safeguards](../oversight/independent-oversight.md) define the organizational requirements this implementation must respect.

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

## Access approval, execution and review

**v1.1 procedure specification — GOV-04 adoption and live control tests not verified.** New retention/privacy commitments and cross-organization delegations need recorded adoption. These procedures do not prove a storage system, backup or bot exists. Do not accept confidential case files until suitable restricted storage and a named custodian have been verified.

1. Request states person/app, task, specific permissions, scope, case authorization if any, duration and approver. Owning Director approves routine work access; relevant unconflicted OIO case owner approves case visibility. Technology Director approves technical necessity of privileged maintenance; actual Owner separately approves `Administrator`, ownership-sensitive recovery and privileges beyond delegated scope. Nobody approves their own privilege increase; COO/Owner substitutes for a conflicted technical approver, without bypassing case-owner consent.
2. Separate executor applies approved roles/overwrites using actual native permissions. Record approver, executor, UTC time, before/after and expiry. If only one qualified executor exists, a different unconflicted approver checks the resulting configuration; do not invent two technicians. No executor may add unapproved permissions. If no independent approval exists, pause optional changes; emergency containment below is narrower.
3. Verify effective permissions across all roles and channel overwrites, role order and bot role limits. Test using a consenting appropriate test account/role without exposing real case data; record expected/actual result and date. Include negative tests: ordinary staff cannot read case files, grade roles grant no admin, Council role cannot sanction, acting role expires/revokes, backup can recover the intended asset. A test record, not this page, establishes implementation.
4. Maintain a restricted access inventory: purpose, owner, authorized users/apps, approver, executor, expiry, recovery custodian, last test. Review privileged access monthly and immediately on resignation, role change, compromise or case recusal; review routine access at assignment review. Revoke departure/conflicted access promptly when notified and reachable, contain if delayed, and verify removal including shared links, integrations and external storage—not just grade role.

Discord `Administrator` bypasses channel overwrites, but does not erase role hierarchy restrictions. Owner has actual ultimate control. A private Discord channel therefore cannot promise confidentiality from Owner or holders of Administrator. Before sensitive-case operation, choose an existing authorized record system with separately controlled named access, trustworthy recovery, logs and deletion; otherwise disclose limits and keep intake to safe contact/referral. No infrastructure is introduced by this specification. Do not store confidential evidence in Git, public tickets, personal DMs as the sole archive, or a bot accessible to every administrator. No secret copied archive to defeat ownership.

## Security containment and recovery

Technology Director records which consenting named maintainers have **preauthorized emergency revocation** and which assets they can actually control. At least one qualified backup recovery custodian should be available for critical assets before promising service. Use individual accounts, MFA where supported, strong unique credentials and an approved restricted secret store; never share personal passwords/MFA recovery codes in Discord or Git. Record who controls the Discord server, bot application/Developer Portal, hosting and integrations separately—server administrator is not necessarily application owner. Grant application-team access only where platform-supported and necessary. No promise of recovery when the sole owner is absent.

For suspected compromise:

1. Declare S2/S3 under [incident response](incident-response.md). Available preauthorized maintainer may immediately remove compromised app/user roles, disable unsafe integration or remove the bot within actual permissions; no wait for a fresh Council/Director approval. Capture safe identifiers/configuration/audit facts if it does not prolong harm. Channel deny alone does not contain Administrator. If target hierarchy prevents revocation, contact actual higher-role custodian/Owner through verified safe contact, pause affected operations, and report unresolved control.
2. Application owner/authorized application custodian resets compromised bot token in the Developer Portal; replace it only in trusted deployment secret storage and restart cleanly. Removing a bot from this server is not global token revocation. Investigate exposed webhooks and related credentials; revoke/rotate those separately. Account owner uses official account recovery and secure-device/MFA processes for compromised human accounts; no credential harvesting by staff.
3. Preserve relevant audit entries, UTC times, actor/action IDs and safe before/after state in restricted incident evidence. Discord audit logs retain entries for **45 days** and require `View Audit Log`; capture relevant permitted entries promptly. Audit logs are not a complete history of deleted message contents and cannot restore a deleted server. Maintain a minimal access/decision log without secrets.
4. Qualified maintainer checks root cause, clean host/integrations, changed roles/overwrites, secret exposure and reliable backup state. Restore only the minimum necessary functionality. Technology Director or valid acting authority approves **restoration**, with a separate qualified maintainer executing/checking where staffed; if same operator must execute, approver independently checks safe configuration. No self-approved broad privilege restoration. Re-enable least privilege, verify negative tests and log residual risk. Missing recovery credentials or unverified host keeps the affected bot/service offline.
5. Notify affected case owners if evidence/access may be compromised; IA screens possible deliberate staff abuse independently. Give users a proportionate privacy-safe notice of actual exposure/unknowns through COO and Community Experience, seek qualified advice on any applicable reporting duties, and report platform violations directly. Do not assert a breach is fully contained or all data recovered without evidence. Independent Assurance reviews later through an unconflicted assessor.

## Records retention and deletion

**Proposed schedule under GOV-04/GOV-02; not a claim of legal compliance or configured deletion.** These are proportionate internal defaults after adoption. Applicable law/platform obligations may require different treatment; seek qualified advice when relevant. Collect account IDs, relevant links and necessary context, not real identities, ages/ID documents, locations, medical details or speculative profiles. Follow the [serious-safety route](incident-response.md#serious-safety-and-platform-escalation); suspected illegal sexual material must not be downloaded/copied into case storage.

| Record | Default retention after stated event | Accountable custodian |
|---|---|---|
| Rejected/withdrawn inquiry with no safety concern | 90 days after closure; keep only minimal reason if needed | Relevant intake owner |
| Ordinary enforcement/appeal or resolved personnel case | 12 months after final closure; retain only minimal active restriction identifier/reason while restriction remains active, review annually | T&S / Appeals / Personnel owner, separate scoped stores |
| Serious substantiated abuse, corruption or safety case | 24 months after final closure; review continuing need every six months | IA case custodian; independent access oversight |
| Privileged access approvals, incident action logs and permission reviews | 12 months after expiry/closure | Technology access custodian |
| Unsuccessful applicant record | 90 days after final decision/challenge closure | Recruitment custodian |
| Active assignment/qualification record | While active plus six months after departure, except necessary minimal continuing restriction record | Personnel custodian |
| Consented wellbeing/check-in details | Delete at agreed support closure or within 90 days of last contact; retain only necessary agreed availability action in assignment record | Authorized Staff Experience contact |

Open appeals, credible safety need or applicable preservation duty may justify a **specific hold**: case owner records reason, limited record set, responsible custodian and next review within 90 days. No indefinite blanket hold; expiry prompts review, not automatic destruction during an active appeal. Unsupported allegations do not become a permanent blacklist. Warning actionability is distinct from evidence retention under the [sanction framework](../oversight/case-handling.md#evidence-fairness-and-outcomes).

Custodians review due deletions monthly, delete authorized copies/exports and access links, document category/date/action without preserving deleted personal details, and correct erroneous records across recipients. Record backup deletion lag and prevent routine reuse of expired data; before choosing storage, verify what deletion and access logging it actually supports. Case access transfers use an index and transfer log; never silently alter originals. Minimal redacted trend statistics may survive only if genuinely non-identifying, especially in small teams. A person may request access/correction/deletion through the relevant custodian; respond with reasons, protect others' data and escalate uncertain obligations for qualified advice. No blanket promise to erase an active safety hold.

---

[Documentation index](../../README.md) · [Status and review register](../proposals/review-register.md)
