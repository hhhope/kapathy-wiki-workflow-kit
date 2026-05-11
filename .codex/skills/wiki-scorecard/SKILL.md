---
name: wiki-scorecard
description: Inspect report wiki semantic scoring and utilization diagnostics without hidden ranking.
---

Use the wiki scorecard runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-scorecard.md`

When triggered:

1. Confirm the current repository has `scripts/score_wiki_semantics.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/score_wiki_semantics.py`,
   `python3 scripts/derive_wiki_utilization.py`, and
   `python3 scripts/summarize_wiki_scorecard.py`.
4. Read scoring, utilization, and summary JSON when available.
5. Summarize preferred, cautious, and blocked objects with score bands,
   caution reasons, and next inspection actions.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not claim embeddings, hidden semantic ranking, or retrieval proof.
