## 1. Change Setup

- [x] 1.1 Confirm the exact repository-level wording for "repo-local commit hook
  not adopted"
  <!-- 2026-05-06 — wording: repo-local commit hooks are not part of the default governance path; reversal requires a new OpenSpec change -->

## 2. Stable Decision

- [x] 2.1 Add the stable repo-visible decision for no repo-local commit hook
  <!-- 2026-05-06 — added wiki/adr/0030-no-repo-local-commit-hook-default.md -->
- [x] 2.2 Update repo guidance so hook assumptions are no longer implicit
  <!-- 2026-05-06 — updated repo AGENTS.md Phase 1 gate wording -->
- [x] 2.3 Define the reversal boundary for any future hook proposal
  <!-- 2026-05-06 — ADR and spec require a future reversing OpenSpec change with scope, failure mode, evidence, and rollback boundary -->

## 3. Evaluation

- [x] 3.1 Record the previous implicit/ambiguous hook state
  <!-- 2026-05-06 — evaluation.md Before Results records prior ambiguous gate state and absent core.hooksPath -->
- [x] 3.2 Record the after-change default path without hook assumptions
  <!-- 2026-05-06 — evaluation.md After Results records ADR, AGENTS, and spec delta -->
- [x] 3.3 Record residual risks if older candidate pages still mention hooks
  <!-- 2026-05-06 — evaluation.md Residual Risks keeps older hook candidate pages historical -->
