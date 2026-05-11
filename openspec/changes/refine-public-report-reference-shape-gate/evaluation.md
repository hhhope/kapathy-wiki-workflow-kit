# Evaluation: Reference Output Shape Gate

## Pressure Scenarios

1. A newspaper-style company analysis becomes repeated cards or a dashboard-like
   comparison page without explicit user approval.
2. A reader-facing report body includes image-model or Hybrid production
   instructions.
3. A gate-review artifact records retained/rejected patterns but not the
   selected output shape or user-approved shape changes.
4. A report uses cards, grids, tables, dashboards, visual panels, or image
   prompts because the user asked for that shape; the gate must not ban it.

## RED Baseline

- Command: `python3 -m unittest tests.test_public_report_quality_gate`
- Result before implementation: failed 1/7.
- Expected failure: `Reference Output Shape Gate` missing from
  `.codex/skills/public-report-quality-gate/SKILL.md`.
- Baseline also still contained article-flow-specific hard-rule vocabulary in
  compact skill wording.

## GREEN Result

- Command: `python3 -m unittest tests.test_public_report_quality_gate`
- Result after implementation: passed 7/7.
- Validation:
  - `python3 -m unittest discover -s tests` passed 66/66.
  - `openspec validate refine-public-report-reference-shape-gate --strict`
    reported the change is valid.
  - `git diff --check` completed cleanly.
- Evidence added:
  - `SKILL.md` now uses `Reference Output Shape Gate`, `selected output shape`,
    and `explicit user approval`.
  - `SKILL.md` no longer uses `colored-panel`, `card-wall`, or
    `dashboard grid` as compact hard-rule vocabulary.
  - `scorecard.md` defines observable failures and clarifies that cards, grids,
    tables, dashboards, visual panels, and image prompts are allowed when the
    user asks for them or the reference uses them.
  - `gate-review-artifact.md` records selected output shape, retained patterns,
    rejected patterns, and user-approved shape changes.
  - `pressure-scenarios.md` keeps the original card/table drift as replay
    examples under `Reference Output Shape Replay`.

## Residual Risks

- This evidence validates local skill text and replay scenarios. It does not
  prove future agents will load the skill unless the trigger path fires.
