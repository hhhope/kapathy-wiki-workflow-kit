# Tasks

- [ ] 1. Capture baseline evidence that the current frontmatter precheck has
  `blocking_count: 0` but exits nonzero because of producer warnings.
- [ ] 2. Inspect the five producer-warning scripts and decide whether they
  should be registered producers or whether warning-only pass semantics should
  change.
- [ ] 3. Implement the minimal config or precheck change.
- [ ] 4. Add regression evidence that real blocking frontmatter errors still
  fail the gate.
- [ ] 5. Run wiki recovery evidence and confirm producer warnings alone no
  longer block recovery.
- [ ] 6. Run OpenSpec validation and record final evidence.
