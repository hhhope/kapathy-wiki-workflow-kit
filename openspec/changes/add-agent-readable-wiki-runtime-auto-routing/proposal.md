# Proposal: Add Runtime Auto Routing On Top Of Source Integration

## Why

The repository can now produce a bounded source-integrated runtime artifact that tells
an agent:

- which canonical objects are preferred
- which supporting objects are still useful
- which blocked objects must stay out of first-pass reading
- which concrete repository-local source paths correspond to those objects

But the stack still stops one step short of actual runtime use.

The current source-integrated output still leaves one manual decision in the loop:

- which sources should be opened first
- which sources should be queued as follow-up reading
- which blocked objects should stay fully out of first-pass routing

Without that routing layer, the repository has source-integrated guidance but not yet a
bounded auto-selection plan that an agent can follow consistently.

## What Changes

This change adds a first runtime auto-routing layer on top of runtime-context source
integration.

The change will:

- define a minimal runtime auto-routing contract
- derive a bounded first-pass reading plan from the source-integrated runtime artifact
- keep blocked objects out of first-pass source routing
- publish repository-visible guidance for how agents should consume the routing plan

This change does not:

- perform external retrieval
- inject context automatically into every agent entrypoint
- override blocked-object boundaries
- claim runtime autonomy or rollout proof

## Success Criteria

- The repository has a stable runtime auto-routing spec and workflow.
- A source-integrated runtime artifact can be enriched into a deterministic first-pass routing plan.
- Preferred and supporting sources are separated into explicit routing stages.
- Blocked objects remain excluded from first-pass route generation.
- The repository keeps the boundary explicit: runtime auto routing is stronger than source integration, but weaker than autonomous runtime execution.
