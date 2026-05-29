---
name: req-stories
description: Use only for explicit debug or worker context around requirements user-story extraction and completeness checks.
---

Use this skill for the requirements stories worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Extract or review user stories.
- Check that each story has role, want, and benefit.
- Preserve story IDs so later acceptance work can map back to them.

Boundaries:

- It does not write acceptance conclusions.
- It does not decide readiness by itself.
- It does not create OpenSpec drafts.
- It does not ask the user to run Python as the normal path.
