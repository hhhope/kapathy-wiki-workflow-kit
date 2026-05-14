---
description: Summarize bounded apply guidance and repair routes without executing them.
argument-hint: optional repair-plan or execution-plan focus
---

# /wiki:apply

Summarize bounded self-directed execution guidance and diagnostic repair routes
from the existing runtime artifacts. Use this command when the user asks how to
fix a wiki, graph, taxonomy, or runtime diagnostic issue.

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
   - repair routes such as `page-frontmatter-fix`, `taxonomy-config-fix`, `runtime-parser-fix`, and `readable-graph-fix`
   - action source counts
   - caution notes
   - whether direct source inspection is still required
   - whether implementation requires a new or existing OpenSpec change
5. Point the user to:
   - `wiki/ops/agent-readable-wiki-self-directed-execution.md`
   - `wiki/ops/agent-readable-wiki-context-injection.md`

## Repair Routes

When diagnostics identify a repair, summarize the route without performing the
edit:

- `page-frontmatter-fix`: bounded page frontmatter correction when page scope is explicit.
- `taxonomy-config-fix`: taxonomy vocabulary/config correction; route implementation through OpenSpec.
- `runtime-parser-fix`: runtime parser behavior correction; route implementation through OpenSpec.
- `readable-graph-fix`: readable graph summary behavior correction; route implementation through OpenSpec.

State the recommended OpenSpec path when the repair changes runtime behavior,
rules, skills, AGENTS, scripts, or command output.

## Boundaries

- This command is a thin wrapper over `scripts/build_runtime_context_injection.py`, `scripts/derive_self_directed_execution.py`, and their JSON artifacts.
- Do not execute `execute_now` actions from this command; summarize them for the user.
- Do not directly edit runtime files, scripts, rules, skills, AGENTS, or command behavior from this command.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat bounded execution guidance as permission for unbounded agent autonomy or side effects.
