---
name: openspec-archive-change
description: Use when the user wants to archive a completed OpenSpec change after checking artifact status, task completion, and spec-sync implications.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.2.0"
---

Archive a completed OpenSpec change in the current repository.

## Hard Rules

- Use the real OpenSpec CLI and repository files. Do not assume special prompt tools or task runners exist.
- Check `openspec status --change "<name>" --json` before archiving.
- Review `tasks.md` and any delta specs under `specs/` before moving the change.
- If anything is incomplete, show the warning in chat and ask the user directly whether to continue.

## Default Flow

1. Select the change from the user request or `openspec list --json`.
2. Run `openspec status --change "<name>" --json`.
3. Read `tasks.md` and note incomplete items.
4. Inspect `openspec/changes/<name>/specs/` to decide whether delta specs still need syncing.
5. If the user confirms, move the change into `openspec/changes/archive/YYYY-MM-DD-<name>`.

## Output Contract

- State the change name and archive path.
- State whether tasks were complete.
- State whether spec sync was already done, skipped, or still pending.

## Anti-Patterns

- Referring to nonexistent prompt-side or task-runner helpers
- Archiving without checking `tasks.md`
- Treating archive as proof that spec sync already happened
