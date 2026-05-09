# Evaluation: Install OpenSpec Skills User Scope

## Pressure Scenarios

| Scenario | Expected Behavior | Evidence |
|---|---|---|
| User invokes `$openspec-explore` in this repo | Codex lists `openspec-explore` as a user-scope skill without `report-wiki-portfolio:` | Real app-server GREEN result below |
| Repo still has `.codex/skills/openspec-explore` | Test fails because the repo would still expose a namespaced duplicate | `tests.test_openspec_skill_namespace` |
| Contributor needs to audit the skill body | Source remains in repo under `plugins/report-wiki-portfolio/skills/openspec-*` | Source location test and AGENTS table |
| Plugin marketplace is disabled or absent | OpenSpec skill naming should be unaffected | Prior isolation run showed plugin absence still produced namespaced repo-local names |

## RED Baseline

- `python3 -m unittest tests.test_openspec_skill_namespace` failed before
  implementation because OpenSpec skill source files were absent from
  `plugins/report-wiki-portfolio/skills/openspec-*`.
- The same RED run failed because `AGENTS.md` still referenced
  `.codex/skills/openspec-*` repo-local paths.
- Before this change, real `skills/list` showed
  `report-wiki-portfolio:openspec-explore` from
  `.codex/skills/openspec-explore/SKILL.md`.

## GREEN Result

- `python3 -m unittest tests.test_openspec_skill_namespace` passed after moving
  source files and updating `AGENTS.md`.
- Real `codex app-server` `skills/list` returned:
  - `openspec-apply-change` with `scope: "user"`
  - `openspec-archive-change` with `scope: "user"`
  - `openspec-explore` with `scope: "user"`
  - `openspec-propose` with `scope: "user"`
- The returned paths were all under `/home/yan/.codex/skills`.
- No `report-wiki-portfolio:openspec-*` entries were returned.

## Behavior Replay

Input shape: the user sees `$report-wiki-portfolio:openspec-explore` and asks
to remove the `report-wiki-portfolio:` prefix.

Trigger condition: OpenSpec helper skills are loaded from repo-local
`.codex/skills/openspec-*` in a trusted project.

Expected route: keep source copies in the repo, install the skills under
`/home/yan/.codex/skills`, and remove repo-local OpenSpec skill directories so
the namespaced duplicate cannot be listed.

Expected output: `skills/list` shows plain user-scope `openspec-*` names.

Non-promotion boundary: do not rename `PROJECT.md`, and do not change plugin
metadata to solve a repo-local skill namespace issue.

Residual proof boundary: this verifies skill discovery in Codex app-server. A
currently open Codex TUI session may need restart or reload before its cached
skill list reflects the new user-scope install.

## Residual Risks

- The user-scope install is local machine state. Repo source remains available
  for reinstall under `plugins/report-wiki-portfolio/skills/openspec-*`.
- Existing historical wiki and archived OpenSpec pages still mention earlier
  repo-local skill paths; those are not runtime routing records and were left
  unchanged.
