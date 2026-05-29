# Tasks

- [x] 1. Create rewrite gate baseline
  - Record the failed-draft diagnosis, revised article intent, revised content
    standard, and source-to-section map in the gate review.
  - Commit only the gate review and this task status update if needed.

- [x] 2. Rewrite account-domain H5 sections
  - Rewrite cover, group responsibility, capability map, system architecture,
    core chain, business objects, typical problems, active projects, and
    technical planning.
  - Verify required account-domain content and excluded capability groups.
  - Commit only the H5, gate review, and this task status update if needed.

- [x] 3. Rewrite AI and newcomer sections
  - Rewrite AI collaboration, AI maturity, 3-day / first-week path, 30/60/90
    path, task pool, and closing.
  - Tie AI content to account-domain engineering work.
  - Commit only the H5, gate review, and this task status update if needed.

- [x] 4. Verify visual quality and sensitive boundary
  - Run HTML parser.
  - Run required content grep.
  - Run excluded capability grep.
  - Run sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.
  - Commit only the gate review and this task status update if needed.

- [x] 5. Final local review status
  - Update gate review decision.
  - Verify report index still links to the H5.
  - Run `openspec validate rewrite-account-group-onboarding-h5-domain-depth
    --strict`.
  - Commit only final review/status files if needed.
