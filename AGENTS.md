# Repo Instructions

This file adds repository-specific constraints for `report-wiki-portfolio`.

## OpenSpec Trigger

- Treat changes to repository-default workflow, collaboration behavior, routing defaults, escalation boundaries, or default output rules as OpenSpec-level changes.
- For these changes, create or select an active OpenSpec change before editing `wiki/`, `scripts/`, `skills-drafts/`, or other repository guidance files.
- Do not ship temporary wiki-only or skill-draft-only fixes first and backfill OpenSpec later.
- If the user asks to change how Codex should usually behave in this repository, assume it is a workflow change unless the request is explicitly limited to one page or one one-off run.

## Material Processing Default

- When the user drops materials and asks Codex to process them, do not stop at placeholder intake output.
- Default completion means readable `source` output first, then linked `ops` output when the material contains action signals.
- Ask the user only at real output fork-points, such as whether to update `html/h5/preview` artifacts in addition to wiki records.
