---
name: lore-bootstrap
description: Use when installing, bootstrapping, or migrating the Lore Wiki into a separate git repository, including requests to initialize a shared team-lore repo, choose where it lives, create wiki/project pages, wire agent paths, or move legacy flat lore into the wiki model.
---

# Lore Bootstrap

Install and migrate the Lore Wiki as a separate git-backed memory repository.

**Ownership split:**
- `lore-bootstrap` owns install, bootstrap, and migration
- `lore` owns runtime query, review, lint, and reuse
- OpenSpec still owns change lifecycle

All durable wiki pages must live in the shared git repo. Local project `logs/` stay in the project repo.

---

## Hard rules

- ❌ Do not treat onboarding prose as a completed installation
- ❌ Do not merge the project code repo and the shared Lore Wiki repo
- ❌ Do not leave durable wiki pages outside git
- ❌ Do not store local execution logs in the shared wiki repo
- ❌ Do not rewrite legacy `LORE.md` in place and call that migration
- ❌ Do not assume `~/team-lore` if the install target was not confirmed

---

## Use this skill for

- `install lore wiki`
- `bootstrap team-lore`
- `initialize lore for this project`
- `migrate flat LORE.md to wiki`
- `set up shared lore repo`

Do not use this skill for weekly review, lore retrieval, or code archaeology. Those remain in `lore`.

---

## Install target selection

The install path is part of the setup contract and must be made explicit.

Current preferred default for this environment:
- Shared repo root: `/mnt/d/team-lore`
- Wiki root: `/mnt/d/team-lore/wiki`

If the user already has another location, keep it only when they explicitly confirm it.
If the user asks where to put it, recommend a user-controlled git-backed path on the data drive instead of `$HOME`.

## Install targets

- Shared repo root: `<chosen-team-lore-root>`
- Wiki root: `<chosen-team-lore-root>/wiki`
- Project entrypoint: `<chosen-team-lore-root>/wiki/projects/<project>/overview.md`
- Global schema path: `team-lore: <chosen-team-lore-root>/wiki`

Project repo keeps:
- `PROJECT.md`
- OpenSpec change docs
- local `logs/`

Shared wiki repo keeps:
- `wiki/index.md`
- project overview + domain pages
- shared `pitfalls/`
- shared `principles/`
- optional `templates/`

---

## Phase 1 — Detect mode

Classify the request before writing anything:

1. **Fresh install**
   - no chosen team-lore repo
   - or no `wiki/`
2. **Existing repo bootstrap**
   - chosen repo `.git` exists
   - wiki exists or can be completed
3. **Migration**
   - legacy flat lore file exists
   - user wants the wiki model to replace it as default

Stop if the user is only asking for runtime Lore usage. Route back to `lore`.

---

## Phase 2 — Bootstrap the shared repo

Required result:

- `<chosen-team-lore-root>/.git`
- `<chosen-team-lore-root>/wiki/index.md`
- `<chosen-team-lore-root>/wiki/projects/<project>/overview.md`
- `<chosen-team-lore-root>/wiki/projects/<project>/domains/`
- `<chosen-team-lore-root>/wiki/pitfalls/`
- `<chosen-team-lore-root>/wiki/principles/`

Preferred helper:
- `scripts/bootstrap_lore_wiki.sh`

Bootstrap steps:

1. Resolve project name from `PROJECT.md` frontmatter, else repo dir name
2. Resolve the install target explicitly; default to `/mnt/d/team-lore` in this environment if the user did not override it
3. Ensure the shared repo exists and is git-backed
4. Ensure the wiki root and base directories exist
5. Copy template pages if missing
6. Seed one project overview page and one starter domain page using retrieval-ready templates
7. Update or create the global schema path (`team-lore: ...`)

Bootstrap is not complete merely because the files exist. Starter pages should already expose an agent-usable operating surface rather than prose-only placeholders.

---

## Phase 3 — Migrate legacy flat lore

If a legacy `LORE.md` is provided:

1. Copy it into `wiki/projects/<project>/legacy/LORE-legacy.md`
2. Create `migration-notes.md` in the same project directory
3. Record the split targets:
   - project overview
   - domain pages
   - pitfall pages
   - principle pages
4. Mark the flat file as compatibility-only, not the default retrieval path

Do not pretend a single copy operation completed semantic migration.

---

## Phase 4 — Verify installation

Minimum pass conditions:

- shared repo is a git repo
- wiki root exists
- project overview exists
- starter domain page exists
- starter overview and domain pages expose retrieval-ready sections such as applicability, top facts, watchpoints, and next-hop guidance
- global schema points to the wiki root
- project-local `logs/` remain outside the shared repo
- chosen install path is reported back to the user

Use `evals/run-bootstrap-checks.sh` for fixture validation.

---

## Output format

When the install or migration finishes, report:

1. mode used: fresh / bootstrap / migration
2. selected install path and whether it was defaulted or explicitly provided
3. shared repo path
4. created or verified files
5. git state
6. any remaining manual follow-up

---

## Validation assets

- `evals/SKILL-EVAL.md`
- `evals/evals.json`
- `evals/README.md`
- `evals/run-bootstrap-checks.sh`
