# Design: Resolve Ops Identity Conventions

## Goal

Reduce remaining `wiki/ops` unresolved identity pressure by recognizing explicit
filename conventions already used by ops pages.

## Supported Conventions

- `wiki/ops/<object>-intake.md` -> `<object> / intake`
- `wiki/ops/<object>-explore[-YYYY-MM-DD].md` -> `<object> / explore`
- `wiki/ops/<object>-retro[-YYYY-MM-DD].md` -> `<object> / retro`
- `wiki/ops/<object>-reminder[-YYYY-MM-DD].md` -> `<object> / reminder`
- `wiki/ops/<object>-reanchor.md` -> `<object> / reanchor`
- `wiki/ops/sample-<object>.md` -> `<object> / sample`

Stable fixed entry pages:

- `wiki/ops/main-thread.md` -> `main-thread / focus-thread`
- `wiki/ops/reminders.md` -> `reminders / reminder-index`
- `wiki/ops/codex-handoff-rules.md` -> `codex-handoff / method`
- `wiki/ops/project-management-weekly-loop.md` ->
  `project-management-weekly-loop / method`

## Priority

1. Frontmatter identity
2. Existing dedicated object-family resolvers
3. Bounded OpenSpec/ADR/example path resolvers
4. Bounded ops path resolvers
5. Warning

## Boundary

The resolver SHALL NOT infer from arbitrary prose. Ops pages that do not match
the supported filename conventions stay unresolved.

## Verification

- Unit tests cover intake, dated explore, sample, fixed entry pages, and
  unsupported ops pages.
- Live extraction should reduce warnings from the current 30.
- OpenSpec validation and affected runtime tests should pass.
