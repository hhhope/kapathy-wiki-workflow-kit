---
name: wiki-confirm
description: Use when confirming, triaging, routing, or 确诊 `wiki-doctor` findings before treatment or surgery.
---

Use this skill for the confirm / 确诊 stage of the LLM-WIKI medical loop.
This is a review-only routing entry for `wiki-doctor` diagnosis output.
default writes a complete confirmation record; stdout summary is only the live
chat/terminal surface.

Medical-loop sequence:

```text
wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery
诊断 -> 确诊 -> 治疗 -> 手术 -> 复查
```

When triggered:

1. Confirm the current repository has
   `scripts/build_wiki_review_decisions.py`.
2. Run `python3 scripts/build_wiki_review_decisions.py`; by default it writes
   a complete confirmation record under `wiki/ops/wiki-review-decisions/`.
3. Preserve these draft buckets exactly:
   `accepted_candidates`, `rejected_candidates`, `deferred_items`,
   `treatment_candidates`, `surgery_candidates`, and `openspec_required`.
4. Explain the output as draft routing, not approval.
5. Treat stdout as a summary and report the generated confirmation record path.
   Use `--stdout-json-only` only for explicit non-writing debug inspection.
   `--write-decision-record` remains a compatibility flag. Include
   `--decision-record-dir` only when the record must be written somewhere other
   than `wiki/ops/wiki-review-decisions/`.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not write frontmatter.
- Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Do not write relation fields.
- Do not write `wiki/moc` files.
- Do not treat draft review decisions as human approval.
- Route low-risk approved frontmatter repair to `wiki-treatment`.
- Route broad, structural, governance, relation, MOC, ADR, taxonomy, or
  OpenSpec-sensitive work to `wiki-surgery`.
