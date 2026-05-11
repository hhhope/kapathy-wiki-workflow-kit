---
name: wiki-manifest
description: Inspect the generated report wiki source and routing manifest without changing runtime state.
---

Use the wiki manifest runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-manifest.md`

When triggered:

1. Confirm the current repository has `scripts/build_wiki_status.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/build_wiki_status.py`.
4. Read `wiki/status/manifest.json`.
5. Summarize manifest counts, source coverage, stale inputs, route pressure,
   and missing generated artifacts.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not infer hidden source meaning beyond the manifest fields.
