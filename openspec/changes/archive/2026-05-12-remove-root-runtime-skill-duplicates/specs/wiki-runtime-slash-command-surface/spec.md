## MODIFIED Requirements

### Requirement: README SHALL document the wiki skill surface

The README SHALL list the available repo-local wiki skill surface so users can
discover the runtime layers without relying on unsupported custom slash commands
or user-scope installation.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki runtime skills are available
- **THEN** the README SHALL list status, manifest, inbox, query, graph,
  scorecard, route, context, apply, and queue skills
- **AND** it SHALL keep `.codex/skills/wiki-status/SKILL.md` as the status
  source path
- **AND** it SHALL warn not to install this repo's `wiki-*` skills into
  root/user scope because that creates duplicate entries

### Requirement: Repo SHALL avoid root-scope wiki runtime duplicates

User-scope or root-scope wiki runtime installs SHALL NOT duplicate this
repository's repo-local wiki skill surface.

#### Scenario: User-scope duplicate appears

- **WHEN** `/home/yan/.codex/skills` contains `wiki-*` runtime skills for this
  repository
- **THEN** those root-scope duplicates SHALL be removed
- **AND** `.codex/skills/wiki-*` SHALL remain the supported source

### Requirement: Repo SHALL not publish wiki runtime through plugin metadata

The repository SHALL NOT publish the wiki runtime skill surface through repo
plugin marketplace metadata or plugin skill copies.

#### Scenario: Contributor inspects runtime surfaces

- **WHEN** the repository contains `.codex/skills/wiki-*`
- **THEN** `.agents/plugins/marketplace.json` SHALL be absent
- **AND** `plugins/report-wiki-portfolio/.codex-plugin/plugin.json` SHALL be
  absent
- **AND** `plugins/report-wiki-portfolio/skills` SHALL be absent
- **AND** README SHALL warn not to reintroduce plugin marketplace metadata for
  this runtime surface
