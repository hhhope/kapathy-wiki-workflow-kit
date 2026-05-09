---
description: Preview a bounded wiki change queue without executing or mutating OpenSpec state.
argument-hint: optional queue focus
---

# /wiki:queue

Preview candidate wiki work from the existing self-directed execution layer.

## Workflow

1. Build the preview queue:

```bash
python3 scripts/build_wiki_change_queue_preview.py > /tmp/wiki-change-queue-preview.json
```

2. Read `/tmp/wiki-change-queue-preview.json`.
3. Summarize the queue preview in the conversation, including:
   - `ready`
   - `needs_user_decision`
   - `blocked`
   - source paths
   - caution notes
   - proof boundaries
4. Point the user to:
   - `wiki/ops/agent-readable-wiki-self-directed-execution.md`
   - `wiki/ops/agent-readable-wiki-context-injection.md`

## Boundaries

- This command is a thin wrapper over `scripts/build_wiki_change_queue_preview.py` and existing self-directed execution artifacts.
- Do not execute preview queue items from this command.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue execution.
- Do not treat queue preview as permission for unbounded agent autonomy or side effects.
