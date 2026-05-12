## 1. Baseline

- [x] 1.1 Add a failing focused test proving the current gate lacks generic,
  non-subjective Reference Output Shape wording.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` failed 1/7 before implementation; missing `Reference Output Shape Gate`. -->

## 2. Skill And References

- [x] 2.1 Replace article-flow-specific compact skill wording with the
  Reference Output Shape Gate.
- [x] 2.2 Update scorecard and gate-review references with selected-shape,
  approval, and observable-failure fields.
- [x] 2.3 Update pressure scenarios so incident examples remain replay cases,
  not core hard-rule vocabulary.

## 3. Evaluation

- [x] 3.1 Record RED/GREEN evidence in `evaluation.md`.
- [x] 3.2 Run focused unit tests.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_public_report_quality_gate` passed 7 tests. -->
- [x] 3.3 Run full tests, OpenSpec validation, and diff checks.
  <!-- 2026-05-11 — `python3 -m unittest discover -s tests` passed 66 tests; `openspec validate refine-public-report-reference-shape-gate --strict` valid; `git diff --check` clean. -->
