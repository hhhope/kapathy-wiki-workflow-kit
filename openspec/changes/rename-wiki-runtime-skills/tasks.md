## 1. Test First

- [x] 1.1 Add failing tests for the expected `wiki-*` skill source files and
  README skill surface.
- [x] 1.2 Verify the tests fail before the skill source exists.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_runtime_skills` failed because `plugins/report-wiki-portfolio/skills/wiki-*` source files were absent and README still documented `/wiki:*` plugin commands. -->

## 2. Implementation

- [x] 2.1 Add installable wiki runtime skill source files named `wiki-*`.
- [x] 2.2 Update README documentation from `/wiki:*` slash commands to
  `$wiki-*` skills.
- [x] 2.3 Install the `wiki-*` skills into the user Codex skill directory.
  <!-- 2026-05-09 — copied `plugins/report-wiki-portfolio/skills/wiki-*` to `/home/yan/.codex/skills/` after confirming no existing user-scope `wiki-*` skills were present. -->

## 3. Evaluation

- [x] 3.1 Run targeted unit tests.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_codex_plugin_marketplace tests.test_wiki_runtime_commands` passed: 13 tests. Also ran wiki status/graph/scorecard/queue helper tests: 9 tests passed. -->
- [x] 3.2 Run real `codex app-server` `skills/list` and confirm plain
  `wiki-*` user-scope names are visible.
  <!-- 2026-05-09 — real `skills/list` returned user-scope `wiki-apply`, `wiki-context`, `wiki-graph`, `wiki-inbox`, `wiki-manifest`, `wiki-query`, `wiki-queue`, `wiki-route`, `wiki-scorecard`, and `wiki-status` from `/home/yan/.codex/skills`, with no `report-wiki-portfolio:` prefix. -->
- [x] 3.3 Add behavior replay and pressure-test evidence.
- [x] 3.4 Run `openspec validate rename-wiki-runtime-skills --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise appeared after the local valid result. -->
- [x] 3.5 Run `git diff --check` for touched repo files.
  <!-- 2026-05-09 — passed for README, wiki runtime skill source, tests, and OpenSpec change files. -->
- [x] 3.6 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: b16f21c docs: record Codex slash command runtime limit; git status showed task-related README/tests/OpenSpec/skill-source files plus pre-existing unrelated dirty wiki/status/inbox/local tool paths. -->

## 4. Stop Boundary

- [x] 4.1 Stop after the skill surface is installed and verified.
- [x] 4.2 Do not continue into plugin replacement, command deletion, runtime
  script changes, or OpenSpec archive work.
