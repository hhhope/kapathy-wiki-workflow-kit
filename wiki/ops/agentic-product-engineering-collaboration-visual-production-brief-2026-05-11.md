---
artifact_type: visual-production-brief
title: agentic-product-engineering-collaboration / visual production brief
canonical_object: agentic-product-engineering-collaboration
layer: ops
domain: product-engineering-collaboration
ops_area: report-quality
created: 2026-05-11
status: draft
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/assets/account-wiki-runtime-card.png
  - wiki/reports/assets/account-wiki-validation-card.png
  - wiki/reports/agentic-visual-assets/
---

# Visual Production Brief

## Route

Use a hybrid route: hand-drawn illustration layer plus deterministic Chinese
text overlay. Do not use H5 card screenshots as final visual output.

Image model can generate low-text visual layers: paper texture, icons,
hand-drawn objects, arrows, badges, and composition. Chinese titles, section
labels, source counts, and conclusions must be overlaid deterministically.

Reference grammar:

- `account-wiki-onepager.png`: high-density vertical teaching poster.
- `account-wiki-runtime-card.png`: horizontal process teaching card.
- `account-wiki-validation-card.png`: horizontal framework card with objects,
  four modules, and bottom golden sentence.

## 00 Total Infographic

Format: vertical 2:3 or 3:4 long poster.

Core metaphor: a factory line that turns human/process middle work into a
reviewable operating system. Left side shows meetings, Jira, documents, and
human context passing. Middle shows `spec / eval / review / owner` conversion.
Right side shows `agent queue / review packet / wiki-rules-tests writeback`.

Modules:

1. Title: `AI Agent 时代，产研协作怎么变`
2. `01 行业在争什么`: four dispute axes.
3. `02 公司位置像哑铃`: execution automation end, governance end, bridge.
4. `03 作业系统变了`: ticket/spec/PR/eval/wiki/CI/logs as production objects.
5. `04 可审查循环`: target, context, queue, review packet, replay, writeback.
6. `05 人的位置`: CEO/GM, PM, design, engineering, QA/Data/Ops, HR/Manager.
7. `06 边界结论`: 30-60 day pilot, no full-automation promise.

Objects: relay baton, meeting table, Jira ticket, document pile, conveyor belt,
clipboard, replay tape, wiki pages, permission lock, audit magnifier, pilot
signpost.

Bottom sentence: `Agent 的价值不是替人判断，而是把中间工作变成可审查、可回放、可沉淀的系统循环。`

Acceptance:

- Reads as a chaptered poster, not a table of modules.
- At least six modules, each no more than four short lines.
- Chinese text is readable on mobile preview.
- Uses thick marker outlines, colored numbering, warm paper, doodle objects.

## 01 Industry Debate

Format: 16:9 horizontal teaching card.

Core metaphor: debate compass / debate arena.

Center question: `Agent 到底是工具、员工，还是作业系统？`

Dispute axes:

- `Coding solved?` vs `PM/协作没有消失`
- `速度提升` vs `责任归属`
- `小团队增强` vs `大组织治理`
- `员工派` vs `对象派`

Objects: arena, four-direction compass, microphones, voting cards, scale,
stopwatch, shield, question bubbles, source-card stack.

Boundary badge: `262 source entries 是源池规模，不是全网总量`

Bottom sentence: `争的不是会不会写代码，而是谁定义目标、验收结果、承担责任。`

Acceptance:

- Structure is understandable from the center diagram before reading bullets.
- Four axes are visually distinct.
- Does not say `全网`.
- Count anchor is visible but framed as source-pool size.

## 02 Company Dumbbell

Format: 16:9 horizontal teaching card.

Core metaphor: dumbbell plus load-bearing bridge.

Left end: `执行自动化端`

- issue
- IDE
- PR
- CI
- agent queue

Right end: `组织治理端`

- permission
- audit
- responsibility
- knowledge
- risk

Bridge: `产研协作桥`

- spec
- eval
- review
- owner
- writeback

Objects: real dumbbell outline, mechanical arms, PR cards, control tower, lock,
seal, ledger, riveted bridge, warning sign.

Warning block: `别把中间人消失当结论`

Boundary sentence: `这不是行业定论，而是观察框架；中间层没有消失，责任被抬高。`

Acceptance:

- No empty circles.
- Each end has at least four concrete objects.
- The bridge visually carries load.
- Shows traditional collaboration still existed, but its carrier changes.

## 03 Operating System Shift

Format: 16:9 horizontal teaching card.

Core metaphor: old human handoff line transformed into an executable work-object
console.

Left: old state

- PM translates.
- TL decomposes.
- QA catches quality.
- Ops chases status.

Middle converter: `会议/文档 -> 可执行对象`

Right: new work surface

- ticket: goal and boundary
- spec: context and constraint
- PR: result
- eval/test: acceptance evidence
- wiki/log: memory and replay

Attribute stamps:

- call
- review
- replay
- writeback

Objects: telephone chain, meeting notes, Jira card, conversion funnel, work
object panel, validation stamp, replay arrow, archive box.

Bottom sentence: `Agent 没有发明中间层，它重写了中间层的承载方式。`

Acceptance:

- Must show left/right contrast and middle conversion.
- At least five production objects appear.
- Attribute stamps look like stamps, not UI pills.
- Does not imply people disappear.

## 04 Reviewable Loop

Format: 16:9 horizontal teaching card, with a near-square loop as the main
diagram.

Core metaphor: circular track with human gates.

Loop nodes:

- `人定目标`
- `可执行上下文`
- `Agent Queue`
- `Review Packet`
- `Replay Trail`
- `System Writeback`

External gates:

- `人工审查`
- `失败冻结 / 退回修改`

Objects: circular track, queue tray, review folder, traffic-light gate, replay
film, wiki inbox, test checklist, human approval stamp, rollback arrow.

Bottom sentence: `每次执行都要留下证据、审查和写回。`

Acceptance:

- First glance shows a loop, not horizontal modules.
- Failure return path is visible.
- `Review Packet` is drawn as an evidence packet.
- High-risk nodes require human review.
- Includes all six loop nodes.
