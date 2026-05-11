## Why

The current public report gate can catch narrative drift, judgment ownership,
voice leakage, and missing visual plans. It does not yet explicitly catch a
reference-shaped report that keeps the right facts but renders them in the wrong
composition system.

The recent company playbook repair exposed this gap. The requested reference was
the existing newspaper report style, but the draft repeatedly fell back to
card-wall, colored-panel, and table-like comparison layouts. The content became
closer to the user's judgment only after the page was converted into newspaper
article flow: section rhythm, prose paragraphs, evidence ledgers, and numbered
lines instead of repeated cards.

## What Changes

- Add an Article Flow Layout Gate to `public-report-quality-gate`.
- Require reference-shaped reader-facing drafts to map the reference's layout
  system before drafting, not only its topic or section names.
- Treat card walls, repeated boxed company cells, dashboard grids, and prompt /
  visual-script residue as hard failures when the reference calls for newspaper
  article flow.
- Extend gate-review artifacts and pressure scenarios with replayable evidence
  for layout drift.
- Add tests proving the gate wording and replay artifacts exist.

## Impact

- Updates `.codex/skills/public-report-quality-gate/`.
- Updates focused tests for public-report gate behavior.
- Updates `openspec/specs/public-report-quality-gate/spec.md` via spec delta.
- Does not rewrite existing reports retroactively.
