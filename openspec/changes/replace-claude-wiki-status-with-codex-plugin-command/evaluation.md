# Evaluation

## RED Baseline

The previous implementation created a Claude command:

- `.claude/commands/wiki/status.md` existed.
- `.codex-plugin/plugin.json` did not exist.
- `commands/wiki-status.md` did not exist.

RED test result:

- `python3 -m unittest tests.test_wiki_status_command` failed because the
  Codex plugin manifest was missing and the Claude-only command remained.

## GREEN Evidence

- Added `.codex-plugin/plugin.json` with plugin name
  `report-wiki-portfolio`.
- Added `commands/wiki-status.md` documenting invocation as
  `/report-wiki-portfolio:wiki-status`.
- Removed `.claude/commands/wiki/status.md`.
- `python3 -m unittest tests.test_wiki_status_command` passed.
- `python3 -m json.tool .codex-plugin/plugin.json` passed.
- `openspec validate replace-claude-wiki-status-with-codex-plugin-command --strict`
  passed.
- `git diff --check` passed for touched files.

The OpenSpec command printed PostHog DNS flush errors after the valid result;
those are telemetry network noise and not validation failures.

## Residual Risks

- Repo-local Codex commands require the repo plugin to be available to the
  Codex environment; plain root `.codex/prompts` lookup is not the supported
  path for this need.
- The actual TUI slash picker cannot be exercised non-interactively here; the
  implementation is validated against the local Codex plugin command shape and
  installed plugin examples.
