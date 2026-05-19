# Proposal: medical-agent MOC surgery preview

## Summary

Add a read-only `moc_surgery_preview` route to the wiki medical agent.

## Problem

The MOC generator can already produce dry-run object lifecycle previews, but
the normal `$report-wiki-portfolio:wiki-medical-agent` entry point does not
recognize MOC preview requests. A request such as `moc preview status` is
currently classified as `treatment_preview`, which is the wrong medical-loop
route.

MOC is structurally sensitive. It should not be treated as treatment, because
MOC create/update/orphan actions are generated navigation changes that require
surgery review.

## Scope

In scope:

- Add a read-only `moc_surgery_preview` intent.
- Route explicit MOC preview/surgery/review requests before generic treatment
  preview matching.
- Build a MOC dry-run plan and pass it to existing surgery preview logic.
- Return compact MOC and surgery summaries in the medical-agent payload.
- Add tests proving MOC preview does not write `wiki/moc` or update the case.

Out of scope:

- Writing `wiki/moc`.
- Running MOC `--apply`.
- Writing treatment records.
- Writing surgery records.
- Updating the active case file.
- Mutating `Confirmed Decisions`, taxonomy config, ADRs, AGENTS, skills,
  unrelated OpenSpec lifecycle state, or archiving changes.

## Success Criteria

- `moc preview surgery` routes to `moc_surgery_preview`.
- `preview apply confirmed treatments` still routes to `treatment_preview`.
- With one active case, the medical-agent payload includes `moc_projection` and
  `surgery_preview`.
- With no active case, the route blocks with `no_active_case`.
- Preview creates no `wiki/moc` directory and does not modify the case file.
