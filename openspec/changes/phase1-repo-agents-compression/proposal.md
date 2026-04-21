## Why

The repository has already completed and archived the repo-level Phase 0 gate
for `agents-governance-drift`, but the repo `AGENTS.md` remains large and still
duplicates material that now has stable homes in ADRs, specs, and wiki pages.

The next repository-local step is Phase 1:

- compress the repo `AGENTS.md`
- convert repeated governance blocks into bounded proxies
- keep repo-specific execution rules that still need to live in the repo entry
  point

Without a dedicated Phase 1 change, the repository risks drifting between:

- "Phase 0 is done, so migration can just happen ad hoc"
- "candidate migration ideas still count as the plan"

## What Changes

- Define the accepted migration target for the repo `AGENTS.md`.
- Compress repeated governance sections into bounded proxy wording.
- Keep repo-specific execution constraints that still belong in repo
  `AGENTS.md`.
- Verify that every new proxy points to a stable repo-visible source.
- Record before/after evidence for line count, proxy coverage, and remaining
  repo-only sections.

## Capabilities

### New Capabilities

- `phase1-repo-agents-compression`: The repository SHALL execute repo-level
  `AGENTS.md` compression and proxy migration only through an explicit Phase 1
  change.

### Modified Capabilities

- `repo-agents-governance-phase0`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/phase1-repo-agents-compression/`.
- Targets the repo `AGENTS.md` as the main implementation surface.
- Does not automatically include root dotfiles or commit hook implementation.
