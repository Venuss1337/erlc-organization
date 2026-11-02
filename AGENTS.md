# Repository instructions for agents

- Read [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), the relevant canonical policies and [review register](docs/proposals/review-register.md) before editing.
- This is a Markdown documentation repository with an Astro Starlight static website. Use lightweight text tooling for ordinary documentation edits. Use Bun exclusively for site packages and scripts; do not introduce other frameworks or infrastructure.
- The current project version is **1.3.0**, status **Official release**, dated **2026-11-02**. It releases Organizational Restructuring & Management Efficiency guidance; v1.0.0 remains the first official release. Earlier iterations were unreleased development drafts. Keep release metadata aligned with README and CHANGELOG. Do not infer resolution of open governance decisions from a release label.
- Do not change policy without authorization. Preserve ranks, appointment eligibility, reporting, voting, reserved powers, independent case safeguards, volunteer protections and permission boundaries. If wording conflicts, record it for review rather than inventing a resolution.
- Each rule has one canonical home in the README index. Edit that home and use relative links elsewhere. Charts, decision-routing tables, examples and checklists summarize the linked rules; do not make them competing policy definitions.
- Keep all substantive examples, tables, fenced records and templates. Blank templates are not approval records. Never add completed confidential records to this repository.
- [docs/source-map.json](docs/source-map.json) records the original baseline and destinations. Never rewrite the baseline or suppress preservation failures to conceal a policy change. Future authorized changes must document their approval and explain any updated preservation exception.
- Run `python scripts/validate_docs.py`, inspect the diff, and verify Git status. Use conventional descriptive commits when committing is requested. Preserve history; do not create a remote or publish unless requested.

## Website architecture and publication

- Canonical policy sources remain in `docs/`; the landing page is `docs/index.md`. Never maintain duplicate policy files. `scripts/site.mjs` generates ignored `src/content/docs/` at dev/build time; those files are disposable and must never be edited or committed.
- `site.config.mjs` is the explicit publication list. Adding Markdown does not authorize publication. Review any addition for approval status and confidential information before adding it. Proposals, review/migration records and `docs/source-map.json` remain repository-only; do not expose them as active policies or search entries. Blank templates are illustrative; never publish populated confidential records.
- Markdown links remain relative repository paths in the sources. The generator converts published links to `/erlc-organization/` routes and repository-only links to GitHub. Preserve legacy section anchors. Derive display titles from each source's H1, and do not rewrite policy wording for presentation.
- Use `bun install`, `bun run dev`, `bun run check`, and `bun run build`. Commit only `bun.lock` as the package lockfile. `bun run build` includes output-link/publication checks; also run the Python preservation validator. Do not commit dependencies, `.astro/`, staging content or `dist/`.
- Keep `site` and `base` aligned with the GitHub remote. The Pages workflow builds on pushes to `main` or manual dispatch; deploying requires Pages Source = GitHub Actions. Do not change Pages settings, visibility, push or publish without explicit authorization.
- Project version is 1.3.0. Framework/dependency versions and the LBDT template version are unrelated. Preserve LICENSE and its upstream notice; the website footer links to the generated license display.

## Context7

When a task asks about a library, framework, SDK, API, CLI tool or cloud service (including syntax, setup, configuration, migrations or tool-specific debugging), use Context7: resolve its library ID first unless an exact `/org/project` ID is supplied, then query the selected documentation with the full relevant question. Prefer relevant high-reputation matches and version-specific IDs where requested. General programming concepts, business-logic debugging, code review and structural refactoring do not require Context7 by themselves.

## v1.1 adoption and preservation

- Read `docs/proposals/v1-1-ratification.md` and the current register before treating new procedures as effective. No Council vote, Owner ratification, reviewer availability or live security test has been verified. A release/commit is not policy adoption.
- Constitutional/OIO changes remain Proposed. Public procedure pages are released specifications with visible activation gates; do not remove those gates without actual approval evidence. Keep proposals and readiness/tabletop records outside publication/search.
- `policy_amendments` in the source map records exact authorized supersessions. The validator reverses only hash-checked recorded replacements before the original migration checks; never alter baseline hashes or waive whole-document preservation. Additions do not exempt unrelated original text.
- Future releases preserve v1.0.0 history and align all current metadata; never create tags or publish without explicit authorization. Tabletop assumptions are not appointments, availability commitments or tested controls.

## Staff guidance and v1.2 publication

- Three staff guides are instructional: `docs/start-here/staff-guide.md`, `docs/operations/everyday-work.md` and `docs/oversight/get-help.md`. They link authority to its canonical home and must never add powers, blanket rank command or mandatory forms. Role profiles remain grouped beside their owning mandates; actual names remain in restricted assignment records.
- `published` is an explicit source allowlist independent of the task-based sidebar. Navigation uses Starlight slug links; keep each public source reachable once without copying its Markdown. `repositoryOnly` is not a privacy boundary; never store confidential data in this repository.
- `usability_baseline` checks every v1.1 policy content block against immutable commit `8e45c4773ae990e566bf8ce08bfe1884cbe8e327`, excluding release metadata. Editorial additions do not authorize altering case powers, approval gates, rank eligibility or volunteer protections.
- Do not claim approval/time/retention gains from navigation changes. `docs/usability-v1-2.md` records scenario-specific decisions, approvals, handoffs and reading paths. Walkthroughs are analytical, not actual user research.

## R13 precedence

The user explicitly authorized structural replacement. Three divisions plus Technology Office, no ED or Unit Manager office, is the selected pending target. R13 adoption/cutover is not verified. Historical preservation now compares old content against immutable pre-reform Git snapshots and hashes every amended target source; do not treat preserved history as active authority. Structural validator governs roster/reporting and ownership.
