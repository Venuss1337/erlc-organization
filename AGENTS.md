# Repository instructions for agents

- Read [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), the relevant canonical policies and [review register](docs/proposals/review-register.md) before editing.
- This is a documentation repository. Use lightweight text tooling; do not add a framework, build system or dependencies for ordinary documentation work.
- The current project version is **1.0.0**, status **Official release**, dated **2026-11-02**. This is the first official release; earlier iterations were unreleased development drafts. Keep release metadata aligned with README and CHANGELOG. Do not infer resolution of open governance decisions from a release label.
- Do not change policy without authorization. Preserve ranks, appointment eligibility, reporting, voting, reserved powers, independent case safeguards, volunteer protections and permission boundaries. If wording conflicts, record it for review rather than inventing a resolution.
- Each rule has one canonical home in the README index. Edit that home and use relative links elsewhere. Charts, decision-routing tables, examples and checklists summarize the linked rules; do not make them competing policy definitions.
- Keep all substantive examples, tables, fenced records and templates. Blank templates are not approval records. Never add completed confidential records to this repository.
- [docs/source-map.json](docs/source-map.json) records the original baseline and destinations. Never rewrite the baseline or suppress preservation failures to conceal a policy change. Future authorized changes must document their approval and explain any updated preservation exception.
- Run `python scripts/validate_docs.py`, inspect the diff, and verify Git status. Use conventional descriptive commits when committing is requested. Preserve history; do not create a remote or publish unless requested.

## Context7

When a task asks about a library, framework, SDK, API, CLI tool or cloud service (including syntax, setup, configuration, migrations or tool-specific debugging), use Context7: resolve its library ID first unless an exact `/org/project` ID is supplied, then query the selected documentation with the full relevant question. Prefer relevant high-reputation matches and version-specific IDs where requested. General programming concepts, business-logic debugging, code review and structural refactoring do not require Context7 by themselves.
