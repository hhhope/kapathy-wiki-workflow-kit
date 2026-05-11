---
name: wiki-status
description: Refresh and summarize the report wiki status surface from manifest and status artifacts.
---

Use the wiki status runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-status.md`

When triggered:

1. Confirm the current repository has `scripts/build_wiki_status.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/build_wiki_status.py`.
4. Read `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
5. Summarize only the current status, warnings, stale inputs, and next
   inspection points.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not implement a query engine, graph UI, scorecard, or change queue from
  this skill.
