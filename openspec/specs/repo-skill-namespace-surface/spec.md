# repo-skill-namespace-surface Specification

## Purpose
TBD - created by archiving change install-openspec-skills-user-scope. Update Purpose after archive.
## Requirements
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
