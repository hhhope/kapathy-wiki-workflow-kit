# Tasks

- [x] 1. Record heading/roadmap repair baseline
  - Create OpenSpec artifacts for the requested heading and roadmap repair.
  - Record the issue in the gate review if needed.

- [x] 2. Add technical planning fishbone visual
  - Create editable SVG fishbone roadmap.
  - Export PNG for stable H5 embedding.
  - Verify SVG parse and visual screenshot.

- [x] 3. Repair H5 headings and section shape
  - Remove the process-oriented source-visual index section.
  - Restore user-requested section titles.
  - Rewrite `你加入的是什么小组` in formal onboarding language.
  - Rename supported object and active project sections.
  - Replace technical-planning card grid with the fishbone roadmap and concise
    route notes.

- [x] 4. Verify and finalize
  - Run HTML parser.
  - Run required heading grep.
  - Run removed-title grep.
  - Run sensitive-info grep.
  - Take and inspect desktop and mobile screenshots.
  - Run `git diff --check`.
  - Update gate review.
  - Run `openspec validate repair-account-h5-headings-roadmap --strict`.
