---
name: req-scope
description: Use only for explicit debug or worker context around requirements domain, roles, ownership, and boundary clarification.
---

Use this skill for the requirements scope worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Normalize actors, role-obligation ownership, boundaries, and unknowns after
  DDD domain analysis.
- Use `requirements/config/requirements-taxonomy.yaml` as the requirements
  vocabulary.
- Use source actors as the starting point for user-story role refs.
- Assign DDD role obligations from `domain_model.role_obligations` to concrete
  owners, systems, or explicit open questions.
- Keep unknown actors, owners, domains, contexts, or obligations as
  `candidate_pending` or awaiting
  confirmation.

Boundaries:

- It does not mutate taxonomy.
- It does not force candidate values into existing taxonomy IDs.
- It does not treat role obligations as user-story actors by default.
- It does not write user stories or acceptance functions.
- It does not decide readiness or create OpenSpec drafts.
