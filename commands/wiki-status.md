---
description: Refresh the repo-local LLM Wiki manifest and summarize the generated status report.
argument-hint: optional focus text
---

# /report-wiki-portfolio:wiki-status

Refresh and summarize the repository's LLM Wiki status surface.

## Workflow

1. Run:

```bash
python3 scripts/build_wiki_status.py
```

2. Read `wiki/status/wiki-status.md`.
3. Summarize the status in the conversation, including:
   - wiki page count
   - source record count
   - pending inbox count
   - active and complete OpenSpec change counts
   - the pending inbox list when present
4. Point the user to:
   - `wiki/status/manifest.json`
   - `wiki/status/wiki-status.md`

## Boundaries

- This command is a repo-local Codex plugin command, not a global prompt and not a Claude command.
- Do not implement query, scorecard, graph UI, or change queue.
- Do not open, modify, archive, or create OpenSpec changes from this command.
- Do not treat generated status as product judgment; it is only a source manifest and routing surface.
