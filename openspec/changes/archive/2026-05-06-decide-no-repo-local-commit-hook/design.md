## Context

The repository already completed Phase 0 with a weaker boundary:

- commit-gate status must be explicit before Phase 1

The user has now made the stronger product decision:

- repo-local commit hook should not be done

That is a narrower and more final statement than the current archived Phase 0
materials.

## Goals / Non-Goals

**Goals**

- Turn the "do not do repo-local commit hook" direction into a stable repo
  decision.
- Remove hook assumptions from the default future path.
- Preserve a clean reversal boundary for later changes.

**Non-Goals**

- Do not implement any hook.
- Do not revisit generic enforcement theory.
- Do not reopen the whole Phase 0 gate discussion.

## Decisions To Resolve

### Decision: "Not part of the default path" vs "forbidden forever"

The repository should likely decide:

- not part of the default path
- future change required for reversal

rather than trying to say hooks are impossible forever.

### Decision: Candidate pages need wording cleanup

Once the stable decision is recorded, older candidate pages should not remain
the strongest visible statement about hooks.
