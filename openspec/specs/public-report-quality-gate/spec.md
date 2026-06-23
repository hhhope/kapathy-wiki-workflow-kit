# public-report-quality-gate Specification

## Purpose
TBD - created by archiving change add-public-report-quality-gate. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL provide a public report quality gate

The repository SHALL provide a repo-local skill that gates reader-facing
reports, Feishu review drafts, public share drafts, and H5/report-style outputs
before they are published, synced, or claimed ready for review.

#### Scenario: User asks for a reader-facing material

- **WHEN** the user asks to write, polish, create, sync, or prepare a public
  report, Feishu review draft, H5/share draft, or reader-facing material
- **THEN** the system SHALL route the output through the public report quality
  gate before publishing or syncing

#### Scenario: User provides a reference artifact for output shape

- **WHEN** the user provides a Feishu page, article, example, visual, or
  existing report as a reference for the output shape
- **THEN** the gate SHALL require a reference structure map before writing or
  rewriting the reader-facing draft
- **AND** if the reference is a Feishu wiki node with child pages or a reading
  map with concrete links, the gate SHALL require linked-page readback before
  the Reference Structure Gate can pass

### Requirement: Public report gate SHALL enforce hard publish blockers

The public report gate SHALL block publish or Feishu sync when any hard gate
fails.

#### Scenario: Voice gate fails

- **WHEN** a reader-facing draft contains chat residue, slogan simplification,
  loose narrator, weak section openings, internal ops leakage, or tone mismatch
- **THEN** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Core narrative drifts

- **WHEN** the stated story or reader promise changes during the draft, such as
  rewriting an evolution path into a static responsibility split
- **THEN** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Multi-part content is overloaded into one article

- **WHEN** the material spans multiple reader jobs such as overview, runtime,
  migration, validation, and roadmap
- **THEN** the gate SHALL require an explicit split strategy before reader-facing
  publication or sync

#### Scenario: A hard gate is not fully passed

- **WHEN** any hard gate is failed, partial, unknown, or not tested
- **THEN** the draft SHALL NOT receive a numeric score
- **AND** the scorecard SHALL be recorded as `INVALID`
- **AND** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Reference visuals are missing

- **WHEN** the reference artifact uses essential visuals for structure,
  sequence, contrast, maturity, or decision logic
- **AND** the reader-facing draft lacks corresponding visual assets or a
  concrete visual plan
- **THEN** the Visual Gate SHALL fail rather than treating the gap as a residual
  risk

### Requirement: Public report gate SHALL preserve existing workflow gates

The public report gate SHALL coordinate existing source, learning, visual,
Feishu, and verification skills without replacing their boundaries.

#### Scenario: Source or reference learning is needed

- **WHEN** a reader-facing report uses external articles, repositories, Feishu
  pages, or examples as references
- **THEN** the system SHALL still preserve the applicable learning-capture,
  source-grounding, and adaptation-boundary gates

#### Scenario: Feishu sync is requested

- **WHEN** the draft is intended for Feishu creation or update
- **THEN** the system SHALL pass the public report quality gate before using
  Feishu document write operations

### Requirement: Public report gate SHALL preserve a repo-visible gate review artifact

The public report gate SHALL preserve the quality decision in a repo-visible
artifact before Feishu sync, publication, or a review-ready claim.

#### Scenario: Reader-facing draft is prepared for Feishu or review

- **WHEN** a reader-facing draft is intended for Feishu sync, publication, or a
  review-ready claim
- **THEN** the system SHALL create or update a `wiki/ops/*-report-gate-review.md`
  artifact before the sync, publication, or claim
- **AND** the artifact SHALL include the reference structure map, hard gate
  results, scorecard, decision, residual risks, and proof boundary
- **AND** when the reference contains linked pages, the artifact SHALL include
  linked-page titles, links or tokens, and confirmed page jobs

#### Scenario: Feishu write is completed

- **WHEN** a Feishu document is created or updated after passing the public
  report quality gate
