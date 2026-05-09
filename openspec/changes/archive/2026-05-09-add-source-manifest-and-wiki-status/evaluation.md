## RED Baseline

Before this change:

- No `scripts/build_wiki_status.py` exists.
- No `wiki/status/manifest.json` exists.
- No `wiki/status/wiki-status.md` exists.
- The repository cannot compute pending inbox files versus represented source
  records in one command.
- The repository cannot summarize active versus complete OpenSpec changes in a
  wiki status surface.

## Planned RED Tests

- A temp repo with two inbox files and one source page referencing one inbox
  file should mark the other inbox file as pending.
- A temp repo with one partial OpenSpec tasks file and one all-complete tasks
  file should report one active change and one complete change.

## GREEN Evidence

RED result:

- `python3 -m unittest tests.test_wiki_status` initially failed with
  `ModuleNotFoundError: No module named 'scripts.build_wiki_status'`, confirming
  the tests exercised missing behavior before implementation.

Targeted unit test result:

- `python3 -m unittest tests.test_wiki_status` passes with 4 tests.

Generated artifact readback:

- `python3 scripts/build_wiki_status.py` writes:
  - `wiki/status/manifest.json`
  - `wiki/status/wiki-status.md`
- `python3 -m json.tool wiki/status/manifest.json` parses successfully.
- `wiki/status/wiki-status.md` currently reports:
  - 168 wiki pages
  - 8 source records
  - 12 inbox files
  - 6 pending inbox files
  - 1 active OpenSpec change
  - 6 complete active-directory OpenSpec changes

OpenSpec strict validation:

- `openspec validate add-source-manifest-and-wiki-status --strict` passed.
- The command printed PostHog DNS flush errors after the valid result; those are
  telemetry network noise and not validation failures.

Scope readback:

- Implemented `scripts/build_wiki_status.py`.
- Added tests in `tests/test_wiki_status.py`.
- Generated `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
- Added `wiki/status/index.md` and `wiki/index.md` navigation.
- Did not implement query, scorecard calibration, graph UI, or change queue.

## Residual Risks

- The first manifest is file-level, not semantic.
- Hashes prove file content identity, not correctness.
- The status report is generated on demand; no hook updates it automatically.
- Pending inbox files can include local junk until later ignore rules are
  formalized.
