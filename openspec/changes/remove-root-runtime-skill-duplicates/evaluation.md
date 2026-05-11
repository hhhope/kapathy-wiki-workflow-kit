# Evaluation: Remove Root Runtime Skill Duplicates

## Pressure Scenarios

| Scenario | Expected Behavior | Evidence |
|---|---|---|
| Root/user-scope contains `wiki-*` copies | Remove those copies and keep repo-local wiki skills | Targeted tests passed |
| Root/user-scope contains `openspec-*` copies | Remove those copies and keep repo-local OpenSpec skills | Targeted tests passed |
| Repo plugin metadata registers `report-wiki-portfolio` | Remove plugin metadata and plugin skill copies | Targeted tests passed |
| Future guidance suggests root copies are optional | Tests fail because README must warn against duplicates | Targeted tests passed |

## RED Baseline

Before removal, `/home/yan/.codex/skills` contained root/user-scope duplicates
for `wiki-*` and three `openspec-*` helpers.

Before plugin cleanup, the repo also contained:

- `.agents/plugins/marketplace.json`
- `plugins/report-wiki-portfolio/.codex-plugin/plugin.json`
- `plugins/report-wiki-portfolio/skills/*`

## GREEN Result

- `/home/yan/.codex/skills` has no `wiki-*` or `openspec-*` duplicates.
- `.codex/skills/wiki-*` and `.codex/skills/openspec-*` remain present.
- `.agents/plugins/marketplace.json`,
  `plugins/report-wiki-portfolio/.codex-plugin/plugin.json`, and
  `plugins/report-wiki-portfolio/skills` were removed.
- `python3 -m unittest tests.test_openspec_skill_namespace
  tests.test_wiki_runtime_skills tests.test_wiki_status_command
  tests.test_codex_plugin_marketplace` passed: 12 tests.
- `openspec validate remove-root-runtime-skill-duplicates --strict` passed.
- `openspec validate --all` passed: 48 items, 0 failed. PostHog DNS flush
  warnings were telemetry noise after validation success.

## Behavior Replay

Input shape: the user sees `report-wiki-portfolio:openspec-explore` and duplicate
wiki skill surfaces after repo-local skills were restored.

Trigger condition: repo-owned runtime skills exist both under `.codex/skills`
and `/home/yan/.codex/skills`.

Expected route: keep repo-local skills, remove root/user-scope duplicates, and
remove plugin metadata/source copies that can reintroduce the
`report-wiki-portfolio:*` namespace. Record that neither root/user-scope
duplicate installs nor plugin skill copies should be used for these repo-owned
runtime skills.

Expected output: root/user-scope has no `wiki-*` or `openspec-*` duplicates for
this repository; plugin marketplace metadata and plugin skill copies are absent;
repo-local skill files remain present.

Residual proof boundary: file-state checks prove duplicate source removal. A
running Codex session may need reload before its already-loaded skill list
reflects the deletion.

## Residual Risks

- A currently running Codex session may need reload before its loaded skill list
  reflects deletion of root-scope duplicates and plugin metadata.
