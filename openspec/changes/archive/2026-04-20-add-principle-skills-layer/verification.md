# Verification

## RED

- Baseline commit before this change: `81e73bf^`
- `git show 81e73bf^:AGENTS.md | rg -n "High-Frequency Principles|clarify-before-acting|simplicity-first|surgical-changes|verify-before-claiming"`
- Result: no output
- `git ls-tree -r --name-only 81e73bf^ -- .codex/skills | sort | rg 'clarify-before-acting|simplicity-first|surgical-changes|verify-before-claiming'`
- Result: no output

## GREEN

- `sed -n '1,80p' AGENTS.md`
- Result confirmed the new `High-Frequency Principles` section routes to the principle layer
- `find .codex/skills -maxdepth 2 -name SKILL.md | sort`
- Result confirmed:
  - `.codex/skills/clarify-before-acting/SKILL.md`
  - `.codex/skills/simplicity-first/SKILL.md`
  - `.codex/skills/surgical-changes/SKILL.md`
  - `.codex/skills/verify-before-claiming/SKILL.md`
- `openspec validate add-principle-skills-layer`
- Result: `Change 'add-principle-skills-layer' is valid`
- Manual walkthrough evidence only: the principle layer is formally published and routed, but real multi-session behavior still needs later rollout proof.
