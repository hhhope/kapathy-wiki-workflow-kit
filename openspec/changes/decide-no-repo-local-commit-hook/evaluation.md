# Evaluation

## Baseline Scenarios

1. Phase 0 required the repo-local commit-gate status to be explicit before
   Phase 1 repo `AGENTS.md` migration.
2. The repo did not yet record whether the default path requires, defers, or
   rejects a repo-local commit hook.
3. Older candidate wiki material still discusses hook-based enforcement strongly
   enough that a future migration could inherit it as an implicit default.

## Before Results

- `AGENTS.md` required "an explicit decision on the repo-local commit gate" but
  did not state the decision.
- `repo-agents-governance-phase0` allowed either "required" or "deferred" gate
  decisions, but did not include the "not default" decision now chosen.
- `git config --get core.hooksPath` returned no configured repo-local hooks
  path in this repository.

## After Results

- `wiki/adr/0030-no-repo-local-commit-hook-default.md` records the stable
  repository decision.
- `AGENTS.md` states that repo-local commit hooks are not part of the default
  governance path and that reversal requires a new OpenSpec change.
- OpenSpec deltas add `no-repo-local-commit-hook-default` and update
  `repo-agents-governance-phase0` so Phase 1 can proceed without silently
  inheriting hook assumptions.

## Self-Check

| Column | Result | Evidence |
|---|---|---|
| Structural | pass | ADR, spec deltas, evaluation, and tasks exist under the active change |
| Semantic | pass | Decision is repo-local; no root `~/.codex/AGENTS.md` or `~/.claude/CLAUDE.md` behavior is changed |
| Evidence | pass | Baseline records the prior ambiguous gate state and absence of configured `core.hooksPath` |
| Boundary | pass | No hook implementation, checker, CI gate, root dotfile edit, or Phase 1 repo `AGENTS.md` compression is included |

## Residual Risks

- Older candidate wiki pages still mention Git hooks and Claude-specific hooks.
  They remain historical candidate material, not the accepted default path.
- This is a prose/spec decision. It does not mechanically prevent a future
  contributor from proposing hooks; it requires such a proposal to be explicit.
