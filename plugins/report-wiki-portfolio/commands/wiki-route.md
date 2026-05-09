---
description: Run the existing runtime source-integration and auto-routing scripts, then summarize reading order.
argument-hint: optional canonical object or route focus
---

# /wiki:route

Build and summarize the repository's source-integrated runtime reading route.

## Workflow

1. Resolve runtime context to repo-local sources:

```bash
python3 scripts/resolve_runtime_context_sources.py > /tmp/wiki-runtime-sources.json
```

2. Derive runtime auto routing from the source-integrated output:

```bash
python3 scripts/derive_runtime_auto_routing.py /tmp/wiki-runtime-sources.json > /tmp/wiki-runtime-auto-routing.json
```

3. Read `/tmp/wiki-runtime-sources.json`, `/tmp/wiki-runtime-auto-routing.json`, and, when useful, the sample artifacts:
   - `scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json`
   - `scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json`
4. Summarize the route, including:
   - preferred source count
   - supporting source count
   - blocked object count
   - `open_first`
   - `open_next`
   - `do_not_open_first`
   - whether direct source inspection is still required
5. Point the user to the governing wiki pages:
   - `wiki/ops/agent-readable-wiki-runtime-context-source-integration.md`
   - `wiki/ops/agent-readable-wiki-runtime-auto-routing.md`

## Boundaries

- This command is a thin wrapper over `scripts/resolve_runtime_context_sources.py`, `scripts/derive_runtime_auto_routing.py`, and their JSON artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not reorder routes with semantic guesses beyond the script output.
- Do not treat route output as automatic context injection or runtime autonomy.
