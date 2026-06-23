# visual-agent-entry-route Specification

## ADDED Requirements

### Requirement: Image-like reference requests SHALL preserve mode ownership

`visual-agent` SHALL treat requests that provide or name a PNG, screenshot,
poster, cover, image, or image-like reference and ask for a similar image or
visual as image-mode pressure unless the user explicitly chooses deterministic
`H5/HTML` or `SVG` output.

#### Scenario: User asks for a similar PNG-style image

- **WHEN** the user provides an existing H5/report/content source
- **AND** the user names or provides a PNG, screenshot, poster, cover, or image
  reference as the desired style or output shape
- **AND** the user has not explicitly chosen `H5/HTML`, `SVG`, `Image model`,
  or `Hybrid`
- **THEN** the response SHALL expose `Using visual-agent`
- **AND** it SHALL ask or confirm the bounded mode fork before production
- **AND** it SHALL treat `Image model` or `Hybrid` as active route pressure
- **AND** it SHALL NOT start HTML/CSS/SVG/browser-screenshot production merely
  because deterministic rendering is safer for Chinese text

#### Scenario: User later chooses deterministic rendering

- **WHEN** the user explicitly chooses deterministic `H5/HTML`, `SVG`, or
  browser screenshot output after the mode fork
- **THEN** deterministic rendering MAY proceed
- **AND** the response SHALL state that it is deterministic rendering rather
  than image-model generation
