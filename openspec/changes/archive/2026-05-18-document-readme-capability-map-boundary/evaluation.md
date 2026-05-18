# Evaluation: README capability map boundary

## Evidence

| Check | Result | Notes |
| --- | --- | --- |
| `openspec validate document-readme-capability-map-boundary --strict` | PASS | Change validated. The command printed a PostHog telemetry network flush error after validation, but exited successfully. |
| `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md` | TARGET PASS | `target.entry_count: 0`. Whole-wiki gate remains failed on pre-existing legacy drift. |
| `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0034-readme-capability-map-is-project-description.md` | TARGET PASS | `target.entry_count: 0`. Whole-wiki gate remains failed on pre-existing legacy drift. |
| Diff scope review | PASS | Edited README, ADR index, new ops trace, new ADR, and this OpenSpec change only. No runtime scripts, skills, AGENTS, or command behavior files were edited. |

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: user asks to describe the project layers and capability map in README | Route through repo-public README lightweight path; update README as project description; record drift evidence and ADR because the boundary is stable | PASS |
| Negative: user asks to make README the runtime first-read contract | Reject promotion; keep README descriptive; route runtime behavior through OpenSpec/ADR/skills/command docs | PASS |

## RED Baseline

Input or situation shape: user said the project hierarchy and capability map
should be described in README before runtime work.

Trigger condition: live brainstorming discussion was already saturated with
runtime/MOC terms, so the agent drifted.

Observed failure: the answer first proposed a separate runtime capability-map
artifact, then described README as a runtime first-read contract.

## GREEN Result

Expected route: README lightweight public artifact path plus OpenSpec/ADR
boundary documentation.

Repo-visible artifacts:

- `README.md`
- `wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md`
- `wiki/adr/0034-readme-capability-map-is-project-description.md`
- `openspec/changes/document-readme-capability-map-boundary`

Expected output: README describes project layers and capabilities, while the
ADR states README is project description and not runtime authority.

Promotion or non-promotion boundary: README prose does not promote future MOC
or runtime behavior to an implemented capability.

Proof boundary: validation proves documentation boundary only, not runtime
behavior.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/specs/public-report-quality-gate/spec.md`
- `openspec/specs/behavior-replay-gate/spec.md`
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`
- `.codex/skills/public-report-quality-gate/SKILL.md`

Owns:

- README-specific capability map description boundary.

References:

- Public report lightweight path for repo-public artifacts.
- Existing wiki runtime layer boundary for runtime authority separation.
- Behavior replay gate for future-behavior claims.

Rejects:

- Moving generic git, testing, or behavior-asset rules into README.
- Treating README as runtime source of truth.

## Parent Gate Preservation

Parent gate: repo-public README edits still preserve the public-report
lightweight path. This change keeps README as a reader-facing project
description and preserves the specialized gates for OpenSpec, ADR, skills,
command docs, generated status, and runtime implementation evidence.

## Residual Risks

- README can still grow too detailed if future changes add operational rules
  there instead of linking to the owning artifacts.
- The boundary is documentation-only; future runtime changes still need their
  own OpenSpec and replay evidence.

## Expected Checks

- `openspec validate document-readme-capability-map-boundary --strict`
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md`
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0034-readme-capability-map-is-project-description.md`

## Boundary

This evaluation only proves the documentation boundary and targeted frontmatter
shape. It does not prove Obsidian MOC projection, runtime routing changes, or
new command behavior.
