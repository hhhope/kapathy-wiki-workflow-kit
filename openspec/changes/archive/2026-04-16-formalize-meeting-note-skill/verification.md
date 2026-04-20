## Verification

### RED Evidence

Baseline commit: `005dcff` (`spec: formalize meeting-note skill publication`)

Command:

```bash
git ls-tree -r --name-only 005dcff -- .codex/skills/meeting-note-output skills-drafts/meeting-note-output AGENTS.md wiki/adr/index.md
```

Observed result:

- `skills-drafts/meeting-note-output/SKILL.md` existed
- `skills-drafts/meeting-note-output/references/meeting-note-format-example.md` existed
- `.codex/skills/meeting-note-output/` did not exist

Conclusion:

- The old state documented meeting-note behavior only in draft space
- The formal project-local skill path was absent

### GREEN Evidence

Command:

```bash
test -d .codex/skills/meeting-note-output && echo GREEN_formal_skill_present || echo RED_formal_skill_missing
find .codex/skills/meeting-note-output -maxdepth 3 -type f | sort
```

Observed result:

- `GREEN_formal_skill_present`
- `.codex/skills/meeting-note-output/SKILL.md`
- `.codex/skills/meeting-note-output/references/meeting-note-format-example.md`

Conclusion:

- The meeting-note workflow is now formally published under the project-local skill directory

### Guidance Alignment Evidence

Command:

```bash
rg -n "skills-drafts/meeting-note-output|\\.codex/skills/meeting-note-output|draft space only" AGENTS.md wiki/adr
```

Observed result:

- `AGENTS.md` now points to `.codex/skills/meeting-note-output/SKILL.md`
- `AGENTS.md` explicitly marks `skills-drafts/meeting-note-output/` as draft space only
- `wiki/adr/0006-formal-project-local-skills-over-drafts.md` records the stable boundary between formal skills, drafts, and manual agent role templates

Conclusion:

- Repo-visible guidance no longer treats the draft path as the authoritative publication mechanism
