# Verification

## Structure

- `openspec validate make-disagreement-replay-harness-executable`
- Result: `Change 'make-disagreement-replay-harness-executable' is valid`

## GREEN

- `python3 scripts/disagreement_replay_check.py scripts/examples/disagreement_stage_boundary_replay.json`
  - Result confirmed the executable harness passes on a valid sample replay record
- `sed -n '1,260p' wiki/ops/disagreement-management-replay-harness.md`
  - Result confirmed the wiki harness page now documents executable usage and limits
- `sed -n '1,240p' scripts/disagreement_replay_check.py`
  - Result confirmed the checker validates required fields and required pass-condition checks

## Proof Boundary

- This verifies that the repository now has executable structural replay validation.
- It does not verify semantic correctness of the disagreement itself.
- It does not upgrade replay proof into rollout proof.
