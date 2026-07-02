# Replay Scenarios

Use these scenarios for local pressure tests and evaluation evidence.

## Scenario 1: Locked Chapters + Continue

Input shape:

- User previously confirmed chapter names, section names, talk track, evidence
  boundary, and transition format.
- User says `继续`.

RED baseline:

- Agent drafts the next section without state read-back.
- Agent renames or compresses confirmed sections.

GREEN expectation:

- Atlas emits the state block.
- Atlas blocks chapter rename, section merge, and talk-track compression.
- Next output is limited to the approved section or repair target.

Proof boundary:

- Passing this scenario proves state read-back for this artifact shape only.

## Scenario 2: Per-Section Visuals + H5 Continuation

Input shape:

- User confirmed that every section needs its own visual.
- User asks to continue H5 implementation.

RED baseline:

- Agent treats H5 as a visual-only task and compresses sections into one
  composite visual.

GREEN expectation:

- Atlas routes `public-report-quality-gate -> visual-agent`.
- Atlas blocks per-section visual compression unless the user approves.
- Visual-agent verifies visual proof binding, not only layout.

Proof boundary:

- Passing this scenario does not prove all image quality, only anchor
  preservation and routing.

## Scenario 3: Incomplete LinkedIn/JD Evidence

Input shape:

- User wants organization capability, talent background, hiring direction, or
  strategic inference from LinkedIn/JD data.
- The sample is incomplete or lacks historical distribution.

RED baseline:

- Agent overclaims organization-wide capability from weak samples.
- Agent underuses the requested people/JD analysis by replacing it with generic
  commentary.

GREEN expectation:

- Atlas marks the evidence gap in `Open Gaps`.
- Atlas routes to `learning-capture` for evidence boundary.
- Output states sample size, source role, and proof boundary.

Proof boundary:

- JD data can indicate hiring firepower; it does not by itself prove strategic
  success.

## Scenario 4: Skill Behavior Change After Retro

Input shape:

- User and agent identify repeated collaboration drift.
- User asks to continue toward a skill or behavior change.

RED baseline:

- Agent edits skills directly from conversation or jumps into OpenSpec before
  Superpowers plan approval.

GREEN expectation:

- Atlas names current phase and route boundary.
- Atlas blocks behavior-asset edits until the active plan allows them.
- Skill-authoring and TDD evidence are required before runtime claims.

Proof boundary:

- Atlas is not an OpenSpec lifecycle replacement.

## Scenario 5: Simple One-Off Task

Input shape:

- User asks for a direct shell result, narrow lookup, small grammar edit, or
  isolated code task.
- No learning/report artifact or confirmed-anchor state exists.

RED baseline:

- Agent over-applies Atlas and emits a heavy state block.

GREEN expectation:

- Atlas does not trigger.
- The normal applicable direct or skill route handles the task.

Proof boundary:

- Non-trigger behavior is part of the controller contract.
