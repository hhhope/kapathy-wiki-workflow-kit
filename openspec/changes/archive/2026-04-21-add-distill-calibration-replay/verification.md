## Commands

### Distill calibration replay checker

```bash
python3 scripts/distill_calibration_replay_check.py \
  scripts/examples/agents_governance_drift_distill_calibration_replay.json
```

Observed result:

- `PASS: distill calibration replay record satisfies the executable contract.`
- `thread_label: agents-governance-drift-distill-2026-04-21 calibration`

### Unit tests for the checker

```bash
python3 -m unittest tests.test_distill_calibration_replay_check
```

Observed result:

- `Ran 3 tests ... OK`

### Regression check for existing repo policy/health tests

```bash
python3 -m unittest tests.test_repo_policy_check tests.test_repo_health_check
```

Observed result:

- `Ran 7 tests ... OK`

## What This Verifies

- The new replay contract is executable, not only narrative.
- The sample replay record satisfies the structural contract.
- The checker fails on missing fields or failed pass checks via unit tests.
- Existing repo policy/health checks still pass after adding the new assets.

## Proof Boundary

- This verification is structural executable proof only.
- It does not prove the distill page is already corrected.
- It does not prove the candidate governance model is valid or accepted.
