# Evaluation: add completion bridge gate

## RED Baseline

- Command:
  `python3 -m unittest tests.test_completion_bridge_gate -v`
- Initial failure:
  `ModuleNotFoundError: No module named 'scripts.completion_bridge_gate'`
- Meaning:
  the repository had no executable replay surface for checking completion
  reports that list delivery evidence but omit the user's original experiment
  or north-star question.

## GREEN Result

- Command:
  `python3 -m unittest tests.test_completion_bridge_gate -v`
- Result:
  `Ran 5 tests` / `OK`

- Command:
  `python3 scripts/completion_bridge_gate.py scripts/examples/completion_bridge_gate_replay.json`
- Result:
  `PASS: completion bridge replay record satisfies the executable contract.`

- Command:
  `openspec validate add-completion-bridge-gate --strict`
- Result:
  `Change 'add-completion-bridge-gate' is valid`

## Replay Coverage

Covered cases:

- Explicit original question required:
  - requires `delivery_result`
  - requires `original_question`
  - requires `bridge_answer`
- Delivery-only completion report:
  - fails when an original experiment question was present
- Lightweight small task:
  - passes with concise delivery evidence when no broader question was asked
- Scope boundary:
  - rejects `continue_implementation` as a completion next action
- CLI replay:
  - validates `scripts/examples/completion_bridge_gate_replay.json`

## Proof Boundary

- This is structural replay proof, not a claim that every future live answer
  will automatically satisfy the bridge without agent discipline.
- The implementation does not edit `.codex/skills/*`, `AGENTS.md`, global
  rules, relation fields, taxonomy config, or OpenSpec lifecycle state beyond
  this active change.
- The bridge does not authorize additional implementation after completed
  OpenSpec scope; it only permits report, archive review, new proposal, explicit
  user decision, or no action.
