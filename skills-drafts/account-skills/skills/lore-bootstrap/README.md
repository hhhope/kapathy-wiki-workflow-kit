# Lore Bootstrap

Bootstrap and migrate Lore Wiki into a separate git repository.

## Scope

- Install or initialize a shared `team-lore` repo
- Create `wiki/` structure and project entrypoint pages
- Wire the global `team-lore` path
- Preserve project-local `logs/`
- Migrate a legacy flat `LORE.md` into a tracked legacy snapshot plus migration notes

## Install location

- Preferred default in this environment: `/mnt/d/team-lore`
- The install target should be confirmed during setup, not silently assumed
- Keep the shared wiki in a user-controlled git repo outside the project repo

## Out of scope

- weekly review
- lore retrieval
- code archaeology
- OpenSpec lifecycle execution

Those remain in `skills/lore/`.
