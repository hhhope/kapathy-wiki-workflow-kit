## Context

The repo already has `public-report-quality-gate` for reader-facing output.
That skill should remain compact. It is a trigger and hard-gate surface, not a
full editorial department.

Complex materials need heavier judgment:

- multiple pages or a report series
- external reference structure
- Feishu/H5/share publication
- scoring or gate-review artifacts
- user-reported drift or failed draft
- template or visual-style choice

When those signals combine, the main agent should not silently choose a
template and score its own output. It should route to a manual reviewer role.

## Decision

Add `public-report-reviewer` as a repo-local manual agent template. The public
report quality gate only decides whether the reviewer is required and records
that decision.

The reviewer owns:

- proposition check
- 2-3 candidate templates
- recommended template and user-choice requirement
- learning use map review
- hard-gate review
- evidence-backed score
- sync readiness decision

The main implementation agent owns:

- source reading
- drafting after template choice
- Feishu update
- read-back verification

## Boundary

The reviewer template is a manual role. It must not be treated as an automatic
sub-agent trigger. Future agents may load the template when the user asks for
review or when the gate says reviewer is required, but spawning still requires
explicit user permission.

## Reviewer Escalation Rule

Reviewer is required when at least two complexity signals are true:

- multi-page or series output
- external reference structure or visual example
- Feishu/H5/public share target
- scorecard or gate-review evidence is required
- user has reported drift, failed quality, or missing template choice
- template choice, visual style, or learning-use mapping is needed

For simple single-page reader-facing edits with no reference or scoring need,
the skill can proceed without reviewer.
