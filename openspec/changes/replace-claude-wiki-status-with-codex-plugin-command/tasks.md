## 1. Test First

- [x] 1.1 Update the command contract test to require a repo-local Codex plugin command.
- [x] 1.2 Verify the test fails before implementation.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` failed because `.codex-plugin/plugin.json` did not exist and `.claude/commands/wiki/status.md` still existed -->

## 2. Implementation

- [x] 2.1 Add `.codex-plugin/plugin.json`.
- [x] 2.2 Add `commands/wiki-status.md`.
- [x] 2.3 Remove `.claude/commands/wiki/status.md`.

## 3. Evaluation

- [x] 3.1 Run targeted command contract test.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` passed -->
- [x] 3.2 Run `openspec validate replace-claude-wiki-status-with-codex-plugin-command --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid result -->
- [x] 3.3 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for plugin, command, test, deleted Claude command, and OpenSpec artifacts -->
- [x] 3.4 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: 73833d1 feat: add wiki status slash command; dirty tree includes pre-existing unrelated paths plus this correction -->

## 4. Stop Boundary

- [x] 4.1 Stop after the repo-level Codex command correction is complete.
- [x] 4.2 Do not implement query, scorecard, graph UI, or change queue.
