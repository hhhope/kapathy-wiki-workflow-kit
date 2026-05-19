## Context

The confirmed Superpowers design lives at:

`docs/superpowers/specs/2026-05-19-interview-deep-reading-board-design.md`

This OpenSpec change copies that approved design into the repository lifecycle
surface and defines the implementation boundary.

## Design

### Interview Module

Create `.codex/skills/interview-deep-reading-board/SKILL.md` as an
interview-specific module.

The module owns:

- detecting interview-like source shapes and compression-sensitive requests;
- asking the fork question before building the full-window reading board;
- preserving source order, speaker turns, adjacent-window continuity, and
  user-highlighted passages;
- defining how word cloud, timeline, temperature axis, and evidence panel work
  together;
- preserving copyright-safe coverage through paraphrase, source position, and
  short evidence snippets.

The module does not own public reader intent, review-ready claims, Feishu sync,
publication, generic material processing, WeChat fetching, or OpenSpec
lifecycle.

### Required Fork Question

When the trigger matches, the skill should ask:

> 这类访谈适合做“全文窗口式精读板”：按访谈顺序拆成足够多的阅读窗口，保留人物回合、时间线、温度轴、关键词和证据。要不要做这个类型？

The English skill body may include an English equivalent for authoring clarity,
but the normal user-facing question should be usable in Chinese because this
repository's source-processing collaboration is commonly Chinese-facing.

### Public Output Gate Integration

`public-report-quality-gate` remains the parent gate for reader-facing HTML,
H5, share drafts, and public reports.

Add `interview-deep-reading-board` to the gate's delegation map for:

- interview deep reading;
- interview word clouds;
- interview timelines;
- temperature-axis evidence boards;
- draggable evidence H5 outputs.

Add a hard route check: if the source is interview-like and the requested
reader-facing output includes deep reading, word cloud, timeline, temperature
axis, draggable evidence, or a no-compression/full-text-coverage request, the
agent must not jump straight into ordinary report drafting or HTML production.
It must route through `interview-deep-reading-board` first.

### AGENTS Routing

Update the repo `AGENTS.md` High-Frequency Skills table with one lightweight
row for this skill.

`AGENTS.md` should only route to the skill. It should not duplicate window
counts, temperature-axis semantics, copyright handling, or H5 reference
details.

### H5 Reference and Example

Add a skill reference:

`/.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`

The reference should describe the reusable H5 shape:

- source-order reading windows as the primary content unit;
- word cloud as an index only;
- temperature axis as the horizontal reading control;
- timeline markers preserving interview sequence;
- evidence panel linked to selected windows;
- default focus on user-highlighted or previously missed passages when
  repairing a drifted output;
- copyright boundary for short evidence plus paraphrase and source position.

Add a wiki example:

`wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`

The example should point to:

- `wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html`
- `wiki/reports/lixiang-luoyonghao-ai-agent-reading-board-data.js`
- `wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md`
- `wiki/reports/lixiang-luoyonghao-ai-agent-wordcloud.html` as a counterexample

### Evaluation

Because this semantically creates a repo-local skill and modifies output gate
routing, evaluation must include:

- pressure scenarios;
- RED baseline;
- GREEN result;
- residual risks;
- prior-art/common-rule dedupe;
- behavior replay evidence;
- reference/example visibility proof.

### Non-Goals

- Do not regenerate or restyle the Li Xiang H5 in this change.
- Do not sync anything to Feishu.
- Do not create a generic long-form article reading skill.
- Do not replace `material-collaboration-defaults`,
  `public-report-quality-gate`, `weixin-reader`, or `learning-capture`.
- Do not copy full copyrighted interview text into the skill, example, or
  reference.

## Verification

Implementation verification should include:

```bash
python3 scripts/check_behavior_assets.py
rg -n 'interview-deep-reading-board|访谈|temperature|full-window|全文窗口' AGENTS.md .codex/skills openspec/changes/add-interview-deep-reading-board wiki/examples
python3 -m html.parser wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html
```

If the wiki example introduces frontmatter, also run:

```bash
python3 scripts/check_wiki_frontmatter.py
```
