# Proposal

## Why

The requirements taxonomy now uses a DDD context model, but the requirements
readiness checker still reads the old flat `domains` and `roles` vocabulary.
That makes every new v2 case look unclassified even when it has valid
ecosystem, subdomain, bounded context, aggregate, handoff, and role-obligation
evidence.

The gate should no longer answer only "is there a known domain and role list?"
It should answer two separate questions:

- Is the domain model assignment ready enough for humans and Agents to share a
  stable boundary?
- Is the requirement delivery evidence ready enough to produce stories,
  acceptance functions, and handoff?

## What Changes

- Add a DDD readiness gate model for requirements cases.
- Teach the checker to read taxonomy v2 roots:
  `business_ecosystems`, `subdomains`, `bounded_contexts`,
  `role_archetypes`, `context_map`, and `readiness_gate_model`.
- Split readiness evidence into `domain_model_gate` and
  `requirement_delivery_gate`.
- Require confirmed ecosystems, subdomains, bounded contexts, aggregate roots,
  context handoffs, fact owners, and role obligations when strict DDD mode is
  used.
- Preserve legacy compatibility mode for old case files.
- Record proof that v2 taxonomy no longer fails because old `domains/roles`
  roots are absent.

## What Does Not Change

- Does not update `req-agent`, `req-domain-analysis`, or `req-scope` output
  templates.
- Does not migrate all historical requirement cases.
- Does not archive previous completed requirement changes.
- Does not create implementation drafts from requirement cases.

## Source Design

- `docs/superpowers/specs/2026-06-03-requirements-ddd-context-model-design.md`
