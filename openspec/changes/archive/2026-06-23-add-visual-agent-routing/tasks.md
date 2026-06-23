# Tasks

- [x] Add OpenSpec proposal, design, spec delta, and evaluation for visual-agent routing.
- [x] Add `.codex/skills/visual-agent/SKILL.md` and skill-local evaluation evidence.
- [x] Register `visual-agent` in the repo high-frequency routing table.
- [x] Run behavior asset checks, OpenSpec validation, and scoped route checks.
- [x] Commit the scoped files and stop at the OpenSpec completion boundary.

Verification note: `openspec validate add-visual-agent-routing --strict` passed.
`python3 scripts/check_behavior_assets.py` no longer reports this change; it
still fails on pre-existing `openspec/changes/initialize-llm-wiki-seed-repo`
evaluation gaps.
