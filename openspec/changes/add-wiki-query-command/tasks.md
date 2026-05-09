# Tasks

## 1. Contract tests

- [x] 1.1 Add failing command contract coverage for `/wiki:query`.
- [x] 1.2 Verify the test fails before adding the command.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_runtime_commands` failed because `commands/wiki-query.md` did not exist. -->

## 2. Command and docs

- [x] 2.1 Add `commands/wiki-query.md`.
- [x] 2.2 Update README command list with `/wiki:query`.
- [x] 2.3 Ensure `/wiki:query` states proof boundaries and OpenSpec non-mutation boundaries.

## 3. Verification

- [x] 3.1 Run targeted unittest coverage.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed: 10 tests. -->
- [x] 3.2 Run OpenSpec strict validation.
  <!-- 2026-05-09 — `openspec validate add-wiki-query-command --strict` passed. PostHog DNS flush errors appeared after the valid result and are telemetry noise. -->
- [x] 3.3 Run `git diff --check` on touched files.
  <!-- 2026-05-09 — `git diff --check` passed. -->

## 4. Stop condition

- [x] 4.1 Stop after the bounded query command is implemented; do not add vector search, embeddings, graph UI, or change queue automation in this change.
