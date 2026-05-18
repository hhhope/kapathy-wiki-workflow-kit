# Design

## Parent Workflow Boundary

Delivery-sensitive work must enter the workflow that owns intent, output shape,
review, and evidence before any low-level executor runs.

For reader-facing reports and H5 pages, `public-report-quality-gate` remains the
outer gate. When the work needs visual assets, it delegates article-level visual
planning to `knowledge-article-visual`, per-image scripts to
`infographic-onepager`, and bitmap generation to `imagegen`.

The required visual chain is:

`public-report-quality-gate -> knowledge-article-visual -> infographic-onepager -> imagegen`

## Anti-pattern

`Tool Executor Bypass` means routing directly to a low-level tool because the
user mentioned the tool, while skipping the parent workflow that owns the
deliverable.

The first local example is visual production: user asks for H5 section images
and mentions image model; the agent jumps to `imagegen` before inspecting
existing visuals or creating per-image scripts.

## Proof Boundary

The behavior asset and replay evidence improve repo-visible routing. They do
not prove every future client will automatically load the right skill. The proof
only covers repository instructions, skill text, pressure scenarios, and the
current H5 visual route.

## Triggering H5 Application Boundary

The current triggering H5 visual work is an application of the corrected route,
not a general art-direction rule for every future report.

For this H5 only, the visual assets must reuse the existing report grammar:
warm paper background, thick black marker outlines, large handwritten Chinese
headings, colored number badges, boxed modules, arrows, doodle icons, and
bottom takeaway banners.

Image-model output may be used directly only if Chinese text is readable. If
text quality fails, use a hybrid route: image-model background or texture plus
deterministic Chinese text overlay.
