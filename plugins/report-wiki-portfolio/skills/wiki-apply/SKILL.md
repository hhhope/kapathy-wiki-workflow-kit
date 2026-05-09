---
name: wiki-apply
description: Inspect bounded wiki self-directed execution suggestions without executing them.
---

Use the wiki apply runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-apply.md`

When triggered:

1. Confirm the current repository has `scripts/derive_self_directed_execution.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/build_runtime_context_injection.py` and
   `python3 scripts/derive_self_directed_execution.py`.
4. Read self-directed execution JSON when available.
5. Summarize `execute_now`, `defer_for_followup`, and `do_not_execute` as
   suggestions only.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not implement `execute_now` items unless the user gives a separate
  proceed signal and the repo gates pass.
