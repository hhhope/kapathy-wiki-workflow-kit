# Tasks

- [x] Add OpenSpec proposal, design, spec delta, and evaluation evidence.
- [x] Update `.codex/skills/visual-agent/SKILL.md` with the image-reference
      mode ownership hard rule.
- [x] Update `.codex/skills/visual-agent/evaluation.md` with the pressure
      scenario and residual risk.
- [x] Run scoped text checks, OpenSpec validation, behavior-asset check, and
      `git diff --check`.
- [x] Commit only task-related files.

Verification note: `openspec validate enforce-visual-image-mode-ownership
--strict` passed. Scoped `git diff --check -- .codex/skills/visual-agent
openspec/changes/enforce-visual-image-mode-ownership` passed. `python3
scripts/check_behavior_assets.py` still returns non-zero for pre-existing
`initialize-llm-wiki-seed-repo/evaluation.md` gaps and the parallel
`realign-stripe-h5-redesign-sections` missing evaluation; it did not report this
change after evaluation evidence was added.
