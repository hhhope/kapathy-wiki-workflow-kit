## Context

The repository already defines a canonical cross-runtime installer model in wiki and ADR content, but the user-facing entrypoints are fragmented:

- `main` still presents an almost empty root README.
- The richer branch README is English-only and does not lead Chinese readers through setup.
- The bootstrap script installs only part of the documented kit and omits `inbox/README.md` and `scripts/inbox_intake.py`.
- The verification script assumes a fixed install shape and reports false failures for optional modes.
- Repo-local `openspec-*` skills were locally expanded to reference tools and slash commands that do not exist in the current Codex environment.

This is a cross-cutting change because it touches public docs, bootstrap behavior, verification logic, and behavior assets that shape how contributors use OpenSpec in the repo.

## Goals / Non-Goals

**Goals:**
- Make the root README the authoritative bilingual entrypoint for first-time readers.
- Ensure bootstrap output matches the documented quick-start and minimum runtime surface.
- Make verification mode-aware so optional installation modes do not fail by default.
- Keep the OpenSpec CLI as the truth source while removing misleading runtime assumptions from repo-local skills.
- Record the current gap between the repository and the referenced Feishu article without pretending the article body has already been synced.

**Non-Goals:**
- Build full Cursor adapter files or new runtime-specific automation beyond documenting current boundaries.
- Expand inbox intake logic beyond ensuring the minimum entrypoints are installed and documented.
- Sync or rewrite the entire Feishu article body inside the repository.
- Refactor unrelated wiki structures, examples, or reporting content.

## Decisions

### 1. Root README becomes the canonical bilingual onboarding surface

The repository needs one obvious entrypoint. The root README will become Chinese-first with a separate English section, following the repo language policy rather than mixing both languages inside the same paragraph. This keeps Chinese readers on the primary path while still giving English readers a complete install and orientation flow.

Alternative considered: keep README short and link out to wiki pages. Rejected because new users should not need to discover the right wiki pages before understanding prerequisites and runtime boundaries.

### 2. Bootstrap installs the minimum runnable kit, not just a subset of docs

The bootstrap contract will explicitly include the inbox intake surface and any scripts that README presents as the minimum workflow path. If README tells users to run `scripts.inbox_intake`, the bootstrap output must contain that script and the inbox landing page.

Alternative considered: keep bootstrap minimal and reword docs around it. Rejected because the current repo position is that the validated kit is installable; reducing docs to match an incomplete bootstrap would preserve a broken first-run experience.

### 3. Verification becomes installation-mode aware

The verification script will classify required paths by installation mode instead of assuming a single fixed layout. Required paths will be split into:

- always required
- required when OpenSpec is installed
- required when Obsidian is installed
- required when examples are installed

This removes false negatives and makes bootstrap options trustworthy.

Alternative considered: keep one strict default and document optional-mode failures. Rejected because verification should confirm the selected installation, not punish valid omissions.

### 4. Repo-local OpenSpec skills describe current Codex behavior, not hypothetical tooling

The current runtime has a working OpenSpec CLI but not the exact tool names and slash-command shell assumed by the modified skill text. The skills will be rewritten to:

- keep CLI-first instructions
- use current interaction mechanisms
- avoid references to nonexistent helper tools
- stay compact per the skill authoring contract

Alternative considered: keep the expanded text and only add a note about environment differences. Rejected because the wrong tool references are the main source of confusion and make the skills operationally misleading.

### 5. Feishu article alignment is recorded explicitly as a comparison page

The repository cannot currently read the referenced Feishu page body from this environment. Instead of blocking all entrypoint work, the repo will add a comparison page that records:

- the original link
- what the repository already reflects
- what still requires source sync

This preserves provenance and avoids pretending the current docs are a verified transcription.

## Risks / Trade-offs

- [README grows too large] → Keep sections short, front-load quick start, and move detailed comparison context to wiki.
- [Bootstrap changes drift from verification again] → Add tests that assert installed paths and verification outcomes together.
- [Skill rewrite changes behavior unintentionally] → Capture baseline and after-change evaluation in `evaluation.md` using the current broken assumptions as RED evidence.
- [English section drifts from Chinese section] → Keep both sections parallel in structure and verify commands/paths are shared.
- [Users infer Cursor native support from documentation] → State adapter boundary explicitly and avoid promising generated `.cursor/rules/` output in this change.

## Migration Plan

1. Create and approve this OpenSpec change with updated specs and tasks.
2. Add failing tests for bootstrap and verification behavior.
3. Update bootstrap and verification code until tests pass.
4. Rewrite README and Feishu comparison/source guidance to match the implemented contract.
5. Update repo-local OpenSpec skills and record evaluation evidence.
6. Re-run script-level verification and targeted OpenSpec CLI checks before finalizing the change.

Rollback is low-risk because the change is limited to docs, scripts, and behavior assets; reverting the commits returns the old onboarding and skill behavior.

## Open Questions

- None for implementation. The runtime scope, bilingual README shape, and Feishu handling strategy are now fixed by the agreed plan.
