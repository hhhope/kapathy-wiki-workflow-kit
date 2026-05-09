# Change: Preserve Blocked Queue Source Paths

## Why

After runtime graph identity warnings reached zero, `/wiki:scorecard` and
`/wiki:queue` became structurally coherent, but the blocked side of the queue
still loses source traceability. Ready and decision-needed items show concrete
source paths; blocked items often only show reasons, leaving the user unable to
inspect which wiki/spec page caused the block.

This weakens the core LLM Wiki contract: Capture -> Compile -> Retrieve -> Apply
should keep explicit source evidence visible even when an object is not safe to
use as first-pass execution context.

## What Changes

- Preserve repository-local source references for blocked objects as trace-only
  evidence through source integration, routing, context injection, and
  self-directed execution.
- Keep blocked references out of first-pass routes and injected excerpts.
- Make `/wiki:queue` able to show blocked source paths when the underlying graph
  has source references.

## Impact

- Affected specs:
  - `wiki-runtime-context-source-integration`
  - `wiki-runtime-auto-routing`
  - `wiki-context-injection`
  - `wiki-self-directed-execution`
  - `wiki-runtime-slash-command-surface`
- Affected scripts:
  - `scripts/resolve_runtime_context_sources.py`
  - `scripts/derive_runtime_auto_routing.py`
  - `scripts/build_runtime_context_injection.py`
  - `scripts/derive_self_directed_execution.py`
  - `scripts/build_wiki_change_queue_preview.py`
