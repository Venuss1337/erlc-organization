# Contributing

## Documentation conventions

- Put substantive organizational documentation under `docs/`. Use descriptive lowercase hyphenated filenames and relative Markdown links, including stable anchors when linking a section.
- Edit the canonical home listed in the [documentation index](README.md#documentation-index). Other pages may summarize or illustrate it, but must link to that home instead of creating another definition. Keep examples and templates beside their owning process.
- Preserve the distinction between rank, job, appointment, qualification, authority and permissions. Mark planning examples, suggestions, service targets and proposals as such.
- Keep tables and fenced examples readable. Use UTF-8 and LF line endings. Record substantive document changes in [CHANGELOG.md](CHANGELOG.md); editorial refactors do not automatically change the organizational version.
- Keep completed personnel, applicant, well-being, investigation and appeal records in authorized restricted systems. Repository templates are blank examples, not permission to publish sensitive records.

## Proposing and approving changes

For an editorial correction, update the owning page and explain why meaning is unchanged. For policy changes, add a descriptive proposal under `docs/proposals/`, using the [Council proposal template](docs/governance/governance-council.md#governance-council-policy-proposal-template) where applicable. Clearly mark it **Proposed**, name its Driver and policy owner, link the current canonical text, show the proposed wording, and record consultation, conflicts, impact, implementation and review plans. The [review register](docs/proposals/review-register.md) lists unresolved source questions; logging one does not resolve it.

Decision ownership follows the [delegated decision matrix](docs/operations/authority-and-escalation.md#delegated-decision-matrix). Routine team procedures remain with their designated owners. Organization-wide policy and major structural proposals follow the [Council's consultation, quorum and voting rules](docs/governance/governance-council.md#meetings-voting-and-conflicts); reserved changes also require explicit Owner ratification. Independent oversight advice and individual case decisions remain protected under the [OIO charter](docs/oversight/independent-oversight.md).

After the required decision is documented, record the outcome and minutes/ratification reference, approved text, effective date, implementation owner and review date. Update the canonical policy and links, retain the proposal's decision record, and update status/version only as supported by that record. A Git commit, pull-request merge or repository maintainer's review alone does not approve organizational policy. No adoption record exists in the supplied source.

## Before committing

Read the changed policy with its dependencies; check for altered powers, eligibility, safeguards or approval thresholds. Run `python scripts/validate_docs.py` and review the diff. The preservation check compares the migration to its baseline; a later authorized policy change must have its approval recorded and its source-map exception explicitly maintained, never silently weaken validation. Use descriptive conventional commits such as `docs: clarify session assignment navigation`.
