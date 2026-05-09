# Design: Preserve Blocked Queue Source Paths

## Goal

Keep blocked queue items inspectable without promoting them into execution
targets.

## Current Shape

The runtime chain currently carries sources only for preferred/supporting
objects:

1. `resolve_runtime_context_sources.py` resolves `preferred_sources` and
   `supporting_sources`.
2. `derive_runtime_auto_routing.py` turns them into `open_first` and
   `open_next`.
3. `build_runtime_context_injection.py` injects excerpts for those routed
   sources.
4. `derive_self_directed_execution.py` emits `action_sources` only for
   execute-now and follow-up entries.
5. `build_wiki_change_queue_preview.py` can only show source paths if
   `action_sources` exists.

Blocked objects are preserved as blocked, but the trace path is dropped.

## Proposed Shape

Use a separate trace-only source field for blocked objects:

- source integration: `blocked_source_refs`
- routing: `blocked_source_refs`
- context injection: `excluded_source_refs`
- self-directed execution: `action_sources`

The blocked field must not be named `route_sources` or `injected_sources`, so
the implementation does not imply first-pass routing or excerpt injection.

## Boundaries

- Do not add queue execution.
- Do not auto-create OpenSpec changes from queue output.
- Do not inject full excerpts for blocked objects.
- Do not change scoring, utilization, or graph extraction rules.
- Do not hide blocked objects with no source refs; they remain visible with an
  empty `source_paths` list.

## Verification

- Unit tests prove blocked source refs survive into `/wiki:queue`.
- Live queue preview shows at least one blocked item with source paths after the
  current graph has zero unresolved identity warnings.
- OpenSpec validation passes.
