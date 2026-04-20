# Verification

## Commands

```bash
openspec validate require-local-skill-pressure-tests
python3 -m unittest tests.test_repo_health_check
python3 scripts/repo_health_check.py --repo-root .
```

## Expected Outcome

- OpenSpec validation passes.
- The unit test proves the RED/GREEN section gate:
  - old descriptive evaluation headings fail
  - explicit pressure-test headings pass
- Repo health checks remain green after backfilling existing skill-change evaluations.

## Results

- `python3 -m unittest tests.test_repo_health_check`
  - `Ran 5 tests ... OK`
- `python3 scripts/repo_health_check.py --repo-root .`
  - `PASS draft-skill-runtime-surface`
  - `PASS skill-evaluation-evidence`
- `openspec validate require-local-skill-pressure-tests`
  - `Change 'require-local-skill-pressure-tests' is valid`
