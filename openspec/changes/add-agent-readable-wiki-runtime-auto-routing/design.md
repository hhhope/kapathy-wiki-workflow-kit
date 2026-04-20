# Design: Runtime Auto Routing

## Problem

The repository can resolve runtime context into concrete source references, but it
still does not say how a live agent should stage those sources into an actual reading
order.

That means the stack is still missing one operational bridge:

- source integration says which sources belong to which object
- but it does not yet say which sources should be opened first versus held as follow-up

Without that bridge, every live task still requires a manual staging decision.

## Design Goals

This change should:

- stay downstream of runtime-context source integration
- produce a deterministic first-pass routing plan
- preserve blocked-state boundaries
- keep the output cheap for an agent to inspect

## Core Approach

Version 1 should stay deterministic and repository-local.

The workflow should:

1. read the source-integrated runtime artifact
2. stage preferred sources into an explicit first-pass route
3. stage supporting sources into an explicit second-pass route
4. preserve blocked objects as excluded from routing

## Routing Strategy

Version 1 should produce only bounded route groups such as:

- `open_first`
- `open_next`
- `do_not_open_first`

The mapping should stay explicit and deterministic rather than heuristic-heavy.

## Minimum Output

The runtime auto-routing artifact should include at least:

- summary
- open-first route
- open-next route
- blocked objects
- routing notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can turn source-integrated runtime output into a deterministic reading plan
- preferred sources can become first-pass reading targets
- supporting sources can remain second-pass targets
- blocked objects stay outside the first-pass plan

This change should not claim:

- external retrieval integration
- automatic prompt injection
- runtime autonomy
- semantic understanding of unresolved pages

## Non-Goals

- no Feishu integration
- no vector index integration
- no automatic context injection into all agent runs
- no blocked-object override logic

## Open Questions

- whether version 1 should open all preferred sources or cap the first-pass route
- whether supporting sources should stay grouped by canonical object or flatten into one route
- whether runtime caution should be able to suppress first-pass expansion further
