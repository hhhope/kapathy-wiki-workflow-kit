---
name: wiki-queue
description: Preview ready, decision-needed, and blocked report wiki work without executing it.
---

Use the wiki queue runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-queue.md`

When triggered:

1. Confirm the current repository has `scripts/build_wiki_change_queue_preview.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/build_wiki_change_queue_preview.py`.
4. Read queue preview JSON when available.
5. Summarize `ready`, `needs_user_decision`, and `blocked` work with source
   paths and caution notes.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not turn preview items into tasks or commits by default.
