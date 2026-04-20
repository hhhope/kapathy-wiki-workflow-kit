## Baseline Scenarios

### Scenario 1: Policy-only validation

- `live-conversation-reanchor-gate` already existed as policy, retro, ADR, and formal spec
- validation still lived mainly in narrative RED/GREEN text

### Scenario 2: Executable replay validation

- the current drift dispute is replayed as a structured record
- the checker should fail if required gate evidence is missing

## RED Baseline

Before this change:

- the gate had repository policy proof
- the gate had repo-visible retro proof
- the gate had ADR and spec proof
- but it did not yet have executable replay proof

So TDD remained narrative instead of executable.

## GREEN Result

After this change:

- `scripts/reanchor_gate_replay_check.py` validates the replay contract
- `scripts/examples/live_conversation_reanchor_gate_replay.json` passes the checker
- `wiki/ops/live-conversation-reanchor-gate-replay-harness.md` makes the proof boundary explicit

Executable check command:

```bash
python3 scripts/reanchor_gate_replay_check.py scripts/examples/live_conversation_reanchor_gate_replay.json
```

Expected result:

- `PASS: re-anchor replay record satisfies the executable contract.`

## Residual Risks

- This remains structural executable proof, not semantic certainty.
- The checker cannot decide whether a borderline disagreement was truly drift.
- The checker does not prove full rollout behavior.
