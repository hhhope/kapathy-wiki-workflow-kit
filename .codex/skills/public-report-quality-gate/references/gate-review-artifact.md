# Gate Review Artifact

Create or update a repo-visible gate-review artifact before Feishu sync or a
review-ready claim.

## Location

Use `wiki/ops/<canonical-object>-report-gate-review.md`.

If the report belongs to an existing canonical object, reuse that object in the
filename. Do not keep the gate review only in chat, `/tmp`, or the Feishu
document.

## Required Sections

| Section | Required Content |
|---|---|
| Review Target | Target title, destination, scope, and non-scope |
| Reference Structure Map | Source, reader job, page group, reading path, visual logic, writing standard, reuse boundary |
| Hard Gate Results | Reference, split, voice, narrative, visual, and publish gate results |
| Scorecard | Point breakdown and total score |
| Decision | Whether the draft may update Feishu or be claimed review-ready |
| Residual Risks | Proof boundary and known gaps |
| Feishu Update Verification | Update command result, title, update log id, read-back result, read-back log id, and opening text |

## Stable Workflow

```text
reader-facing request
  -> draft reader-facing content
  -> create/update wiki/ops/*-report-gate-review.md
  -> pass hard gates and score >= 80
  -> update Feishu or publish target
  -> read back target
  -> append update/read-back evidence to gate-review artifact
  -> commit gate-review artifact
```

If the gate-review artifact is missing or incomplete, do not sync to Feishu and
do not claim the draft is ready for review.
