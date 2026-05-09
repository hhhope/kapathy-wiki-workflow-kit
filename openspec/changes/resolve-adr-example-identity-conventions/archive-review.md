# Archive Review: Resolve ADR and Example Identity Conventions

## Result

Archive review passes.

## Scope Checked

- Numbered ADR paths now resolve to `<slug> / adr`.
- `wiki/examples/*-example.md` paths now resolve to `<slug> / example`.
- LLM Wiki runtime ADR special mappings still take priority over the generic
  ADR resolver.
- Unmapped `wiki/ops` pages remain unresolved unless they have frontmatter or a
  dedicated resolver.

## Evidence

- `python3 -m unittest tests.test_wiki_graph_extraction_identity tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace`
- `openspec validate resolve-adr-example-identity-conventions --strict`
- `git diff --check`
- Live extraction summary: `node_count: 138`, `edge_count: 108`,
  `warning_count: 30`

## Measured Runtime Change

- Before this change: `warning_count: 49`
- After this change: `warning_count: 30`
- Remaining warning distribution: ADR `0`, examples `0`, ops `30`

## Boundary Checked

- No arbitrary prose inference was added.
- No `wiki/ops` legacy material was migrated.
- No graph UI, scoring formula, command behavior, or OpenSpec lifecycle
  behavior was changed.

## Residual Risk

- The remaining 30 unresolved pages are ops pages with mixed semantics and need
  a separate targeted migration.
