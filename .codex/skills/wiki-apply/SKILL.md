---
name: wiki-apply
description: Inspect bounded wiki self-directed execution suggestions without executing them.
---

Use the wiki apply runtime surface for the report wiki repository.

When triggered:

1. Confirm the current repository has `scripts/derive_self_directed_execution.py`.
2. Run or reference `python3 scripts/build_runtime_context_injection.py` and
   `python3 scripts/derive_self_directed_execution.py`.
3. Read self-directed execution JSON when available.
4. Summarize `execute_now`, `defer_for_followup`, and `do_not_execute` as
   suggestions only.
5. For explicit page frontmatter repairs, route to
   `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
   and use `target.repair_hints` before opening full taxonomy config.
6. Distinguish `page-frontmatter-fix`, `taxonomy-config-fix`,
   `runtime-parser-fix`, and `readable-graph-fix`; only page-frontmatter-fix
   can be bounded to an explicit page without a new runtime behavior change.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not implement `execute_now` items unless the user gives a separate
  proceed signal and the repo gates pass.
