# Proposal

## Why

The taxonomy and readiness checker now use DDD context modeling, but the
requirements analysis agent still produces old `domain.confirmed` output from a
flat alias table. That leaves `req-agent` unable to produce a case shape that
passes strict taxonomy v2 readiness.

The latest role discussion also clarified an important boundary:

- intent recognition should identify real actors and business events;
- DDD role obligations are derived from selected contexts and should not be
  treated as first-line user-story actors.

Without this split, names such as `subscription_owner` can leak into user
stories as fake actors.

## What Changes

- Update requirements analysis output to include DDD `domain_model`.
- Add actor evidence separate from role obligations.
- Resolve payment and Agent-service subscription material into ecosystems,
  subdomains, bounded contexts, aggregate roots, fact owners, role obligations,
  and context handoffs.
- Keep unknown terms as candidates instead of forcing them into taxonomy.
- Update req-domain-analysis / req-scope skill guidance to reflect the actor
  versus role-obligation split.
- Add behavior evidence for the semantic skill changes.

## What Does Not Change

- Does not mutate the DDD taxonomy skeleton.
- Does not archive earlier requirement changes.
- Does not migrate historical case files.
- Does not create OpenSpec drafts until the strict readiness gate passes.
- Does not continue into implementation from a requirement case.

## Source Design

- `docs/superpowers/specs/2026-06-03-requirements-ddd-context-model-design.md`
- `openspec/changes/rewrite-requirements-readiness-gate-for-ddd-model/tasks.md`
