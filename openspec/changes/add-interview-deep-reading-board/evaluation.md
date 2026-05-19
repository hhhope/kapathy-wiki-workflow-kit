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

Verified GREEN evidence after implementation:

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Interview deep-reading trigger asks the output-type fork question | `.codex/skills/interview-deep-reading-board/SKILL.md` includes interview triggers and the Chinese full-window reading-board fork question. | PASS |
| Word cloud is index-only | `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md` states word cloud is an index into source-order windows and evidence. | PASS |
| User-highlighted passage protection is explicit | `SKILL.md` and the skill evaluation require named passages to become explicit windows or window groups. | PASS |
| Public H5 output preserves parent gate | `.codex/skills/public-report-quality-gate/SKILL.md` delegates interview H5 structure while retaining reader intent, reference, visual, judgment, publish, and sync blockers. | PASS |
| Repo entrypoint routes the skill | `AGENTS.md` includes a lightweight route to `interview-deep-reading-board`. | PASS |
| H5 reference/example is visible | `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md` links the validated H5/data/source and old word-cloud counterexample. | PASS |

Verification snippets:

```text
test -e .codex/skills/interview-deep-reading-board/SKILL.md
skill_exists_after=0

test -e wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md
example_exists_after=0

rg -n 'interview-deep-reading-board|全文窗口式精读板|temperature-axis evidence board|interview deep reading' AGENTS.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/interview-deep-reading-board wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md
AGENTS.md: route to `.codex/skills/interview-deep-reading-board/SKILL.md`
public-report-quality-gate/SKILL.md: delegation row and hard route check
interview-deep-reading-board/SKILL.md: required Chinese fork question
wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md: validated output-shape example
```

## Behavior Replay Evidence

| Situation | Trigger | Expected route | Repo-visible artifact | Expected output or non-output | Boundary |
|---|---|---|---|---|---|
| User asks for a word cloud from a long interview | Interview-like material plus word-cloud output | Ask whether to create the full-window interview reading board | `interview-deep-reading-board/SKILL.md` and `references/h5-output-shape.md` | Word cloud becomes an index into windows and evidence, not the main structure | Does not create a generic long-form article skill |
| User says a passage was compressed or dropped | User names missing interview passage | Preserve the passage as an explicit window or window group | skill evaluation and Li Xiang wiki example | Named passage is not hidden under generic `Agent` keywords | Does not store full transcript verbatim |
| User asks for a reader-facing interview H5 | H5/share/report output from interview-like material | `public-report-quality-gate` parent route, then interview module | public gate skill plus AGENTS route | Public output gates remain active before review/publish/sync claims | Interview module does not replace public gate |
| Future agent needs the H5 shape | Similar interview reading-board request | Load H5 reference and wiki example | `references/h5-output-shape.md` and `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md` | Validated H5 is the positive shape; old word cloud is the counterexample | Example is output-shape guidance, not publication proof |

## Prior-Art / Common-Rule Dedupe

Scanned:

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

## Validation Evidence

Commands run on 2026-05-19:

```text
python3 scripts/check_behavior_assets.py
PASS

rg -n 'interview-deep-reading-board|访谈|temperature|full-window|全文窗口' AGENTS.md .codex/skills openspec/changes/add-interview-deep-reading-board wiki/examples
PASS - route, skill, gate, OpenSpec, and wiki example hits found

python3 -m html.parser wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html
PASS

python3 scripts/check_wiki_frontmatter.py
PASS

openspec validate add-interview-deep-reading-board --strict
PASS - Change 'add-interview-deep-reading-board' is valid
```

The first behavior-asset check failed until this evaluation used the required
`Scanned:` label for prior-art/common-rule dedupe. After the label was fixed,
the checker passed.

OpenSpec validation printed PostHog DNS flush errors after the local valid
result. Those errors are telemetry network failures and do not change the local
validation result.
