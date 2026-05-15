# Design: wiki medical case file

## Core Model

Each medical-loop run has one canonical case file:

```text
wiki/ops/wiki-medical-cases/YYYY-MM-DD-<case-slug>.md
```

The case file is the durable chart. Stage records are evidence attachments.

```text
case file
  -> doctor evidence records
  -> confirm evidence records
  -> treatment run records
  -> surgery run records
  -> recovery run records
```

Later stages must read and update the case file instead of treating the latest
stage record as the current source of truth.

## Required Case Sections

The case file contains:

- `Case Source`: trigger, scan root, source records, and generated-at history.
- `Diagnosis`: doctor summary and abnormal findings.
- `Confirmed Decisions`: accepted, rejected, deferred, treatment, surgery, and
  OpenSpec-required decisions.
- `Treatment`: approved low-risk repairs and applied run records.
- `Surgery Plan`: structural repair plan derived from confirmed decisions.
- `Recovery`: post-action checks and remaining blockers.
- `Archive / Next Action`: whether the case is closed, blocked, or awaiting a
  new OpenSpec change.
- `Evidence Attachments`: links to generated doctor, confirm, treatment,
  surgery, and recovery records.
- `Proof Boundary`: what the case does not authorize.

Sections may be marked `pending`, but they must stay present so later agents
see the whole lifecycle shape.

## Review Semantics

Humans primarily review `Confirmed Decisions`.

Surgery review is a fidelity check:

- Did the surgery plan use only confirmed surgery candidates?
- Did it preserve `relation_weak_evidence` as manual review, not an automatic
  relation write?
- Did it route `drift_risk`, `adr_risk`, and `openspec_required` items to
  OpenSpec or governance review instead of direct edits?
- Did it avoid frontmatter, taxonomy, relation, MOC, ADR, AGENTS, and OpenSpec
  mutations unless a later explicit apply workflow approves them?

The surgery record is therefore not a new diagnosis. It is a plan section that
must be traceable back to confirmed case decisions.

## Stage Record Role

Stage records remain useful because they preserve raw generation evidence and
tool output. They should be linked from the case file as attachments:

```text
Evidence Attachments
- doctor: wiki/ops/wiki-doctor-runs/...
- confirm: wiki/ops/wiki-review-decisions/...
- treatment: wiki/ops/wiki-treatment-runs/...
- surgery: wiki/ops/wiki-surgery-runs/...
- recovery: wiki/ops/wiki-recovery-runs/...
```

An attachment can add evidence, but it cannot silently change the case
decision. Any new finding must update the case file decision table explicitly or
open a new case.

## CLI Direction

The first implementation should be conservative:

1. Add a case-file builder or updater that can assemble a case from doctor and
   confirm records.
2. Add explicit case-file arguments to treatment, surgery, and recovery.
3. Make surgery planning require either a case file or a confirmed decision
   record, then write its plan into the case file.
4. Keep old stage record output available during migration.

Changing every stage default at once is not required for the first pass.

## Boundaries

This change defines case-file workflow and evidence routing. It does not approve
or apply repairs.

Do not use the case file to bypass:

- frontmatter taxonomy gates
- relation evidence review
- MOC projection review
- ADR stability rules
- OpenSpec lifecycle gates
- repo behavior-asset evaluation gates

## Verification

Minimum verification:

- A sample case can be generated from existing doctor and confirm records.
- The surgery plan section names its source confirmed decisions.
- Stage evidence links remain attachments, not replacement authority.
- A replay scenario proves that "latest surgery record wins" is rejected.
