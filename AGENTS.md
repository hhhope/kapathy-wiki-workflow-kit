# Repo Instructions

This file adds repository-specific constraints for `report-wiki-portfolio`.

## OpenSpec Trigger

- Treat changes to repository-default workflow, collaboration behavior, routing defaults, escalation boundaries, or default output rules as OpenSpec-level changes.
- For these changes, create or select an active OpenSpec change before editing `wiki/`, `scripts/`, `skills-drafts/`, or other repository guidance files.
- Do not ship temporary wiki-only or skill-draft-only fixes first and backfill OpenSpec later.
- If the user asks to change how Codex should usually behave in this repository, assume it is a workflow change unless the request is explicitly limited to one page or one one-off run.

## Decision Observability

- For workflow-level changes, record stable decisions in `wiki/adr/` rather than leaving the rationale only in chat history.
- If the work is interrupted, blocked, or leaves an unresolved branch, write a checkpoint note in the active change artifacts or linked repo guidance before stopping.
- A valid checkpoint must state:
  - what was decided
  - what is still open
  - what the next action is
- Do not claim a future “tighter process” unless the new constraint is written into repo-visible artifacts.
- OpenSpec change artifacts still own current scope, task progress, and interruption checkpoints; `wiki/adr/` owns stable project decisions.

## High-Frequency Principles

- The repo's principle-skills layer lives under `.codex/skills/` and complements, but does not replace, repo governance or workflow skills.
- Any active change that publishes or semantically edits `.codex/skills/` must include `evaluation.md` in the change directory.
- `evaluation.md` is the behavior-proof artifact and must include: `Baseline Scenarios`, `Before Results`, `After Results`, and `Residual Risks`.
- Use `clarify-before-acting` when a request still has material ambiguity and the agent is about to silently choose an interpretation.
- Use `simplicity-first` when the solution is starting to grow speculative abstractions or future-proofing not required by the task.
- Use `surgical-changes` when the edit risks expanding into unrelated cleanup, formatting, or adjacent refactors.
- Use `verify-before-claiming` when the agent is about to say something is complete, fixed, or synced without a fresh check.

## Skill Authoring Contract

- Repo-local `.codex/skills/*` files are English-first behavior assets. Do not let the wiki's Chinese-first policy bleed into `SKILL.md`.
- Keep repo-local `SKILL.md` files compact. Put only trigger conditions, hard rules, anti-patterns, and short loading pointers in the main body.
- Move long examples, templates, or heavy format details into linked `references/` files when they would bloat trigger-time retrieval.
- Before authoring or editing a repo-local skill, read this repo `AGENTS.md` and any repo pages that define delivery boundaries for that workflow.
- If a skill affects Feishu-facing, reader-facing, or other delivery-sensitive outputs, make the repo boundary explicit in the skill or reference the governing repo document directly.
- Semantic skill changes must include local pressure-test evidence in `evaluation.md`: `Pressure Scenarios`, `RED Baseline`, `GREEN Result`, and `Residual Risks`.
- Multi-end or rollout proof is optional follow-up evidence, not the minimum completion gate for a semantic skill change.

## Archive Review Default

- In this repository, when an OpenSpec change becomes `complete`, the default next action is `archive review`.
- `complete` means stop implementation; it does not mean the change is already archive-ready.
- If archive review finds an ordinary closing tail such as missing sync or final verification, keep the blocker visible in `tasks.md` and explain the reason and next action in git history.
- If archive review depends on scope ambiguity, reusable governance judgment, or context that would be hard to recover from `tasks.md` and git history alone, add `archive-review.md` inside the current change directory.
- Archive review must also check whether the completed change generated disagreement material that:
  - should remain in method or `wiki/ops retro` form
  - should already be promoted to `ADR`
  - was flattened away without a durable record
- Only archive a change after archive review passes.

## Explore Trace Default

- In this repository, every `openspec-explore` run must leave a repo-visible trace in `wiki/ops/` before the exploration continues.
- The trace reuses the existing `intake` page type instead of creating a new page type.
- If the explore request clearly continues the same topic thread, update the existing `wiki/ops/` trace instead of creating a duplicate page.
- The explore trace records the opening context for the topic; it does not replace formal OpenSpec artifacts when the work later becomes a scoped change.
- The explore trace should stay lightweight and capture at least the trigger question, current focus, current hypotheses, open questions, and next step.

## Conversation Handoff Default

- When the live conversation repeatedly converges on the same north-star goal, the default behavior is to enter `handoff mode` rather than keep treating the exchange as disconnected Q&A.
- Handoff mode is triggered by repeated north-star pull, not by a single hard counter. Same-topic discussion beyond two rounds is a strong signal, but not the only trigger.
- Higher-priority signals include:
  - the user repeatedly correcting the framing back to the same goal
  - the user rejecting local fixes and restating the larger objective
  - the user explicitly asking for the topic to be remembered, reused, or made durable
