# Add Wiki Medical Loop Skills

## Why

The repository now has executable doctor, confirm/review, treatment, surgery,
and recovery layers, but most of the user-facing skill surface still exposes
implementation names or does not exist. This caused the workflow to be
explained as Python commands instead of as the LLM-WIKI medical loop.

`wiki-review-decisions` is also an implementation-shaped name. The user-facing
stage should be `wiki-confirm`, matching the medical-loop vocabulary: doctor
diagnoses, confirm routes, treatment or surgery writes, recovery proves.

## What Changes

- Add repo-local skills for `wiki-confirm`, `wiki-treatment`, `wiki-surgery`,
  and `wiki-recovery`.
- Keep `wiki-review-decisions` as a legacy compatibility alias that points to
  `wiki-confirm`.
- Strengthen `wiki-doctor` so it points users to the next medical-loop stage
  instead of exposing only the raw adjudication CLI.
- Add skill marker tests and evaluation evidence for the drift fix.

## Out Of Scope

- Changing the already-implemented Python executors.
- Applying treatment or surgery automatically.
- Turning `wiki-doctor` into a full triage router; that is a later phase after
  the stage skills are stable.
- Writing README or public-facing marketing docs.
