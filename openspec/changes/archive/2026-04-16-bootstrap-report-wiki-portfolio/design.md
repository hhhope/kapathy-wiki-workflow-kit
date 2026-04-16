## Context

The repository currently contains only a placeholder `README.md` and an initialized OpenSpec config. There is no project identity file, no wiki entry point, and no stable shape for storing report knowledge. The reporting material itself is expected to come from Feishu documents, meeting notes, and periodic report outputs, which means the first implementation must create a repository structure that can absorb external sources without forcing immediate full-content migration.

The design must support two parallel needs:
- A human-maintained markdown wiki that remains usable without automation.
- A future AI workflow that can ingest source metadata, generate summaries, propose links, and assemble report drafts from indexed knowledge.

## Goals / Non-Goals

**Goals:**
- Establish the repository as a report knowledge base with a defined `PROJECT.md`, wiki index, and stable navigation model.
- Create four top-level wiki domains that separate business topics, report outputs, time views, and source evidence.
- Standardize a page metadata shape so pages can be indexed along topic, audience, period, and status.
- Provide starter templates and sample pages that prove the structure can represent Feishu-backed material and report drafting flow.
- Leave clear extension points for later automation around source syncing and AI-generated content.

**Non-Goals:**
- Implement Feishu API syncing in this change.
- Build retrieval, embedding, or agent runtime code.
- Migrate all existing report material into the wiki.
- Finalize a production-grade governance model for every future report type.

## Decisions

### Decision: Use one repository as a knowledge mother-ship
The repository will remain a single git repo that stores the durable markdown layer for report knowledge. This avoids splitting a still-forming reporting system into multiple repos too early.

Alternatives considered:
- Separate repos by business stream: rejected because source documents and report outputs cross-reference heavily.
- Keep only a flat `docs/` tree: rejected because it weakens later AI indexing and human navigation.

### Decision: Use four top-level wiki domains with cross-links instead of a single tree
The wiki will contain four stable root sections:
- `domains/` for business topic views
- `reports/` for deliverable and audience views
- `timeline/` for time-based views
- `sources/` for evidence and external source pages

This preserves multiple navigation paths without duplicating knowledge pages. A source or report item can be referenced from several index pages.

Alternatives considered:
- Only topic-first hierarchy: rejected because report consumers often start from audience or period.
- Only time-first hierarchy: rejected because it fragments reusable topic knowledge.

### Decision: Use lightweight frontmatter as the page contract
Each durable wiki page will use YAML frontmatter with a small shared field set:
- `title`
- `type`
- `domain`
- `audience`
- `period`
- `source_links`
- `status`
- `updated_at`
- `ai_generated`

This keeps the pages readable as plain markdown while giving future automation stable fields to parse.

Alternatives considered:
- No frontmatter, headings only: rejected because machine indexing becomes brittle.
- A separate registry file for all metadata: rejected because page-local truth is easier to maintain.

### Decision: Treat external systems as source-of-evidence, not source-of-truth for the wiki
Feishu documents remain authoritative raw sources in the short term, but the wiki is the long-lived retrieval and synthesis layer. Source pages will record links, summaries, ownership hints, and related report indexes without requiring full-body mirroring by default.

Alternatives considered:
- Copy every source document into markdown immediately: rejected because the migration cost is high and early structure matters more than full capture.
- Keep only Feishu links without local metadata: rejected because it blocks useful indexing and AI-assisted reuse.

### Decision: Model AI involvement as explicit workflow stages
The wiki will reserve explicit sections and fields for:
- source ingestion notes
- AI summary drafts
- relationship suggestions
- report draft assembly
- human review signoff

This prevents AI output from being mixed with accepted human conclusions and keeps later automation backwards-compatible with the markdown structure.

Alternatives considered:
- Hide AI usage entirely inside prompts: rejected because there would be no persistent audit trail.
- Generate final reports directly from sources only: rejected because users need an intermediate knowledge layer.

## Risks / Trade-offs

- [Risk] The initial taxonomy may be too coarse for some business lines. → Mitigation: keep the first-level domains stable and allow sub-pages to evolve underneath them.
- [Risk] Manual metadata upkeep may drift before automation exists. → Mitigation: keep the field set small and provide templates plus sample pages.
- [Risk] Feishu links may become dead or permission-limited. → Mitigation: store summary context and source ownership hints alongside the link.
- [Risk] AI-generated summaries could be mistaken for approved conclusions. → Mitigation: mark AI-originated content explicitly with frontmatter and section labels.
- [Risk] The repo may accumulate many placeholder pages without operational value. → Mitigation: require each root section to include at least one sample page and an intended usage note.

## Migration Plan

1. Add `PROJECT.md` so the repository has a declared purpose and operating model.
2. Replace the template `README.md` with repository-specific onboarding guidance.
3. Create the `wiki/` root, top-level index, and four root section indexes.
4. Add reusable templates for source pages, report pages, timeline pages, and domain pages.
5. Add sample content that demonstrates one source flowing into a domain view, a time view, and a report draft.
6. Document the intended AI workflow as scaffolding only, without claiming full automation is implemented.

Rollback strategy:
- The change is documentation-only. Rollback is a straightforward revert of the created files if the structure proves unsuitable.

## Open Questions

- Which Feishu document classes should be prioritized first for semi-automatic syncing after the skeleton is validated.
- Whether later report drafts should live only in `wiki/reports/` or also under project-specific subtrees once the taxonomy grows.
