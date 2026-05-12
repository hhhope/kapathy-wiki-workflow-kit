## REMOVED Requirements

### Requirement: Repo SHALL avoid namespaced OpenSpec runtime skills

The repository SHALL NOT expose OpenSpec helper skills from repo-local
`.codex/skills/openspec-*` when the desired runtime invocation is the plain
`openspec-*` name.

#### Scenario: User looks for OpenSpec helper skills

- **WHEN** Codex lists available skills for this trusted repository
- **THEN** OpenSpec helper skills SHALL be visible as user-scope `openspec-*`
  names
- **AND** the repo SHALL NOT also expose `report-wiki-portfolio:openspec-*`
  duplicates

### Requirement: Repo SHALL keep installable OpenSpec skill sources

The repository SHALL keep source copies of the OpenSpec helper skills in a
non-repo-local skill-loading directory.

#### Scenario: Contributor audits OpenSpec skill source

- **WHEN** a contributor wants to audit or reinstall OpenSpec helper skills
- **THEN** the source files SHALL be available under
  `plugins/report-wiki-portfolio/skills/openspec-*`
- **AND** repo guidance SHALL reference the plain `$openspec-*` invocation
  names

## ADDED Requirements

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
