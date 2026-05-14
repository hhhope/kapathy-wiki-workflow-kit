---
name: wiki-react
description: Use when a wiki request needs explicit intent, route, boundary, or decision-trace replay before action.
---

Use the bounded wiki ReAct decision-trace surface for the report wiki repository.

When triggered:

1. Confirm the current repository has
   `wiki/ops/wiki-react-decision-trace-runtime.md`.
2. Read `wiki/ops/wiki-react-decision-trace-runtime.md`.
3. Classify the wiki request intent, evidence object, and risk level.
4. Produce a compact `decision_trace` with action, observation, decision,
   boundary, and forbidden actions checked.
5. For replay or evaluation, use `wiki/evals/wiki-react-trace-cases.json` and
   `python3 scripts/eval_wiki_decision_trace.py --traces TRACE_JSON`.
6. Route onward to the appropriate wiki skill, such as `wiki-status`,
   `wiki-query`, `wiki-apply`, `wiki-explore`, or `wiki-scorecard`.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not treat article weight, temperature, source confidence, relation
  strength, or scorecard bands as hard gates.
- Do not use Python to classify natural-language intent; Python only validates
  agent-produced traces.
