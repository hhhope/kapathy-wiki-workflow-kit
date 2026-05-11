## 1. Test First

- [x] 1.1 Update the marketplace contract test to require a loader-compatible
  repo-local plugin subdirectory path.
- [x] 1.2 Verify the updated test fails against the current metadata.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace` first failed because `.agents/plugins/marketplace.json` still used `source.path: "."`; after loader evidence showed `./` and `./.` are also rejected for the marketplace root, the final RED failed because metadata used `source.path: "./."` and README still pointed at root `commands/wiki-status.md`. -->

## 2. Implementation

- [x] 2.1 Package the plugin under `plugins/report-wiki-portfolio/`.
- [x] 2.2 Update `.agents/plugins/marketplace.json` to use
  `source.path: "./plugins/report-wiki-portfolio"`.
- [x] 2.3 Keep the README install command unchanged as
  `codex plugin marketplace add .`.

## 3. Evaluation

- [x] 3.1 Run targeted marketplace and wiki command tests.
  <!-- 2026-05-09 — `python3 -m unittest tests.test_codex_plugin_marketplace tests.test_wiki_status_command tests.test_wiki_runtime_commands` passed: 10 tests. -->
- [x] 3.2 Validate marketplace JSON and plugin JSON parse cleanly.
  <!-- 2026-05-09 — `python3 -m json.tool .agents/plugins/marketplace.json` and `python3 -m json.tool plugins/report-wiki-portfolio/.codex-plugin/plugin.json` passed. -->
- [x] 3.3 Run `openspec validate fix-repo-plugin-local-source-path --strict`.
  <!-- 2026-05-09 — passed; PostHog DNS flush noise ignored after valid local result. -->
- [x] 3.4 Check current Codex log evidence for the old loader rejection and
  record the fix boundary.
  <!-- 2026-05-09 — `~/.codex/log/codex-tui.log` showed `path: "."` rejected because local paths must start with `./`, `path: "./"` rejected as empty, and `path: "./."` rejected as outside the marketplace root. After switching to `./plugins/report-wiki-portfolio`, recent log tail showed no new `skipping marketplace plugin` warning for this plugin. -->
- [x] 3.5 Run `codex plugin marketplace add .` with a temporary HOME.
  <!-- 2026-05-09 — `env HOME=/tmp/codex-marketplace-subdir-check-20260509 codex plugin marketplace add .` added marketplace `report-wiki-portfolio` from this repo; helper-binary warning was expected for temporary `/tmp` HOME. -->
- [x] 3.6 Run `git diff --check` for touched files.
  <!-- 2026-05-09 — passed for marketplace, README, tests, plugin package, and OpenSpec artifacts. -->
- [x] 3.7 Verify git status/log before commit or completion claim.
  <!-- 2026-05-09 — git log -1: 0949471 chore: archive blocked wiki queue sources; git status showed task-related marketplace, README, tests, plugin package, and OpenSpec change files plus pre-existing unrelated dirty/wiki/inbox/local tool paths. -->

## 4. Stop Boundary

- [x] 4.1 Stop after the marketplace path repair is verified.
- [x] 4.2 Do not add or modify wiki runtime command behavior.
