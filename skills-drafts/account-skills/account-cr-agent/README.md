# Account CR Agent Skills

This directory preserves the CR Agent skill bundle from `account-skills` as
ordinary skill source material. It is not a plugin package in this mirror.

## Included Skills

- `cr-agent`
- `cr-intake`
- `cr-branch-governance`
- `cr-diff`
- `cr-scope`
- `cr-technical-review`
- `cr-evidence`
- `cr-issues`
- `cr-gate`
- `cr-report`
- `cr-replay`
- `release-diff-cr`

## Direct Use

Review the skill folders under `skills/` directly. If one of these skills should
become active in a target repo, promote that individual skill through a separate
evaluation and copy/install step. Do not treat this mirrored directory as an
active runtime registration.

## Report Contract

`cr-agent` is the user-facing entry point. Report, gate, and full-CR runs should
write a human-review Markdown report and return its path; a chat-only summary is
not complete.

Chinese CR reports are rendered by `cr-report` from the current `cr-gate` and
`cr-issues` data. The default reader-first template is bundled at
`skills/cr-report/references/chinese-cr-report-template.md`; installed runs
should not depend on local historical paths.

If a user provides a prior CR report, use it only as style evidence: extract the
reader-facing structure, decision placement, finding shape, and scoring/audit
section style. Do not treat the prior report as a runtime dependency.

Every rendered CR report should preserve the reader-first order: conclusion,
blocking items, basic change information, scorecards, CR execution audit, branch
governance, technical review, debt/TODOs, test evidence, release risk, and
actions.

Report scorecards cover two separate subjects:

- Technical quality scoring for the reviewed code/change.
- CR execution audit scoring for review completeness, evidence quality, worker
  coverage, gate/issue trace consistency, and unresolved blind spots.

The CR execution audit must list these workers when applicable: `cr-intake`,
`cr-branch-governance`, `cr-diff`, `cr-scope`, `cr-technical-review`,
`cr-evidence`, `cr-issues`, `cr-gate`, and `cr-report`. For each worker, record
whether it was applicable, whether it executed, what evidence it produced, and
any gap or risk.
