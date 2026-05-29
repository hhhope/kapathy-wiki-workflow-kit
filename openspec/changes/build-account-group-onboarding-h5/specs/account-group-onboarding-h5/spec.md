## ADDED Requirements

### Requirement: Internal account-group onboarding H5

The repository SHALL provide a standalone internal H5 draft that translates
account-group domain, project, onboarding, and AI collaboration materials into
a newcomer-facing training page.

#### Scenario: H5 presents the account-domain learning path

- **WHEN** a newcomer opens the H5
- **THEN** it SHALL explain the account group responsibility boundary, account
  capability map, core business chain, business objects, typical problems,
  active project entries, and technical planning direction
- **AND** the page SHALL avoid copying source PPT/PDF content as raw slide
  dumps.

#### Scenario: H5 includes AI collaboration and growth path

- **WHEN** a newcomer reaches the AI and onboarding sections
- **THEN** the H5 SHALL explain the OpenSpec / Lore / Graphify /
  lore-bootstrap collaboration model, AICoding L1-L4 maturity position, Day
  1/2/3 and first-week onboarding rhythm, 30/60/90 growth path, and task pool
  mapped to gained capabilities.

#### Scenario: H5 preserves internal-sensitive boundaries

- **WHEN** the H5 is prepared for local review
- **THEN** it SHALL exclude credentials, internal URLs, personal contact
  details, personal rankings, Feishu tokens, and sensitive production details
  from the reader-facing body
- **AND** it SHALL keep a report gate review record with reader intent,
  source-to-screen evidence mapping, sensitive-information boundary,
  verification evidence, and the absence of Feishu sync.
