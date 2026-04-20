# Proposal: Add Automatic Context Injection On Top Of Runtime Auto Routing

## Why

The repository can now produce a bounded runtime auto-routing artifact that tells an
agent:

- which repo-local sources belong in `open_first`
- which sources belong in `open_next`
- which blocked objects must stay out of first-pass routing

But the stack still stops one step short of actual context assembly.

The current runtime auto-routing output still leaves one manual step in the loop:

- taking the routed source plan
- loading the selected source content
- packaging that content into a bounded context-injection bundle

Without that injection layer, the repository has reading-order guidance but not yet a
bounded, machine-readable context payload that can be passed into live agent work.

## What Changes

This change adds a first automatic context-injection layer on top of runtime
auto routing.

The change will:

- define a minimal automatic context-injection contract
- derive a bounded injected-context bundle from the runtime auto-routing artifact
- keep blocked objects out of injected first-pass context
- publish repository-visible guidance for how agents should consume the injected bundle

This change does not:

- perform external retrieval
- enable agent autonomy or self-directed execution
- override blocked-object boundaries
- claim rollout proof for all entrypoints

## Success Criteria

- The repository has a stable automatic context-injection spec and workflow.
- A runtime auto-routing artifact can be enriched into a deterministic injected-context bundle.
- `open_first` sources are injected into first-pass context, while `open_next` sources stay explicitly secondary.
- Blocked objects remain excluded from injected first-pass context.
- The repository keeps the boundary explicit: automatic context injection is stronger than routing guidance, but weaker than agent autonomy.
