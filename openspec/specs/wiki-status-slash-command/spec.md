# wiki-status-slash-command Specification

## Purpose
TBD - created by archiving change add-wiki-status-slash-command. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL publish Codex plugin marketplace metadata

The repository SHALL include marketplace metadata that allows Codex to discover
the repo-local plugin from the repository root. The repo-local wiki command
plugin SHALL be installed by default when the marketplace is loaded.

#### Scenario: User installs repo marketplace locally

- **WHEN** the user runs `codex plugin marketplace add .` from the repository
  root
- **THEN** the repository SHALL provide `.agents/plugins/marketplace.json`
- **AND** the marketplace entry SHALL use
  `source.path: "./plugins/report-wiki-portfolio"`
- **AND** the plugin manifest SHALL exist at
  `plugins/report-wiki-portfolio/.codex-plugin/plugin.json`
- **AND** the marketplace entry SHALL use
  `policy.installation: "INSTALLED_BY_DEFAULT"`

### Requirement: Repository SHALL document wiki status command installation

The repository README SHALL document how to make the repo-local Codex command
available and how to invoke it.

#### Scenario: User reads README

- **WHEN** the user wants to use the wiki status slash command in Codex
- **THEN** the README SHALL show `codex plugin marketplace add .`
- **AND** it SHALL show `/wiki:status`

### Requirement: Repository SHALL expose wiki status as a Codex skill

The repository SHALL provide an installable user-scope Codex skill that refreshes
and summarizes the generated wiki status surface.

#### Scenario: User invokes wiki status

- **WHEN** the user invokes `$wiki-status`
- **THEN** the skill SHALL run or reference `python3 scripts/build_wiki_status.py`
- **AND** it SHALL read `wiki/status/manifest.json`
- **AND** it SHALL read `wiki/status/wiki-status.md`
- **AND** it SHALL preserve the existing wiki status boundary

### Requirement: Wiki status skill SHALL preserve scope boundaries

The wiki status skill SHALL remain a thin status wrapper and SHALL NOT implement
a natural-language query engine, scorecard, graph UI, or change queue.

#### Scenario: Wiki status skill completes

- **WHEN** `$wiki-status` reports the current wiki status
- **THEN** it SHALL NOT create, modify, or archive OpenSpec changes
- **AND** it SHALL NOT mark OpenSpec tasks complete
- **AND** it SHALL NOT claim hidden semantic search or runtime autonomy