- **THEN** the gate review artifact SHALL record the Feishu update result and
  read-back verification
- **AND** the Feishu document SHALL NOT be treated as the process evidence by
  itself

### Requirement: Public report gate SHALL separate local visual assets from Feishu image insertion

The public report gate SHALL treat local visual asset generation and Feishu
image insertion as separate delivery operations.

#### Scenario: User will add images manually

- **WHEN** a reader-facing report needs generated images or one-pagers
- **AND** the user says they will add images manually
- **THEN** the system SHALL generate or preserve local visual assets and asset
  paths
- **AND** SHALL NOT insert those images into Feishu
- **AND** MAY perform text-only Feishu sync when separately approved and gates
  pass

#### Scenario: Feishu sync is approved but image insertion is not explicit

- **WHEN** a reader-facing draft has local visual assets
- **AND** the user approves Feishu sync without explicitly approving image
  insertion
- **THEN** the system SHALL treat the Feishu operation as text-only
- **AND** SHALL record local asset paths or manual-image instructions instead
  of inserting image blocks

#### Scenario: User explicitly asks the agent to insert Feishu images

- **WHEN** the user explicitly asks the agent to insert generated images into a
  Feishu document
- **THEN** the system SHALL state the known client-freeze risk
- **AND** SHALL get explicit approval for the image-insertion operation
- **AND** SHALL record image tokens and read-back logs as audit evidence only,
  not as proof of client usability

#### Scenario: Image-bearing Feishu document freezes a client

- **WHEN** Codex, Feishu, or the user reports a freeze on an image-bearing
  Feishu document
- **THEN** the system SHALL stop further image-included Feishu writes for the
  current work
- **AND** SHALL switch to text-only sync, local asset paths, or a separately
  approved client-safe image workflow before any further delivery claim

### Requirement: Public report gate SHALL anchor drafts with an article intent contract

The public report gate SHALL establish the reader-facing target before complex
drafting, scoring, Feishu sync, or review-ready claims.

#### Scenario: Complex reader-facing draft is prepared

- **WHEN** a reader-facing report, Feishu review draft, H5/share draft, or
  public material has reviewer-routing complexity signals, user-reported drift,
  or a required scorecard
- **THEN** the gate SHALL record an Article Intent Contract before drafting or
  scoring
- **AND** the contract SHALL identify the reader, reader decision or action,
  main line, non-goals, user-owned judgments, and agent-allowed operations

### Requirement: Public report gate SHALL provide section and paragraph drift diagnostics

The public report gate SHALL review sections and important paragraphs against
the article intent before review-ready claims.

#### Scenario: Draft sections are reviewed for drift

- **WHEN** a complex or drift-corrected reader-facing draft is reviewed
- **THEN** the gate SHALL record a Section And Paragraph Drift Review
- **AND** the review SHALL include section objective, paragraph claim, mainline
  role, target fit score, narrative drift score, evidence fit score, judgment
  source, and action
- **AND** the action SHALL be one of retain, compress, rewrite, delete, or ask
  the user

#### Scenario: Paragraph changes article judgment

- **WHEN** a paragraph changes the article's main line, conclusion,
  prioritization, or public stance without source support or user confirmation
- **THEN** the Paragraph Drift Gate SHALL fail
- **AND** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

### Requirement: Public report gate SHALL preserve user judgment ownership

The public report gate SHALL treat user-owned thought and judgment as separate
from delegable writing process.

#### Scenario: Agent makes an unsourced public judgment

- **WHEN** the agent turns source material, reference examples, or smooth prose
  into a local strategic conclusion, priority, proof-strength claim, or public
  stance that the user has not confirmed
- **THEN** the Judgment Ownership Gate SHALL fail
- **AND** the gate-review artifact SHALL identify the judgment source as user,
  source material, agent inference, or unknown

#### Scenario: Hard gate fails but diagnostics are useful

