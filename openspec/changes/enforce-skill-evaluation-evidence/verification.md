# Verification

## RED

- Add a health-check test for an active change that references `.codex/skills/` but lacks `evaluation.md`.
- Confirm the test fails before the new evidence check exists.

## GREEN

- Re-run the targeted health-check tests after implementation.
- Confirm the missing-evidence scenario fails with a named health-check result.
- Confirm a change with a valid `evaluation.md` passes.
- Confirm `openspec validate enforce-skill-evaluation-evidence` succeeds.
