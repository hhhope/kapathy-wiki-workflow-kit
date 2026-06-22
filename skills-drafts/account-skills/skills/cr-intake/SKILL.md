---
name: cr-intake
description: Use only inside cr-agent to normalize CR type, range, ticket, evidence, and output-mode inputs.
---

Collect the CR input package and report missing blockers.

Required fields:

- project root or repository identifier
- CR type
- start ref and end ref, or branch and target
- Jira, requirement, incident, or release ticket references when available
- test, UAT, production, rollback, and impact-confirmation evidence when available
- requested output mode: status, gate, report, replay, or full CR

Output:

- normalized CR case skeleton
- missing-input blockers
- next valid worker

Do not infer release range from a feature branch when the user asks for release CR.
