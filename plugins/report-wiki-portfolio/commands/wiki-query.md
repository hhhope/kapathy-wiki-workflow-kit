---
description: Build a bounded task-shaped wiki context packet from status, route, context, and explicit text search evidence.
argument-hint: task or focus text
---

# /wiki:query

Build and summarize a bounded LLM Wiki context packet for the user's current
task or focus.

## Workflow

1. Refresh the status and manifest surface:

```bash
python3 scripts/build_wiki_status.py
```

2. Build runtime route and context artifacts:

```bash
python3 scripts/derive_runtime_auto_routing.py > /tmp/wiki-runtime-auto-routing.json
python3 scripts/build_runtime_context_injection.py > /tmp/wiki-context-injection.json
```

3. If the user provided task or focus text, run explicit text search over the
   repo knowledge surface:

```bash
rg -n "<focus text>" wiki openspec/specs commands README.md
```

4. Read:
   - `wiki/status/manifest.json`
   - `wiki/status/wiki-status.md`
   - `/tmp/wiki-runtime-auto-routing.json`
   - `/tmp/wiki-context-injection.json`
   - explicit `rg -n` matches when focus text is provided
5. Summarize a bounded context packet in the conversation, including:
   - `open_first`
   - `open_next`
   - `do_not_anchor`
   - explicit text search matches
   - caution notes
   - proof boundary notes

## Boundaries

- This command is bounded retrieval guidance, not semantic search.
- Use explicit text search and existing runtime artifacts only; no embeddings.
- No hidden semantic ranking; do not invent unstated relevance scores.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not execute `/wiki:apply` or `execute_now` actions from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat query output as final judgment; direct source inspection is still required for claims.
