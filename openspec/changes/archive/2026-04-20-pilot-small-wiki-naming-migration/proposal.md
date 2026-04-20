# Proposal: Pilot Small Wiki Naming Migration

## Why

The repository has now completed three upstream layers:

- naming model
- frontmatter model
- graph extraction

The remaining step in the original sequence is not full migration. It is a small,
controlled pilot that proves the naming and frontmatter models can be applied to a
real set of legacy pages without turning into a repository-wide rewrite.

## What Changes

This change performs a small migration on one intentionally narrow page family.

The pilot will:

- choose one existing object family with a real evolution chain
- rename a small set of pages toward the `canonical object / artifact type` model
- add minimal frontmatter fields required by the new model
- update local index links affected by the pilot
- verify graph extraction still works after the migration

This change does not:

- migrate the whole repository
- redefine the naming model
- redefine the frontmatter model
- force old pages outside the pilot scope to change

## Success Criteria

- The pilot page family follows the naming and frontmatter models end to end.
- Links and indexes remain valid after the migration.
- Graph extraction still emits expected nodes for the migrated pages.
- The pilot remains small enough to teach migration patterns without becoming a broad cleanup.
