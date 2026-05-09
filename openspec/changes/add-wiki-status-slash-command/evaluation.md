## RED Baseline

Before this change:

- `.claude/commands/wiki/status.md` does not exist.
- There is no slash command contract for refreshing wiki status.

## Planned RED Test

- A test should assert that `.claude/commands/wiki/status.md` exists and
  includes:
  - `/wiki:status`
  - `python3 scripts/build_wiki_status.py`
  - `wiki/status/manifest.json`
  - `wiki/status/wiki-status.md`

## GREEN Evidence

RED result:

- `python3 -m unittest tests.test_wiki_status_command` failed because
  `.claude/commands/wiki/status.md` did not exist.

Targeted command test:

- `python3 -m unittest tests.test_wiki_status_command` passed.

OpenSpec strict validation:

- `openspec validate add-wiki-status-slash-command --strict` passed.
- The command printed PostHog DNS flush errors after the valid result; those are
  telemetry network noise and not validation failures.

Scope readback:

- Added `.claude/commands/wiki/status.md`.
- Added `tests/test_wiki_status_command.py`.
- Did not implement query, scorecard calibration, graph UI, or change queue.
- Did not stage existing untracked `.claude/commands/opsx/*` files.

## Residual Risks

- This command is a Claude command surface. Codex skill routing still uses skill
  invocation, not Claude slash commands.
- The command refreshes generated artifacts on demand; it is not an automatic
  hook.