- **WHEN** Paragraph Drift Gate or Judgment Ownership Gate fails
- **THEN** the overall scorecard SHALL remain `INVALID`
- **AND** the gate MAY still record diagnostic 0-5 drift scores and required
  repair actions for sections or paragraphs

### Requirement: Public report gate SHALL own the outer route for reader-facing output

The public report gate SHALL remain the outer route for reader-facing reports,
H5/share drafts, Feishu review drafts, public materials, and external-facing
visual packages even when specialized skills perform source, learning, visual,
image-generation, Feishu, or verification work.

#### Scenario: Reader-facing article asks for knowledge cards

- **WHEN** the user asks to turn an existing reader-facing article, H5, or
  share draft into knowledge cards, chapter visuals, or a one-page infographic
- **THEN** the system SHALL route through the public report gate first
- **AND** the public report gate SHALL preserve the Article Intent Contract,
  Judgment Ownership Gate, Visual Gate, and Publish Gate
- **AND** visual skills SHALL be treated as delegated production routes rather
  than replacements for the public report gate

#### Scenario: Specialized skill is needed during public output work

- **WHEN** a reader-facing output needs source learning, visual package design,
  per-image infographic scripting, image generation, Feishu writing, or final
  verification
- **THEN** the public report gate SHALL identify the subordinate skill route
- **AND** the subordinate skill SHALL NOT weaken the public report gate's
  review-ready, publish, sync, source-boundary, visual, or judgment-ownership
  blockers

#### Scenario: Visual asset is generated for a public draft

- **WHEN** a visual asset is generated for a reader-facing draft
- **THEN** the public report gate review SHALL record the visual's intended
  reader-facing role, local asset path or delivery boundary, and remaining
  visual QA risk before any review-ready, publish, or sync claim

### Requirement: Public report gate SHALL enforce reference-shaped article flow

The public report gate SHALL verify reference-shaped article flow when a
reader-facing draft uses a newspaper, article, or report reference for output
shape, preserving the reference's layout system rather than silently replacing
it with a card, dashboard, table, or prompt-script composition.

#### Scenario: Newspaper reference becomes a card wall

- **WHEN** the user asks for a reader-facing draft that references an existing
  newspaper or article-style report
- **AND** the draft renders prose-heavy company or topic analysis as repeated
  boxed cards, colored panels, comparison cells, or dashboard-like grids
- **THEN** the Article Flow Layout Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready until the content is
  converted into article flow with prose paragraphs and disciplined evidence
  callouts

#### Scenario: Visual prompt leaks into report body

- **WHEN** the requested final image route is image-model or Hybrid
- **AND** prompt text, visual-script instructions, or output-mode notes appear
  inside the reader-facing report body
- **THEN** the Article Flow Layout Gate SHALL fail
- **AND** the prompt or visual production route SHALL be moved to a separate
  asset brief or removed from the report body

#### Scenario: Gate review records layout replay

- **WHEN** a draft is repaired after layout drift against a newspaper/article
  reference
- **THEN** the gate-review artifact SHALL record the reference layout system,
  retained patterns, rejected card/table patterns, and replay result

### Requirement: Public report gate SHALL enforce reference output shape fidelity

The public report gate SHALL verify the selected output shape when a user
request or reference artifact establishes one, and SHALL block review-ready,
publish, or sync claims when the draft silently replaces that shape with a
different primary structure.

#### Scenario: Draft silently changes selected output shape

- **WHEN** a user request or reference artifact establishes an output shape
- **AND** the draft changes to a different primary structure without explicit
  user approval
- **THEN** the Reference Output Shape Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready, published, or synced
  until repaired or explicitly approved by the user

#### Scenario: Production route leaks into reader-facing content

- **WHEN** the selected output shape is reader-facing content
- **AND** production instructions, image prompts, tool notes, or Hybrid routing
  text appear inside that content
- **THEN** the Reference Output Shape Gate SHALL fail
- **AND** the production route SHALL be moved to a separate asset brief,
  worklog, or other non-reader-facing location

