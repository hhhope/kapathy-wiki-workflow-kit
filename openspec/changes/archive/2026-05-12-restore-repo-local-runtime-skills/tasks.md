# Tasks

- [x] 1.1 Add RED tests that require OpenSpec and wiki runtime skills under
  `.codex/skills`.
- [x] 1.2 Verify the tests fail before restoring repo-local runtime skills.
  <!-- 2026-05-11 — targeted unittest run failed because repo-local OpenSpec/wiki runtime skill files were absent and README/AGENTS still referenced plugin/user-scope paths. -->
- [x] 2.1 Restore `.codex/skills/openspec-*` from the existing source copies.
- [x] 2.2 Restore `.codex/skills/wiki-*` from the existing source copies.
- [x] 2.3 Update README and AGENTS routing to describe repo-local skill
  ownership and not plugin/user-scope installation as the supported path.
- [x] 2.4 Update OpenSpec specs to reverse the user-scope/plugin dependency.
- [x] 2.5 Record skill evaluation evidence for the routing behavior.
- [x] 3.1 Run targeted skill namespace and wiki runtime tests.
  <!-- 2026-05-11 — `python3 -m unittest tests.test_openspec_skill_namespace tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed: 9 tests. -->
- [x] 3.2 Run OpenSpec validation for this change and all specs.
  <!-- 2026-05-11 — `openspec validate restore-repo-local-runtime-skills --strict` passed; `openspec validate --all` passed: 47 items, 0 failed. PostHog DNS flush warnings were telemetry noise after successful validation. -->
- [x] 3.3 Inspect git status and commit only task-related files.
  <!-- 2026-05-11 — git status inspected. Task-related files are AGENTS/README, repo-local openspec/wiki skills, OpenSpec specs/change files, and targeted tests. Pre-existing dirty wiki/report/inbox/local-tool paths remain unstaged. -->
