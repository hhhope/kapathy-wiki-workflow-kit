---
name: req-scope
description: Use only for explicit debug or worker context around requirements domain, roles, ownership, and boundary clarification.
---

Use this skill for the requirements scope worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Normalize domain, roles, ownership, boundaries, and unknowns.
- Use `requirements/config/requirements-taxonomy.yaml` as the requirements
  vocabulary.
- Keep unknown domains or roles as `candidate_pending` or awaiting
  confirmation.

Boundaries:

- It does not mutate taxonomy.
- It does not force candidate values into existing taxonomy IDs.
- It does not write user stories or acceptance functions.
- It does not decide readiness or create OpenSpec drafts.
