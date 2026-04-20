## Baseline Scenarios

### Scenario 1: Drifted continuation after the original requirement was already restated

- Original requirement had already been narrowed to agent-readable wiki structure for disagreement / decision evolution
- Work later continued into:
  - runtime context
  - source integration
  - auto routing
  - context injection
  - bounded self-directed execution
- The user explicitly signaled drift and asked to return to the earlier requirement

### Scenario 2: Ordinary correction without real drift

- The user gives a single factual correction or wording adjustment
- The mainline remains the same

## RED Baseline

Before this change, the repository already had:

- disagreement preservation
- anti-compression states
- `retro before ADR`

But that layer did not force interruption. The practical RED failure was:

- disagreement could still be preserved too late
- `continue` could inherit the current technical chain
- the live conversation did not have a stop-and-reanchor gate
- this current drift dispute did not automatically land in `wiki/ops retro`

So preservation existed, but interruption did not.

## GREEN Result

After this change, the repository now defines a distinct live conversation gate with:

- concrete trigger signals
- mandatory stop-and-reanchor action
- repo-visible retro capture before further continuation
- explicit unblock conditions

Published surfaces:

- `AGENTS.md`
- `wiki/ops/disagreement-management-method.md`
- `wiki/ops/live-conversation-reanchor-gate-retro.md`
- `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`

The boundary is now explicit:

- disagreement preservation alone is not enough
- drift signals must stop continuation before more implementation

## Residual Risks

- The gate still depends on honest recognition of drift signals; it is not automatic runtime enforcement.
- `continue` remains a risky user input if the conversation state is badly summarized.
- This change improves repository-default behavior, but does not guarantee perfect detection.
