# Evaluation: interview deep reading board

## Pressure Scenarios

### Positive scenario: User asks for a word cloud from a long interview

- input or situation shape: user asks for a word cloud or visual reading aid
  for a long, multi-speaker interview.
- trigger condition: the source is interview-like and the requested artifact is
  likely to compress the interview.
- expected route: ask whether to create the full-window interview reading
  board before building the output.
- repo-visible artifact:
  `.codex/skills/interview-deep-reading-board/SKILL.md`,
  `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`,
  `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`, and this
  OpenSpec change.
- expected output: the word cloud is treated as an index into ordered reading
  windows and evidence, not as the main content container.
- promotion or non-promotion boundary: this promotes an interview module, not a
  generic long-form reading skill.
- proof boundary: markdown replay and local behavior-asset evidence, not
  automatic runtime dispatch proof in every future client.

### Positive scenario: User says the output compressed or dropped a passage

- input or situation shape: user points to a missing interview passage such as
  code volume, Feishu, Coworker, stable employee Agent, subagents, data, and
  MCP.
- trigger condition: user reports compression, fragmentation, or missing
  evidence in an interview deep-reading output.
- expected route: preserve the named passage as an explicit reading window or
  window group, and default repair focus to that passage when useful.
- repo-visible artifact:
  `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`
  and `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`.
- expected output: the passage is not hidden under generic keywords such as
  `Agent` or `Agent to C`.
- promotion or non-promotion boundary: user-highlighted passage protection is
  local to interview reading-board output and does not change generic summary
  behavior.
- proof boundary: pressure scenario evidence, not a claim that every past H5 is
  retroactively fixed.

### Positive scenario: Reader-facing interview H5 is requested

- input or situation shape: user asks to produce an H5/share/report artifact
  from an interview.
- trigger condition: the deliverable is reader-facing and interview-specific
  deep-reading structure is needed.
- expected route: `public-report-quality-gate` remains the parent gate, then
  delegates interview structure to `interview-deep-reading-board`.
- repo-visible artifact:
  `.codex/skills/public-report-quality-gate/SKILL.md`,
  `.codex/skills/interview-deep-reading-board/SKILL.md`, and
  `openspec/changes/add-interview-deep-reading-board/specs/public-report-quality-gate/spec.md`.
- expected output: public reader intent and review/publish boundaries remain
  under the public report gate.
- promotion or non-promotion boundary: the interview module does not become an
  independent public-output gate.
- proof boundary: behavior-asset wording and replay evidence, not Feishu sync
  or publication proof.

### Negative / should-not-trigger scenario: Non-interview article summary

- input or situation shape: user asks for a short ordinary article summary with
  no dialogue structure, no timeline/temperature axis, and no full-coverage
  concern.
- trigger condition: source is not interview-like and no compression-sensitive
  interview output is requested.
- expected route: use existing material, learning, or public-report workflows;
  `interview-deep-reading-board` should not trigger.
- repo-visible artifact: `AGENTS.md` routing and the skill's When Not To Use
  section.
- expected output: no unnecessary full-window interview board fork question.
- promotion or non-promotion boundary: avoids over-routing all long-form
  material into the interview module.
- proof boundary: local pressure scenario only.

## RED Baseline

Before this change:

| Scenario | Evidence | RED Result |
|---|---|---|
| Long interview word-cloud request preserves source-order reading | The first Li Xiang artifact treated the word cloud as the primary container and compressed the interview into loose keywords. | FAIL |
| Timeline and temperature axis are tied to concrete evidence | The early output did not reliably connect keyword temperature, source order, and evidence windows. | FAIL |
| User-highlighted passage remains visible | The Coworker / Feishu / stable Agent / subagent / MCP passage was dropped or compressed until the user pasted it back. | FAIL |
| Public H5 output route catches interview-specific deep reading | `public-report-quality-gate` has no interview-specific delegation route. | FAIL |
| Repo entrypoint routes interview deep-reading requests to a dedicated skill | `AGENTS.md` has no High-Frequency Skills row for interview reading boards. | FAIL |
| H5 output shape is reusable as a reference | The validated Li Xiang H5 exists as a report artifact but not as a skill reference or wiki example. | FAIL |

## GREEN Result

Expected GREEN evidence after implementation:

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Interview deep-reading trigger asks the output-type fork question | `.codex/skills/interview-deep-reading-board/SKILL.md` includes the trigger and required fork question. | PENDING |
| Word cloud is index-only | `references/h5-output-shape.md` states word cloud is an index into source-order windows and evidence. | PENDING |
| User-highlighted passage protection is explicit | `SKILL.md` and `evaluation.md` require named passages to become explicit windows or window groups. | PENDING |
| Public H5 output preserves parent gate | `public-report-quality-gate` delegates interview H5 structure while retaining public reader gates. | PENDING |
| Repo entrypoint routes the skill | `AGENTS.md` includes a lightweight route to `interview-deep-reading-board`. | PENDING |
| H5 reference/example is visible | `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md` links the validated H5/data/source and old word-cloud counterexample. | PENDING |

## Prior-Art / Common-Rule Dedupe

Scanned before implementation:

- repo `AGENTS.md`
- `PROJECT.md`
- `docs/superpowers/specs/2026-05-19-interview-deep-reading-board-design.md`
- `.codex/skills/material-collaboration-defaults/SKILL.md`
- `.codex/skills/public-report-quality-gate/SKILL.md`
- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/weixin-reader/SKILL.md`
- `openspec/specs/public-report-quality-gate/spec.md`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `wiki/config/behavior-asset-evaluation.yaml`
- shared writing-skills and test-driven-development guidance

Owns:

- interview-specific full-window reading-board routing;
- interview H5 output-shape reference;
- interview user-highlighted passage protection;
- interview word-cloud-as-index boundary.

References:

- `public-report-quality-gate` for reader-facing output readiness,
  review-ready claims, Feishu sync, and publish boundaries;
- `material-collaboration-defaults` for source-first material processing;
- `weixin-reader` for WeChat source retrieval;
- `learning-capture` for reusable learning capture;
- repo behavior-asset gates for skill evaluation and replay evidence.

Rejects:

- copying full interview rules into `AGENTS.md`;
- replacing the public report gate;
- creating a generic long-form article reading skill;
- storing full copyrighted interview transcripts verbatim in skill references
  or wiki examples;
- treating the old word-cloud-only artifact as the recommended output shape.

## Residual Risks

- Local behavior-asset evidence does not prove every future client will
  auto-load the skill.
- "Full coverage" remains a structured reading-window commitment, not a right
  to store an entire copyrighted transcript verbatim.
- Window-count guidance must stay proportional to source length.
- A visually polished H5 can still fail if the reading-window map is
  incomplete.
- Existing historical interview outputs are not automatically repaired.
