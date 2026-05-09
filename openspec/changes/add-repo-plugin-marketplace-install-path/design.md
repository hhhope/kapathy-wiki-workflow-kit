# Design

## Decision

Use Codex's marketplace-based local plugin discovery:

```text
.agents/plugins/marketplace.json
.codex-plugin/plugin.json
commands/wiki-status.md
```

The marketplace source path points to `.` because the plugin root is the
repository root: `.codex-plugin/plugin.json` lives directly in this repo.

## Install Flow

From the repository root:

```bash
codex plugin marketplace add .
```

Then restart or reload Codex so it sees the marketplace. The documented command
remains:

```text
/wiki:status
```

## Validation

Tests validate:

- marketplace JSON exists and parses
- the marketplace entry references `report-wiki-portfolio`
- the entry resolves to the repo root plugin through `source.path: "."`
- README documents the install command and `/wiki:status`

## Boundary

This change only closes the install/discovery path for the existing status
command. It does not add new LLM Wiki runtime capabilities.