#### Scenario: Gate review records shape replay

- **WHEN** a reference-shaped draft is prepared for review, publish, or sync
- **THEN** the gate-review artifact SHALL record the selected output shape,
  retained patterns, rejected patterns, user-approved shape changes, and replay
  result

### Requirement: Public report gate SHALL route HTML-target visual requests to visual assets first before HTML edits

The public report gate SHALL route reader-facing HTML report or H5 page requests
to visual asset work first when the request also asks for visual deliverables.
It SHALL NOT treat the HTML target path as permission to satisfy the request by
adding in-page H5 sections only.

#### Scenario: Existing HTML report asks for knowledge cards and a one-page infographic

- **WHEN** the user names an existing `.html` report or H5 page
- **AND** the request includes visual-deliverable wording such as `一图流`,
  `知识卡`, `章节配图`, `图片`, `生图`, `跑图`, or `图片模型`
- **THEN** the system SHALL stop before direct HTML body edits
- **AND** SHALL route first to visual package scripting, output-mode selection
  or inference, and standalone visual asset production or planning
- **AND** SHALL NOT claim the request is complete by adding only HTML sections

#### Scenario: HTML embedding is explicitly requested or follows accepted visual assets

- **WHEN** the user explicitly asks for an in-page H5/HTML module
- **OR** standalone visual assets have already been accepted and the next step
  is embedding or linking those assets in HTML
- **THEN** HTML editing MAY proceed within the public report gate boundary

#### Scenario: Ordinary HTML report edits do not ask for visual deliverables

- **WHEN** the user names an `.html` report and asks for ordinary text, evidence,
  layout, or citation edits without visual-deliverable wording
- **THEN** the gate MAY allow scoped HTML/report editing without requiring
  standalone visual asset production first

### Requirement: Public report gate SHALL require citation surfaces for newspaper outputs

The public report gate SHALL require a reader-visible citation surface for
newspaper-style H5/share packages and public newspaper drafts before
review-ready, publish, sync, or share claims.

#### Scenario: Newspaper has source map but no citation surface

- **WHEN** a newspaper-style H5, share package, or public newspaper draft has an
  internal source map, learning use map, or gate-review artifact
- **AND** the reader-facing output lacks a visible citation surface for
  load-bearing claims, figures, company examples, or visual panels
- **THEN** the Newspaper Citation Surface Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready, published, synced, or
  shared as final

#### Scenario: Citation surface records source strength

- **WHEN** a newspaper citation surface cites a source for a claim, number,
  company example, or visual panel
- **THEN** it SHALL identify the citation target and source class
- **AND** it SHALL include a boundary note when the cited source is secondary,
  practitioner, transcript mirror, candidate, paywalled without primary access,
  or otherwise too weak for a hard fact claim

#### Scenario: Existing newspaper replay

- **WHEN** the AI Agent Product Engineering Collaboration newspaper is evaluated
  for review-ready, publish, sync, or share status
- **THEN** the gate review SHALL cite the output artifact
  `wiki/reports/agentic-product-engineering-collaboration-newspaper.html`
- **AND** it SHALL cite the supporting source map
  `wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md`
- **AND** it SHALL verify that load-bearing newspaper panels have reader-visible
  citation routes or explicit boundary notes

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

### Requirement: Public report visual wording SHALL include colloquial visual asks

The public report quality gate SHALL treat casual requests to make, add, polish,
or convert visuals for reader-facing artifacts as visual deliverable requests,
even when the exact terms `一图流`, `知识卡`, `章节配图`, `图片`, `生图`, `跑图`,
or `图片模型` are absent.

#### Scenario: H5 request asks casually for visuals

- **WHEN** the user names a reader-facing H5/report/share artifact
- **AND** asks in casual language to make it visual, add some images, turn it
  into cards, or otherwise produce visual assets
- **THEN** the gate SHALL route visual production through `visual-agent`
- **AND** it SHALL NOT satisfy the request by silently adding only in-page
  H5/SVG sections
