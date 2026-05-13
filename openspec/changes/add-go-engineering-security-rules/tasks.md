# Tasks

- [x] 1. Add OpenSpec boundary
  - Create proposal, design, tasks, and spec delta.
  - Validate the change with `openspec validate add-go-engineering-security-rules --strict`.

- [x] 2. Add compressed source learning evidence
  - Add a repo-visible wiki/ops learning note.
  - Preserve source URLs and compressed transfer decisions.
  - Do not copy article bodies.

- [x] 3. Add Go engineering/security rule
  - Add `rules/go/engineering-security.md`.
  - Include the confirmed stack convention.
  - Include `go tool fix` migration boundaries.

- [x] 4. Route the rule from repo instructions
  - Update `AGENTS.md` with a compact Go rule route.
  - Do not duplicate the full rule body in `AGENTS.md`.

- [x] 5. Verify
  - Add tests for route, stack convention, source compression, and `go tool fix`
    boundary.
  - Run targeted tests.
  - Run OpenSpec validation.
  - Record known frontmatter drift separately if checker remains non-zero.
