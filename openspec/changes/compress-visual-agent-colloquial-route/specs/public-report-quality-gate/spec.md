# public-report-quality-gate Specification

## ADDED Requirements

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
