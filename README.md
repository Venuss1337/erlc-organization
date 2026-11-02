# ER:LC Organization — v1.4.0

An organizational operating system for an independently operated ER:LC Discord/Roblox community. This repository separates governance, personnel, delivery and independent oversight so each policy has a clear home and can evolve without conflicting definitions.

**Project version:** 1.4.0  
**Release date:** 2026-11-02  
**Status:** Official release — **Office of the COO & Distributed Executive Management**. This is a released documentation specification; R14, retained GOV protections and actual appointments/controls require explicit adoption. R13 was not evidenced as adopted and is historical. v1.0.0 remains the first official release.

## Simplified hierarchy

```text
Owner / CEO
├── COO — Office of the Chief Operating Officer
│   ├── Direct delivery reports: three Division Heads + Technical Lead
│   └── Specialized Office work: Integration, CoS, conditional Planning
└── Oversight Commissioner — protected IA / Appeals / Assurance
Council: collective policy, not an operating management layer
```

Office specialists are lateral decision owners within written mandates, not intermediaries supervising Heads. [Office charter](docs/governance/office-of-the-coo.md), [current authority before cutover](docs/governance/current-authority.md), [R14 adoption](docs/proposals/v1-4-ratification.md) and [workload/staffing evidence](docs/executive-readiness-v1-4.md) distinguish specification, actual authority and unverified capability.

## Start with your work

- [Find your role](docs/start-here/staff-guide.md): new staff, enforcement, sessions, specialists, managers, executives and oversight.
- [Everyday staff tasks](docs/operations/everyday-work.md): 16 common tasks with owners, records and escalation.
- [Get help, report misconduct or appeal](docs/oversight/get-help.md): safe routes without reading a full case manual.

These guides summarize the canonical rules below. They are not another approval system; actual local assignments, qualifications, playbooks and contacts remain necessary.

[R14 amendment and migration](docs/proposals/v1-4-ratification.md) · [Function map](docs/operations/function-map.md) · [Staffing and comparative tests](docs/executive-readiness-v1-4.md)

## Documentation index

| Domain | Canonical documents and policies |
|---|---|
| Governance | [Current controlling reference](docs/governance/current-authority.md) · [Office of the COO](docs/governance/office-of-the-coo.md) · [Structure, executive mandates and charter index](docs/governance/structure.md) · [Governance Council: membership, voting and adoption](docs/governance/governance-council.md) |
| Personnel | [Eight ranks, eligibility, promotions and appointments](docs/personnel/ranks-and-appointments.md) · [Home teams, cross-team assignments and workload conflicts](docs/personnel/assignments.md) · [Recruitment and onboarding](docs/personnel/recruitment.md) · [Management review and professional development](docs/personnel/management-and-development.md) |
| Trust & Safety / Game & RP | [Trust & Safety](docs/directorates/trust-and-safety.md) · [Live Operations](docs/directorates/live-operations.md) · [Roleplay Programs](docs/directorates/roleplay-programs.md) |
| Community & People / Technology | [Community Experience and player voice](docs/directorates/community-experience.md) · [People & Culture and staff experience](docs/directorates/people-and-culture.md) · [Technology & Systems](docs/directorates/technology-and-systems.md) |
| Independent oversight | [OIO: protected functions, referrals, independence and case safeguards](docs/oversight/independent-oversight.md) · [Case lifecycle, adjudication, appeals and alternates](docs/oversight/case-handling.md) |
| Operating procedures | [Authority, decision owners and escalation](docs/operations/authority-and-escalation.md) · [Discord permissions and privacy](docs/operations/discord-permissions.md) · [Cadence, capacity and implementation](docs/operations/operating-practices.md) · [Incident response](docs/operations/incident-response.md) · [Temporary authority and continuity](docs/operations/continuity.md) |
| Pending review | [Approval and implementation register](docs/proposals/review-register.md) · [Exact ratification package](docs/proposals/v1-1-ratification.md) · [Readiness evidence and tabletop tests](docs/readiness-v1-1.md) |

## Find a specific policy

