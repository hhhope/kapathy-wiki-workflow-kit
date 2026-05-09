# Design: Enhance Wiki Runtime Action Surfaces

## Goal

Make the wiki runtime commands answer product questions instead of only listing
raw functions:

- `/wiki:graph`: what objects exist, how they are structurally supported, and
  where unresolved structure concentrates.
- `/wiki:scorecard`: which objects are currently preferred, cautious, or
  blocked, and what inspection action follows.
- `/wiki:queue`: what the current runtime would place in a preview queue, with
  ready, deferred, and blocked groups.

## Approach

Add small read-only helper scripts:

- `scripts/summarize_wiki_graph.py`
- `scripts/summarize_wiki_scorecard.py`
- `scripts/build_wiki_change_queue_preview.py`

Each helper can run its upstream runtime script when no input artifact is
provided, and each emits bounded JSON that can be summarized by the slash
command. The helpers do not write repository state.

## Boundaries

- No embeddings.
- No hidden semantic ranking.
- No graph UI.
- No natural-language query engine.
- No OpenSpec change creation, modification, archiving, task completion, or
  execution.
- `/wiki:queue` is a preview queue only; it does not schedule work.

## Verification

- Focused unit tests cover each helper's grouping and proof-boundary behavior.
- Runtime command tests cover the new `/wiki:queue` command and helper-script
  references.
- OpenSpec validation confirms the change is structurally valid.
