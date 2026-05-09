# Change: Resolve Ops Identity Conventions

## Why

After ADR and example identity resolution, the graph runtime still reports 30
unresolved identities, all under `wiki/ops`. Many of these pages use explicit
ops filename conventions such as `*-intake`, `*-explore-YYYY-MM-DD`,
`*-retro-YYYY-MM-DD`, `*-reminder-YYYY-MM-DD`, and `sample-*`.

These conventions can be resolved without reading arbitrary prose or editing
dirty legacy ops files.

## What Changes

- Add bounded `wiki/ops` filename convention resolvers.
- Add a small fixed resolver map for stable ops entry pages.
- Keep ops pages without supported conventions unresolved.
- Add tests proving convention coverage and non-inference boundaries.

## Impact

- Affected spec: `wiki-graph-extraction`
- Affected runtime: graph extraction and downstream graph/scorecard/queue
- Non-goals: no broad ops page migration, no prose inference, no command changes
