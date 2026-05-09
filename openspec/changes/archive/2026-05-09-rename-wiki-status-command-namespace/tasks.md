## 1. Test First

- [x] 1.1 Add/update the command test to require `/wiki:status` and reject `/report-wiki-portfolio:wiki-status`.
- [x] 1.2 Verify the test fails before implementation.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` failed because `commands/wiki-status.md` still documented `/report-wiki-portfolio:wiki-status` -->

## 2. Implementation

- [x] 2.1 Update `commands/wiki-status.md` to document `/wiki:status`.
- [x] 2.2 Update the spec delta to require `/wiki:status`.

## 3. Evaluation

- [x] 3.1 Run targeted command contract test.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` passed -->
- [x] 3.2 Run `openspec validate rename-wiki-status-command-namespace --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid result -->
- [x] 3.3 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for command, test, and OpenSpec artifacts -->
- [x] 3.4 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: c0c06c8 docs: trace wiki status slash command reanchor; dirty tree includes pre-existing unrelated paths plus this change -->

## 4. Stop Boundary

- [x] 4.1 Stop after the namespace rename is complete.
- [x] 4.2 Do not implement query, scorecard, graph UI, or change queue.
