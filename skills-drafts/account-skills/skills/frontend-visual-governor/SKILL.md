---
name: frontend-visual-governor
description: Use when an existing frontend page, dashboard, chart surface, icon system, widget layout, or UI interaction needs visual repair, polish, density cleanup, or interaction cleanup.
---

# Frontend Visual Governor

Use this skill for frontend visual polish and interaction cleanup on an
existing UI surface, especially dashboards, analytics pages, charts, icon usage,
and widget-style boards.

This is a child worker, not a visual-production controller. Ordinary requests
to make, draw, generate, convert, or choose a visual artifact must enter through
`visual-agent` first. When called from `visual-agent`, keep the route block and
mode/verification boundary visible.

## Scope

Apply this skill when the user asks to:
- improve an existing frontend page style, polish, layout, or overall visual quality
- fix awkward interactions in dashboards or data-heavy pages
- improve charts, legends, tooltips, axes, hover states, or visual density
- choose or replace chart/icon/UI libraries
- simplify a frontend page that is getting too large to edit safely

Do not use this skill for:

- new diagrams, cards, posters, infographics, image-model output, whiteboards,
  or visual asset packages
- choosing between SVG, H5/HTML, image model, or hybrid output modes
- backend-only work

If the request is visual but not about an existing frontend/UI surface, route
back to `visual-agent`.

## Core rules

1. Prefer mature open-source over hand-rolled UI.
- For charts, prefer mainstream libraries already in the project.
- If current dependencies are insufficient, inspect existing deps first, then confirm with the user before adding a new frontend dependency.
- Do not hand-roll SVG charts unless the requirement is trivial.

2. Fix structure before color.
- If the page feels messy, first inspect layout model, density, spacing, hierarchy, and interaction model.
- Do not start with random color/button tweaks when the real issue is mixed layout systems or oversized components.

3. Keep component responsibilities narrow.
- Frontend files over 200 lines should trigger refactor-first behavior.
- Split into page shell, components, and composables before continuing major UI changes.
- Avoid rebuilding a large page as another large page.

4. Make interactions feel productized.
- Remove explicit implementation noise like drag hints, debug labels, and heavy control text from the surface.
- Prefer lightweight icon/menu controls for widget management.
- Hide/restore semantics should be clear; avoid ambiguous delete-vs-collapse behavior.

5. Charts must explain themselves.
- Axes, legends, and hover states must be readable.
- Use a clear rule for visual encoding. Example: bar = total, line = grouped series.
- If chart semantics are unclear, stop and confirm the metric meaning before polishing the chart.

6. Icons are optional.
- If icon meaning is not obvious, leave it out.
- Do not add decorative icons just to fill space.

7. Verify with real UI behavior.
- Build success is necessary but not sufficient.
- Check actual layout logic, control visibility, state transitions, and density.
- For long-running frontend work, report progress proactively if a step goes past 10 seconds.

## Default workflow

1. Inspect current page structure.
- Identify whether the page mixes multiple layout systems.
- Identify oversized files and interaction hotspots.

2. Inspect current dependencies.
- Check whether the repo already has a suitable chart/UI dependency.
- Reuse existing mature dependencies when possible.

3. Decide the real layer of change.
- Layout/model issue -> restructure first.
- Interaction issue -> simplify controls and state semantics.
- Visual issue -> unify spacing, surface style, density, and typography.
- Library issue -> confirm before introducing a new dependency.

4. Implement in this order unless there is a strong reason not to.
- page shell / layout model
- component split
- interaction cleanup
- chart replacement or polish
- final visual pass

5. Verify.
- Run the local frontend build.
- Check diff hygiene.
- If practical, confirm the live page behavior instead of trusting static code.

## Patterns to prefer

### Dashboard / analytics pages
- Use a unified widget model.
- Keep toolbar separate from board content.
- Put metrics, trends, risks, and tables into the same layout system.
- Let settings manage visibility, order, and size, not business meaning.

### Chart pages
- Prefer ECharts or another mainstream library already present.
- Keep legend lighter than data.
- Use compact hover content.
- Reduce grid and border noise.
- Make the chart readable before making it flashy.

### Settings / management drawers
- Group by user intent, not implementation fields.
- Use chip/button groups for presets where appropriate.
- Avoid exposing internal model jargon unless the user already works with it.

## Guardrails

- Do not add a new frontend dependency without first confirming the current dependencies are insufficient and telling the user.
- Do not hide structural problems behind color tweaks.
- Do not keep editing a large file in place once it crosses the repo threshold.
- Do not invent chart semantics; confirm unclear metrics first.
