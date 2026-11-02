# ER:LC Organization

An operating-system proposal for an independently operated ER:LC Discord/Roblox community. This repository separates governance, personnel, delivery and independent oversight so each policy has a clear home and can evolve without conflicting definitions.

**Organizational document version:** 3.2.2 — full edition, integrated organizational ranks and appointments  
**Source date:** 2 November 2026  
**Status:** Proposed full-structure edition; builds on v3.2.1 without changing its governance or reporting design. Repository restructuring does **not** constitute adoption.

The model combines six operating directorates, two executive portfolios, a five-seat Governance Council and one independent oversight office with three protected functions. Staff have one home team and one permanent people manager, with approved secondary assignments. Organizational rank, job, appointment, qualification and technical access are distinct; actual authority follows the assigned mandate.

## Simplified hierarchy

```text
Owner / CEO
├── COO
│   ├── Chief of Staff (coordination; non-voting Council Secretary)
│   ├── Executive Director — Operations
│   │   ├── Trust & Safety
│   │   ├── Live Operations
│   │   └── Roleplay Programs
│   └── Executive Director — Community & Services
│       ├── Community Experience
│       ├── People & Culture
│       └── Technology & Systems
└── Oversight Commissioner — Office of Independent Oversight
    ├── Internal Affairs & Investigations
    ├── Appeals & Member Advocacy
    └── Standards & Assurance

Policy flow (not line management): CEO ··· Governance Council ··· COO
```

This is the target structure, activated according to workload. The Council is a collective policy body; independent oversight is outside COO/Council command. See the [full chart and reporting rules](docs/governance/structure.md#organization-chart-and-lines-of-accountability) for exact relationships and visualization safeguards.

## Documentation index

| Domain | Canonical documents and policies |
|---|---|
| Governance | [Structure, executive mandates and charter index](docs/governance/structure.md) · [Governance Council: membership, voting and adoption](docs/governance/governance-council.md) |
| Personnel | [Eight ranks, eligibility, promotions and appointments](docs/personnel/ranks-and-appointments.md) · [Home teams, cross-team assignments and workload conflicts](docs/personnel/assignments.md) · [Recruitment and onboarding](docs/personnel/recruitment.md) |
| Operations portfolio | [Trust & Safety](docs/directorates/trust-and-safety.md) · [Live Operations](docs/directorates/live-operations.md) · [Roleplay Programs](docs/directorates/roleplay-programs.md) |
| Community & Services portfolio | [Community Experience and player voice](docs/directorates/community-experience.md) · [People & Culture and staff experience](docs/directorates/people-and-culture.md) · [Technology & Systems](docs/directorates/technology-and-systems.md) |
| Independent oversight | [OIO: protected functions, referrals, independence and case safeguards](docs/oversight/independent-oversight.md) |
| Operating procedures | [Authority, decision owners and escalation](docs/operations/authority-and-escalation.md) · [Discord permissions and privacy](docs/operations/discord-permissions.md) · [Cadence, staffing, team mandates and implementation phases](docs/operations/operating-practices.md) |
| Pending review | [Source limitations, open decisions and pre-existing ambiguities](docs/proposals/review-register.md) |

## Find a specific policy

- **Who can approve an action?** Start with the [delegated decision matrix](docs/operations/authority-and-escalation.md#delegated-decision-matrix); follow its canonical dependencies for grade eligibility, Council voting or case safeguards.
- **Can someone hold multiple roles?** Use [staff assignments](docs/personnel/assignments.md) and [rank relationships](docs/personnel/ranks-and-appointments.md#three-rank-to-position-relationships).
- **Where does a complaint or appeal go?** Use the [jurisdiction and referral matrix](docs/oversight/independent-oversight.md#one-intake-one-case-owner--jurisdiction-and-referrals).
- **Where are examples and forms?** The [worked-example index](docs/governance/structure.md#worked-examples) and [template index](docs/governance/structure.md#adoption-templates) link to all original examples and templates beside their owning processes.
- **Is a rule approved?** The source remains proposed. Consult the [review register](docs/proposals/review-register.md); no approval record was supplied.

## Maintaining this repository

Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing policies. [AGENTS.md](AGENTS.md) supplies agent-specific rules. [CHANGELOG.md](CHANGELOG.md) separates editorial repository changes from organizational design history.

Run the dependency-free check from the repository root with Python 3.9 or newer:

```sh
python scripts/validate_docs.py
```

The [migration and validation report](docs/migration-report.md) explains preservation checks and limitations. The [machine-readable source map](docs/source-map.json) maps every original line to its destination. The untouched source is preserved in baseline commit `ea0f598` as `ERLC_Organization_Operating_System_v3.2.2_Hybrid_Ranks.md`; it is historical evidence, not a second live policy document.

## License & Copyright

**Proprietary — All Rights Reserved.** Copyright © 2026 [Copyright Holder].

This repository is not open-source and grants no public reuse license. Protected materials may not be reused, redistributed, or adapted without authorization, subject to applicable law and any applicable third-party terms. See [LICENSE](LICENSE) for the full notice.
