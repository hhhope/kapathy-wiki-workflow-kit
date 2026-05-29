# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Card Layout Is Not Dominant

The H5 SHALL NOT use repeated card grids as the dominant information structure.

#### Scenario: reviewer scans the page

- **WHEN** a reviewer opens the H5 on desktop or mobile
- **THEN** repeated content is presented primarily as technical handout rows,
  definition blocks, compact matrices, or diagram annotations
- **AND** boxed card grids do not dominate the reader's first impression.

### Requirement: Source Diagrams Remain Primary Visual Evidence

The H5 SHALL keep source-backed diagrams as the primary visual evidence for
architecture, capability, chain, project, and roadmap sections.

#### Scenario: visuals carry technical meaning

- **WHEN** a reviewer reads the capability, architecture, chain, project, and
  roadmap sections
- **THEN** the diagram remains the load-bearing visual element
- **AND** surrounding text supports the diagram without replacing it with
  generic cards.
