## Why

A fresh company-playbook failure showed that the public-output routing fix was
too broad. The existing pressure scenarios covered "H5/article + knowledge
cards / one-page infographic", but did not cover the sharper input shape:

`existing .html file + 一图流 / 知识卡 / 章节配图`

That gap let the agent treat the `.html` target path as permission to edit the
HTML page directly, even though the user was asking for visual deliverables and
had already rejected H5/SVG-like output quality.

## What Changes

- Add a public-report gate rule for reader-facing HTML targets combined with
  visual-deliverable wording.
- Require the route to stop direct HTML section editing and produce or plan
  standalone visual assets first.
- Add pressure scenarios and behavior replay evidence for the exact failure:
  `agentic-product-engineering-collaboration-company-playbook.html要增加一图流，每个公司要增加章节知识卡`.
- Keep ordinary HTML/report text edits allowed when the request is not asking
  for visual deliverables.

## Impact

- Future agents should not satisfy `一图流` / `知识卡` requests by adding colored
  cards inside an HTML report.
- HTML embedding remains possible after the visual asset route is accepted or
  when the user explicitly asks for an in-page H5/HTML module.
- This change does not generate final images, publish reports, sync Feishu, or
  archive any completed change.
