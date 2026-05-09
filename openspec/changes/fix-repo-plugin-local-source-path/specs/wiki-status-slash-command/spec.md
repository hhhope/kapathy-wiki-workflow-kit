## MODIFIED Requirements

### Requirement: Repository SHALL publish Codex plugin marketplace metadata

The repository SHALL include marketplace metadata that allows Codex to discover
the repo-local plugin from the repository root. The marketplace entry SHALL
point to a plugin package directory under `./plugins/`, and that package
directory SHALL contain `.codex-plugin/plugin.json`.

#### Scenario: User installs repo marketplace locally

- **WHEN** the user runs `codex plugin marketplace add .` from the repository
  root
- **THEN** the repository SHALL provide `.agents/plugins/marketplace.json`
- **AND** the marketplace entry SHALL use
  `source.path: "./plugins/report-wiki-portfolio"`
- **AND** the plugin manifest SHALL exist at
  `plugins/report-wiki-portfolio/.codex-plugin/plugin.json`
