---
name: openspec-propose
description: Use when the user wants to start a new OpenSpec change for repository-level work and needs the proposal, design, specs, and tasks created in the current repository.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.2.0"
---

Create a new OpenSpec change in the current repository.

## Hard Rules

- Use the real `openspec` CLI in the repo. Do not assume slash commands or helper tools exist.
- If the change name is unclear, ask the user directly in chat or derive a kebab-case name from the request.
- Before creating later artifacts, read `openspec status --change "<name>" --json` and the matching `openspec instructions ... --json` output.
- Keep artifact bodies repo-specific and concise. Do not copy instruction metadata blocks into the files.

## Default Flow

1. Run `openspec new change "<name>"`.
2. Run `openspec status --change "<name>" --json`.
3. Create each artifact in dependency order:
   - `proposal.md`
   - `design.md`
   - `specs/**/*.md`
   - `tasks.md`
4. Re-run `openspec status --change "<name>" --json` after each artifact batch until `tasks` is `done`.

## Output Contract

- State the selected change name and location.
- State which artifacts were created.
- Tell the user the change is ready for implementation once `tasks.md` exists.

## Anti-Patterns

- Referring the user to imaginary slash commands
- Requiring nonexistent prompt-side helper tools
- Creating only `.openspec.yaml` and stopping before the apply-ready artifacts exist
