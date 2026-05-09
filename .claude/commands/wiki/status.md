---
name: "Wiki: Status"
description: Refresh the LLM Wiki manifest and show the generated wiki status report
category: Wiki
tags: [wiki, status, manifest]
---

Refresh the LLM Wiki manifest and summarize the current wiki status.

Use this command as:

```text
/wiki:status
```

## Steps

1. Refresh generated status artifacts:

   ```bash
   python3 scripts/build_wiki_status.py
   ```

2. Read and summarize:

   ```text
   wiki/status/wiki-status.md
   ```

3. Point the user to both generated artifacts:

   ```text
   wiki/status/manifest.json
   wiki/status/wiki-status.md
   ```

## Output

Report the key counts and next actions from `wiki/status/wiki-status.md`:

- wiki page count
- source record count
- inbox file count
- pending inbox files
- active OpenSpec changes
- complete active-directory OpenSpec changes
- generated next actions

## Boundaries

Do not implement query, scorecard, graph UI, or change queue.

Do not open, modify, or archive OpenSpec changes. This command only refreshes
and surfaces the generated wiki status artifacts.
