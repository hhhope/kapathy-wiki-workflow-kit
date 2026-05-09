# Archive Review: Enhance Wiki Runtime Action Surfaces

## Result

Archive review passes.

## Scope Checked

- `/wiki:graph` now has a bounded object-view summary over graph extraction and
  relation analysis.
- `/wiki:scorecard` now has bounded diagnostics over scoring and utilization.
- `/wiki:queue` exists as preview-only queue documentation and helper output.
- README and runtime command tests include `/wiki:queue`.

## Evidence

- `python3 -m unittest tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace`
- `openspec validate enhance-wiki-runtime-action-surfaces --strict`
- `git diff --check`
- Live smoke:
  - `python3 scripts/summarize_wiki_graph.py wiki-runtime --limit 3`
  - `python3 scripts/summarize_wiki_scorecard.py wiki-runtime --limit 3`
  - `python3 scripts/build_wiki_change_queue_preview.py`

## Boundary Checked

- No command executes queue items.
- No command creates, modifies, archives, or queues OpenSpec changes.
- No command marks tasks complete.
- No graph UI, natural-language query engine, embedding search, or hidden
  semantic ranking was added.

## Residual Risk

- The queue is still a preview layer, not multi-change orchestration.
- Repository-wide unresolved warning pressure remains high in the live runtime
  outputs.
- Push remains dependent on external GitLab SSH network availability.
