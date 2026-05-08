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
| Reference Structure Map | Source, reader job, page group, reading path, visual logic, writing standard, reuse boundary, and linked-page readback when the reference has child pages or concrete reading-map links |
| Learning Use Map | Applicable learning artifacts, domain/topic, reusable capability type, learning point, intended output use, and skip reason when relevant |
| Hard Gate Results | Learning use, reference, split, voice, narrative, visual, and publish gate results |
| Scorecard | Point breakdown and total score only after all hard gates pass; otherwise `INVALID` with the failing gate |
| Decision | Whether the draft may update Feishu or be claimed review-ready |
| Residual Risks | Proof boundary and known gaps |
| Feishu Update Verification | Update command result, title, update log id, read-back result, read-back log id, and opening text |

## Stable Workflow

```text
reader-facing request
  -> create/update wiki/ops/*-report-gate-review.md
  -> complete reference structure map and linked-page readback
  -> complete learning use map when learned references are applicable
  -> choose split strategy and destination map
  -> draft reader-facing content
  -> pass hard gates and score >= 80
  -> update Feishu or publish target
  -> read back target
  -> append update/read-back evidence to gate-review artifact
  -> commit gate-review artifact
```

If the gate-review artifact is missing or incomplete, do not sync to Feishu and
do not claim the draft is ready for review.

If the reference map is incomplete, or any hard gate is failed, partial,
unknown, or not tested, record the score as `INVALID` and stop before Feishu
sync or review-ready claims.

If the output claims to use learned references but the learning use map is
missing, incomplete, or only says "used the reference" without a concrete output
use or skip reason, stop before drafting, Feishu sync, or review-ready claims.
