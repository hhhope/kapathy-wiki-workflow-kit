# Verification

## RED

- `python3 -m unittest tests.test_repo_health_check`
- Result before implementation:
  - 4 tests failed because `run_health_checks()` returned only the draft-skill result
  - the health-check had no `skill-evaluation-evidence` gate yet

## GREEN

- `python3 -m unittest tests.test_repo_health_check`
- Result:
  - `Ran 4 tests ... OK`
  - confirms a skill-touching active change without `evaluation.md` now fails
  - confirms a skill-touching active change with a valid `evaluation.md` now passes
- `python3 scripts/repo_health_check.py --repo-root .`
- Result:
  - `PASS draft-skill-runtime-surface`
  - `PASS skill-evaluation-evidence`
- `openspec validate enforce-skill-evaluation-evidence`
- Result:
  - `Change 'enforce-skill-evaluation-evidence' is valid`
- `openspec validate add-principle-skills-layer`
- Result:
  - `Change 'add-principle-skills-layer' is valid`
