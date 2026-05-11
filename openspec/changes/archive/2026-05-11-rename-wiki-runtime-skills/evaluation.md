# Evaluation: Rename Wiki Runtime Skills

## Pressure Scenarios

| Scenario | Expected Behavior | Evidence |
|---|---|---|
| User looks for wiki runtime entrypoints in current Codex | `skills/list` exposes plain `wiki-*` user-scope names | Real app-server GREEN result below |
| Repo-local skill source would still carry the project namespace | Do not publish wiki runtime skills under repo `.codex/skills` | Design records current trusted-project behavior |
| User invokes `$wiki-query` expecting retrieval help | Skill uses explicit route/context/text-search evidence only | `wiki-query/SKILL.md` rejects embeddings and hidden ranking |
| User invokes `$wiki-apply` or `$wiki-queue` | Skill summarizes suggestions or preview items only | All skill files include OpenSpec and queue execution boundaries |

## RED Baseline

- `python3 -m unittest tests.test_wiki_runtime_skills` failed before
  implementation because `plugins/report-wiki-portfolio/skills/wiki-*` did not
  exist.
- The same RED run failed because README still documented the wiki runtime as a
  repo-local Codex plugin with `/wiki:*` commands.
- Real `codex app-server` `skills/list` before implementation showed existing
  repo-local skills as `report-wiki-portfolio:*`, including
  `report-wiki-portfolio:openspec-explore`.

## GREEN Result

- `python3 -m unittest tests.test_wiki_runtime_skills
  tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed
  after adding the skill source and README updates.
- The repo skill source files use `name: wiki-*` and point to the matching
  `plugins/report-wiki-portfolio/commands/wiki-*.md` command contracts.
- The installed user-scope skills were verified with real `codex app-server`
  `skills/list`:
  - `wiki-apply`
  - `wiki-context`
  - `wiki-graph`
  - `wiki-inbox`
  - `wiki-manifest`
  - `wiki-query`
  - `wiki-queue`
  - `wiki-route`
  - `wiki-scorecard`
  - `wiki-status`

## Behavior Replay

Input shape: the user asks for the ugly `report-wiki-portfolio:` prefix to be
removed and wants wiki skills named in the `wiki-*` style.

Trigger condition: current Codex exposes user skills by plain skill name, while
trusted project-local skills can be displayed with the project namespace.

Expected route: install the wiki runtime entrypoints as user-scope skills and
keep repo-local command contracts as source evidence.

Expected output: the runtime skill list contains `wiki-status` through
`wiki-queue` with `scope: "user"` and paths under `/home/yan/.codex/skills`.

Non-promotion boundary: do not add `.codex/skills/wiki-*` in this repo, because
that would risk `report-wiki-portfolio:wiki-*` duplicates in the trusted
project.

Residual proof boundary: this verifies Codex app-server skill discovery. It
does not prove future custom slash command support, and it does not remove or
archive the earlier plugin command contracts.

## Residual Risks

- The installed user-scope skills are machine-local state under
  `/home/yan/.codex/skills`; repo source remains under
  `plugins/report-wiki-portfolio/skills` for reinstall or review.
- Existing plugin files still exist as command contracts and may need a later
  cleanup change if the repo decides to retire plugin packaging entirely.
