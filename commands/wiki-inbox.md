---
description: Inspect pending inbox files and optionally run the existing wiki intake draft generator.
argument-hint: optional inbox focus or file path
---

# /wiki:inbox

Inspect pending `inbox/` material and summarize the repo-local intake route.

## Workflow

1. Refresh the status manifest:

```bash
python3 scripts/build_wiki_status.py
```

2. Read `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
3. Summarize pending inbox files, including:
   - original inbox path
   - whether an existing source record already references the file
   - likely next repo-local target when the status artifact provides enough evidence
4. When the user explicitly wants intake drafts created, run the existing intake script:

```bash
python3 -m scripts.inbox_intake --inbox inbox --sources wiki/sources --ops wiki/ops
```

5. Summarize any generated source or ops draft paths and point the user to:
   - `wiki/inbox-intake.md`
   - generated `wiki/sources/` drafts
   - generated `wiki/ops/` intake drafts

## Boundaries

- This command is a thin wrapper over `scripts/build_wiki_status.py`, `scripts.inbox_intake`, and the repo-local inbox/status artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not automatically upgrade intake drafts into focus threads, reminders, Codex handoffs, team lore, or accepted conclusions.
- Do not overwrite existing wiki conclusions with raw inbox material.
