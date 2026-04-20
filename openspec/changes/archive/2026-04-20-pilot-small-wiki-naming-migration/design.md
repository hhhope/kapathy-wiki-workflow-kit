# Design: Pilot Small Wiki Naming Migration

## Problem

The repository now has formalized rules for naming, frontmatter, and graph extraction,
but those rules have only been applied to newly added pages.

Without a real migration pilot, the repository still lacks proof that the new model
can be applied to existing legacy pages without scope drift.

## Design Goals

The pilot should:

- stay intentionally small
- touch one coherent object family
- demonstrate title, frontmatter, and index migration together
- leave a reusable migration pattern for later work

## Candidate Scope

The safest pilot target is the `conversation-handoff` family because it is:

- already formalized in naming/spec/policy
- small in page count
- less entangled than broader ops families

Candidate pilot pages:

- `wiki/ops/conversation-handoff-mode.md`
- `wiki/ops/sample-handoff-topic.md`
- related links in `wiki/ops/index.md`

Potential follow-up if still small enough:

- align the page titles and frontmatter first
- keep file path migration limited to the chosen pilot only

## Migration Pattern

The pilot should apply the new model in this order:

1. add frontmatter identity fields
2. add typed relation fields where appropriate
3. align titles to `canonical object / artifact type`
4. update local links and indexes
5. re-run graph extraction

## Validation Boundary

The pilot proof should confirm:

- migrated pages now expose canonical object and artifact type explicitly
- local navigation still points to the right paths
- extractor output continues to include the migrated pages as nodes

The pilot proof should not claim:

- full repository migration readiness
- global naming consistency across every legacy page
- that one pilot family settles all migration edge cases

## Non-Goals

- no whole-repo rename
- no bulk frontmatter backfill
- no graph UI work
- no migration of unrelated legacy ops pages

## Open Questions

- whether the pilot should rename file paths as well as page titles in the first pass
- whether `conversation-handoff` is the best pilot or whether `example-driven-capture` would yield cleaner evidence
