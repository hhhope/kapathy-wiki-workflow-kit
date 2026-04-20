## Context

`live-conversation-reanchor-gate` is now formalized, archived, and published in:

- `AGENTS.md`
- `wiki/ops/disagreement-management-method.md`
- `wiki/ops/live-conversation-reanchor-gate-retro.md`
- `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`
- `openspec/specs/live-conversation-reanchor-gate/spec.md`

But the current validation is still policy-level evidence. The user explicitly asked to "do TDD" rather than stop at descriptive RED/GREEN.

The disagreement-management stack already has a reusable executable replay checker. This change should reuse that validation style instead of inventing a larger framework.

## Goals / Non-Goals

**Goals**

- Add a minimal executable replay contract for re-anchor-gate validation
- Reuse the repository's existing replay-harness style
- Keep the proof boundary explicit: structural executable proof, not semantic certainty

**Non-Goals**

- Do not add runtime automation
- Do not claim perfect drift detection
- Do not add a generic policy engine
- Do not create a full multi-thread replay suite in this change

## Decisions

### Decision: Re-anchor replay should validate the gate-specific fields, not only generic disagreement fields

The existing disagreement replay checker validates generic disagreement preservation. Re-anchor needs its own contract because it must additionally prove:

- original requirement was preserved
- current drift chain was made explicit
- trigger signals were present
- stop action happened
- unblock condition was recorded

Alternative considered:
- Reuse the disagreement replay checker unchanged.
  - Rejected because it cannot fail on missing re-anchor-specific evidence.

### Decision: Keep the checker structural and bounded

The executable checker should fail on missing fields and missing required pass conditions, not on semantic interpretation.

Alternative considered:
- Attempt semantic scoring of whether the drift was "real enough."
  - Rejected because that is a larger and less reliable problem.

### Decision: Validate the current drift dispute as the first replay example

The first replay should use the actual dispute that exposed this gap:

- early requirement confirmed
- continuation drifted into runtime / execution stack
- user explicitly called out the drift
- the repository did not interrupt early enough

Alternative considered:
- Invent a synthetic example first.
  - Rejected because the current real thread is the clearest RED/GREEN baseline.

## Replay Contract

Minimum replay fields:

- `thread_label`
- `original_requirement`
- `current_drift_chain`
- `trigger_signals`
- `stop_action`
- `reanchor_artifact`
- `unblock_condition`
- `red_baseline`
- `green_result`
- `residual_risk`

Required pass checks:

- `drift_signal_present`
- `original_requirement_preserved`
- `continuation_stopped`
- `repo_visible_reanchor_recorded`
- `no_runtime_autonomy_claim`

## Risks / Trade-offs

- [Risk] The checker could be mistaken for semantic proof. -> Mitigation: publish explicit proof-boundary language.
- [Risk] The contract could become too broad. -> Mitigation: keep it specific to re-anchor-gate evidence.
