## Context

The repository now has a bilingual onboarding README, but it is still optimized for completeness over immediate scan value. The Hermes README uses a stronger sequence:

- bold identity statement
- quick install block
- command-oriented getting started
- compact comparison tables
- documentation index table

That structure is useful here because this repo is also an installable workflow surface, not just a documentation dump. However, this repo must preserve its own constraints:

- Chinese-first main content
- English as a separate parallel section
- no false claims about runtime surfaces that are not actually shipped
- no implication that the Feishu source is already fully synced

## Goals / Non-Goals

**Goals:**
- Make the root README feel more like a high-signal entrypoint and less like a passive repo summary.
- Preserve bilingual readability with separate Chinese and English sections.
- Keep installation and runtime guidance consistent with the actual repo contents.
- Ensure bootstrap-generated README follows the same shape.

**Non-Goals:**
- Rebrand the project around Hermes or copy its wording.
- Introduce badges, external marketing assets, or unsupported install promises.
- Change bootstrap behavior beyond the generated README content.

## Decisions

### 1. Keep the repository's bilingual rule, but adopt Hermes-like section order

The new README will borrow structure, not wording. Chinese comes first, English follows as a separate mirrored section. Each section will use a Hermes-like sequence:

1. identity / why this repo exists
2. quick install
3. getting started commands
4. runtime quick reference
5. documentation map

This gives the repo the same “scan in one minute” feel without violating the language policy.

### 2. Prefer command blocks and tables over long prose

Hermes is effective because it lets readers spot the first command, first workflow, and next docs hop quickly. This repo README will therefore compress setup and usage into:

- one quick-install block
- one getting-started command block
- one runtime quick-reference table
- one documentation map table

### 3. Keep truthfulness over symmetry

The README must still state that Cursor is an adapter target rather than a shipped runtime surface. Hermes can claim concrete runtime support because it ships those surfaces. This repo will keep the same structure but only claim what is actually present.

## Risks / Trade-offs

- [README becomes too product-like and loses repo specificity] → Anchor every section in actual repo paths and commands.
- [Hermes inspiration turns into wording drift] → Reuse layout patterns, not copied prose.
- [Bootstrap template diverges again] → Update the template in the same change.
- [English section drifts from Chinese section] → Mirror section headings and command lists across both sections.

## Migration Plan

1. Rewrite the root README into the new layout.
2. Mirror the same layout in `scripts/bootstrap_assets/README.md.template`.
3. Verify the bootstrap test still passes and that generated README files exist with the new structure.

## Open Questions

- None. The source inspiration and repository constraints are clear enough for implementation.
