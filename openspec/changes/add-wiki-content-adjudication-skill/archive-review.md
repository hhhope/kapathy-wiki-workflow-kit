# Archive Review

Decision: archive as superseded; skip stable spec promotion.

## Evidence

- `tasks.md` is complete: 4/4 checked.
- `openspec validate add-wiki-content-adjudication-skill --strict` passed.
- The follow-up change `rename-wiki-content-adjudication-skill-to-doctor`
  supersedes this user-facing skill name before stable spec promotion.
- The active repo-local skill surface now uses `wiki-doctor`, not
  `wiki-content-adjudication`.

## Boundary

- Do not promote `wiki-content-adjudication-skill` into `openspec/specs/`.
- Keep this change as historical evidence for the intermediate direct-entry
  design.
- Stable skill behavior is owned by
  `rename-wiki-content-adjudication-skill-to-doctor`.

## Residual Risk

Archive history will contain the old intermediate name. Current runtime tests
and README skill-surface tests reject obsolete or unsupported active surfaces.
