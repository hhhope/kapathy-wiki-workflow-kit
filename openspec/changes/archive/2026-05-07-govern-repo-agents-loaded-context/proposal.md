## Why

Repo `AGENTS.md` remains 510 lines and carries long-form governance material
whose stable homes now exist in ADRs, OpenSpec specs, wiki ops pages, and
published skills.

The earlier change name `phase1-repo-agents-compression` is intentionally
retired because "Phase 1" conflicts with an older intake definition. The root
successor has completed and the repo-local commit-hook default has been
decided, so the repo-level work can now continue under a clearer target:
repo `AGENTS.md` loaded-context governance.

The goal is not line-count aesthetics. The goal is a repo entrypoint that keeps
repo-only hard stops inline, replaces stable repeated governance prose with
bounded proxies, and proves that a future agent can still find source records,
verification paths, and stop conditions.

## What Changes

- Rename and rescope the parked repo AGENTS compression change to
  `govern-repo-agents-loaded-context`.
- Define repo `AGENTS.md` compression as loaded-context governance, not a
  generic line-count cleanup.
- Require each removed or shortened governance block to map to either:
  - an inline repo-only hard stop
  - a stable proxy to ADR / OpenSpec spec / wiki ops page / skill
  - an explicitly deferred candidate
- Record before/after evidence for line count, proxy coverage, hard-stop
  preservation, and agent legibility.

## Capabilities

### New Capabilities

- `repo-agents-loaded-context`: The repository SHALL govern repo `AGENTS.md` as
  a loaded-context entrypoint with inline hard stops and stable proxies.

### Modified Capabilities

- `repo-agents-governance-phase0`

## Impact

- Targets repo `AGENTS.md` as the implementation surface in a later step.
- May update this change's evaluation and tasks as implementation evidence.
- Does not edit root `~/.codex/AGENTS.md`.
- Does not edit `~/.claude/CLAUDE.md`.
- Does not add a repo-local commit hook.
- Does not implement repo `AGENTS.md` compression in this rename/rescope step.
