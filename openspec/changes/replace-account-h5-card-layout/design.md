# Design: Replace Account H5 Card Layout

## Layout Direction

Use a technical handout model:

- Sections are the page rhythm.
- Diagrams carry architecture and planning.
- Text blocks are lists, rows, and matrices rather than cards.
- Repeated items use separators, columns, and labels, not boxed cards.

## Specific Changes

- Replace `.card` visuals with `.brief-item` behavior: no boxed background,
  no card shadow, no colored card border; use a small label and a left rule or
  row separator.
- Replace card grids with lower-noise matrices where possible.
- Keep source visual frames around diagrams, because those are the load-bearing
  visuals.
- Keep mobile behavior as single-column rows, with separators rather than card
  blocks.

## Verification

- HTML parser.
- Grep for required section titles and AI/account harness phrasing.
- Grep that rejected process titles and sensitive terms are absent.
- Desktop and mobile screenshot inspection focused on reducing card-grid feel.
- `git diff --check`.
- `openspec validate replace-account-h5-card-layout --strict`.
