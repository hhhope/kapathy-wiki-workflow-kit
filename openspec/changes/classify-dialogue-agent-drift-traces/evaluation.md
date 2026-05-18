# Evaluation: classify dialogue agent drift traces

## RED Baseline

- Command:
  `python3 -m unittest tests.test_dialogue_agent_drift -v`
- Initial failure:
  `ModuleNotFoundError: No module named 'scripts.dialogue_agent_drift'`
- Additional boundary RED:
  `test_default_scan_skips_generated_medical_runtime_records` failed because
  generated `wiki-*-runs` runtime records were included in the default scan.

## GREEN Result

- Command:
  `python3 -m unittest tests.test_dialogue_agent_drift -v`
- Result:
  `Ran 9 tests in 0.360s` / `OK`

- Command:
  `openspec validate classify-dialogue-agent-drift-traces --strict`
- Result:
  `Change 'classify-dialogue-agent-drift-traces' is valid`
- Note:
  the CLI emitted non-blocking PostHog DNS flush warnings after validation.

## Candidate Replay

- Command:
  `python3 scripts/build_dialogue_agent_drift.py --root . --candidates-json /tmp/dialogue-candidates.json`
- Result summary:
  - `agent-drift`: 1
  - `supporting-example`: 1
  - `not-dialogue-drift`: 1

Replay items:

| Detail | Path | Proposed bucket | Next action |
|---|---|---|---|
| `detail-0097` | `wiki/ops/sample-disagreement-retro.md` | `supporting-example` | `no-op` |
| `detail-0108` | `wiki/ops/visual-output-routing-drift-explore-2026-05-11.md` | `agent-drift` | `openspec-candidate` |
| `detail-0081` | `wiki/ops/nirvana-weekly-intake-2026-04-13.md` | `not-dialogue-drift` | `defer-cleanup` |

## Proof Boundary

- The classifier and CLI produce review JSON only.
- They do not write wiki frontmatter, relation fields, taxonomy config, ADRs,
  AGENTS, skills, or OpenSpec lifecycle state.
- The default scan excludes generated medical runtime record directories such
  as `wiki/ops/wiki-*-runs/`; explicit candidate JSON can still replay a manual
  surgery set.
