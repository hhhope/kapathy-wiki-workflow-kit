## 1. Baseline

- [x] 1.1 Add a failing focused test proving the current gate lacks article-flow
  layout drift checks and replay scenarios.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` failed 1/6 before implementation; missing `Article Flow Layout Gate`. -->

## 2. Skill Gate

- [x] 2.1 Update `public-report-quality-gate` hard rules with an Article Flow
  Layout Gate.
- [x] 2.2 Update scorecard and gate-review reference artifacts with layout
  system fields and failure conditions.
- [x] 2.3 Update pressure scenarios with replay cases for card-wall/table drift
  against a newspaper reference.

## 3. OpenSpec And Evaluation

- [x] 3.1 Add spec deltas for the public report quality gate.
- [x] 3.2 Record RED/GREEN behavior evidence in `evaluation.md`.
- [x] 3.3 Run focused unit tests.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` passed 6 tests. -->
- [x] 3.4 Run OpenSpec validation and diff checks.
  <!-- 2026-05-11 — `python3 -m unittest discover -s tests` passed 65 tests; `openspec validate enforce-public-report-article-flow-gate --strict` valid; `git diff --check` clean. -->
