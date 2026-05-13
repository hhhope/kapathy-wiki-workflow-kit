# Tasks

- [x] 1. Add official-source and 300-threshold RED tests
  - Test that the Go source-learning page records official/GitHub sources.
  - Test that the source-learning evidence records the referenced global
    Go/Rust/Java `>300` guardrail.
  - Test that the Go rule keeps generic thresholds out of the local rule body.

- [x] 2. Update Go rule and source learning
  - Add official-source guidance for context, interfaces, and layout caution.
  - Preserve the user-confirmed stack and `go tool fix` boundary.
  - Record the 300 threshold as a global reference, not Go-local ownership.

- [x] 3. Verify and record replay evidence
  - Add evaluation evidence with pressure scenarios, prior-art dedupe, replay,
    RED baseline, GREEN result, and residual risks.
  - Run targeted tests, behavior checker, wiki frontmatter checker, OpenSpec
    validation, repo health check, and diff check.
