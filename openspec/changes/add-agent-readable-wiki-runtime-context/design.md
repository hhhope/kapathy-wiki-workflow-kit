# Design: Agent-Readable Wiki Runtime Context Integration

## Problem

The repository can now extract, analyze, score, and classify canonical objects, but it
still does not turn that guidance into a ready-to-use runtime context bundle.

That leaves a practical gap:

- utilization says which objects are preferred, cautious, or blocked
- but there is still no stable artifact that packages those decisions for live use

Without a runtime-context layer, the stack remains advisory rather than operational.

## Design Goals

This change should:

- stay downstream of utilization
- define a runtime-ready bundle without pretending full retrieval is solved
- preserve caution and blocked-state boundaries
- produce a machine-readable artifact that an agent can inspect cheaply

## Core Approach

Version 1 should stay explicit and deterministic.

The workflow should:

1. read utilization output
2. map utilization bands into runtime context sections
3. preserve reasons and caution flags
4. emit a small context bundle for live agent use

## Runtime Context Sections

Version 1 should include at least:

- `preferred_context`
- `supporting_context`
- `blocked_context`
- `runtime_caution`

The bundle may also include a small read-order hint.

## Minimum Output

The runtime-context artifact should include at least:

- overall summary
- preferred context entries
- supporting context entries
- blocked context entries
- runtime caution notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can derive a runtime-ready context bundle from existing guidance
- preferred, supporting, and blocked items stay distinct
- caution is preserved instead of flattened away

This change should not claim:

- autonomous runtime routing
- external retrieval integration
- semantic understanding of unresolved pages
- that the context bundle alone is enough for final decision quality

## Non-Goals

- no external vector index
- no automatic agent entrypoint integration
- no runtime auto-edit behavior
- no autonomous promotion from blocked to preferred

## Open Questions

- whether version 1 should emit only canonical-object bundles or also include page-path hints
- whether preferred context should be capped to a small top-N list
- whether repository caution should always appear even when there are preferred objects
