---
name: wiki-review-decisions
description: Use when confirming, triaging, or routing `wiki-doctor` findings into review decisions.
---

Use the wiki review-decision surface for the report wiki repository.
This is a review-only routing entry for `wiki-doctor` diagnosis output.

When triggered:

1. Confirm the current repository has
   `scripts/build_wiki_review_decisions.py`.
2. Run or reference `python3 scripts/build_wiki_review_decisions.py`.
3. Preserve these draft buckets exactly:
   `accepted_candidates`, `rejected_candidates`, `deferred_items`,
   `treatment_candidates`, `surgery_candidates`, and `openspec_required`.
4. Treat outputs as draft review routing, not approval.
5. If the user explicitly asks to generate or write a decision record, run
   `python3 scripts/build_wiki_review_decisions.py --write-decision-record`;
   include `--decision-record-dir` only when the record must be written
   somewhere other than the default `wiki/ops/wiki-review-decisions/`
   directory.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not write frontmatter.
- Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Do not write relation fields.
- Do not write `wiki/moc` files.
- Do not treat draft review decisions as human approval.
