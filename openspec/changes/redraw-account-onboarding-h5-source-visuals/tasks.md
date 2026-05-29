# Tasks

- [x] 1. Record failed visual gate baseline
  - Mark the prior visual gate result invalid in the gate review.
  - Record why the box-heavy H5 failed the reader-facing Visual Gate.
  - Commit only OpenSpec and gate-review baseline files if needed.

- [x] 2. Produce standalone source-backed visuals
  - Create account capability map SVG.
  - Create account system architecture SVG.
  - Create account core chain SVG.
  - Create Nirvana/latest-project entry map SVG.
  - Verify the SVG files parse and do not contain sensitive source URLs,
    credentials, personal contacts, or excluded capability groups.

- [x] 3. Refactor the H5 around redrawn visuals
  - Add a source-visual index.
  - Replace the capability, architecture, core-chain, and active-project
    sections with image-first sections.
  - Keep the accepted section order and onboarding/AI content.
  - Preserve the sensitive-info boundary.

- [x] 4. Run visual and content verification
  - Run HTML parser.
  - Run asset-reference grep.
  - Run excluded capability grep.
  - Run sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.

- [x] 5. Finalize repair evidence
  - Update the gate review with new asset paths, screenshots, proof boundary,
    and decision.
  - Run `openspec validate redraw-account-onboarding-h5-source-visuals
    --strict`.
  - Commit only task-related files.
