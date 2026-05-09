# Change: Reduce Wiki Runtime Identity Pressure

## Why

The graph runtime still reports high unresolved identity pressure. The latest
live output shows 91 unresolved pages, including many stable OpenSpec specs and
core LLM Wiki runtime governance pages. That weakens `/wiki:graph`,
`/wiki:scorecard`, and `/wiki:queue` because they must treat important runtime
evidence as warnings rather than structured nodes.

## What Changes

- Add a bounded identity resolver for `openspec/specs/<name>/spec.md` so stable
  OpenSpec specs become structural graph nodes without adding YAML frontmatter
  to OpenSpec spec files.
- Add explicit LLM Wiki runtime ADR identity mappings where the filename already
  names the runtime object.
- Add missing frontmatter to the core graph extraction ops page.
- Add tests that prove the resolver reduces known runtime identity warnings
  without semantic inference.

## Impact

- Affected spec: `wiki-graph-extraction`
- Affected runtime: graph extraction, relation analysis, scorecard, queue
- Non-goals: no graph UI, no full old-page migration, no semantic guessing
