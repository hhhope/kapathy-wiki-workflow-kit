# Proposal: Add Bounded Agent Self-Directed Execution On Top Of Context Injection

## Why

The repository can now produce a bounded injected-context bundle that tells an agent:

- which first-pass context should be injected
- which secondary context should remain available but not dominate
- which excluded objects must stay out of first-pass context

But the stack still stops one step short of actual self-directed work planning.

The current injected-context output still leaves one manual step in the loop:

- deciding what the next bounded actions should be
- deciding which actions are safe to attempt now
- deciding which actions should stay blocked pending human choice

Without that execution layer, the repository has injected context but not yet a
bounded self-directed execution plan that an agent can follow consistently.

## What Changes

This change adds a first bounded self-directed execution layer on top of automatic
context injection.

The change will:

- define a minimal bounded self-directed execution contract
- derive a deterministic execution-plan bundle from the injected-context artifact
- keep blocked objects out of first-pass execution
- publish repository-visible guidance for how agents should consume the execution plan

This change does not:

- perform external retrieval
- allow autonomous side effects without explicit bounded routing
- override blocked-object boundaries
- claim full agent autonomy or rollout proof

## Success Criteria

- The repository has a stable bounded self-directed execution spec and workflow.
- An injected-context artifact can be enriched into a deterministic execution-plan bundle.
- First-pass injected context becomes explicit `execute_now` guidance, while secondary context stays clearly deferred.
- Blocked objects remain excluded from first-pass execution.
- The repository keeps the boundary explicit: bounded self-directed execution is stronger than injected context, but weaker than full agent autonomy.
