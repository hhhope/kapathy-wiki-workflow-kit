---
name: req-handoff
description: Use only for explicit debug or worker context around requirements readiness gates and OpenSpec draft handoff.
---

Use this skill for the requirements handoff worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Run the hard readiness gate.
- Use `scripts/check_requirements_case.py` as internal evidence when a case is
  available.
- Confirm `domain_model_gate`, `domain_coverage_gate`, and
  `requirement_delivery_gate` all pass before draft creation.
- Confirm any Human Review artifact linked from the case has no unsynchronized
  `demand_fact` before draft creation.
- Create an OpenSpec draft only after the hard readiness gate passes.
- Treat draft creation as a stop condition.

Boundaries:

- It does not create drafts for blocked or unready requirements cases.
- It does not treat a Human Review document as the source of truth; the machine
  requirements case remains authoritative.
- It does not overwrite existing OpenSpec changes.
- It does not continue into implementation automatically.
- Do not continue into implementation automatically.
