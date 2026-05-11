# repo-skill-namespace-surface Specification

## Purpose
TBD - created by archiving change install-openspec-skills-user-scope. Update Purpose after archive.
## Requirements
### Requirement: Repo SHALL expose OpenSpec helper skills as repo-local skills

The repository SHALL provide the OpenSpec helper skill bodies under
`.codex/skills/openspec-*` so the repo runtime surface is available without
plugin marketplace support or user-scope installation.

#### Scenario: User looks for OpenSpec helper skills

- **WHEN** the repository is checked out and trusted by Codex
- **THEN** OpenSpec helper skill files SHALL exist under `.codex/skills`
- **AND** the available helper set SHALL include `openspec-apply-change`,
  `openspec-archive-change`, `openspec-explore`, and `openspec-propose`
- **AND** repo guidance SHALL reference `.codex/skills/openspec-*` as the
  supported repo-owned source

### Requirement: Repo SHALL treat user-scope OpenSpec skills as optional

User-scope or root-scope OpenSpec skill installs SHALL NOT be the repository's
required source of truth for this workflow.

#### Scenario: User-scope install drifts

- **WHEN** `/home/yan/.codex/skills` is missing an OpenSpec helper skill
- **THEN** the repository SHALL still provide the required helper source under
  `.codex/skills`
- **AND** the workflow SHALL NOT require copying plugin source into user scope
  before the repo can be used
