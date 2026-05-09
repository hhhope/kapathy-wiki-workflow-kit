---
description: Refresh the repo-local LLM Wiki manifest and summarize the machine-readable repository inventory.
argument-hint: optional focus text
---

# /wiki:manifest

Refresh and summarize the repository's machine-readable LLM Wiki manifest.

## Workflow

1. Run:

```bash
python3 scripts/build_wiki_status.py
```

2. Read `wiki/status/manifest.json`.
3. Summarize the manifest in the conversation, including:
   - generated timestamp
   - wiki page count
   - source record count
   - pending inbox count
   - active and complete OpenSpec change counts
   - any manifest warnings or missing expected sections
4. Point the user to:
   - `wiki/status/manifest.json`
   - `wiki/status/wiki-status.md`

## Boundaries

- This command is a thin wrapper over `scripts/build_wiki_status.py` and the generated `wiki/status/manifest.json` artifact.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat the manifest as product judgment; it is only a generated inventory and routing surface.
