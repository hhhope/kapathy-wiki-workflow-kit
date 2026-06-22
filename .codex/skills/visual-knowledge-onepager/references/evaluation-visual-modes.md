# Evaluation: HTML Visual Modes

Date: 2026-05-04

## Baseline Scenario

User provides an article/report and asks for a Xiaohongshu HTML one-pager, then rejects the output because it is too text-heavy compared with a hand-drawn reference image.

## RED Baseline

`rg -n "hand|draw|visual mode|mode|reference|手绘|类型" skills/visual-knowledge-onepager`

Baseline result:

- `SKILL.md` only routed HTML one-pagers to retro-grid visual language.
- `html-onepager-template.md` only described a retro pop-art grid page.
- No selectable `handdrawn-teaching` mode existed.

Likely failure:

- Future runs would add more cards, chips, or conclusions instead of changing the visual grammar toward concrete hand-drawn teaching objects.

## GREEN Result

Added:

- `SKILL.md` rule requiring an HTML visual mode choice.
- `references/html-visual-modes.md` with `retro-grid` and `handdrawn-teaching` selection rules.
- `references/html-onepager-template.md` mode-specific visual rules.

Expected behavior:

- For data-heavy reports, choose or offer `retro-grid`.
- For concept teaching, hand-drawn references, or user complaints about too much text, choose or offer `handdrawn-teaching`.
- For unclear prompts, ask the user to choose between the two types.

## Residual Risks

- This is documentation-level behavior proof, not a multi-agent rollout proof.
- The next real use should verify whether the agent actually asks for or infers the mode before drafting HTML.
