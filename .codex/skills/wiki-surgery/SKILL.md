---
name: wiki-surgery
description: Use when planning broad, structural, governance-sensitive, relation, MOC, ADR, taxonomy, or OpenSpec-sensitive wiki repair.
---

Use this skill for the surgery / 手术 stage of the LLM-WIKI medical loop.
Surgery is plan-only in this repository until a later explicit apply workflow
or OpenSpec change exists.

Medical-loop sequence:

```text
wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery
诊断 -> 确诊 -> 治疗 -> 手术 -> 复查
```

When triggered:

1. Confirm the current repository has `scripts/build_wiki_surgery.py`.
2. Run or reference `python3 scripts/build_wiki_surgery.py`.
3. Use surgery planning for `relation_weak_evidence`, `drift_risk`,
   `adr_risk`, `openspec_required`, taxonomy candidates, MOC projection
   changes, governance pages, and broad batch repair.
4. If the user asks for a surgery record, run
   `python3 scripts/build_wiki_surgery.py --write-surgery-record`.
5. Explain the output as a plan-only surgery package, not surgery approval.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not write frontmatter.
- Do not write relation fields.
- Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Do not write `wiki/moc` files.
- Do not mutate ADR decisions, AGENTS, skills, or OpenSpec state.
- Do not treat a surgery plan as approval to apply surgery.
- Route post-operation checks to `wiki-recovery`.
