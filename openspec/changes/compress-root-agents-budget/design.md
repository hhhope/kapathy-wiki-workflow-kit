## Design Boundary

Target layer: Root AGENTS.

Root `~/.codex/AGENTS.md` owns cross-repo safety floor and entrance routing. It
must not own repo-local archive detail, rule bodies, skill bodies, or wiki
method content.

This change only performs structural compression of the current root guidance.
It keeps the same authority model and moves detailed routing data into a
root-local support file when that data is too bulky for the entrance card.

## Reused Governance

This change reuses the archived `decide-root-governance-alignment` model:

- Six principles: single source of truth, authority order, triggered assets,
  instruction budget, evidence before behavior change, candidate vs decided.
- Six-step process: declare layer, check source of truth, check authority,
  choose surface by semantic weight, record evidence, self-check.
- Pattern Catalog target: Root AGENTS.
- Self-Check four columns: structure, semantic, evidence, boundary.

No new pattern, checklist field, or rule category is introduced here.

## Compression Strategy

### 1. Extract Rule Routing Detail

The existing `Global Rule Routing` table is valid root-layer content, but it is
too detailed for the root entrance card. The root file should retain a compact
instruction to load the root-local routing reference before non-trivial
implementation or verification. The detailed table moves to
`~/.codex/rule-routing.md`.

The support file remains root-local, stack-generic, and personal. It is not a
repo policy page and does not replace repo `AGENTS.md`.

### 2. Consolidate Git and Execution Discipline

The current `Execution discipline` and `Git discipline` sections overlap on:

- dirty tree handling
- committing only task-related files
- resume checks
- push/claim truth-source checks

The consolidated section must preserve the behavioral stops while removing
duplicated wording.

### 3. Preserve Hard Stops

The compression must not weaken:

- pre-task health check
- active OpenSpec requirement for large work
- OpenSpec completion stop
- destructive git protection
- dirty tree preservation
- raw-data validation for new APIs or fields
- skill semantic edit gate
- long-step reporting

## Budget Target

Primary target: `~/.codex/AGENTS.md` at or below 220 lines.

Stretch target: at or below 200 lines.

The 150-200 target remains the reference budget, but this change may pass with
an explicit justification above 200 only if every retained line maps to Root
AGENTS Purpose / Owns and the largest remaining bulky section has a named
follow-up boundary.

## Evidence Plan

`evaluation.md` records:

- baseline line/word/byte counts
- after line/word/byte counts
- section mapping before and after
- extracted support-file line count
- Self-Check four-column result
- residual risks
