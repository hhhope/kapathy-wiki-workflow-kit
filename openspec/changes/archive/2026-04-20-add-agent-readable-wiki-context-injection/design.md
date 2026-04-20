# Design: Automatic Context Injection

## Problem

The repository can derive a bounded runtime reading plan, but it still does not turn
that plan into an actual injected-context payload.

That means the stack is still missing one operational bridge:

- runtime auto routing says what should be opened first
- but it does not yet provide a ready-to-consume context bundle with page content

Without that bridge, every live task still requires a manual content-loading step.

## Design Goals

This change should:

- stay downstream of runtime auto routing
- produce a deterministic injected-context bundle
- preserve blocked-state boundaries
- keep the output bounded and cheap for an agent to inspect

## Core Approach

Version 1 should stay deterministic and repository-local.

The workflow should:

1. read the runtime auto-routing artifact
2. load content for `open_first` routes into a bounded first-pass context bundle
3. keep `open_next` routes visible but secondary
4. preserve blocked objects as excluded from injected first-pass context

## Injection Strategy

Version 1 should produce only bounded context groups such as:

- `injected_first_pass`
- `secondary_context`
- `excluded_objects`

The mapping should stay explicit and deterministic rather than heuristic-heavy.

## Minimum Output

The automatic context-injection artifact should include at least:

- summary
- injected first-pass context
- secondary context
- excluded objects
- injection notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can turn runtime auto-routing output into a deterministic injected-context bundle
- `open_first` routes can become first-pass injected context
- `open_next` routes can remain secondary context
- blocked objects stay outside injected first-pass context

This change should not claim:

- external retrieval integration
- runtime autonomy
- agent self-directed execution
- unresolved page understanding

## Non-Goals

- no Feishu integration
- no vector index integration
- no blocked-object override logic
- no autonomous execution loop

## Open Questions

- whether version 1 should inject full page bodies or bounded excerpts
- whether injected first-pass context should cap total source count
- whether secondary context should preserve object grouping or flatten into one list
