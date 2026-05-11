## 1. Test First

- [x] 1.1 Update marketplace test to require `INSTALLED_BY_DEFAULT`.
- [x] 1.2 Verify the updated test fails against the current `AVAILABLE` policy.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace` failed because marketplace policy still used `installation: "AVAILABLE"`. -->

## 2. Implementation

- [x] 2.1 Update `.agents/plugins/marketplace.json` to use
  `policy.installation: "INSTALLED_BY_DEFAULT"`.
- [x] 2.2 Keep marketplace path, command names, and README install command
  unchanged.

## 3. Evaluation

- [x] 3.1 Run targeted marketplace and wiki command tests.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace tests.test_wiki_status_command tests.test_wiki_runtime_commands` passed: 10 tests. -->
- [x] 3.2 Validate marketplace and plugin JSON.
  <!-- 2026-05-09 — `python3 -m json.tool .agents/plugins/marketplace.json` and `python3 -m json.tool plugins/report-wiki-portfolio/.codex-plugin/plugin.json` passed. -->
- [x] 3.3 Refresh the real local Codex marketplace registration.
  <!-- 2026-05-09 — `codex plugin marketplace add .` against real HOME reported marketplace already added from this repo and refreshed the installed marketplace root. -->
- [x] 3.4 Run `openspec validate install-repo-plugin-by-default --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid local result. -->
- [x] 3.5 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for marketplace, marketplace test, and OpenSpec artifacts. -->
- [x] 3.6 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: c32f95a fix: package repo Codex plugin under marketplace path; git status showed task-related marketplace/test/OpenSpec files plus pre-existing unrelated dirty/wiki/inbox/local tool paths. -->

## 4. Stop Boundary

- [x] 4.1 Stop after default-install policy is verified.
- [x] 4.2 Do not add or modify wiki runtime command behavior.
