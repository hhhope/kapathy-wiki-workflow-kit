# Archive Review

Decision: archive-ready.

## Evidence

- `tasks.md` is complete: 13/13 checked.
- `openspec validate rename-wiki-runtime-skills --strict` passed.
- `evaluation.md` records RED/GREEN skill-surface evidence and behavior replay.
- Delta scope updates the discoverable wiki runtime surface from `/wiki:*`
  plugin commands to user-scope `$wiki-*` skills while preserving command
  contracts and non-promotion boundaries.

## Boundary

- Runtime scripts, graph extraction, score formulas, queue semantics, and
  OpenSpec lifecycle behavior are unchanged.
- Plugin command contracts are intentionally retained as source contracts.
- No routine closing tail remains for this change.

## Residual Risk

The proof covers Codex app-server skill discovery. An already-open Codex TUI
session may need reload before showing the user-scope skill list.
