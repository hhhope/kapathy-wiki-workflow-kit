# account-meeting-lore

Markdown-first report knowledge base for recurring business updates, meeting materials, and AI-assisted reporting workflows.

## What This Repo Is

This repository is the long-lived wiki layer for report assets. It is meant to absorb material from Feishu docs, meeting notes, and periodic deliverables, then reorganize that material into a structure that is easy to archive, search, cross-link, and reuse.

## Core Structure

- `PROJECT.md`: project identity, operating model, and source assumptions
- `openspec/`: change proposals, design docs, specs, and implementation tasks
- `wiki/`: durable knowledge pages, templates, source indexes, and AI workflow guidance

## How To Use It

1. Add or update source evidence under `wiki/sources/`.
2. Link that evidence into topic, report, and timeline pages instead of duplicating it.
3. Use `wiki/templates/` when creating new durable pages.
4. Keep AI-generated summaries or draft text clearly labeled for review.
5. Use OpenSpec changes for large structural or workflow updates.

## Codex Plugin

This repo also ships a repo-local Codex plugin for the LLM Wiki status surface.
From the repository root, add the local marketplace:

```bash
codex plugin marketplace add .
```

Restart or reload Codex after adding the marketplace. Wiki runtime commands:

- `/wiki:status`: refresh and summarize the generated wiki status surface.
- `/wiki:manifest`: inspect the generated source and routing manifest.
- `/wiki:inbox`: review pending inbox items that need wiki intake.
- `/wiki:query`: build bounded task-shaped context from route, context, and explicit text search evidence.
- `/wiki:graph`: expose the structural wiki graph layer.
- `/wiki:scorecard`: expose wiki scoring and utilization outputs.
- `/wiki:route`: expose runtime auto-routing suggestions.
- `/wiki:context`: expose the runtime context bundle.
- `/wiki:apply`: expose bounded self-directed execution suggestions.
- `/wiki:queue`: preview ready, decision-needed, and blocked wiki work without executing it.

These commands expose existing wiki runtime layers. They do not create, modify,
or archive OpenSpec changes.

The `/wiki:status` command contract lives in `commands/wiki-status.md`. It
refreshes `wiki/status/manifest.json` and `wiki/status/wiki-status.md` by running:

```bash
python3 scripts/build_wiki_status.py
```

## Knowledge Views

The wiki is organized around four first-level views:

- `domains/`: business topics and thematic knowledge
- `reports/`: audience-oriented or deliverable-oriented report views
- `timeline/`: time-based report views
- `sources/`: evidence pages for Feishu docs and other upstream material

## Initial Goal

The current milestone is to bootstrap the wiki skeleton and management model. It does not yet implement Feishu sync or automated AI pipelines, but it establishes the structure those workflows will use.
