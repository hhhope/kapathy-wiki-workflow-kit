---
name: wiki-frontmatter-taxonomy
description: Use when creating or modifying report wiki frontmatter, wiki templates, or repo-local scripts that generate wiki frontmatter.
---

Use the repo-local wiki frontmatter taxonomy gate.

Load:

- `wiki/config/frontmatter-taxonomy.yaml`
- `scripts/check_wiki_frontmatter.py`
- `docs/superpowers/specs/2026-05-13-wiki-frontmatter-taxonomy-design.md` when design context is needed

Hard rules:

- Do not duplicate taxonomy vocabulary in this skill.
- Treat user language, AI drafts, folder names, and script guesses as hints until validated.
- Do not use local skill templates or ad hoc agent judgment as final taxonomy authority.
- Run `python3 scripts/check_wiki_frontmatter.py` before claiming taxonomy compliance or completion.
- If the checker reports errors, do not claim the taxonomy work is complete.

When creating or modifying frontmatter:

1. Read `wiki/config/frontmatter-taxonomy.yaml`.
2. Determine the page layer by path and task.
3. Apply the path rule from the taxonomy contract.
4. Use explicit uncertainty fields when classification is not known.
5. Run the checker and summarize remaining drift.

Boundaries:

- Do not batch-migrate legacy pages unless the active OpenSpec change lists them.
- Do not edit global agent instructions.
- Do not change scorecard scoring formulas from this skill.
- Do not treat checker warnings as proof that all legacy drift has been resolved.
