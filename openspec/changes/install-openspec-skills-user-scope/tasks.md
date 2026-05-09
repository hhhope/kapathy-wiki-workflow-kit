## 1. Test First

- [x] 1.1 Add failing tests for OpenSpec skill source location and namespace
  guidance.
- [x] 1.2 Verify the tests fail while `.codex/skills/openspec-*` still exists.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_openspec_skill_namespace` failed because OpenSpec source files were not under `plugins/report-wiki-portfolio/skills/openspec-*` and `AGENTS.md` still referenced `.codex/skills/openspec-*`. -->

## 2. Implementation

- [x] 2.1 Move OpenSpec skill source files to
  `plugins/report-wiki-portfolio/skills/openspec-*`.
- [x] 2.2 Update repo guidance to reference `$openspec-*` user-scope skills and
  source paths.
- [x] 2.3 Install OpenSpec skills into `/home/yan/.codex/skills`.
  <!-- 2026-05-09 — copied the four OpenSpec skill source directories to `/home/yan/.codex/skills/` after confirming no user-scope `openspec-*` skills were present. -->

## 3. Evaluation

- [x] 3.1 Run targeted unit tests.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_openspec_skill_namespace tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed: 9 tests. -->
- [x] 3.2 Run real `codex app-server` `skills/list` and confirm plain
  `openspec-*` user-scope names are visible.
  <!-- 2026-05-09 — real `skills/list` returned user-scope `openspec-apply-change`, `openspec-archive-change`, `openspec-explore`, and `openspec-propose` from `/home/yan/.codex/skills`; no `report-wiki-portfolio:openspec-*` entries appeared. -->
- [x] 3.3 Add behavior replay and pressure-test evidence.
- [x] 3.4 Run `openspec validate install-openspec-skills-user-scope --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise appeared after the local valid result. -->
- [x] 3.5 Run `git diff --check` for touched repo files.
  <!-- 2026-05-09 — passed for AGENTS, OpenSpec skill sources, namespace test, and OpenSpec change files. -->
- [x] 3.6 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: dab73df fix: expose wiki runtime skills; git status showed task-related AGENTS/OpenSpec/test/OpenSpec-skill-source moves plus pre-existing unrelated dirty wiki/status/inbox/local tool paths. -->

## 4. Stop Boundary

- [x] 4.1 Stop after the OpenSpec skill namespace surface is installed and
  verified.
- [x] 4.2 Do not continue into plugin deletion, unrelated skill moves, or
  OpenSpec archive work.
