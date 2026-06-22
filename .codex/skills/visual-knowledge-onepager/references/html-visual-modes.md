# HTML Visual Modes

Use this reference when the HTML one-pager branch is selected. The mode choice controls the page's visual grammar, not only its colors.

## Mode A: retro-grid

Choose `retro-grid` when the user wants:

- Swiss grid
- dense cards
- modular comparison
- metrics, standards, thresholds, rankings, or management-report density
- a clean one-flow infographic that feels structured and scannable

Visual grammar:

- hero plus 3-6 grid sections
- 3-column or 4-column blocks
- large numeric anchors
- tables, matrices, segmented comparison cards
- black-background warning block
- retro palette with thick borders and offset shadows

Failure mode:

- Do not let it become a generic dashboard. It should still read like Xiaohongshu dry-content, not SaaS UI.

## Mode B: handdrawn-teaching

Choose `handdrawn-teaching` when the user wants:

- more diagrams than text
- a hand-drawn reference image
- "像原图", "图示多一点", "不是结论的问题", or "不要全是文字"
- a concept explanation that should feel like a whiteboard teaching poster
- a governance model, operating principle, metaphor, or abstract framework made concrete

Visual grammar:

- one concrete visual action per section
- speech bubble -> document -> robot style flows
- bad vs good comparison scenes
- clipboard -> target essence diagrams
- numbered structure cards connected by dotted lines
- circular iteration loops with icons
- toolbox / brain / lightning / document / megaphone style conclusion objects
- short explanatory bullets placed beside or below the main drawing

Hard rule:

- Every main section must include at least one recognizable object or action. Abstract boxes alone do not satisfy this mode.

Failure mode:

- Do not solve the user's complaint by adding more conclusions, chips, or text blocks. The fix must change the visual grammar.

## Selection Behavior

If the user already provided a reference image, match the reference's mode unless they ask otherwise.

If the source is an article/report and no visual mode is implied, ask:

```text
这张一图流你想走哪种视觉类型？
1. retro-grid：网格卡片型，适合数据、对比、矩阵、管理汇报
2. handdrawn-teaching：手绘教学型，适合概念解释、流程拆解、少文字多图示
```

If the user says "都行" or "你定", choose:

- `handdrawn-teaching` for abstract concepts, methods, workflows, and mental models
- `retro-grid` for numeric reports, product comparisons, buying guides, and operational metrics
