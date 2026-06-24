# visual-agent-entry-route Spec Delta

## ADDED Requirements

### Requirement: Reference-image visual work SHALL map source roles before generation

`visual-agent` SHALL require a source-role map before prompt/script generation
when a visual request uses a prior image, screenshot, poster, generated output,
or other image-like artifact as a reference.

#### Scenario: Reference image is style source only

- **WHEN** the user asks for image-model or hybrid visual work
- **AND** the user provides or names a prior image, screenshot, poster, generated
  output, or similar image as a reference
- **THEN** the response SHALL identify the current content source
- **AND** it SHALL identify the reference artifact as a style source unless the
  user explicitly asks to reuse its content
- **AND** it SHALL identify the selected executor route
- **AND** it SHALL state what the output image communicates and what must be
  verified after generation
- **AND** it SHALL NOT treat the reference artifact's semantic topic as the new
  image content source

#### Scenario: Historical reference content is explicitly requested

- **WHEN** the user explicitly asks to reuse semantic content from a reference
  image
- **THEN** that image MAY be treated as a content source
- **AND** the response SHALL state that the user explicitly made the reference a
  content source

### Requirement: Image delivery SHALL be gated by available file capability

`visual-agent` SHALL verify image delivery capability before promising
repo-local image files for image-model output.

#### Scenario: Codex CLI can show image artifact but cannot expose file

- **WHEN** the selected output mode is `image_model` or image-model visual layer
- **AND** the user asks for local image files
- **AND** the current runtime can only show a chat `Generated Image` artifact
  without a repo-local file path, artifact export, or valid image API fallback
- **THEN** the response SHALL NOT claim that local image files were generated
- **AND** it SHALL produce client-mode prompt markdown or an equivalent copyable
  prompt package instead
- **AND** the prompt package SHALL include reference image paths, source-role
  boundary, copyable prompt, and verification checklist

#### Scenario: API fallback is considered

- **WHEN** local image generation depends on an API fallback
- **THEN** Codex login tokens SHALL NOT be treated as OpenAI Platform Images API
  credentials unless image-generation scope is verified
- **AND** a missing or unusable `OPENAI_API_KEY` SHALL block local file
  generation rather than trigger a false file-delivery claim

#### Scenario: Local file capability is available

- **WHEN** an artifact export path, repo-local generated image path, or valid
  image API credential is available
- **THEN** `visual-agent` MAY route to image generation that produces local files
- **AND** it SHALL preserve the source-role map and visual verification
  requirement
