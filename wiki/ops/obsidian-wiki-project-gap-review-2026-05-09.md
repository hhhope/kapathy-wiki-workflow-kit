---
layer: ops
domain: wiki
ops_area: learning-capture
canonical_object: obsidian-wiki-reference-gap-review
artifact_type: learning-note
related_objects:
- agent-readable-wiki
- learning-capture-routing
- account-knowledge-base-workbench
derived_from:
- https://github.com/Ar9av/obsidian-wiki
validates:
- readme-learning-capture
---

# obsidian-wiki project gap review / learning-note

## Time

2026-05-09

## Source

- `https://github.com/Ar9av/obsidian-wiki`
- Source class: implementation reference
- Source artifact type: GitHub repository README, setup notes, root agent context, and selected skill files
- Access date: 2026-05-09

## Admission And Score

| Criterion | Score | Note |
|---|---:|---|
| Source access and provenance | 20 / 20 | Stable public repo URL plus README, setup, agent context, and selected skills were accessible. |
| Evidence or method density | 23 / 25 | Repo includes concrete skill routes, ingest/status/query/lint/export workflows, and setup matrix. |
| Local capability gain | 22 / 25 | Strong comparison against this repo's wiki runtime stack and material-processing workflow. |
| Transfer path | 13 / 15 | Maps to wiki ops learning now; possible later OpenSpec changes for manifest/status/hot-cache only if selected. |
| Verification path | 12 / 15 | Local gaps can be checked with repo scripts, index coverage, and file presence. |

Total score: 90 / 100.

Decision: deep-read enough for gap review and record durable wiki learning.

## What Reused

- Treat the wiki as a compiled artifact maintained by agents, not as raw RAG or repeated summarization.
- Use an ingest ledger concept to track source path, timestamp/hash, produced pages, and stale-source delta.
- Add a cheap retrieval path before opening full pages: index, frontmatter summaries, targeted grep, then full page only when required.
- Separate read-side operations into status, query, lint, graph/export, and cross-linking instead of relying only on ad hoc agent reading.
- Keep image and transcript ingestion as first-class source modes, while marking interpretation and ambiguity explicitly.

## What Modified For This Repo

This repository already has a stronger governance and lifecycle stack than the reference repo:

- OpenSpec owns scoped workflow changes and completion boundaries.
- ADRs own stable decisions.
- `wiki/ops` owns repo-visible traces, retros, and learning notes.
- The agent-readable wiki stack already has naming, frontmatter, graph extraction, relation analysis, semantic scoring, utilization, runtime context, source integration, runtime routing, context injection, and self-directed execution layers.

So the useful transfer is not to copy the vault taxonomy. The useful transfer is to add missing operational surfaces around the existing stack:

- source manifest / delta status
- health and lint output for the whole wiki
- hot-cache or current-context summary
- query/status skills that are user-facing and cheap by default
- graph export or visualization artifacts that are consumable outside scripts
- claim-level provenance confidence for synthesized report knowledge, where needed

## Missing Points In This Repo

| Gap | Current repo state | Why it matters |
|---|---|---|
| Manifest ledger | Sources and ops pages exist, but no repo-wide `.manifest.json` equivalent tracking source hash, produced pages, and stale status. | We cannot answer "what changed since last ingest" without bespoke grep or manual inspection. |
| Wiki status dashboard | We have scripts and indexes, but no single user-facing status command/report for ingested, pending, stale, orphaned, and changed material. | Users keep asking "还有什么任务/缺什么"; status should be computed rather than reconstructed from memory. |
| Hot cache | We have `main-thread`, ops notes, and OpenSpec tasks, but no compact recent-activity snapshot updated after writes. | New sessions still need to crawl AGENTS, OpenSpec, index, and recent ops files. |
| Claim provenance mix | We use source pages, gate reviews, RED/GREEN evidence, and proof boundaries, but not a consistent extracted/inferred/ambiguous marker on ordinary wiki claims. | Reader-facing report knowledge can blur source facts, agent synthesis, and unresolved ambiguity. |
| Lifecycle/confidence fields | OpenSpec and ADR lifecycle are strong, but ordinary wiki pages do not carry per-page confidence or review lifecycle. | It is hard to distinguish draft synthesis from reviewed or verified knowledge outside OpenSpec artifacts. |
| Cross-link lint | We have graph extraction for covered evolution layers, but no whole-wiki lint for broken links, orphan pages, stale pages, or contradiction candidates. | The wiki can grow readable pages while losing graph hygiene. |
| Query skill | Runtime routing helps agents decide what to read, but there is no explicit repo-local "answer from wiki cheaply, with citations" workflow. | Agent responses still depend on ad hoc reading paths. |
| Export / viewer | We generate JSON samples and HTML report artifacts, but no standard whole-wiki graph export to browser/GraphML/Neo4j-like formats. | The structure is machine-readable for scripts, not yet broadly explorable by humans. |
| Cross-agent history ingest | We have rich Codex governance traces, but no controlled ingestion of Codex/Claude history into durable topic pages. | Useful decisions stay buried in sessions unless manually promoted. |
| Obsidian-compatible link mode | This repo favors Markdown paths and repo links; it does not optimize for Obsidian `[[wikilinks]]`. | Fine for Git/repo reading, but weaker if the target is Obsidian graph UX. |

## What Rejected Or Not Formalized

- Do not import the reference repo's full category taxonomy (`concepts`, `entities`, `skills`, `references`, `synthesis`, `journal`) as-is; this repo's `sources/domains/reports/timeline/ops` split is purpose-built for report workflows.
- Do not adopt automatic archive/rebuild as a default; this repo's OpenSpec archive review and ADR gates are stricter.
- Do not make image-bearing Feishu delivery part of this learning; the current Feishu image client-freeze boundary remains separate.
- Do not immediately create new runtime skills or scripts from this comparison; that would be an OpenSpec-level workflow change.

## Repo Target

Current target: `wiki/ops` learning record.

Possible future OpenSpec changes, if selected:

1. Add repo-wide source manifest and status report.
2. Add wiki lint/status command for broken links, stale pages, missing frontmatter, and orphan-adjacent pages.
3. Add a lightweight hot-cache page updated by material-processing and OpenSpec completion workflows.

## Next Step

Use this as a comparison map, not an accepted implementation plan. If the next task is to close one gap, start with manifest/status because it directly answers "what changed, what is pending, what is stale" and supports the rest of the operational surface.
