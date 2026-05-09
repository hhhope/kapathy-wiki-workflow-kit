---
description: Run the existing runtime context and context-injection scripts, then summarize bounded context bundles.
argument-hint: optional canonical object or context focus
---

# /wiki:context

Build and summarize the repository's bounded runtime context bundles.

## Workflow

1. Build the runtime context bundle:

```bash
python3 scripts/build_wiki_runtime_context.py > /tmp/wiki-runtime-context.json
```

2. Build bounded context injection from the live route:

```bash
python3 scripts/build_runtime_context_injection.py > /tmp/wiki-context-injection.json
```

3. Read `/tmp/wiki-runtime-context.json`, `/tmp/wiki-context-injection.json`, and, when useful, the sample artifacts:
   - `scripts/examples/agent_readable_wiki_runtime_context_sample.json`
   - `scripts/examples/agent_readable_wiki_context_injection_sample.json`
4. Summarize the context bundles, including:
   - preferred, supporting, and blocked runtime context counts
   - injected first-pass count
   - secondary context count
   - excluded object count
   - caution notes
   - whether direct source inspection is still required
5. Point the user to the governing wiki pages:
   - `wiki/ops/agent-readable-wiki-runtime-context.md`
   - `wiki/ops/agent-readable-wiki-context-injection.md`

## Boundaries

- This command is a thin wrapper over `scripts/build_wiki_runtime_context.py`, `scripts/build_runtime_context_injection.py`, and their JSON artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not inject whole pages or bypass the script's bounded excerpt policy.
- Do not treat context bundles as final judgment or proof of runtime autonomy.
