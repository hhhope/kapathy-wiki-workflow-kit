## Why

Learning capture currently records useful external-source takeaways, and the
public report gate blocks weak reader-facing drafts. The gap is between them:
the agent can learn from articles, repos, or examples, then write the next
report without using the learning artifacts as constraints.

The latest Account Harness Wiki discussion exposed this failure mode. We read
reference materials, captured trace notes, and added report gates, but the
output path still did not force a visible map from learned practice to draft
section, visual, metric, boundary, or skip reason.

## What Changes

- Add a learning-output reuse gate for reader-facing outputs that claim to use
  external-source learning or reference examples.
- Extend learning capture records to distinguish:
  - source domain/topic: what the material is about
  - reusable capability type: what output capability we learned from it
- Require reader-facing drafts to map applicable learning artifacts before
  drafting or review-ready claims.
- Add stable pressure scenarios proving that learning artifacts are used,
  skipped with reasons, or kept out of scope.

## Impact

- Updates `.codex/skills/learning-capture/`.
- Updates `.codex/skills/public-report-quality-gate/`.
- Adds OpenSpec coverage for learning-output reuse.
- Does not rewrite the Account Harness Wiki draft.
- Does not update Feishu.
- Does not promote root/global skills.
