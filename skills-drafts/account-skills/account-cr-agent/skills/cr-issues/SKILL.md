---
name: cr-issues
description: Use only inside cr-agent to maintain the normalized CR issue registry used by cr-gate.
---

Own the single CR issue registry.

Every finding from branch governance, diff, technical review, evidence review, and replay must use:

- CR-ID
- source_worker
- severity
- category
- title
- evidence
- impact
- required_action
- owner
- blocking
- status
- related_files
- related_commits

Severity values: `critical`, `high`, `medium`, `low`, `info`.

Status values: `open`, `needs_confirmation`, `accepted_risk`, `fixed`, `waived`.

Only `fixed`, `waived`, or explicitly accepted non-blocking risks can stop an issue from blocking through `cr-gate`.
