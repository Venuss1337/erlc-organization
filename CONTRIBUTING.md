# Contributing

## Documentation conventions

- Put substantive organizational documentation under `docs/`. Use descriptive lowercase hyphenated filenames and relative Markdown links, including stable anchors when linking a section.
- Edit the canonical home listed in the [documentation index](README.md#documentation-index). Other pages may summarize or illustrate it, but must link to that home instead of creating another definition. Keep examples and templates beside their owning process.
- Preserve the distinction between rank, job, appointment, qualification, authority and permissions. Mark planning examples, suggestions, service targets and proposals as such.
- Keep tables and fenced examples readable. Use UTF-8 and LF line endings. Record substantive document changes in [CHANGELOG.md](CHANGELOG.md); editorial refactors do not automatically change the organizational version.
- Keep completed personnel, applicant, well-being, investigation and appeal records in authorized restricted systems. Repository templates are blank examples, not permission to publish sensitive records.
- Website publication is opt-in via `site.config.mjs`; keep approved public sources in `docs/` and never edit generated `src/content/docs/`. Proposals and maintenance records remain repository-only. Review the publication list for confidential content; run `bun run check` and `bun run build` when changing site behavior or published content. Use Bun and commit its lockfile. See the [website instructions](README.md#documentation-website).

## Proposing and approving changes

For an editorial correction, update the owning page and explain why meaning is unchanged. For policy changes, add a descriptive proposal under `docs/proposals/`, using the [Council proposal template](docs/governance/governance-council.md#governance-council-policy-proposal-template) where applicable. Clearly mark it **Proposed**, name its Driver and policy owner, link the current canonical text, show the proposed wording, and record consultation, conflicts, impact, implementation and review plans. The [review register](docs/proposals/review-register.md) lists unresolved source questions; logging one does not resolve it.

Decision ownership follows the [delegated decision matrix](docs/operations/authority-and-escalation.md#delegated-decision-matrix). Routine team procedures remain with their designated owners. Organization-wide policy and major structural proposals follow the [Council's consultation, quorum and voting rules](docs/governance/governance-council.md#meetings-voting-and-conflicts); reserved changes also require explicit Owner ratification. Independent oversight advice and individual case decisions remain protected under the [OIO charter](docs/oversight/independent-oversight.md).

After the required decision is documented, record the outcome and minutes/ratification reference, approved text, effective date, implementation owner and review date. Update the canonical policy and links, retain the proposal's decision record, and update status/version only as supported by that record. A Git commit, pull-request merge or repository maintainer's review alone does not approve organizational policy. The official release baseline does not itself supply Council votes or resolve items in the review register.

## Release conventions

The current official project version is **1.4.0**, released **2026-11-02**, named **Office of the COO & Distributed Executive Management**. v1.0.0 remains the first official release. Use `MAJOR.MINOR.PATCH` in metadata and changelog entries, `vMAJOR.MINOR.PATCH` in titles and Git tags, and **Official release** as the released-document status. README is the version entry point; align policy-page metadata and the source map with it. Keep the changelog in Keep a Changelog style with newest official releases first. Earlier development iterations are historical drafts, not release entries. New proposals remain **Proposed** until authorized; release labeling does not resolve open decisions. Preserve existing commits and tags, and never push or publish a release without authorization.

## Before committing

Read the changed policy with its dependencies; check for altered powers, eligibility, safeguards or approval thresholds. Run `python scripts/validate_docs.py` and review the diff. The preservation check compares the migration to its baseline; a later authorized policy change must have its approval recorded and its source-map exception explicitly maintained, never silently weaken validation. Use descriptive conventional commits such as `docs: clarify session assignment navigation`.

## Specification versus adoption

The [v1.1 ratification package](docs/proposals/v1-1-ratification.md) names each approval unit and dependency. The [register](docs/proposals/review-register.md) distinguishes proposed policy, implementation tasks and verified artifacts. New public procedures are specification pages with explicit adoption gates. Record actual consultation, votes/ratification, effective scope, staffing and tests before changing them to active policy. Never publish a proposal as an approved handbook rule or copy confidential case/appointment records into Git. Preserve the exact authorized amendment ledger when superseding baseline content; additions alone do not justify a preservation exception.

For staff-facing changes, edit one of the three linked guides and relevant role profiles; check its summaries against the canonical authority, including pending adoption gates. Navigation/editorial changes do not alter approvals. Preserve the v1.1 policy-block baseline and report measured structural differences separately from hypothetical human outcomes.

R14 has one selected target and a [current-authority reference](docs/governance/current-authority.md) before adoption. Edit the [Office charter](docs/governance/office-of-the-coo.md) for Office powers, not parallel rules in guides. Run `python scripts/validate_executive.py` with the existing validators; legacy fragments must lead to substantive matching content, not empty tail anchors. The exact amendment ledger separates documented engineering authorization from still-pending organizational approval.