- Handoff mode should preserve at least:
  - north star
  - constraints
  - failure modes
  - preferences
  - disagreements
  - open questions
  - candidate practices
  - repo targets
- The first version of handoff mode is capture-and-structure only. It must not auto-edit `.codex/skills/*`, `AGENTS.md`, or other repository-default rules directly from conversation state.
- Durable output should go to the lowest layer that preserves recovery:
  - `trace / intake` for newly opened operating topics
  - `retro` for drift, disagreement, or repeated process confusion
  - `ADR` for stable cross-change decisions
  - `OpenSpec change` for scoped workflow or implementation changes
  - `archive-review.md` for governance-heavy closure reasoning on a current change

## Example-Driven Capture Default

- When the user provides an external repo, README, article, or concrete in-chat example and the discussion extracts a reusable learning, the default behavior is to create or update a repo-visible wiki record in the same turn.
- Do not wait for an extra reminder such as `write this to wiki` when the discussion has already clarified:
  - what was reused
  - what was modified or rejected
  - what is still not formalized
  - what the next step is
- This rule is about extracted learning, not raw link presence. Do not create a wiki page for every external link or pasted example.
- Minimum record fields for example-driven capture:
  - time
  - source reference
  - what was reused
  - what was modified
  - what was not yet formalized
  - repo target
  - next step
- Default routing:
  - `wiki/ops` for workflow, governance, and operating learnings
  - `wiki/examples` for validated output-shape examples
  - `wiki/team-lore-candidates.md` only after a project-local page already exists and the learning appears reusable across projects

## Disagreement Management Default

- When a live disagreement is still doing goal-calibration work, do not rush to compress it into `ADR`, spec, skill, or route-level explanation.
- Preserve the disagreement as calibration material first, especially when the user keeps rejecting the current framing or the discussion is still changing what the real object is.
- Minimum preserved raw material before summary or promotion:
  - rejected framing
  - correction pressure
  - redirection moment
  - current clarity state
  - protected target, if visible
- Explicit anti-compression states:
  - `I haven't seen it clearly yet`
  - `We should not name the pattern yet`
- First positive naming is only valid when:
  - the rejected object has stabilized
  - redirection has occurred
  - the name explains the disagreement's evolution, not only the endpoint
- Default routing after the method layer:
- `wiki/ops retro` when the disagreement already needs repo-visible preservation but is not yet stable enough for `ADR`, spec, or skill
  - `ADR` when the disagreement has produced a stable cross-change decision
  - OpenSpec spec or repo-local skill only after the disagreement is stable enough to formalize

## Wiki Naming Model Default

- For new pages in evolution-bearing layers, use the `canonical object / artifact type` naming model.
- Version 1 covers only:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- For covered layers, the title core should express only:
  - canonical object
  - artifact type
- Do not use the title core to carry:
  - dates
  - status words
  - validation rounds
  - change identifiers
  - local symptom words such as `gap`, `issue`, `missing`, `leak`
- A topic only qualifies as a canonical object when it:
  - is not a one-time event
  - already spans at least two repository containers or artifact layers
  - can unify a real evolution chain instead of a temporary symptom
- First-wave canonical objects:
  - `disagreement-management`
  - `conversation-handoff`
  - `example-driven-capture`
- Cross-layer consistency is required across:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- Rollout rule:
  - strong for new pages
  - weak for existing pages until they are touched or intentionally migrated
- Current non-goals:
  - no immediate rename of existing pages
  - no directory migration
  - no graph metadata model yet
  - no relation-analysis or graph tooling yet

## Wiki Frontmatter Model Default

- For new pages in covered evolution-bearing layers, use the repository's minimal frontmatter model.
- Version 1 covers only:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- New covered-layer pages must include:
  - `canonical_object`
  - `artifact_type`
- New covered-layer pages should express direct structural relations through the shared field vocabulary:
  - `related_objects`
  - `derived_from`
  - `validates`
  - `formalizes`
- Optional helper fields in version 1:
  - `supersedes`
  - `replaces`
  - `notes_scope`
- Rollout rule:
  - strong for new pages
  - weak for existing pages until they are touched or intentionally migrated
- Current non-goals:
  - no graph extractor yet
  - no relation scoring yet
  - no bulk metadata backfill yet
  - no forced migration for old pages

## Wiki Graph Extraction Default

- Graph extraction is downstream of both:
  - the wiki naming model
  - the wiki frontmatter model
- Version 1 extraction only covers:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- Extraction output should preserve at least:
  - nodes with page path, canonical object, artifact type, and source layer
  - edges with source page path, relation type, and target
- Supported relation types in version 1:
  - `related_objects`
  - `derived_from`
  - `validates`
  - `formalizes`
- Optional relation types when present:
  - `supersedes`
  - `replaces`
- Extraction proof is structural proof only. Do not overclaim it as:
  - semantic completeness
  - graph quality scoring
  - graph UI readiness
- Unresolved pages may emit warnings; version 1 does not require semantic guessing to force full node coverage

## Wiki Relation Analysis Default

