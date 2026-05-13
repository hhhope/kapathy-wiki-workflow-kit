# Tasks

- [x] 1. Add prior-art/common-rule dedupe gate first
  - Extend the behavior-asset checker/config to require dedupe evidence for new
    behavior-asset changes.
  - Add RED/GREEN tests for missing and present prior-art evidence.

- [x] 2. Normalize Go engineering/security rule ownership
  - Keep Go-specific stack, Gin/GORM/Redis, concurrency, security, and
    `go tool fix` boundaries.
  - Reference global/common guidance for generic file-size, git, testing, and
    behavior-asset gates instead of duplicating thresholds or workflows.

- [x] 3. Verify behavior replay and rule tests
  - Add/update tests for the Go rule boundary.
  - Add evaluation evidence with pressure scenarios, RED baseline, GREEN result,
    replay fields, and residual risks.
  - Run targeted tests, behavior-asset checker, OpenSpec validation, and diff
    checks.
