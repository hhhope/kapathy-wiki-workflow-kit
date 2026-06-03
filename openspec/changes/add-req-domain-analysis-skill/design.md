# Design

## Scope

This change publishes the `req-domain-analysis` worker skill and makes it
visible from `req-agent`. It is a behavior-asset change, so it carries local
pressure-test evidence in `evaluation.md`.

## Routing Position

The normal requirements route becomes:

1. `req-agent`
2. `req-intake`
3. `req-domain-analysis`
4. `req-scope`
5. `req-stories`
6. `req-acceptance`
7. `req-handoff`

`req-domain-analysis` is intentionally placed before `req-scope`: it decides the
domain classification shape; `req-scope` then clarifies roles, ownership,
boundaries, and unknowns using that domain result.

## Skill Ownership

`req-domain-analysis` is a module skill under the parent `req-agent` gate. It
does not become a normal user-facing entry point. Direct use is allowed only for
explicit debug or worker context, following the existing worker pattern used by
`req-intake`, `req-scope`, `req-stories`, `req-acceptance`, and `req-handoff`.

## Domain Analysis Contract

The worker uses:

- `requirements/config/requirements-taxonomy.yaml` for active domain IDs and
  aliases;
- `openspec/changes/define-requirements-domain-standards-and-payment-skeleton`
  as the active domain-standard source until archived;
- `req-agent` as the parent gate and case-state authority.

It classifies candidate terms as:

- top-level domain;
- subdomain;
- capability;
- case slug;
- system/process name;
- alias;
- rejected non-domain.

It must not force unknown or weak candidates into existing taxonomy IDs.

## Proof Boundary

This change proves the local skill body, parent route, and behavior-asset
evaluation evidence. It does not prove broad multi-session rollout or archive
the previous domain-standard change.
