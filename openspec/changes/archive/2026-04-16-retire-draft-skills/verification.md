# Verification

## RED

- Baseline commit: `243d9f9`
- `git ls-tree -r --name-only 243d9f9 -- skills-drafts .codex/skills/material-collaboration-defaults AGENTS.md wiki/adr/index.md`
- Result showed:
  - `skills-drafts/material-collaboration-defaults/SKILL.md`
  - `skills-drafts/meeting-note-output/SKILL.md`
  - `skills-drafts/meeting-note-output/references/meeting-note-format-example.md`
  - no `.codex/skills/material-collaboration-defaults/...`

## GREEN

- `find .codex/skills/material-collaboration-defaults -maxdepth 2 -type f | sort`
- Result:
  - `.codex/skills/material-collaboration-defaults/SKILL.md`
- `find skills-drafts -name SKILL.md | sort`
- Result: no output
- `rg -n "draft space only|promoted into \\.codex/skills|promoted or retired|material-collaboration-defaults" AGENTS.md wiki/adr openspec/changes/retire-draft-skills -g '*.md'`
- Result confirmed:
  - `AGENTS.md` points material-processing workflow to `.codex/skills/material-collaboration-defaults/SKILL.md`
  - repo guidance says workflow changes cannot stop with an active draft `SKILL.md`
  - ADR-0007 records the promotion-or-retire rule
- `openspec validate retire-draft-skills`
- Result: `Change 'retire-draft-skills' is valid`
