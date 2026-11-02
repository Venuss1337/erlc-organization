# Migration and validation report

**Project version:** 1.2.0 · **Release date:** 2026-11-02 · **Status:** Official release.

This report records the migration from an unreleased development draft and the establishment of the first official release. The release changes version/status labels and release history, without changing organizational policies or resolving open decisions.

This paragraph and the sections below describe the **historical migration and v1.0.0 baseline**, not the later update. Current authorized supersessions, specification/adoption boundaries, tabletop results and validation are recorded in the [v1.1 readiness report](readiness-v1-1.md); current release metadata above identifies the maintained repository version.

## Baseline and architecture

The only source Markdown file discovered was the original development draft identified by the historical source path in the source map (1,158 lines). Its original content was committed before restructuring in baseline `ea0f598`. The [source map](source-map.json) records the full commit ID, SHA-256, contiguous original line ranges and destination paths. Retrieve the source from that baseline using Git history; it is deliberately absent from the live tree to avoid competing definitions.

Sixteen substantive policy/review pages follow logical ownership. Examples and templates remain beside the relevant policy. Oversight stays in one document so its three functions, referral matrix and independence safeguards are reviewed together. Operating cadence, staffing scale and implementation phases share a document. The [README index](../README.md#documentation-index) is the navigation entry point.

## Original section coverage

| Original section | Destination |
|---|---|
| Metadata and §1 executive summary | [Operating model](governance/structure.md) and [four personnel records / ranks](personnel/ranks-and-appointments.md) |
| §2 chart, Council and leadership | [Structure and Chief of Staff](governance/structure.md) and [Council charter](governance/governance-council.md) |
| §3 six directorates | One document each: [Trust & Safety](directorates/trust-and-safety.md), [Live Operations](directorates/live-operations.md), [Roleplay Programs](directorates/roleplay-programs.md), [Community Experience](directorates/community-experience.md), [People & Culture](directorates/people-and-culture.md), [Technology & Systems](directorates/technology-and-systems.md) |
| §4 independent oversight | [OIO charter, functions and safeguards](oversight/independent-oversight.md) |
| §5 multi-team membership | [Assignments](personnel/assignments.md) |
| §6 integrated career / rank framework | [Ranks and appointments](personnel/ranks-and-appointments.md); approving authorities linked to the decision matrix |
| §7 recruiting and assigning | [Recruitment](personnel/recruitment.md) and [secondary assignments](personnel/assignments.md) |
| §8 authority and decisions | [Authority and escalation](operations/authority-and-escalation.md) |
| §9 cadence and accountability | [Operating practices](operations/operating-practices.md) |
| §10 Discord roles and privacy | [Discord permissions](operations/discord-permissions.md) |
| §11 growth and 60-person illustration | [Operating practices](operations/operating-practices.md#how-small-or-large-units-should-grow) |
| §12 examples A–I | All nine retained verbatim beside their owners; [example index](governance/structure.md#worked-examples) |
| §13 templates 13.1–13.7 | All seven retained verbatim beside their owners; [template index](governance/structure.md#adoption-templates). The §5 allocation record and §7 position request are also retained. |
| §14 implementation phases | [Operating practices](operations/operating-practices.md#implementation-phases) |
| §15 eighteen charter rules | [Ordered canonical-policy index](governance/structure.md#proposed-charter-rule-index); full rules remain in their policy homes |
| §16 references, limits and open questions | [Review register](proposals/review-register.md); development summaries retained in Git history; official release history in [CHANGELOG.md](../CHANGELOG.md) |
| Final principle | [Operating model](governance/structure.md) |

## Preservation and duplication review

The migration changes headings, converts numbered-section references to relative links, and replaces repeated principle/charter summaries and selected redundant rank, approval and capacity passages with canonical links. Each replacement is explicitly recorded in the source map with hashes, destination, replacement text and rationale. Approval details unique to the original rank section remain with the [decision matrix](operations/authority-and-escalation.md#delegated-decision-matrix), including portfolio/COO review for exceptional cross-directorate grade 04–05 promotions.

The full reporting diagrams, tables, allocation examples, record formats, proposal form and restricted-record warnings remain intact. Cross-cutting charts, leadership catalogues and decision tables are marked as summaries or routing aids and link to the relevant policy owner; they do not establish separate rank, voting or investigation rules. Development-only design-history summaries remain in Git history. The changelog begins with the first official release.

The reviewed authority dependencies preserve equal-grade Director reporting, separate grade-07 executive mandates, the Chief of Staff's coordination boundary, assignment-scoped task leads, Council voting/ratification, and independent investigation/adjudication/appeal separation. Pre-existing ambiguities are recorded as [REV-01–REV-03](proposals/review-register.md#pre-existing-ambiguities-requiring-review); no policy resolution was applied.

## Reproducible checks

From the repository root, run:

```sh
python scripts/validate_docs.py
git diff --check
git status --short --branch
```

The validator uses only the Python standard library and Git. It checks every original line's destination and source hash, explicitly accounts for authorized release-metadata edits and development-history retirements, accounts for whole source paragraphs/lists/tables/fences or explicit summary redirects, verifies unchanged tables and fenced blocks after recorded link edits, checks all nine worked examples, and validates local Markdown paths, fragments, table widths and closed fences. It prints counts so later runs can be compared. It needs the baseline commit available locally; shallow copies must fetch that history.

**Original migration result (before release labeling):** All checks passed: 21 Markdown files, 216 relative links/fragments, 1,158 baseline lines assigned to 48 contiguous ranges, 170 retained source content blocks and seven explicitly redirected repeated-summary blocks. All 22 original tables, 14 fenced blocks, nine worked examples and seven adoption templates are retained. Git's whitespace check also passes; intentional Markdown two-space hard breaks are preserved and checked separately by the validator.

This is a source comparison and local link check, not a Markdown build or external-link availability test. Hashes establish traceability, not semantic equivalence of redirected summaries; that is supported by the manual ownership and policy review above. Future authorized policy amendments must retain their approval records and explicitly explain any changed preservation expectations.

## Initial official release verification

Version 1.0.0 is the first official release. The source map retains the original baseline commit, historical filename and hashes as provenance only. Its release-baseline edits record exact source ranges, hashes and replacement text for status-only changes. Three development change summaries are explicitly retained in Git history instead of the current changelog. The validator reconstructs only those recorded editorial edits for comparison; all substantive policy tables, examples and templates remain checked. LICENSE and copyright notices are unchanged.
