---
name: wiki-treatment
description: Use when applying or previewing explicitly approved low-risk wiki frontmatter treatment after diagnosis and confirmation.
---

Use this skill for the treatment / 治疗 stage of the LLM-WIKI medical loop.
Treatment handles bounded low-risk frontmatter repair after explicit human
approval.

Medical-loop sequence:

```text
wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery
诊断 -> 确诊 -> 治疗 -> 手术 -> 复查
```

When triggered:

1. Confirm the current repository has `scripts/build_wiki_treatment.py`.
2. Run or reference `python3 scripts/build_wiki_treatment.py`.
3. Default to dry-run: treatment defaults to dry-run and must not write files
   unless `--apply` is present.
4. Require explicit human approval through `--approved-domain` or
   `--approved-detail`.
5. Treat `--write-treatment-record` as a reviewable treatment record under
   `wiki/ops/wiki-treatment-runs/`, not as surgery approval.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not apply treatment without `--apply`.
- Do not apply treatment without `--approved-domain` or `--approved-detail`.
- Do not write relation fields.
- Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Do not write `wiki/moc` files.
- Do not mutate ADR decisions, AGENTS, skills, or OpenSpec state.
- Route broad, structural, governance, relation, MOC, ADR, taxonomy, or
  OpenSpec-sensitive work to `wiki-surgery`.
