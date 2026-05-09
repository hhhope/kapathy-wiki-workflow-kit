## 1. Test First

- [x] 1.1 Add a failing test for repo marketplace metadata and README install instructions.
- [x] 1.2 Verify the test fails before implementation.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace` failed because `.agents/plugins/marketplace.json` did not exist and README did not document `codex plugin marketplace add .` -->

## 2. Implementation

- [x] 2.1 Add `.agents/plugins/marketplace.json`.
- [x] 2.2 Update `README.md` with Codex plugin install and `/wiki:status` usage.

## 3. Evaluation

- [x] 3.1 Run targeted marketplace/install test.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace tests.test_wiki_status_command` passed -->
- [x] 3.2 Run `codex plugin marketplace add .` with a temporary HOME to verify CLI acceptance without changing the user's global config.
  <!-- 2026-05-09 — `HOME=/tmp/codex-marketplace-install-check codex plugin marketplace add .` added marketplace `report-wiki-portfolio` from this repo -->
- [x] 3.3 Run `openspec validate add-repo-plugin-marketplace-install-path --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid result -->
- [x] 3.4 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for marketplace, README, tests, and OpenSpec artifacts -->
- [x] 3.5 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: 6afd7ab feat: rename wiki status slash command; dirty tree includes pre-existing unrelated paths plus this change -->

## 4. Stop Boundary

- [x] 4.1 Stop after the repo plugin discovery/install path is documented and verified.
- [x] 4.2 Do not implement query, scorecard, graph UI, or change queue.
