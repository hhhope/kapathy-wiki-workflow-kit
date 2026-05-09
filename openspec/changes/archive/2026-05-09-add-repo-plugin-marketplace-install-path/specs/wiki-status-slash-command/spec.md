## ADDED Requirements

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
