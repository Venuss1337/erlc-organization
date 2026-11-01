<a id="discord-implementation-and-permissions"></a>
# Discord implementation and permissions

**Source version:** 3.2.2 · **Source date:** 2 November 2026 · **Status:** Proposed; no approval inferred.

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

---

[Documentation index](../../README.md) · [Status and review register](../proposals/review-register.md)
