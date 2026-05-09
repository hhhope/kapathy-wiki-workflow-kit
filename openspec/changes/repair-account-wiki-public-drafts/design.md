## Scope

This change repairs the local Account Wiki public-draft package after the
failed reference-readback correction recorded in
`wiki/ops/team-knowledge-base-overview-report-gate-review.md`.

The repair covers four workstreams:

1. local draft content for runtime and validation/cases
2. local visual assets for runtime and validation/cases
3. gate-review evidence and behavior replay
4. `infographic-onepager` skill gap evaluation and minimal repair if needed

## Current State

- `openspec list` shows the relevant prior changes as complete:
  `add-public-report-quality-gate`,
  `connect-learning-capture-to-output-gates`, and
  `route-complex-public-reports-to-reviewer`.
- The existing gate-review artifact freezes the five-article Feishu packet as a
  failed draft after reference readback.
- `wiki/reports/team-knowledge-base-runtime.md` is mostly a staged routing
  table. It does not yet narrate a real material journey from intake to reuse.
- `wiki/reports/team-knowledge-base-validation-cases.md` has only summary-level
  evidence. It does not yet expose concrete replay, failed-freeze, Feishu
  readback, and skill RED/GREEN cases as reviewable data.
- `wiki/reports/account-wiki-visuals.html` contains overview and generic visual
  cards. It lacks dedicated runtime and validation/cases visuals.
- Reference images `14.png` through `17.png` were found outside the repository
  at `/mnt/c/Users/yan/Desktop/1/`. They are 1672x941 horizontal hand-drawn
  teaching cards. They support a chapter-card pattern rather than a vertical
  one-page infographic.

## Repair Strategy

### Runtime Page

Rewrite the runtime page around a concrete material journey:

- input arrives
- source is preserved
- route is selected
- draft / learning / governance path diverges
- evidence is written back
- public output is gated
- closeout records what was reused and what remains candidate

The page should keep reader-facing language and avoid internal gate jargon unless
translated into a reader-facing decision.

### Validation And Cases Page

Rewrite the validation/cases page as an evidence ledger:

- reference readback failure and freeze
- Feishu update/readback checks
- public-report gate RED/GREEN corrections
- learning-capture output-use mapping
- visual gate correction
- remaining non-claims

Evidence must distinguish:

- completed proof
- manual replay proof
- local draft proof
- missing final publication proof

### Visuals

Update the local visual artifact with two dedicated diagrams:

- runtime one-flow: source -> route -> asset -> output -> writeback
- validation one-flow: claim -> evidence -> replay -> gate decision -> boundary

The diagrams should reuse the hand-drawn teaching-card language from the
reference style without copying external content directly. Chinese text must be
readable and diagram roles must be explicit.

### Skill Gap

Evaluate `infographic-onepager` against the failed Account Wiki scenario. The
minimum gap under test is:

- Account Wiki multi-page article sets should not silently become a single
  generic onepager.
- Runtime and validation/cases pages need their own visual jobs, not only an
  overview poster.
- Short chapter-supporting visuals should be allowed to become horizontal 16:9
  teaching cards when the content does not need a dense one-page infographic.
- Reference images should contribute structure, density, hierarchy, and visual
  language, not copied subject matter.

If the skill is changed, record RED/GREEN evidence in this change's
`evaluation.md` before marking the task complete. If the selected skill file is
outside the repository writable root, request approval before editing it.

## Verification

- OpenSpec strict validation for this change.
- Static content checks for required runtime and validation evidence headings.
- Visual artifact check for dedicated runtime and validation/cases sections.
- Behavior replay in `evaluation.md` for the failed packet and skill gap.
- Feishu sync is allowed only after explicit user approval, with update logs,
  media insertion evidence, and read-back verification recorded in the
  gate-review artifact.
- If image-bearing Feishu documents freeze Codex or the Feishu client,
  read-back evidence remains audit-only and further image-included sync is
  blocked for this change.
