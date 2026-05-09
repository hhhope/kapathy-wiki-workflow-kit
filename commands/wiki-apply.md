---
description: Run the existing self-directed execution script and summarize bounded apply guidance without executing it.
argument-hint: optional execution-plan focus
---

# /wiki:apply

Summarize bounded self-directed execution guidance from the existing runtime artifacts.

## Workflow

1. Build bounded context injection:

```bash
python3 scripts/build_runtime_context_injection.py > /tmp/wiki-context-injection.json
```

2. Derive the bounded execution plan:

```bash
python3 scripts/derive_self_directed_execution.py /tmp/wiki-context-injection.json > /tmp/wiki-self-directed-execution.json
```

3. Read `/tmp/wiki-self-directed-execution.json` and, when useful, the sample artifact:
   - `scripts/examples/agent_readable_wiki_self_directed_execution_sample.json`
4. Summarize the execution plan in the conversation, including:
   - `execute_now`
   - `defer_for_followup`
   - `do_not_execute`
   - action source counts
   - caution notes
   - whether direct source inspection is still required
5. Point the user to:
   - `wiki/ops/agent-readable-wiki-self-directed-execution.md`
   - `wiki/ops/agent-readable-wiki-context-injection.md`

## Boundaries

- This command is a thin wrapper over `scripts/build_runtime_context_injection.py`, `scripts/derive_self_directed_execution.py`, and their JSON artifacts.
- Do not execute `execute_now` actions from this command; summarize them for the user.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat bounded execution guidance as permission for unbounded agent autonomy or side effects.
