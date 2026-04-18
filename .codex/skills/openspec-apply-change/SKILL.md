---
name: openspec-apply-change
description: Use when the user wants to implement or continue an active OpenSpec change in the current repository.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.2.0"
---

Implement an active OpenSpec change from the current repository.

## Hard Rules

- Use the repository's actual OpenSpec CLI and local files. Do not assume slash commands or external helper tools.
- Read `openspec instructions apply --change "<name>" --json` before touching code.
- Use the returned `contextFiles` as the implementation context and keep `tasks.md` in sync with completed work.
- If the change is blocked, missing artifacts, or already complete, report that state instead of pretending implementation can continue.

## Default Flow

1. Select the change name from the user request or by checking `openspec list --json`.
2. Run `openspec status --change "<name>" --json`.
3. Run `openspec instructions apply --change "<name>" --json`.
4. Read the referenced proposal, design, specs, and tasks files.
5. Implement pending tasks in order.
6. Mark finished tasks in `tasks.md`.
7. Re-run status or tests before claiming completion.

## Output Contract

- State which change is being implemented.
- State whether the change is blocked, active, or complete.
- Summarize completed tasks and remaining tasks for the current session.

## Anti-Patterns

- Telling the user to run imaginary slash commands
- Delegating selection to nonexistent helper tooling
- Updating code without reading the current change artifacts
- Claiming the change is complete without updating `tasks.md`