- Relation analysis is downstream of:
  - the wiki naming model
  - the wiki frontmatter model
  - wiki graph extraction
- Version 1 relation analysis only covers the graph extraction surface:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- Relation analysis output should preserve at least:
  - object coverage summary
  - artifact-type distribution
  - relation-type distribution
  - unresolved warning summary
  - proof-boundary notes
- Relation analysis may aggregate unresolved structure by layer, but it must not:
  - invent semantic identities for unresolved pages
  - overclaim retrieval quality
  - overclaim runtime routing readiness
  - treat structural analysis as rollout proof

## Wiki Semantic Scoring Default

- Semantic scoring is downstream of:
  - the wiki naming model
  - the wiki frontmatter model
  - wiki graph extraction
  - wiki relation analysis
- Version 1 semantic scoring only scores canonical objects already present in relation analysis
- Semantic scoring output should preserve at least:
  - object score summary
  - factor breakdown per object
  - unresolved repository context
  - proof-boundary notes
- Version 1 scoring must stay explicit and audit-friendly:
  - no embeddings
  - no hidden semantic guesses
  - no LLM-only score generation
- Semantic scoring must not overclaim:
  - retrieval quality
  - runtime routing readiness
  - semantic understanding of unresolved pages
  - rollout proof

## Wiki Utilization Layer Default

- Utilization guidance is downstream of:
  - the wiki naming model
  - the wiki frontmatter model
  - wiki graph extraction
  - wiki relation analysis
  - wiki semantic scoring
- Version 1 utilization should classify canonical objects into explicit bands such as:
  - `preferred`
  - `cautious`
  - `blocked`
- Utilization output must preserve:
  - explicit reasons
  - repository-level caution signals
  - proof-boundary notes
- Utilization guidance must not overclaim:
  - retrieval readiness
  - runtime autonomy
  - semantic understanding of unresolved pages
  - rollout proof

## Wiki Runtime Context Default

- Runtime-context bundling is downstream of:
  - the wiki naming model
  - the wiki frontmatter model
  - wiki graph extraction
  - wiki relation analysis
  - wiki semantic scoring
  - wiki utilization layer
- Version 1 runtime context should preserve distinct sections such as:
  - `preferred_context`
  - `supporting_context`
  - `blocked_context`
  - `runtime_caution`
- Runtime-context output must preserve:
  - reasons
  - usage guidance
  - repository-level caution
  - proof-boundary notes
- Runtime-context output must not overclaim:
  - retrieval readiness
  - runtime autonomy
  - unresolved page understanding
  - rollout proof

## Wiki Runtime Context Source Integration Default

- Runtime-context source integration is downstream of:
  - the wiki naming model
  - the wiki frontmatter model
  - wiki graph extraction
  - wiki relation analysis
  - wiki semantic scoring
  - wiki utilization layer
  - wiki runtime context
- Version 1 source integration should preserve distinct sections such as:
  - `preferred_sources`
  - `supporting_sources`
  - `blocked_objects`
  - `source_resolution_notes`
- Version 1 source integration must resolve only repository-local sources from:
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- Source-integration output must preserve:
  - concrete page-path references
  - source-layer identity
  - artifact-type identity
  - proof-boundary notes
- Source-integration output must not overclaim:
  - external retrieval readiness
  - runtime autonomy
  - unresolved page understanding
  - rollout proof

## Scope Of Policy

- Repository-default collaboration policy belongs in this repo first, not in global instructions by default.
- Only promote a policy to global guidance when it has been shown to generalize beyond this repository's material-processing workflow.

## Material Processing Default

- Formal material-processing workflow publication uses `.codex/skills/material-collaboration-defaults/SKILL.md`.
- `skills-drafts/` is draft space only; workflow changes cannot stop with an active draft `SKILL.md`.
- Before a workflow-level skill change is complete, every draft skill must be either promoted into `.codex/skills/` or explicitly retired.
- When the user drops materials and asks Codex to process them, do not stop at placeholder intake output.
- Default completion means readable `source` output first, then linked `ops` output when the material contains action signals.
- Ask the user only at real output fork-points, such as whether to update `html/h5/preview` artifacts in addition to wiki records.

## Meeting Note Output

- Formal meeting-note workflow publication uses `.codex/skills/meeting-note-output/SKILL.md`.
- `skills-drafts/meeting-note-output/` is draft space only; it does not count as a formally published repo skill.
- Manual agent role templates are not a substitute for meeting-note workflow routing.
- When handling meeting notes or transcripts, use the repository's fixed meeting-note format rather than a generic summary layout.
- The main meeting-note output must include: meeting metadata, core agenda, numbered topic sections, explicit final/rejected options when applicable, a structured action-item table, and a closing summary.
- Treat note text as the primary output and transcript text as supporting evidence for disputes or rationale.
- Default to a review version first. Review versions must include `待确认` and `需你澄清`.
- Do not publish or sync a final Feishu meeting note until unresolved confirmation items are either answered or explicitly marked as pending.
