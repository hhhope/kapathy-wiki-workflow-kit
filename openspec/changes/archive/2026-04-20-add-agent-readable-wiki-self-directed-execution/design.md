# Design: Bounded Agent Self-Directed Execution

## Problem

The repository can derive a bounded injected-context bundle, but it still does not
turn that bundle into an explicit self-directed execution plan.

That means the stack is still missing one operational bridge:

- context injection says what the agent should have in context
- but it does not yet say what bounded actions the agent should attempt next

Without that bridge, every live task still requires a manual execution-planning step.

## Design Goals

This change should:

- stay downstream of automatic context injection
- produce a deterministic bounded execution-plan bundle
- preserve blocked-state boundaries
- keep the output explicit and cheap for an agent to inspect

## Core Approach

Version 1 should stay deterministic and repository-local.

The workflow should:

1. read the automatic context-injection artifact
2. convert injected first-pass context into explicit `execute_now` actions
3. convert secondary context into explicit `defer_for_followup` actions
4. preserve excluded objects as not executable

## Execution Strategy

Version 1 should produce only bounded execution groups such as:

- `execute_now`
- `defer_for_followup`
- `do_not_execute`

The mapping should stay explicit and deterministic rather than heuristic-heavy.

## Minimum Output

The bounded self-directed execution artifact should include at least:

- summary
- execute-now actions
- deferred follow-up actions
- blocked objects
- execution notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can turn injected-context output into a deterministic execution-plan bundle
- first-pass injected context can become bounded `execute_now` actions
- secondary context can remain deferred
- blocked objects stay outside first-pass execution

This change should not claim:

- external retrieval integration
- unrestricted side effects
- full agent autonomy
- unresolved page understanding

## Non-Goals

- no Feishu integration
- no vector index integration
- no unrestricted agent execution loop
- no blocked-object override logic

## Open Questions

- whether version 1 should emit only one action per canonical object or a small ordered action list
- whether execute-now actions should preserve injected source grouping or flatten into one queue
- whether repository caution should suppress some first-pass actions entirely
