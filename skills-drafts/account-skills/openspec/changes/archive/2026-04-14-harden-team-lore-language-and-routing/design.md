## Context

The archived first slice should certify only retrieval-first page shape, fresh-context startup, and minimal alias-based mixed-language routing.

Two known gaps remain:

1. mixed-language support is still partial at first-load interpretation time
2. routing evidence is representative and manual, not yet a stronger automated contract

This follow-up keeps those gaps separate from broad historical backfill.

## Goals / Non-Goals

**Goals:**
- raise mixed-language support for the highest-value shared pages above alias-only routing
- automate more of the Lore/OpenSpec/Graphify routing checks
- preserve the first-slice contract instead of redefining it

**Non-Goals:**
- full translation of the historical `team-lore` corpus
- replacing Lore with Graphify or merging OpenSpec into the knowledge layer
- broad wiki taxonomy redesign

## Decisions

### Decision: Keep scope on high-value pages and routing checks
Only harden entry pages and the most reused durable pages where mixed-language interpretation still matters. This keeps the follow-up bounded and testable.

### Decision: Treat bilingual hardening as loading quality, not translation completeness
The follow-up should improve first-load interpretation for mixed-language prompts, not require mirrored body content everywhere.

### Decision: Add automated routing checks without pretending classification is solved generically
The follow-up should script stronger representative routing cases and keep the contract explicit, but it should not overclaim universal classifier quality.

## Risks / Trade-offs

- [Risk] Language hardening grows into a translation project. -> Mitigation: keep focus on entry pages, summaries, and operating sections only.
- [Risk] Routing automation still tests only curated cases. -> Mitigation: state that limitation and keep manual mixed cases as a second signal.
- [Risk] Follow-up scope drifts into broad lore cleanup. -> Mitigation: exclude historical backfill and require page-class prioritization up front.

## Acceptance Boundary

This follow-up is successful when it certifies a stronger selected slice, not the whole `team-lore` corpus.

This follow-up may claim:

1. the selected startup pages expose mixed-language first-load support beyond aliases
2. the selected slice preserves retrieval-first operating sections while adding bilingual startup support
3. representative `process / lore / graphify / mixed` routing cases are script-checked rather than explained only in prose

This follow-up must not claim:

1. full bilingual completion of `team-lore`
2. universal routing or classifier completeness
3. full historical backfill beyond the selected slice
