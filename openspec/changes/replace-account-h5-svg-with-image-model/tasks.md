# Tasks

- [x] 1. Record image-model visual replacement baseline
  - Create OpenSpec artifacts for replacing SVG-derived visuals.
  - Validate the change before implementation.

- [ ] 2. Generate image-model visual assets
  - Generate five bitmap visuals with the built-in image generation tool.
  - Save final selected assets under
    `wiki/reports/assets/account-group-onboarding-h5/`.
  - Inspect generated visuals and regenerate once if a visual has unusable text
    or structure.

- [ ] 3. Update H5 references
  - Replace displayed SVG-derived PNG references with image-model PNG assets.
  - Keep section order, headings, and surrounding explanations.

- [ ] 4. Verify and finalize
  - Run HTML parser.
  - Run asset-reference grep.
  - Run sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.
  - Update gate review with prompts and evidence.
  - Run `openspec validate replace-account-h5-svg-with-image-model --strict`.
