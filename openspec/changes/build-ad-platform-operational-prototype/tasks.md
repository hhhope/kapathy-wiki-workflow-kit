# Tasks

- [x] 1. Add OpenSpec boundary
  - Create proposal, design, tasks, and spec delta.
  - Validate the change with `openspec validate build-ad-platform-operational-prototype --strict`.

- [x] 2. Add RED contract test
  - Create `tests/test_ad_platform_operational_prototype.py`.
  - Verify it fails before the prototype and gate review exist.

- [x] 3. Build standalone operational prototype
  - Create `wiki/reports/ad-platform-operational-prototype.html`.
  - Implement required modules, mock state, operations, architecture surfaces,
    sequence surfaces, and reset/persistence behavior.

- [x] 4. Add report gate review
  - Create `wiki/ops/ad-platform-operational-prototype-report-gate-review.md`.
  - Record intent correction, proof boundary, and verification status.

- [x] 5. Verify and record completion
  - Run unit/static tests.
  - Run behavior asset check.
  - Run wiki frontmatter check and record unrelated legacy drift separately.
  - Run browser interaction verification.
  - Update this task list and the gate review evidence.
