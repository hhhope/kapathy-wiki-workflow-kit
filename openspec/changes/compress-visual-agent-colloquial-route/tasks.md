# Tasks

- [x] Add OpenSpec proposal, design, spec deltas, and evaluation for compact colloquial visual routing.
- [x] Compress `visual-agent/SKILL.md` into a short runtime card.
- [x] Generalize AGENTS and public-report visual wording from fixed trigger examples to colloquial visual-request classes.
- [x] Update evaluation evidence for skill compactness and colloquial trigger replay.
- [x] Run scoped RED/GREEN checks, behavior asset checks, and OpenSpec validation.
- [x] Commit scoped task-related files and stop at the OpenSpec completion boundary.

Verification note: `wc -w .codex/skills/visual-agent/SKILL.md` dropped from
917 to 410. Scoped `rg` checks confirmed colloquial trigger wording and removed
the old thick runtime headings. `openspec validate
compress-visual-agent-colloquial-route --strict` passed. `git diff --check`
passed. `python3 scripts/check_behavior_assets.py` still fails only on
pre-existing `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`
evaluation gaps.
