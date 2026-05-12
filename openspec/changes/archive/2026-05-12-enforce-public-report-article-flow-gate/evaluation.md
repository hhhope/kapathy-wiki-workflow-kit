# Evaluation: Article Flow Layout Gate

## Pressure Scenarios

1. A company-analysis page cites an existing newspaper report as the format
   reference, but the draft renders four companies as repeated cards and
   comparison cells.
2. A final takeaway section becomes a 2x2 card wall instead of newspaper
   closing lines.
3. A Hybrid/image-model prompt leaks into the report body.
4. A gate-review artifact records "retain" for the rejected card/table layout
   without noting the reference layout system.

## RED Baseline

- Command: `python3 -m unittest tests.test_public_report_quality_gate`
- Result before implementation: failed 1/6.
- Expected failure: `Article Flow Layout Gate` missing from
  `.codex/skills/public-report-quality-gate/SKILL.md`.

## GREEN Result

- Command: `python3 -m unittest tests.test_public_report_quality_gate`
- Result after implementation: passed 6/6.
- Validation:
  - `python3 -m unittest discover -s tests` passed 65/65.
  - `openspec validate enforce-public-report-article-flow-gate --strict`
    reported the change is valid.
  - `git diff --check` completed cleanly.
- Evidence added:
  - `SKILL.md` has `Article Flow Layout Gate`, `newspaper article flow`,
    `card-wall`, and `prompt text` hard-rule language.
  - `scorecard.md` records repeated boxed cards, comparison cells, dashboard
    grids, colored panels, prompt text, and visual-script residue as hard-fail
    signals when a newspaper/article reference is selected.
  - `gate-review-artifact.md` adds `Reference Layout System` with retained
    patterns, rejected patterns, and Article Flow Layout Gate replay notes.
  - `pressure-scenarios.md` adds Newspaper Article Flow Replay cases.

## Residual Risks

- This is a local pressure test for skill wording and replay artifacts. It does
  not prove every future agent will visually inspect every report unless the
  skill is loaded and followed.
- The gate blocks silent drift from a chosen newspaper/article reference. It
  does not ban all cards or visual grids when the reference or user explicitly
  asks for them.
