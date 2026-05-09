# Archive Review: Preserve Blocked Queue Source Paths

## Result

Archive review passes.

## Scope Checked

- Blocked objects now keep trace-only source refs through source integration,
  runtime routing, context injection, self-directed execution, and queue preview.
- Blocked refs are not named or treated as `route_sources` or
  `injected_sources`.
- `/wiki:queue` can show blocked source paths without executing or queuing work.

## Evidence

- RED baseline:
  - `python3 -m unittest tests.test_wiki_blocked_source_paths`
  - failed with missing `blocked_source_refs`
- GREEN:
  - `python3 -m unittest tests.test_wiki_blocked_source_paths`
  - `python3 -m unittest tests.test_wiki_blocked_source_paths tests.test_wiki_queue_preview tests.test_wiki_runtime_commands`
  - `openspec validate preserve-blocked-queue-source-paths --strict`
  - `git diff --check`
- Live smoke:
  - `python3 scripts/summarize_wiki_scorecard.py --limit 12`
  - `python3 scripts/analyze_wiki_relations.py`
  - `python3 scripts/build_wiki_change_queue_preview.py`

## Live Result

- Graph unresolved warning count remains `0`.
- Scorecard remains structurally coherent:
  - preferred: `10`
  - cautious: `12`
  - blocked: `93`
- Queue preview now has source paths for blocked items:
  - ready: `10`
  - needs user decision: `12`
  - blocked: `93`
  - blocked with sources: `93`

## Boundary Checked

- No queue item is executed.
- No OpenSpec change is created, modified, archived, or queued by the queue
  preview helper.
- No blocked object is promoted into execute-now or deferred-follow-up actions.
- No graph, score, or utilization rule was changed.

## Residual Risk

- `/wiki:queue` still emits many blocked items because this is a transparent
  preview, not a prioritization UI.
- Blocked item source paths are traceability evidence only; they do not prove the
  object is safe to use as runtime context.
- OpenSpec CLI validation succeeded, but telemetry flush emitted network errors
  for PostHog due restricted network; this did not affect local validation.