- **Who can approve an action?** Start with the [delegated decision matrix](docs/operations/authority-and-escalation.md#delegated-decision-matrix); follow its canonical dependencies for grade eligibility, Council voting or case safeguards.
- **Can someone hold multiple roles?** Use [staff assignments](docs/personnel/assignments.md) and [rank relationships](docs/personnel/ranks-and-appointments.md#three-rank-to-position-relationships).
- **Where does a complaint or appeal go?** Use the [jurisdiction and referral matrix](docs/oversight/independent-oversight.md#one-intake-one-case-owner--jurisdiction-and-referrals).
- **Where are examples and forms?** The [worked-example index](docs/governance/structure.md#worked-examples) and [template index](docs/governance/structure.md#adoption-templates) link to all original examples and templates beside their owning processes.
- **What is the current release?** v1.4.0 is the current released documentation; v1.0.0–v1.3.0 remain in the official history. The [review register](docs/proposals/review-register.md) separately tracks unresolved governance and implementation decisions.

## Maintaining this repository

### Documentation website

The Astro Starlight portal is configured for **[ER:LC Organization on GitHub Pages](https://venuss1337.github.io/erlc-organization/)**. It becomes available after you enable Pages and push this implementation; this change does not publish the site itself.

The [handbook landing page](docs/index.md) and the policy files linked above remain the canonical Markdown sources in `docs/`. The explicit publication list in [site.config.mjs](site.config.mjs) includes 26 sources: the existing policy/procedure pages, three staff guides and the landing page. `scripts/site.mjs` automatically prepares ignored, read-only copies in `src/content/docs/` for Starlight, deriving titles and translating repository links into base-aware website links. The sidebar groups work by user need rather than source folder. Most reference groups start collapsed; all published sources remain accessible through navigation and search. Never edit those generated files. `LICENSE` is also rendered without changing its text. Proposals, the review register, readiness/tabletop records, migration records and source-map data are not emitted as website pages or indexed by search; links to them lead to the repository. Repository-only is not private; confidential files and working recovery details must remain outside both Git and the public website. Blank restricted-record templates are examples only, not completed confidential records.

Use **Bun 1.3.11** (the pinned package manager) for installation and all site commands:

```sh
bun install
bun run dev
```

Open `http://localhost:4321/erlc-organization/`. The development command watches canonical `docs/` files and refreshes the generated content. Restart it after changing the publication list or site configuration. To check, build and preview the production site:

```sh
bun run check
bun run build
bun run preview
```

`bun run build` generates static output in ignored `dist/`, builds Starlight's full-text search, and verifies routes, assets, fragments, sidebar groups and the repository base path. Search should be tested in the production preview. `bun run verify` repeats those output checks. Commit `bun.lock`; use `bun install --frozen-lockfile` for reproducible installation. Astro and Starlight dependency versions are separate from project release **1.4.0**.

### GitHub Pages deployment

[deploy.yml](.github/workflows/deploy.yml) follows the [official Astro Pages workflow](https://docs.astro.build/en/guides/deploy/github/), using the Astro build/upload action and GitHub Pages deployment action. Pushes to `main` and manual **Actions → Deploy documentation to GitHub Pages → Run workflow** runs build with Bun and the committed lockfile. Only the deploy job receives Pages/OIDC write permissions. Nothing deploys from a local build.

Before the first deployment, set **Settings → Pages → Build and deployment → Source → GitHub Actions** in `Venuss1337/erlc-organization`. Allow the workflow's actions under **Settings → Actions → General** if repository or organization restrictions require it. If the `github-pages` environment has deployment protection, permit `main` or approve its deployment. Ensure your GitHub plan and repository visibility support Pages; no visibility change is made here. No deployment secret or personal access token is required by this workflow.

The configuration uses `site: https://venuss1337.github.io` and `base: /erlc-organization`. Keep both aligned with the repository if it moves. Do not commit `dist/`, `.astro/`, `node_modules/`, or generated Markdown, and do not add confidential data to the public publication list.

### Repository validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing policies. [AGENTS.md](AGENTS.md) supplies agent-specific rules. [CHANGELOG.md](CHANGELOG.md) separates editorial repository changes from organizational design history.

Run the dependency-free check from the repository root with Python 3.9 or newer:

```sh
python scripts/validate_docs.py
python scripts/validate_structure.py
python scripts/validate_executive.py
```

The [migration and validation report](docs/migration-report.md) explains the original preservation checks. The [v1.1 readiness record](docs/readiness-v1-1.md) preserves the operational-readiness assessment. The [v1.2 usability record](docs/usability-v1-2.md) contains before/after workflow counts, persona walkthroughs, scale tests and preservation evidence. The [machine-readable source map](docs/source-map.json) maps every original line to its destination. The untouched source is preserved in baseline commit `ea0f598` as the original draft file identified in the source map; it is historical evidence, not a second live policy document.

## License & Copyright

**Look-But-Don't-Touch License (LBDT).** Copyright © 2026 Wiktor Fila.

This repository is proprietary and is not open-source. LBDT grants no general public permissions to copy, modify, redistribute, or reuse its protected contents, subject to applicable law and third-party rights. Its most generously licensed feature is closing the tab.

LBDT is a satirical, nonstandard license, not a legally vetted instrument; no claim is made that its humorous restrictions are legally enforceable. See [LICENSE](LICENSE) for the complete text and the upstream attribution notice, which applies only to the third-party license template.
