## MODIFIED Requirements

### Requirement: Repository SHALL expose the wiki runtime as named Codex skills

The repository SHALL provide repo-local Codex skills that expose the existing
LLM Wiki runtime layers through the `wiki-*` skill family under `.codex/skills`.

#### Scenario: User looks for wiki runtime skills

- **WHEN** the user wants to invoke the repo's LLM Wiki runtime capabilities in
  current Codex
- **THEN** the repository SHALL provide skill source files under `.codex/skills`
  for status, manifest, inbox, query, explore, graph, scorecard, route,
  context, apply, and queue surfaces
- **AND** the supported runtime path SHALL NOT require plugin marketplace
  loading or copying skills into user scope

### Requirement: README SHALL document the wiki skill surface

The README SHALL list the available repo-local wiki skill surface so users can
discover the runtime layers without relying on unsupported custom slash commands
or user-scope installation.

#### Scenario: User reads command documentation

- **WHEN** the user wants to know which wiki runtime skills are available
- **THEN** the README SHALL list status, manifest, inbox, query, explore,
  graph, scorecard, route, context, apply, and queue skills
- **AND** it SHALL keep `.codex/skills/wiki-status/SKILL.md` as the status
  source path
- **AND** it SHALL warn not to install this repo's `wiki-*` skills into
  root/user scope because that creates duplicate entries
