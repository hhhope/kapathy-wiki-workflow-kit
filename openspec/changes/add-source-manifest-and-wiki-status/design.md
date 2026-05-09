## Context

The repository already has source pages and many runtime/governance artifacts,
but no repo-wide manifest or status surface. Existing graph scripts cover
selected evolution-bearing layers, while this change needs a broader operational
status view over `wiki/`, `inbox/`, and active OpenSpec changes.

This change implements the first P0 core item from
`wiki/ops/llm-wiki-core-product-contract.md`.

## Decision

Add a small Python script:

```text
scripts/build_wiki_status.py
```

Default outputs:

```text
wiki/status/manifest.json
wiki/status/wiki-status.md
```

The script scans:

- `wiki/**/*.md`, excluding generated `wiki/status/*`
- `inbox/**/*`, excluding directories
- `openspec/changes/*/tasks.md`, excluding archived changes

## Manifest Model

The manifest records:

- generation timestamp
- wiki page records:
  - path
  - sha256
  - byte size
  - top-level wiki section
  - frontmatter fields when present
- source records:
  - source page path
  - declared `source_path`
  - source type/status/domain when present
- inbox files:
  - path
  - sha256
  - byte size
  - whether represented by a source page
- OpenSpec change records:
  - change id
  - task counts
  - state: `active` or `complete`

## Status Report

The Markdown status report summarizes:

- wiki page counts by section
- source record count
- inbox files not yet represented by source records
- active changes
- complete active-directory changes that may need archive review
- next actions

## Boundaries

This is a status surface only.

Out of scope:

- semantic query
- scorecard calibration
- graph UI
- graph relation lint
- learning-to-change queue
- auto-opening or modifying OpenSpec changes
- Feishu sync or client validation

## Idempotency

The script overwrites only its configured output files. Re-running it should
produce the same structure and update generated timestamp / hashes according to
current files.
