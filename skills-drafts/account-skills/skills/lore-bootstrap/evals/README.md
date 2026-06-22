# Lore Bootstrap Eval Fixtures

This directory validates install/bootstrap/migration behavior for `lore-bootstrap`.

## Scenarios

1. Fresh install
   - no shared repo exists
   - bootstrap should create git repo, wiki root, project pages, and AGENTS path
2. Existing repo bootstrap
   - shared repo already has `.git`
   - bootstrap should add missing wiki pages without breaking git
3. Legacy migration
   - flat `LORE.md` exists in the project repo
   - bootstrap should snapshot it into the wiki project area and create migration notes

## Command

```bash
sh skills/lore-bootstrap/evals/run-bootstrap-checks.sh
```

## Expected evidence

- `SKILL-EVAL.md` records RED/GREEN reasoning
- `run-bootstrap-checks.sh` returns zero
- `COMMAND-RESULTS.md` records the latest command-level run
- output proves git-backed wiki creation and migration artifacts
