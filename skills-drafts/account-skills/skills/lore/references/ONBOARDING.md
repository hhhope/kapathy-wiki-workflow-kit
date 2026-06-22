# Lore Wiki — Onboarding

> Do this once per engineer. Prefer 10-15 minutes over improvising every task.

If the user asks the agent to perform this setup directly, route to `skills/lore-bootstrap/` instead of treating this file as a manual checklist only.

---

## Step 1: Clone the shared wiki repo

```bash
git clone {team-lore-repo-url} /mnt/d/team-lore
```

Optional but recommended:
- Open `/mnt/d/team-lore` as an Obsidian vault
- Use git for all durable changes

If you need another location, decide it explicitly during install and keep the same path in the agent schema. Do not silently fall back to `~/team-lore`.

---

## Step 2: Set agent identity and paths

```bash
mkdir -p ~/.claude
cp /mnt/d/team-lore/templates/global-CLAUDE.md ~/.claude/CLAUDE.md
# Edit member: [your-name]
```

The schema should point to the shared wiki root, not a flat `LORE.md` file.

---

## Step 3: Initialize a project area in the wiki

```bash
mkdir -p /mnt/d/team-lore/wiki/projects/{project-name}/domains
cp /mnt/d/team-lore/templates/index.md /mnt/d/team-lore/wiki/index.md
cp /mnt/d/team-lore/templates/project-overview.md \
  /mnt/d/team-lore/wiki/projects/{project-name}/overview.md
```

Create additional pages from templates as needed:
- `domains/{domain}.md`
- `pitfalls/{pitfall}.md`
- `principles/{principle}.md`

---

## Step 4: Prepare the project repo

In the project repository:

```bash
mkdir -p logs
echo "logs/" >> .gitignore
git add .gitignore
git commit -m "[{project}] init local lore logs"
```

`PROJECT.md` stays in the project repo.  
OpenSpec change docs stay in the project repo.  
Lore wiki pages stay in the shared wiki repo.

---

## Step 5: Fill the minimum memory set

For a new project, complete:
- `PROJECT.md`
- `wiki/projects/{project}/overview.md`
- one or two `domains/*.md` pages

For an existing project, run code archaeology on the riskiest module first and convert stable findings into wiki pages.

---

## Daily workflow

```text
Start task
  -> confirm active OpenSpec change
  -> read PROJECT.md
  -> read wiki/index.md
  -> read project overview + matching domain/pitfall/principle pages
  -> execute with self-check

During task
  -> log deviations and new facts

Weekly
  -> weekly review
  -> absorb accepted logs into wiki pages
  -> update index
  -> commit wiki diff

Periodic
  -> lint lore
  -> split oversized pages, fix stale links, remove orphan pages
```

---

## Quick commands

| Say | Agent does |
|-----|-------------|
| `lore: {keyword}` | Search index, then target pages |
| `weekly review` | Absorb logs into wiki pages |
| `code archaeology {path}` | Bootstrap stable knowledge from code |
| `lint lore` | Health-check the wiki |

## Install choice reminder

When using `lore-bootstrap`, the output must say:
- chosen install path
- whether it was explicit or defaulted
- repo root and wiki root
