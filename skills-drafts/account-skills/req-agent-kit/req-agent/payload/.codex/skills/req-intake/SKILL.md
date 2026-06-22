---
name: req-intake
description: Use only for explicit debug or worker context around requirements material intake and case creation.
---

Use this skill for the requirements intake worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Accept source material.
- Record provenance.
- Identify whether the material is requirement-like.
- Create or append to a requirements case.

Boundaries:

- It creates or appends to a requirements case; it does not decide readiness.
- It does not normalize domain, roles, stories, or acceptance conclusions.
- It does not create OpenSpec drafts.
- It does not ask the user to run Python as the normal path.
