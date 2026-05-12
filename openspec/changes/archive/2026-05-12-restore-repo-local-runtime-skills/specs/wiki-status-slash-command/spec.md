## REMOVED Requirements

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

## MODIFIED Requirements

### Requirement: Repository SHALL expose wiki status as a Codex skill

The repository SHALL provide a repo-local Codex skill that refreshes and
summarizes the generated wiki status surface.

#### Scenario: User invokes wiki status

- **WHEN** the user invokes the repo's wiki status skill
- **THEN** the skill source SHALL exist at `.codex/skills/wiki-status/SKILL.md`
- **AND** it SHALL run or reference `python3 scripts/build_wiki_status.py`
- **AND** it SHALL read `wiki/status/manifest.json`
- **AND** it SHALL read `wiki/status/wiki-status.md`
- **AND** it SHALL preserve the existing wiki status boundary
