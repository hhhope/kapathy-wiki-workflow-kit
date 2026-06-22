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
- Produce DDD `domain_model` evidence: ecosystems, subdomains, bounded
  contexts, aggregate roots, fact owners, role obligations, context handoffs,
  non-domain terms, and open questions.
- Produce domain coverage obligations for required/in-scope subdomains,
  bounded contexts, aggregate roots, lifecycle handoffs, failure paths, and
  auditable evidence surfaces.
- Separate real actors from DDD role obligations. Actors are people,
  organizations, systems, or automation named by the source. Role obligations
  are fact-owner obligations derived from contexts and handoffs.
- Identify primary and collaborating contexts when a case crosses boundaries.
- Preserve open questions for weak or unknown candidates.

Output evidence:

- Actor evidence from the source.
- DDD domain model candidate, if one is supportable.
- Collaborating context candidates, when relevant.
- Role obligations that `req-scope` must assign to concrete owners.
- Domain coverage obligations that later stories and acceptance functions must
  satisfy or explicitly classify as light coverage, out of scope, or follow-up.
- Candidate classification table.
- Rejected or demoted names with reasons.
- Open questions and needed confirmation.

Boundaries:

- It does not mutate requirements taxonomy.
- It does not force unknown candidates into existing taxonomy IDs.
- It does not treat role obligations such as `subscription_owner` as user-story
  actors by default.
- It does not normalize owner assignment, user stories, or acceptance
  functions.
- It does not decide readiness or create OpenSpec drafts.
- It does not continue into implementation.
