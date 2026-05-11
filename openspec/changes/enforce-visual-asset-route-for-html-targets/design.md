## Context

The repository already has a public-output parent gate and visual skill routing.
The missed case was not "visual skills never load"; it was that the target file
extension (`.html`) overrode the visual-deliverable wording in the live route.

The user later asked whether pressure tests had covered this. They had not:
existing pressure scenarios included generic H5/article visual requests, but not
the exact ambiguous request shape where an HTML path and visual asset wording
appear together.

## Design

### Visual Asset Route Before HTML Editing

For reader-facing output, if an existing `.html` report/page is named and the
request includes visual-deliverable terms, the public report gate should treat
the work as visual asset production first.

Visual-deliverable terms include:

- `一图流`
- `知识卡`
- `章节配图`
- `图片`
- `生图`
- `跑图`
- `图片模型`

The agent should not begin by editing the HTML report body. It should first
classify or infer the visual output mode and produce a visual script / asset
plan / generated assets as appropriate.

### Allowed HTML Work

HTML remains allowed when:

- the user explicitly asks for in-page H5/HTML modules;
- the visual asset route has already been accepted and the next step is
  embedding or linking approved assets;
- the request is an ordinary report/content/layout edit without visual
  deliverable wording.

### Pressure Testing

The evaluation must explicitly show:

- RED: before this change, current pressure scenarios do not mention `.html`
  target paths and visual-deliverable wording together.
- GREEN: after this change, public-report pressure scenarios and skill text
  contain the exact route stop.
- Behavior replay: future agent can reproduce the expected stop/route from
  repo-visible files.

## Non-Goals

- Do not add another visual skill.
- Do not edit global visual skills unless this public-report route remains
  insufficient after validation.
- Do not generate or QA final visual assets in this change.
