# Verification

## RED

- `python3 -m unittest tests.test_repo_policy_check`
- Result before implementation:
  - `ModuleNotFoundError: No module named 'scripts.repo_policy_check'`
  - confirms the new guard did not exist yet

## GREEN

- `python3 -m unittest tests.test_repo_policy_check`
- Result:
  - `Ran 2 tests ... OK`
  - the test suite confirms the checker reports `skills-drafts/example-skill/SKILL.md` as a violation and allows non-`SKILL.md` draft notes
- `python3 scripts/repo_policy_check.py --repo-root .`
- Result:
  - `OK: no active draft skill files under skills-drafts/`
- `openspec validate enforce-draft-skill-check`
- Result:
  - `Change 'enforce-draft-skill-check' is valid`
