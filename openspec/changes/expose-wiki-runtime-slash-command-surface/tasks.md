# Tasks

## 1. Contract tests

- [x] 1.1 Add failing command-surface tests for the expected `/wiki:*` command files.
- [x] 1.2 Verify the tests fail before adding the new command files.
  <!-- 2026-05-09 — Worker B reported `python3 -m unittest tests.test_wiki_runtime_commands` failed before final boundary wiring because command coverage was incomplete for the existing status command. -->

## 2. Command surface

- [x] 2.1 Add repo-local command files for `/wiki:manifest`, `/wiki:inbox`, `/wiki:graph`, `/wiki:scorecard`, `/wiki:route`, `/wiki:context`, and `/wiki:apply`.
- [x] 2.2 Preserve `/wiki:status` and update its boundary wording if needed.
- [x] 2.3 Update README with the command list and usage boundaries.

## 3. Verification

- [x] 3.1 Run targeted unittest coverage for the wiki command surface.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed: 9 tests. -->
- [x] 3.2 Run OpenSpec strict validation for this change.
  <!-- 2026-05-09 — `openspec validate expose-wiki-runtime-slash-command-surface --strict` passed. PostHog DNS flush errors appeared after the valid result and are telemetry noise. -->
- [x] 3.3 Run `git diff --check` on touched files.
  <!-- 2026-05-09 — `git diff --check commands/wiki-status.md tests/test_wiki_runtime_commands.py tests/test_wiki_status_command.py` passed. -->

## 4. Stop condition

- [x] 4.1 Stop after the slash command surface is implemented and verified; do not add query engine, graph UI, score changes, or change queue automation in this change.
