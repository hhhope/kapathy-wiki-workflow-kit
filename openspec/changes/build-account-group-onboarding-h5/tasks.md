# Tasks

- [x] 1. Add public-output gate review
  - Create `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`.
  - Record reader intent, selected output shape, evidence map,
    sensitive-information boundary, section drift review, and pending
    verification log.
  - Commit only the gate review file and this task status update if needed.

- [x] 2. Build H5 skeleton and visual system
  - Create `wiki/reports/account-group-onboarding-h5.html`.
  - Include the complete HTML document shell, inline CSS, responsive layout
    rules, and fourteen semantic section IDs.
  - Run a basic HTML parse check.
  - Commit only the H5 skeleton and this task status update if needed.

- [ ] 3. Add account-domain content
  - Fill the cover, group, capability map, business chain, business objects,
    typical problems, active projects, and technical planning sections.
  - Verify required account-domain phrases are present.
  - Update the gate review verification log.
  - Commit only the H5, gate review, and this task status update if needed.

- [ ] 4. Add AI collaboration and newcomer path content
  - Fill the AI collaboration, AI maturity, first-week, 30/60/90, task-pool,
    and closing sections.
  - Verify required AI and onboarding phrases are present.
  - Update the gate review verification log.
  - Commit only the H5, gate review, and this task status update if needed.

- [ ] 5. Verify sensitive-info and visual quality
  - Run sensitive-info grep against the reader-facing H5.
  - Run source-to-screen coverage check against the gate review.
  - Run HTML parse check after final content.
  - Take desktop and mobile screenshots and inspect them.
  - Update the gate review verification log with evidence.
  - Commit only the gate review and this task status update if needed.

- [ ] 6. Add reports index entry
  - Update `wiki/reports/index.md` with one entry for the H5.
  - Verify the link path exists.
  - Add the final local-review decision to the gate review.
  - Run `git diff --check` on the H5, index, and gate review.
  - Commit only the index, gate review, and this task status update if needed.
