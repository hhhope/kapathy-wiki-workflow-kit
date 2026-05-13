# Agent Intent Routing Design

Date: 2026-05-13
Status: approved design for follow-up implementation planning

## Problem

The repository has strong delivery gates, but an agent can still treat a
repo-public writing request as an ordinary Markdown edit.

The observed failure was `readMe写一下`: the README was rewritten before the
agent clearly routed the request through the reader-facing output gate and
before it scanned README-specific repository requirements. The missing step was
not a README learning skill. It was an entry-layer intent classification before
acting.

## Goal

Add a lightweight Agent Intent Routing layer that classifies user intent before
execution and routes the request to the applicable parent gate.

The routing layer should prevent repo-public outputs from bypassing
`public-report-quality-gate` while preserving existing specialized gates for
wiki frontmatter, skill authoring, OpenSpec changes, and external learning.

## Non-Goals

- Do not build a large generic output framework.
- Do not make `public-report-quality-gate` the router for all tasks.
- Do not require a `wiki/ops/*-report-gate-review.md` artifact for every small
  README or docs edit.
- Do not let the public gate replace wiki frontmatter taxonomy, skill authoring,
  OpenSpec lifecycle, or learning-capture gates.

## Routing Model

Before acting, the agent classifies user intent.

If the request writes, rewrites, polishes, prepares, or updates an artifact that
will be read outside the current chat or worklog, the agent routes through the
applicable parent gate before editing.

Minimum routing map:

```text
repo-public artifact
  -> public-report-quality-gate lightweight path
  -> examples: README.md, docs/*, examples/*, published templates

reader-facing report / Feishu draft / H5 / share page
  -> public-report-quality-gate full path

external article / repo / README used for learning
  -> learning-capture, then the narrower module

semantic skill edit
  -> skill authoring contract, writing-skills, and TDD requirements

wiki frontmatter edit
  -> wiki-frontmatter-taxonomy gate
```

## Public Gate Lightweight Path

When Agent Intent Routing classifies a request as a repo-public artifact, it
enters a lightweight path under `public-report-quality-gate`.

Required checks:

- Identify the reader and the job the reader should complete.
- Scan artifact-specific constraints before drafting.
- Avoid internal residue unless the artifact intentionally documents repo
  mechanics.
- Verify with fresh evidence before claiming the artifact is complete,
  review-ready, published, or synced.

Gate-review artifact requirement:

- Required for review-ready, publish, Feishu sync, complex reference-shaped, or
  drift-corrected outputs.
- Not required by default for small repo-public documentation edits.

## README Scenario

For `readMe写一下`, the expected route is:

```text
intent = write repo-public artifact
parent gate = public-report-quality-gate lightweight path
artifact constraints = scan README SHALL / README / readme in
  AGENTS.md, PROJECT.md, openspec/specs, .codex/skills, wiki/adr, wiki/ops
draft = README edit
verify = reader target + constraint scan + replay evidence
```

The route should find requirements such as:

- README lists the repo-local wiki skill surface.
- README keeps `.codex/skills/wiki-status/SKILL.md` as the status source path.
- README warns against root/user-scope wiki skill duplicates.
- README warns against plugin marketplace metadata for the wiki runtime surface.

## Assets To Change In Implementation

- `AGENTS.md`: add a short `Agent Intent Routing` section with the entry rule
  and minimal mapping. Keep it compact and avoid duplicating full skill bodies
  or vocabulary.
- `.codex/skills/public-report-quality-gate/SKILL.md`: add repo-public artifact
  trigger semantics and the lightweight path.
- OpenSpec spec: add or update a spec requiring repo-public artifacts to route
  through Agent Intent Routing and the public gate lightweight path.
- Evaluation evidence: record pressure scenarios, RED baseline, GREEN result,
  and residual risks.

## Behavior Replay Scenarios

Implementation must include replay evidence for at least these scenarios:

| Scenario | Expected route |
|---|---|
| `readMe写一下` | Agent Intent Routing -> repo-public artifact -> public gate lightweight path -> README constraint scan |
| `把这个 wiki/ops 改成飞书文章` | reader-facing rewrite -> public gate full path |
| `这个外部 README 学一下能不能复用` | learning-capture -> readme-learning-capture module |
| `改一下 wiki frontmatter` | wiki-frontmatter-taxonomy gate |

The README incident replay must show:

- RED baseline: existing routing allowed a README rewrite without an explicit
  public gate route and artifact-specific constraint scan.
- GREEN result: new routing requires the public gate lightweight path and README
  constraint scan before editing.

## Residual Risks

- Very small wording edits to repo-public artifacts may feel heavy if the gate
  is interpreted as a full report gate. The lightweight path exists to keep that
  cost bounded.
- The constraint scan may surface many unrelated README mentions. The
  implementation should define a focused scan pattern and require relevance
  filtering rather than opening every hit.
- Some artifacts may be both internal wiki records and reader-facing drafts. If
  intent is ambiguous, the agent should re-anchor before editing.
