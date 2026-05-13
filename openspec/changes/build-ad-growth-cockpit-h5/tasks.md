# Tasks

- [x] 1. Add H5 contract test
  - Create `tests/test_ad_growth_cockpit_h5.py`.
  - Verify the test fails before the HTML and gate review files exist.
  - Commit only the test file.

- [x] 2. Build standalone H5 prototype
  - Create `wiki/reports/ad-growth-cockpit-h5.html`.
  - Include the five required sections, navigation, KPI jumps, view toggles,
    alert expansion, and review CTA behavior.
  - Commit only the H5 file.

- [x] 3. Add public output gate review
  - Create `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md`.
  - Use valid wiki frontmatter for an ops report-quality artifact.
  - Run wiki frontmatter validation and keep any unrelated legacy drift separate.
  - Commit only the gate review file and task status update if needed.

- [x] 4. Verify prototype
  - Run `python3 -m unittest tests.test_ad_growth_cockpit_h5 tests.test_public_report_quality_gate -v`.
  - Run `python3 scripts/check_behavior_assets.py`.
  - Run `git diff --check`.
  - Verify the HTML opens and the prototype interactions work at desktop and
    mobile widths.
