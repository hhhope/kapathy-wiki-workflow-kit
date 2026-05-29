# Tasks

- [x] 1. Record card-layout repair baseline
  - Create OpenSpec artifacts for removing card-style visual dominance.
  - Validate the change before implementation.

- [ ] 2. Replace card-style visual system
  - Change repeated content from boxed cards to technical handout rows,
    matrices, and definition blocks.
  - Keep source-backed diagrams as primary visuals.
  - Preserve section order and account-domain content.

- [ ] 3. Verify reader-facing result
  - Run HTML parser.
  - Run required title / AI-offering grep.
  - Run removed-title and sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.
  - Update gate review.
  - Run `openspec validate replace-account-h5-card-layout --strict`.
