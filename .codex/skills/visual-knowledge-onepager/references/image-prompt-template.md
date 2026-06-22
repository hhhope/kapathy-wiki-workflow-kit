# Image Prompt Template

Use this only after the user confirms they want image generation.

## Base prompt skeleton

```text
Create a flat graphic design infographic poster for Xiaohongshu (Little Red Book) about「[主题名称]」.

=== CRITICAL STYLE REQUIREMENTS (MUST FOLLOW EXACTLY) ===

【OVERALL ART STYLE】
- 1970s retro pop art and underground comic illustration style.
- Strict Swiss international grid system layout.
- Pure 2D flat vector aesthetic with subtle screen print texture.
- Uniform thick black outlines for all illustrations, text boxes, and grid dividers.
- Absolutely no gradients, shading, drop shadows, or 3D effects.
- High information density: pack 6-7 modules into distinct grid cells.
- Visually dense but rhythmic, leaving a few colored cells with minimal content for breathing room.

【COLOR PALETTE】
- Background: warm vintage cream / beige (#F5F0E6)
- Accent colors: salmon pink, sky blue, mustard yellow, mint green
- Anchors: pure black (#000000) and pure white (#FFFFFF)
- All outlines: thick black

【HEADER AREA】
- Main title: [主标题]
- Subtitle: [副标题]

【GRID LAYOUT】
- Divide the poster into multiple square and rectangular cells using thick black lines.
- Must include 6-7 distinct modules per image.
- Separate text-heavy and illustration-heavy cells.
- Warning content must appear in a black cell with white text.

【ILLUSTRATIONS】
- Draw custom flat pop-art illustrations for the topic.
- Use quirky simplified product or scenario icons.
- Add abstract symbols, warning signs, stars, arrows, checkerboards, and diagonal textures.
- Faces may use vintage comic-style smiley/frowny indicators when helpful.

【TYPOGRAPHY】
- Bold, highly legible sans-serif or retro display fonts.
- All text in Chinese except optional decorative English words like WARNING or INFO.
- No cursive or messy handwriting.

【WHAT TO AVOID】
- No 3D rendering, realistic material texture, gradients, or soft shadows.
- No thin lines.
- No floating or unstructured layout.
- No pure white background.

【IMAGE SPEC】
- Aspect ratio 3:4 portrait, optimized for Xiaohongshu.

=== CONTENT FOR THIS IMAGE ===
主标题：[主标题]
副标题：[副标题]
网格内容分配：[逐格写明每个 grid 放什么，哪个是黑底警告格，哪个是彩底数据格]
需要绘制的插图：
1. [插图1]
2. [插图2]
3. [插图3]
```

## Module mapping rule

The prompt must explicitly assign content to 6-7 grids. Recommended mapping:

- Grid 1: brand/options cell
- Grid 2: parameter/threshold cell
- Grid 3: scenario comparison cell
- Grid 4: model/type/tip cell
- Grid 5: recommendation or table cell
- Grid 6: black-background warning cell
- Grid 7: optional summary or quick-check cell

## Pre-generation checklist

Before sending the prompt, verify:

- The prompt explicitly says `strict grid system layout`
- Thick black outlines are required everywhere
- The retro color palette is spelled out
- There are 6-7 modules, not fewer
- The warning block is black background with white text
- Gradients, 3D, shadows, and messy layout are explicitly banned

## Output rule

Generate one full prompt per image. Do not merge multiple images into one giant prompt unless the user explicitly wants a combined sheet.
