# wiki-status-slash-command Specification

## Purpose
TBD - created by archiving change add-wiki-status-slash-command. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose wiki status as a repo-level Codex slash command

The repository SHALL provide a repo-local Codex plugin command that refreshes
and surfaces the generated wiki status artifacts, using the wiki capability
namespace as the user-facing command name.

#### Scenario: User invokes wiki status command

- **WHEN** the user invokes `/wiki:status`
- **THEN** the command SHALL run the wiki status generator
- **AND** it SHALL point the user to `wiki/status/manifest.json` and
  `wiki/status/wiki-status.md`

### Requirement: Wiki status slash command SHALL preserve scope boundaries

The wiki status slash command SHALL remain a thin status wrapper and SHALL NOT
implement query, scorecard calibration, graph UI, or learning-to-change
orchestration.

#### Scenario: Command completes

- **WHEN** the command finishes refreshing status
- **THEN** it SHALL summarize status output only
- **AND** it SHALL NOT open, modify, or archive OpenSpec changes

### Requirement: Repository SHALL publish Codex plugin marketplace metadata

The repository SHALL include marketplace metadata that allows Codex to discover
the repo-local plugin from the repository root.

#### Scenario: User installs repo marketplace locally

- **WHEN** the user runs `codex plugin marketplace add .` from the repository
  root
- **THEN** the repository SHALL provide `.agents/plugins/marketplace.json`
- **AND** the marketplace entry SHALL point to the repo-root plugin manifest at
  `.codex-plugin/plugin.json`

### Requirement: Repository SHALL document wiki status command installation

The repository README SHALL document how to make the repo-local Codex command
available and how to invoke it.

#### Scenario: User reads README

- **WHEN** the user wants to use the wiki status slash command in Codex
- **THEN** the README SHALL show `codex plugin marketplace add .`
- **AND** it SHALL show `/wiki:status`
