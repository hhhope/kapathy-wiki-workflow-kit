# Tasks

- [x] 1. Capture baseline evidence that the current frontmatter precheck has
  `blocking_count: 0` but exits nonzero because of producer warnings.
- [x] 2. Inspect the five producer-warning scripts and decide whether they
  should be registered producers or whether warning-only pass semantics should
  change.
- [x] 3. Implement the minimal config or precheck change.
- [x] 4. Add regression evidence that real blocking frontmatter errors still
  fail the gate.
- [x] 5. Run wiki recovery evidence and confirm producer warnings alone no
  longer block recovery.
- [x] 6. Run OpenSpec validation and record final evidence.
