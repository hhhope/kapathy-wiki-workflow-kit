# Design: Replace Account H5 SVG Visuals With Image Model Outputs

## Image Model Direction

Generate polished technical infographic images rather than deterministic SVG
diagrams. The images should look like internal engineering training visuals:
clean, professional, technical, source-aware, and readable in an H5 page.

## Text Accuracy Boundary

Image models may distort dense Chinese text. To keep the output useful:

- Prompts should request large, sparse, high-level Chinese labels only.
- Dense explanations remain in the surrounding H5 text.
- Generated images are accepted only if the visual structure is useful and
  major labels are not visibly broken.
- If a generated image has broken text, regenerate once with fewer labels.

## Asset Plan

Use new filenames so historical SVG-derived assets are not overwritten:

- `account-capability-map-ai.png`
- `account-system-architecture-ai.png`
- `account-core-chain-ai.png`
- `nirvana-project-entry-map-ai.png`
- `account-technical-roadmap-fishbone-ai.png`

## Verification

- Confirm generated files exist in the workspace.
- Inspect each generated image visually.
- Run HTML parser.
- Run H5 asset-reference grep for `-ai.png` filenames.
- Run sensitive-info grep across H5 and generated asset filenames / prompt
  record.
- Take desktop and mobile screenshots and inspect that the new images render.
- Run `git diff --check`.
- Run `openspec validate replace-account-h5-svg-with-image-model --strict`.
