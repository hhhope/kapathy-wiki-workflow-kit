# no-repo-local-commit-hook-default Specification

## Purpose
TBD - created by archiving change decide-no-repo-local-commit-hook. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL NOT use a repo-local commit hook as the default governance path

The repository SHALL NOT treat a repo-local commit hook as part of the default
`agents-governance-drift` governance path.

#### Scenario: Phase 1 repo AGENTS migration is planned

- **WHEN** the repository plans repo `AGENTS.md` compression, proxy migration,
  or structural rewrite
- **THEN** the plan SHALL NOT require a repo-local commit hook as a prerequisite
- **AND** the plan SHALL rely on repo-visible ADR, OpenSpec, wiki, and skill
  boundaries unless a later change explicitly reverses this decision

#### Scenario: A future contributor proposes a repo-local commit hook

- **WHEN** a future change proposes adding a repo-local commit hook for
  governance enforcement
- **THEN** that change SHALL explicitly reverse this default
- **AND** it SHALL record the hook scope, failure mode, evidence, and rollback
  boundary before implementation

