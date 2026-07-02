# Scorecard Registry

Atlas uses progressive disclosure. Load only the gate families needed for the
current artifact.

Do not freeze a single project's correction list as universal behavior.

## Core Gates

Use for any Atlas-triggered task.

| Gate | Pass condition | Fail condition |
|---|---|---|
| State inheritance | Confirmed anchors are read back before action. | The agent continues from memory or starts a new structure. |
| Execution boundary | Allowed and blocked actions are explicit. | The next action expands scope silently. |
| Final consistency | Completion is checked against anchors. | The agent claims done without drift review. |
| Generic vs custom boundary | Artifact-specific preferences stay scoped. | A Stripe-specific correction becomes a universal rule without evidence. |

## Reader Artifact Gates

Use for reports, H5/share drafts, presentations, Feishu-facing drafts, and
reader-facing wiki output.

| Gate | Pass condition | Fail condition |
|---|---|---|
| Mainline clarity | The output preserves the confirmed main line. | The prose sounds better but changes the judgment. |
| Section integrity | Chapter and section names, order, and purpose are preserved. | Confirmed structure is renamed, merged, or compressed. |
| Narrative progression | Each section advances setup, conflict, evidence, mechanism, or transition. | Sections become disconnected summaries. |
| Professional drama | Tension and stakes are concrete without slogan tone. | Titles or claims become bland, generic, or performative. |

## Evidence Gates

Use when claims depend on external sources, LinkedIn/JD samples, financial data,
market timing, regulation, or organization capability.

| Gate | Pass condition | Fail condition |
|---|---|---|
| Evidence duty | Claims state source role and proof boundary. | Evidence is implied but not mapped. |
| Claim strength | The claim strength matches the sample and source type. | Weak samples become broad organization or strategy claims. |
| Method fit | The evidence method fits the question. | JD data is used as people-background proof, or profile samples prove strategy success. |

## Visual Gates

Use for H5/share visuals, section visuals, visual packages, image-model work,
or visual report design.

| Gate | Pass condition | Fail condition |
|---|---|---|
| Visual proof binding | Each visual states what relationship, contrast, mechanism, timeline, or decision it proves. | Visuals decorate or repeat text. |
| Per-section visual integrity | Approved per-section visuals remain separate unless compression is approved. | Multiple sections collapse into one generic visual. |

## Boundary Gates

Use for skill/governance behavior and user-owned judgment.

| Gate | Pass condition | Fail condition |
|---|---|---|
| Hard failure | Drift, missing evidence, or blocked scope stops completion. | Failure is downgraded to residual risk. |
| User-owned judgment | User corrections and decisions remain visible. | The agent replaces the user's judgment with smoother prose. |

## Loading Examples

- simple material cleanup -> Core Gates
- complex report -> Core + Reader Artifact + Evidence Gates
- H5/share visual draft -> Core + Reader Artifact + Visual Gates
- source-heavy strategy report -> Core + Reader Artifact + Evidence + Final Drift
- workflow behavior discussion -> Core + Boundary Gates
