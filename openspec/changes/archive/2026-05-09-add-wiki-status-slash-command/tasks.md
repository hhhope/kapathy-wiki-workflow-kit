## 1. Change Setup

- [x] 1.1 Create proposal, design, tasks, evaluation, and spec delta artifacts.

## 2. Test First

- [x] 2.1 Add failing test for the slash command contract.
- [x] 2.2 Verify the test fails before adding the command.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` failed because .claude/commands/wiki/status.md did not exist -->

## 3. Implementation

- [x] 3.1 Add `.claude/commands/wiki/status.md`.
- [x] 3.2 Verify the command documents usage and output files.

## 4. Evaluation

- [x] 4.1 Run targeted command test.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_status_command` passed -->
- [x] 4.2 Run `openspec validate add-wiki-status-slash-command --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid result -->
- [x] 4.3 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for command, test, and OpenSpec artifacts -->
- [x] 4.4 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: 0c576c8 feat: add wiki manifest status surface; dirty tree includes pre-existing unrelated paths plus this change -->

## 5. Stop Boundary

- [x] 5.1 Stop after the slash command and validation evidence are complete.
- [x] 5.2 Do not implement query, scorecard, graph UI, or change queue.
