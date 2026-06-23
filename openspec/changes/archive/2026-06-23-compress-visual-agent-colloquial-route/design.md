# Design: compact visual-agent runtime card

## Runtime Shape

`visual-agent/SKILL.md` should behave like a dispatch card, not a governance
paper. It should keep:

- when to trigger, including colloquial visual asks;
- the compact response block;
- the four output modes;
- the no-silent-H5/SVG rule;
- the child route map;
- two executor boundaries: visual verification and Feishu insertion approval.

Detailed replay, history, and proof stay in `evaluation.md` and OpenSpec.

## Colloquial Trigger Model

The trigger is the user's intent to create, add, polish, convert, or generate a
visual artifact, even when the wording is casual. Examples are useful only as
non-exhaustive cues.

The skill should not depend on exact phrases. "弄个图", "画一下", "整张图",
"做成卡片", "配几张图", "图像化一下", and similar requests are all the same
class: visual deliverable requested, mode not yet confirmed.

## Evaluation Focus

GREEN evidence must prove two things that the prior gate missed:

- the runtime skill body is compact enough to scan at trigger time;
- colloquial visual asks route to a mode fork instead of deterministic H5/SVG
  fallback.
