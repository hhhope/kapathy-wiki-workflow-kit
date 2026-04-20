# Verification

## Commands

```bash
openspec validate harden-skill-authoring-contract
python3 scripts/repo_health_check.py --repo-root .
rg -n "[\\p{Han}]" .codex/skills/*/SKILL.md
rg -n "English-first|repo-local skill|compact" /home/yan/.codex/skills/writing-skills/SKILL.md /home/yan/.codex/skills/skill-creator/SKILL.md /home/yan/.codex/rules/common/development-workflow.md
```

## Expected Outcome

- OpenSpec validation passes.
- Existing repo health checks still pass.
- Repo-local skill bodies contain only limited workflow-required Chinese labels or trigger examples instead of Chinese governing prose.
- Shared authoring guidance now explicitly mentions:
  - English-first behavior assets
  - repo `AGENTS.md` scanning before repo-local skill authoring
  - compact `SKILL.md` bodies with heavy detail moved to `references/`
