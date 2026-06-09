---
name: req-human-review
description: Use only for explicit debug or worker context around requirements human review artifacts and synchronization checks.
---

Use this skill for the requirements human-review worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Produce or update a Human Review artifact after stories and acceptance
  mappings exist.
- Use `wiki/templates/requirements-human-review-template.md` as the output
  shape.
- Review source coverage, domain judgment, scope, roles, user stories,
  scenario coverage, rule/status coverage, acceptance scope, and design gates.
- Classify Human Review findings as `demand_fact`, `review_prompt`, or
  `design_gate_gap`.
- Synchronize every `demand_fact` back to the machine requirements case before
  handoff.

Boundaries:

- It does not replace the requirements case as the source of truth.
- It does not create OpenSpec drafts.
- It does not write API, DDL, state-machine, rule-model, or engineering design.
- It does not treat reviewer prompts as demand facts until accepted.
- It does not ask the user to run Python as the normal path.
