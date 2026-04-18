---
project: report-wiki-portfolio
status: active
owner: yan
source_of_truth: openspec
---

# Report Wiki Portfolio

## Purpose

This repository is the durable markdown knowledge base for recurring reports, meeting-derived materials, and topic-based reporting assets. It exists to turn scattered reporting inputs into a reusable wiki structure that supports archiving, retrieval, drafting, and review.

## Operating Model

- OpenSpec owns change lifecycle and implementation progress.
- `wiki/` owns durable knowledge, templates, and navigation.
- External systems such as Feishu are treated as source evidence, not the long-term knowledge layer.
- AI-generated content is allowed as a draft aid, but it must remain visibly distinct from approved human conclusions.

## Source Assumptions

- The main upstream inputs are Feishu documents, meeting notes, and periodic reporting materials.
- Early ingestion may be manual or link-based before sync automation exists.
- A source can feed multiple downstream views across topic, audience, and time period.

## Repository Shape

- `openspec/` stores change artifacts and task progress.
- `wiki/` stores report knowledge, templates, and operating guidance.
- `logs/` may be added later for implementation deviations and review notes.

## Success Criteria

- A new source can be recorded once and reused across domain, report, and timeline views.
- A contributor can understand where to place new material within minutes of opening the repo.
- The structure remains useful without automation and becomes stronger when AI or sync tooling is added.
