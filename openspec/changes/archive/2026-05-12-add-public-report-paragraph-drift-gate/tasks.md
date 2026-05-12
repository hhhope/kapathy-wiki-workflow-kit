## 1. Baseline

- [x] 1.1 Run a failing test that proves the current public report gate lacks
  intent, paragraph drift, and judgment ownership checks.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` failed 5/5 before implementation. -->

## 2. Public Report Gate

- [x] 2.1 Update `public-report-quality-gate` hard rules with Article Intent
  Contract, Section And Paragraph Drift Review, and Judgment Ownership Gate.
- [x] 2.2 Update scorecard and gate-review references with diagnostic drift
  scoring and persisted artifact sections.
- [x] 2.3 Update pressure scenarios with judgment and paragraph drift
  regressions.

## 3. Reviewer

- [x] 3.1 Update the public-report reviewer template with reverse outline,
  paragraph drift review, and judgment ownership checks before scoring.

## 4. OpenSpec And Verification

- [x] 4.1 Add spec deltas for public report quality gate and reviewer routing.
- [x] 4.2 Record RED/GREEN behavior evidence in `evaluation.md`.
- [x] 4.3 Run focused unit tests.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` passed 5 tests. -->
- [x] 4.4 Run full unit tests and OpenSpec validation.
  <!-- 2026-05-11 — `python3 -m unittest discover -s tests` passed 64 tests; `openspec validate --all` passed 49 items; `git diff --check` passed. -->
