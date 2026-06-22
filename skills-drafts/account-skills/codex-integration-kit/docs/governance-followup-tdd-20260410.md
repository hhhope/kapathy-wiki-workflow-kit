# Governance Follow-up TDD Traceability

Date: `2026-04-10`
Scope: restore repository memory gate and remove stale governance references from `codex-integration-kit`

## Why This Change

The repository health check was blocked because `PROJECT.md` was missing again. At the same time, some kit assets still referenced the retired `memory/PROJECT.md` path and stale installation semantics from an older repo shape.

This round fixes the gate first, then aligns the remaining governance assets with the current `PROJECT.md` and install model.

## RED

### Baseline blocker

Command:

```bash
find . -name PROJECT.md -not -path './.*' 2>/dev/null | head -1
```

Observed result before the fix:

- No output
- Health check could not proceed

### Baseline stale-reference scan

Command:

```bash
rg -n "memory/PROJECT.md|account-team-efficiency|\\.githooks" \
  codex-integration-kit/agents/planner.md \
  codex-integration-kit/rules/common/development-workflow.md \
  codex-integration-kit/rules/common/git-workflow.md \
  codex-integration-kit/docs/feishu-codex-governance-share.md
```

Observed result before the fix:

- `agents/planner.md` still required `memory/PROJECT.md`
- `rules/common/development-workflow.md` still listed `memory/PROJECT.md`
- `rules/common/git-workflow.md` hard-coded `.githooks`
- `docs/feishu-codex-governance-share.md` still used `memory/PROJECT.md`
- `docs/feishu-codex-governance-share.md` still used old `account-team-efficiency` install paths

## GREEN

### Files changed

- Restored repository memory file: `PROJECT.md`
- Updated `agents/planner.md`
- Updated `rules/common/development-workflow.md`
- Updated `rules/common/git-workflow.md`
- Updated `docs/feishu-codex-governance-share.md`

### Verification commands

Health check:

```bash
find . -name PROJECT.md -not -path './.*' 2>/dev/null | head -1
```

Result after the fix:

- Returns `./PROJECT.md`

Targeted stale-reference scan:

```bash
rg -n "memory/PROJECT.md|account-team-efficiency|\\.githooks" \
  codex-integration-kit/agents/planner.md \
  codex-integration-kit/rules/common/development-workflow.md \
  codex-integration-kit/rules/common/git-workflow.md \
  codex-integration-kit/docs/feishu-codex-governance-share.md
```

Result after the fix:

- No matches

Current-install wording scan:

```bash
rg -n "PROJECT.md|AGENTS.repo-template.md|account-skills/codex-integration-kit/scripts/install-codex-governance.sh|hooks / CI|hooks or validation" \
  codex-integration-kit/agents/planner.md \
  codex-integration-kit/rules/common/development-workflow.md \
  codex-integration-kit/rules/common/git-workflow.md \
  codex-integration-kit/docs/feishu-codex-governance-share.md
```

Result after the fix:

- `PROJECT.md` is the active memory path in planner and development workflow
- hook wording is generic instead of repo-private
- Feishu source now uses current install paths and current target filenames

## Notes

- This change intentionally updates the Feishu source markdown in-repo as part of the same work cycle, because project memory requires share content to stay synchronized with material governance changes.
- Existing unrelated worktree changes were preserved.
