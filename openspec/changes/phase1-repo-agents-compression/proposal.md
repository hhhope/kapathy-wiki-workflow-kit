## Status: Parked (2026-05-06)

This change is parked, not withdrawn. Two reasons:

1. **Name conflict.** "Phase 1" in `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` §12 means "build a manual harness template" (intake's phased recommendation). The name in this change's title refers to repo-AGENTS compression. The conflict is called out in `openspec/changes/archive/2026-05-06-decide-root-governance-alignment/` design-trace §13. Keeping the name while the conflict is unresolved risks future confusion.

2. **Sequencing.** The real drift driver is `~/.codex/AGENTS.md` at 281 lines. A successor change will compress it using the Pattern Catalog adopted by `decide-root-governance-alignment`. Only after that run should repo AGENTS compression be revisited — with real experience of how the catalog handles line-by-line compression.

Unpark decision belongs to a later review. When unparked, this change should be renamed away from "Phase 1" to avoid the intake conflict, or the intake §12 Phase 1 definition should be formally retracted — whichever option the review takes first.

No task closure, spec delta, or implementation work should proceed while this change is parked.

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
