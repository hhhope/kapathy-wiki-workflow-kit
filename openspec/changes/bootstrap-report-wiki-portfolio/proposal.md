## Why

The repository is still an empty template, while the actual reporting material is spread across Feishu docs, meeting notes, and time-based updates. We need a stable lore-style wiki structure so reports can be archived, cross-linked, and reused instead of being rebuilt from scattered source documents.

The first step is to create the knowledge skeleton and operating model, not a full automation platform. That skeleton must support future AI workflows for ingestion, retrieval, report drafting, and review.

## What Changes

- Replace the placeholder repository setup with a project definition and a wiki-first documentation structure.
- Introduce a report knowledge model that indexes content across business topic, report audience, time period, and source evidence.
- Add source pages and templates that can represent Feishu documents and other external materials without duplicating content by default.
- Add AI workflow scaffolding for summary generation, linkage, report drafting, and review handoff.
- Create an OpenSpec-backed implementation plan so the wiki skeleton can be extended incrementally.

## Capabilities

### New Capabilities
- `report-wiki-structure`: Define the top-level wiki layout, index pages, templates, and metadata model for report knowledge.
- `source-ingestion-index`: Define how external sources such as Feishu docs are represented, linked, and tracked inside the wiki.
- `ai-report-workflow`: Define the AI-assisted workflow for summarization, retrieval, draft generation, and review-ready report assembly.

### Modified Capabilities

None.

## Impact

- Affects repository documentation entry points such as `README.md` and a new `PROJECT.md`.
- Adds wiki content, templates, and sample pages under `wiki/`.
- Adds OpenSpec change artifacts under `openspec/changes/bootstrap-report-wiki-portfolio/`.
- Establishes the contract for later automation around Feishu syncing and AI-powered report generation.
