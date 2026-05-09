# Archive Review: Reduce Wiki Runtime Identity Pressure

## Result

Archive review passes.

## Scope Checked

- OpenSpec spec path identity now maps `openspec/specs/<name>/spec.md` to
  `<name> / spec` without adding YAML frontmatter to OpenSpec files.
- Explicit LLM Wiki runtime ADR mappings cover the named runtime ADR chain.
- `wiki/ops/agent-readable-wiki-graph-extraction.md` now has explicit
  frontmatter identity.

## Evidence

- `python3 -m unittest tests.test_wiki_graph_extraction_identity tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace`
- `openspec validate reduce-wiki-runtime-identity-pressure --strict`
- `git diff --check`
- `python3 scripts/extract_wiki_graph.py`

## Measured Runtime Change

- Before: `node_count: 77`, `edge_count: 104`, `warning_count: 91`
- After: `node_count: 119`, `edge_count: 108`, `warning_count: 49`

## Boundary Checked

- No arbitrary prose identity inference was added.
- No OpenSpec spec file format was changed.
- No unrelated intake, report, source, or example pages were migrated.
- No scoring formula or command execution behavior was changed.

## Residual Risk

- 49 unresolved identities remain, mostly older ops, ADR, and example pages.
- The remaining warnings should be handled by later targeted migrations, not by
  broad semantic guessing.
