---
name: req-domain-analysis
description: Use only for explicit debug or worker context around requirements domain classification after intake and before scope.
---

Use this skill for the requirements domain-analysis worker.

Ordinary use routes through `req-agent`.

Use this worker directly only for explicit debug or worker context. Direct
worker output is evidence only; it is not the normal requirements entry.

Responsibility:

- Classify requirement material against the DDD requirements-domain standard.
- Use `requirements/config/requirements-taxonomy.yaml` as the active domain
  vocabulary.
- Separate top-level domains from subdomains, capabilities, case slugs,
  system/process names, aliases, and rejected non-domains.
- Identify primary and collaborating domains when a case crosses boundaries.
- Preserve open questions for weak or unknown candidates.

Output evidence:

- Primary domain candidate, if one is supportable.
- Collaborating domain candidates, when relevant.
- Candidate classification table.
- Rejected or demoted names with reasons.
- Open questions and needed confirmation.

Boundaries:

- It does not mutate requirements taxonomy.
- It does not force unknown candidates into existing taxonomy IDs.
- It does not normalize roles, ownership, user stories, or acceptance functions.
- It does not decide readiness or create OpenSpec drafts.
- It does not continue into implementation.
