## Pressure Scenarios

Scenario 1: The agent relies on repo-local `openspec-*` skills to create or continue a change from the current Codex environment.

Scenario 2: The agent explains how to trigger OpenSpec actions and whether the CLI is available in this repository.

## RED Baseline

- `openspec-propose` told the user to run `/opsx:apply` and relied on `AskUserQuestion` and `TodoWrite`, which do not exist in this Codex runtime.
- `openspec-apply-change` relied on `AskUserQuestion` and `/opsx:apply <other>`.
- `openspec-archive-change` relied on `AskUserQuestion` and a nonexistent `Task tool`.
- `openspec-explore` included `/opsx:explore` as an example entrypoint even though the repo uses normal user requests plus the real OpenSpec CLI.

Evidence came from:

- `rg -n "AskUserQuestion|TodoWrite|Task tool|/opsx:" .codex/skills/openspec-*`

## GREEN Result

- Rewrote all four repo-local `openspec-*` skills into compact CLI-first guides.
- Removed references to `AskUserQuestion`, `TodoWrite`, `Task tool`, and `/opsx:*`.
- Kept the real OpenSpec flow explicit: `openspec new change`, `openspec list --json`, `openspec status --change ... --json`, and `openspec instructions apply --change ... --json`.
- Preserved the repo constraint that workflow-level work still needs a real OpenSpec change and local artifact context.

Verification used:

- `rg -n "AskUserQuestion|TodoWrite|Task tool|/opsx:" .codex/skills/openspec-*` → no matches
- `python3 -m unittest discover -s tests` → 19 tests passed
- `openspec status --change improve-installation-entry-guides --json` → all artifacts done
- `python3 scripts/verify_wiki_workflow_kit.py --help` → mode-aware CLI available

## Residual Risks

- Cursor and Claude adapters are still documented boundaries rather than full generated install outputs.
- The referenced Feishu article body remains unavailable in this environment and may require a later sync pass.
