# Lore Bootstrap Skill Eval

Date: 2026-04-11
Branch: `feat-lore-wiki-openspec`

This file records the required RED/GREEN evidence for introducing the `lore-bootstrap` skill.

## Expected behavior

1. Lore Wiki install/bootstrap/migration should have a dedicated entrypoint skill
2. The workflow should produce a git-backed shared repo, not only prose instructions
3. Legacy flat lore migration should leave a traceable snapshot and migration note
4. Install output should make the chosen wiki path explicit instead of silently assuming `~/team-lore`

## RED — Before the skill

Observed baseline commands:

```bash
test -f skills/lore-bootstrap/SKILL.md
test -f skills/lore-bootstrap/scripts/bootstrap_lore_wiki.sh
```

Observed result:

- `RED: missing lore-bootstrap skill`
- `RED: missing bootstrap command surface`

Why this is a fail:

- install/init/migration existed only as lore onboarding prose
- there was no dedicated trigger for `install lore wiki`
- there was no reusable command surface to validate git/bootstrap behavior
- install guidance implicitly centered `$HOME` rather than a confirmed shared wiki location

## GREEN — After the skill

Expected after implementation:

- `skills/lore-bootstrap/SKILL.md` exists with install/bootstrap/migration scope
- `scripts/bootstrap_lore_wiki.sh` creates or completes a git-backed shared wiki repo and reports the chosen path
- `evals/run-bootstrap-checks.sh` proves fresh install, existing repo bootstrap, and legacy migration

## Limits

- evaluation uses fixture temp directories, not the user's real home directory
- migration validation proves traceable snapshotting, not full semantic page splitting
