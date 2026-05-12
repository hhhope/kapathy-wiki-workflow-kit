# Tasks

- [x] 1.1 Confirm duplicate root/user-scope skill paths.
  <!-- 2026-05-11 — root/user-scope had `wiki-*` and `openspec-*` copies while repo-local `.codex/skills` also had the same runtime surface. -->
- [x] 1.2 Remove root/user-scope duplicates while keeping repo-local skills.
  <!-- 2026-05-11 — removed `/home/yan/.codex/skills/wiki-*` and `/home/yan/.codex/skills/openspec-*`; repo-local `.codex/skills/wiki-*` and `.codex/skills/openspec-*` remain. -->
- [x] 1.3 Remove obsolete repo plugin marketplace metadata and plugin skill copies.
  <!-- 2026-05-11 — removed `.agents/plugins/marketplace.json`, `plugins/report-wiki-portfolio/.codex-plugin/plugin.json`, and `plugins/report-wiki-portfolio/skills/*`. Command contracts under `plugins/report-wiki-portfolio/commands` remain because repo-local skills reference them. -->
- [x] 1.4 Update README/spec/tests to prevent root/user-scope duplicate reinstall and plugin namespace reintroduction.
- [x] 1.5 Run targeted tests and OpenSpec validation.
  <!-- 2026-05-11 — targeted namespace/runtime tests passed: 12 tests. `openspec validate remove-root-runtime-skill-duplicates --strict` passed. `openspec validate --all` passed: 48 items, 0 failed. PostHog DNS flush warnings were telemetry noise after validation success. -->
- [x] 1.6 Inspect git status and commit task-related repo changes.
  <!-- 2026-05-11 — git status inspected. Task-related changes are plugin metadata/skill removals, README/spec/test updates, and the OpenSpec change. Pre-existing dirty wiki/report/inbox/local-tool paths remain unstaged. -->
