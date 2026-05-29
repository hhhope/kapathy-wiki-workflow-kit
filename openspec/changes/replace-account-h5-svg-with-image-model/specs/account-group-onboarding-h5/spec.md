# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Displayed Diagram Assets Use Image Model Outputs

The H5 SHALL display image-model generated bitmap assets for the main visual
sections instead of manually authored SVG-derived PNGs.

#### Scenario: H5 visual references are image-model outputs

- **WHEN** a reviewer inspects the H5 image references
- **THEN** the capability map, system architecture, core chain, Nirvana/project
  entry map, and technical planning roadmap reference `-ai.png` image-model
  output assets
- **AND** the H5 does not rely on the previous SVG-derived PNG filenames for
  those displayed visuals.

### Requirement: Image Model Output Keeps Technical Meaning

The image-model outputs SHALL preserve the high-level technical purpose of each
visual section.

#### Scenario: generated visual is useful in training

- **WHEN** a reviewer opens the H5 on desktop or mobile
- **THEN** the generated image for each main visual section communicates the
  intended capability, architecture, chain, project, or roadmap structure
- **AND** dense account-domain explanations remain in the H5 text around the
  image.
