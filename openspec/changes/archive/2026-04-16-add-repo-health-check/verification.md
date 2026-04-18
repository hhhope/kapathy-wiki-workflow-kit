# Verification

## RED

- `python3 -m unittest tests.test_repo_health_check`
- Result before implementation:
  - `ModuleNotFoundError: No module named 'scripts.repo_health_check'`
  - confirms the unified repo health-check entry did not exist yet

## GREEN

- `python3 -m unittest tests.test_repo_health_check tests.test_repo_policy_check`
- Result:
  - `Ran 4 tests ... OK`
  - confirms the unified health-check entry reports a passing named check on a clean temporary repo
  - confirms the same entry reports a failing named check with `skills-drafts/example-skill/SKILL.md` when a draft skill exists
- `python3 scripts/repo_health_check.py --repo-root .`
- Result:
  - `PASS draft-skill-runtime-surface`
- `openspec validate add-repo-health-check`
- Result:
  - `Change 'add-repo-health-check' is valid`
