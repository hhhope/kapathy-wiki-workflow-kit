# public-report-quality-gate Specification

## ADDED Requirements

### Requirement: Public report visual delegation SHALL preserve visual-agent first

The public report quality gate SHALL preserve `visual-agent` as the first
visual-production route for reader-facing report, H5, share, or Feishu visual
deliverables before delegating to article visual, infographic, or bitmap
executor skills.

#### Scenario: Reader-facing H5 asks for knowledge cards

- **WHEN** the user asks a reader-facing H5/report/share artifact to add
  knowledge cards, a one-page infographic, section images, or visual assets
- **THEN** the gate SHALL route the visual production chain through
  `visual-agent`
- **AND** it SHALL preserve Article Intent, Visual Gate, Judgment Ownership, and
  Publish Gate before review-ready, publish, sync, or share claims

#### Scenario: Public gate delegates to image generation

- **WHEN** bitmap image generation is selected for a reader-facing artifact
- **THEN** `imagegen` SHALL remain an executor after `visual-agent` mode
  selection and public-report gate checks
- **AND** it SHALL NOT be treated as the first planning owner
