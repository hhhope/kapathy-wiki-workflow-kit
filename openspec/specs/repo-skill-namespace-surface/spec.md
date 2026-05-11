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

### Requirement: Repo SHALL avoid root-scope OpenSpec duplicates

User-scope or root-scope OpenSpec helper installs SHALL NOT duplicate this
repository's repo-local OpenSpec helper skill surface.

#### Scenario: User-scope duplicate appears

- **WHEN** `/home/yan/.codex/skills` contains `openspec-*` helpers for this
  repository
- **THEN** those root-scope duplicates SHALL be removed
- **AND** `.codex/skills/openspec-*` SHALL remain the supported source
