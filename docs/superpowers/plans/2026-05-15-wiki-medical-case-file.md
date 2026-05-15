# Wiki Medical Case File Implementation Plan

> Supports OpenSpec change: `introduce-wiki-medical-case-file`.
> This plan is secondary to OpenSpec `tasks.md`.

## Goal

Implement a canonical medical case file so doctor, confirm, treatment, surgery,
and recovery records become evidence attachments instead of competing sources
of truth.

## Scope

In scope:

- Case-file builder/updater under `wiki/ops/wiki-medical-cases/`.
- Case sections for diagnosis, confirmed decisions, treatment, surgery,
  recovery, archive/next action, evidence attachments, and proof boundary.
- Surgery source wiring that derives from confirmed case decisions.
- Replay/test proving a generated surgery record cannot override confirmed
  case decisions.

Out of scope:

- Applying frontmatter, relation fields, taxonomy config, MOC files, ADRs,
  AGENTS, skills, or OpenSpec lifecycle state.
- Removing existing stage records.
- Migrating all historical records.

## Tasks

- [x] 1. Record Superpowers design and replay support for the existing OpenSpec change.
- [ ] 2. Add RED replay/test showing that separate surgery output can drift from confirmed decisions.
- [ ] 3. Implement a case-file builder or updater.
- [ ] 4. Add explicit case-file source wiring for surgery planning.
- [ ] 5. Preserve generated stage records as evidence attachments.
- [ ] 6. Add verification that surgery derives from confirmed case decisions.
- [ ] 7. Run focused tests, frontmatter precheck for new case pages, OpenSpec validation, and behavior-asset checks if skills change.

## RED Baseline

Observed failure:

- Surgery planning generated a stage record from script output.
- The human review target became ambiguous.
- The generated surgery record risked becoming the new source of truth.

## GREEN Target

Expected behavior:

- A medical-loop run opens through one case file.
- Humans review `Confirmed Decisions` first.
- Surgery plan is reviewed only as a fidelity check against those decisions.
- Stage records remain linked evidence attachments.
