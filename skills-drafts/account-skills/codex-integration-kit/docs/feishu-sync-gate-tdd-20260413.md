# Feishu Sync Gate TDD

Date: `2026-04-13`

## Goal

Prevent governance-surface changes in this repository from being treated as complete unless the Feishu-facing source markdown is updated in the same work cycle.

## RED

Command:

```bash
bash codex-integration-kit/tests/test-feishu-sync-gate.sh
```

Initial state:

- `codex-integration-kit/scripts/check-feishu-sync.sh` did not exist
- the test fixture expected a failure when governance files changed without the Feishu source
- the test suite failed immediately because no enforcement script existed

That was the expected RED: the repository had a documented rule but no executable gate.

## GREEN

Implemented:

- [check-feishu-sync.sh](/mnt/d/skills/account-skills/codex-integration-kit/scripts/check-feishu-sync.sh)
- [pre-commit](/mnt/d/skills/account-skills/.githooks/pre-commit)

Verification commands:

```bash
bash codex-integration-kit/tests/test-feishu-sync-gate.sh
bash codex-integration-kit/scripts/check-feishu-sync.sh --staged
```

Observed results:

- `PASS: feishu sync gate`
- `Feishu sync gate passed: no governance-surface change detected.`

## Covered Behavior

- staged governance changes without `docs/feishu-codex-governance-share.md` now fail
- staged governance changes with the Feishu source included now pass
- clean staged state passes without noise

## Scope

This gate is repo-local only.

- It does not modify global `~/.codex` behavior.
- It can be enabled for this repo via `git config core.hooksPath .githooks`.
- It is intentionally staged-based to avoid false positives from unrelated dirty files already present in the worktree.
