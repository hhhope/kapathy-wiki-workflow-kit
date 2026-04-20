# Proposal: Add Agent-Readable Wiki Graph Extraction

## Why

The repository now has two prerequisite layers for agent-readable structure:

- a naming model for evolution-bearing pages
- a frontmatter and relation-field model for covered layers

The next missing layer is extraction: a repeatable way to turn those pages into a
graph-shaped representation that an agent can inspect without re-parsing the whole
wiki as loose prose every time.

## What Changes

This change introduces a minimal graph-extraction workflow for covered layers.

The workflow will:

- read covered-layer pages
- extract canonical object identity and artifact type
- extract typed relation fields
- emit a machine-readable graph artifact
- define the validation boundary for extraction output

This change only covers:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

This change does not:

- migrate old pages in bulk
- rename existing pages
- invent semantic relations beyond the shared field contract
- build a full visualization product

## Success Criteria

- The repository can produce a graph artifact from covered layers.
- The graph artifact preserves object nodes and typed edges derived from naming and frontmatter.
- Extraction does not depend on ad hoc prose heuristics as the primary contract.
- The extraction workflow has a clear proof boundary separate from future graph UI or scoring work.
