# kapathy-wiki-workflow-kit

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

## Knowledge Views

The wiki is organized around four first-level views:

- `domains/`: business topics and thematic knowledge
- `reports/`: audience-oriented or deliverable-oriented report views
- `timeline/`: time-based report views
- `sources/`: evidence pages for Feishu docs and other upstream material

## Initial Goal

The current milestone is to bootstrap the wiki skeleton and management model. It does not yet implement Feishu sync or automated AI pipelines, but it establishes the structure those workflows will use.
