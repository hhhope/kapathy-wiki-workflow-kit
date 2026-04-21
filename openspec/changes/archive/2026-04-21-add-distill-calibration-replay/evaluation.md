## Baseline Scenarios

### Scenario 1: Distill calibration is narrative only

- the repository has a distill page and a separate calibration retro
- the calibration retro identifies overclaiming
- but there is no executable replay contract that can fail when the minimum
  calibration evidence is missing

### Scenario 2: Distill calibration is replay-validated

- a structured replay record is captured for the current distill dispute
- the checker should fail if required calibration fields or pass conditions are
  missing

## RED Baseline

Before this change:

- the repository had narrative calibration material
- the repository had no executable replay contract for distill calibration
- later contributors could still read the distill as if it already represented
  stable governance consensus

So TDD remained descriptive instead of executable.

## GREEN Result

After this change:

- `scripts/distill_calibration_replay_check.py` validates the replay contract
- `scripts/examples/agents_governance_drift_distill_calibration_replay.json`
  passes the checker
- `wiki/ops/distill-calibration-replay-harness.md` makes the proof boundary
  explicit
- `wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md`
  records the first validation result

Executable check command:

```bash
python3 scripts/distill_calibration_replay_check.py \
  scripts/examples/agents_governance_drift_distill_calibration_replay.json
```

Expected result:

- `PASS: distill calibration replay record satisfies the executable contract.`

## Residual Risks

- This remains structural executable proof, not semantic certainty.
- The checker cannot decide whether a proposed governance model is actually
  correct.
- The checker does not prove that future distill pages will automatically stay
  honest.
