## ADDED Requirements

### Requirement: Stripe H5 visual language polish

The Stripe AI company evolution H5 SHALL use reader-facing visual language for
the first-screen volume view, relationship rails, company path, and market
position section.

#### Scenario: Reader opens the first screen

- **WHEN** a reader opens `wiki/reports/stripe-ai-company-evolution-h5.html`
- **THEN** the processed-volume visual SHALL present 2023, 2024, and 2025 scale
  as a clear scale snapshot rather than an awkward precision line
- **AND** the relationship rails SHALL explain transaction and credit
  relationships in plain business language.

#### Scenario: Reader reviews the company path

- **WHEN** a reader reaches `公司路径：五次位置迁移`
- **THEN** the five stages SHALL read as a connected migration path rather than
  a flat card grid.

#### Scenario: Reader reviews market position

- **WHEN** a reader reaches the market-position section
- **THEN** the headline and opening paragraph SHALL use reader-facing report
  language
- **AND** technical caveats about Q1/full-year, revenue/net revenue, TPV, and
  unaudited share SHALL be preserved as source-boundary notes rather than the
  main section voice.

#### Scenario: Reader reviews the company timeline

- **WHEN** a reader reaches the company timeline section
- **THEN** the heading SHALL use a business-analysis claim rather than process
  language such as `并读`
- **AND** the intro SHALL not start with tool instructions such as `拖动年份看`
- **AND** the section SHALL have stronger visual hierarchy than a plain text
  block above controls.

#### Scenario: Reader reviews strategic choices

- **WHEN** a reader reaches `哪些战略造就了 Stripe`
- **THEN** the section SHALL read as a strategic sequence or compounding chain
  rather than a mechanical matrix
- **AND** it SHALL not use labels such as `壁垒读法` in reader-facing copy.

#### Scenario: Reader reviews AI-era payment restructuring

- **WHEN** a reader reaches the AI-era payment section
- **THEN** the section SHALL use concrete business language rather than generic
  AI phrasing about agents understanding or calling capabilities
- **AND** the section SHALL present payment restructuring as control-point
  pressure and Stripe infrastructure response
- **AND** the section styling SHALL be visually distinct from a plain stack of
  cards.

#### Scenario: Reader reviews original-source quotes

- **WHEN** a reader reaches the source-quote section
- **THEN** each quote card SHALL use the same visible grammar for source id,
  source type, claim, short quote, support, and boundary
- **AND** the section heading SHALL not use internal-process phrasing such as
  `原文引用：关键判断必须能回到来源`.

#### Scenario: Reader reviews the signal matrix

- **WHEN** a reader reaches the signal section
- **THEN** the section SHALL render signals as a consistent categorized matrix
  rather than decorative word-cloud chips
- **AND** each signal cell SHALL show its category, term, and evidence route
  or source route.
