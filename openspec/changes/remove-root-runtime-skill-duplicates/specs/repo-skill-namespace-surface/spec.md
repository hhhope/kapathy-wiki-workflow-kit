## MODIFIED Requirements

### Requirement: Repo SHALL avoid root-scope OpenSpec duplicates

User-scope or root-scope OpenSpec helper installs SHALL NOT duplicate this
repository's repo-local OpenSpec helper skill surface.

#### Scenario: User-scope duplicate appears

- **WHEN** `/home/yan/.codex/skills` contains `openspec-*` helpers for this
  repository
- **THEN** those root-scope duplicates SHALL be removed
- **AND** `.codex/skills/openspec-*` SHALL remain the supported source
