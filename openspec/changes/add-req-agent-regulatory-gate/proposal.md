# add-req-agent-regulatory-gate

## Why

The Baofoo legal SMS review exposed a workflow gap: `req-agent` can mark a
case structurally ready while regulatory, identity, security, and evidence
obligations remain only as human-review notes or ad hoc blockers. For
requirements that mention compliance, regulation, legal representative intent,
identity verification, authorization/consent, personal information, SMS links,
or regulated merchant onboarding, those obligations shape user stories and
acceptance criteria. They are not merely detailed-design inputs.

## What Changes

- Add a reusable regulatory obligation gate to requirements readiness.
- Trigger the gate from `risk_compliance` domain evidence or explicit source
  signals such as compliance, regulation, identity verification, authorization,
  consent, personal information, legal representative, SMS link, token, or
  regulated merchant onboarding.
- Require triggered cases to carry `soft_evidence.regulatory_obligations` with
  owner, source basis, acceptance mappings, and unresolved/confirmed status.
- Make missing or unresolved regulatory obligations block `requirements_ready`.
- Update `req-agent` and worker guidance so the obligation is identified after
  domain analysis, assigned during scope, converted to acceptance, and checked
  during human review.

## Out Of Scope

- No legal advice or hard-coded law library.
- No mutation of wiki frontmatter taxonomy.
- No batch migration of historical requirements cases.
- No requirement that every payment case has regulatory obligations; the gate
  triggers only from domain/signals.
- No implementation design, API, DDL, or state-machine design for the Baofoo
  case.
