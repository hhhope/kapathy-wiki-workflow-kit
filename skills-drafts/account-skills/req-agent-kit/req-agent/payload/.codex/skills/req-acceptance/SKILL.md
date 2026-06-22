---
name: req-acceptance
description: Use only for explicit debug or worker context around requirements acceptance functions and story mappings.
---

Use this skill for the requirements acceptance worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Extract observable acceptance function candidates.
- Keep bidirectional user story to acceptance function mappings.
- Add `coverage_types` for observable domain coverage: `state_change`,
  `handoff`, `failure_path`, and `evidence`.
- Tie acceptance functions back to relevant contexts and aggregate roots when
  strict DDD coverage is active.
- Report missing user story or acceptance function links as blockers for
  handoff.

Boundaries:

- It does not decide readiness by itself.
- It does not create OpenSpec drafts.
- It does not mutate requirements taxonomy or wiki taxonomy.
- It does not ask the user to run Python as the normal path.
