---
name: wiki-context
description: Inspect the report wiki runtime context bundle and context-injection output.
---

Use the wiki context runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-context.md`

When triggered:

1. Confirm the current repository has `scripts/build_wiki_runtime_context.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/build_wiki_runtime_context.py` and
   `python3 scripts/build_runtime_context_injection.py`.
4. Read runtime context and context-injection JSON when available.
5. Summarize preferred, supporting, blocked, and caution context within the
   proof boundary of the generated artifacts.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not treat injected context as permission to implement changes.
