# visual-agent evaluation

## Pressure Scenarios

- Ambiguous visual-controller request: user asks the agent to decide among SVG,
  H5/HTML, image-model, and hybrid visual production. Expected:
  response includes `Using visual-agent`, uses `mode_fork`, and presents the
  four output modes.
- Plain visual request without explicit mode. Expected: no silent H5/SVG
  default; ask the bounded mode fork unless strong content evidence selects a
  mode.
- Colloquial visual request with no canonical keyword, such as asking to make
  material more scannable, turn notes into a shareable thing, prepare a visual
  version, add presentation form, or make a page/image/card-like output.
  Expected: trigger `visual-agent`, expose `Using visual-agent`, and ask the
  mode fork unless strong content evidence selects a route.
- Non-keyword mode request: user asks "别直接给我默认做网页或 SVG，先判断该用什么形态".
  Expected: trigger `visual-agent` because the requested action is visual
  medium selection, even without naming a final artifact.
- Flow source: Mermaid sequence, payment clearing flow, or fund flow. Expected:
  route to `svg-flow-diagram` with `Output Mode: svg` unless the user overrides.
- Architecture source: system architecture, interface topology, or deployment
  diagram. Expected: use `architecture-diagram` only if it is available;
  otherwise keep ownership in `visual-agent` and mark the missing worker.
- Reader-facing H5/report source. Expected: preserve
  `public-report-quality-gate` only if it is available; otherwise keep the
  public/report concern visible as a missing parent gate and do not bypass
  `visual-agent`.
- Dense Chinese text plus image-model preference. Expected: warn about text
  accuracy and offer `hybrid` or deterministic overlay.
- Directly named worker: user asks for `infographic-onepager`,
  `svg-flow-diagram`, or `imagegen`. Expected: still enter through
  `visual-agent` first unless the task is worker debug review; execute only
  workers that are actually available.
- Bundled worker availability: this repository bundles
  `knowledge-article-visual`, `infographic-onepager`,
  `visual-knowledge-onepager`, `svg-flow-diagram`, `sequence-diagram`,
  `architecture-diagram`, `frontend-visual-governor`,
  `project-weekly-report-gantt-map`, and `lark-whiteboard`. Expected: route only
  to a child worker that is present in runtime discovery; otherwise keep
  ownership in `visual-agent`, mark the unavailable worker in `Blocked Action`,
  and ask for mode/source confirmation or installation.
- Runtime/system visual routes: `imagegen` is usable only when the runtime
  provides the image tool/skill; `public-report-quality-gate` is preserved only
  when the host repo provides it. Expected: neither is falsely described as a
  bundled account-skills worker.
- Visual worker matrix coverage: article/card set requests route to
  `knowledge-article-visual`; one-pager/poster/long-image requests route to
  `infographic-onepager`; architecture/topology requests route to
  `architecture-diagram`; sequence/call-order authoring routes to
  `sequence-diagram` when present; UI/dashboard polish routes to
  `frontend-visual-governor`; Gantt/capability-map/weekly-report visuals route
  to `project-weekly-report-gantt-map`; whiteboard requests route to
  `lark-whiteboard`; image-model output routes to `imagegen` after mode and
  verification boundaries are set.
- Non-visual meeting notes request. Expected: visual-agent does not trigger.

## RED Baseline

Before this skill, visual routing depended on ad hoc model judgment. A request
could jump directly to image generation, confuse SVG workers, or skip the human
mode fork. Before the entry-route hardening, public-report delegation also
listed `knowledge-article-visual`, `infographic-onepager`, and `imagegen`
directly, and normal visual responses had no required `Using visual-agent`
marker. The first compact version still leaned on a short list of casual
Chinese examples; that was not enough because it described phrases instead of
the generalized visual-deliverable intent class. It also had an incomplete
route table that omitted available companion visual workers and blurred bundled
workers with runtime-provided workers, which could make a future agent claim a
route without checking runtime availability.

## GREEN Result

The skill now defines a compact runtime controller: `Using visual-agent`, mode
fork, no silent H5/SVG fallback, child worker routes, public-report gate
preservation, and verification/Feishu stops. The trigger model covers the
visual-deliverable intent class by artifact role, transformation role, medium
selection role, and visual repair role, instead of depending on fixed trigger
phrases. Child routing now requires runtime availability and uses a complete
bundled visual worker matrix for ordinary visual skills in this repository.
`imagegen` remains a runtime/system tool and `public-report-quality-gate`
remains a host-repo parent gate. Unavailable workers are explicit blockers, not
implicit fallbacks.

## Residual Risks

This skill proves routing behavior only. Final SVG, H5, or bitmap quality still
depends on the selected worker and visual verification.

## 2026-06-22 Bundled Worker Migration

### Pressure Scenarios

- Visual request routes to `knowledge-article-visual`,
  `infographic-onepager`, `visual-knowledge-onepager`, `architecture-diagram`,
  `frontend-visual-governor`, `project-weekly-report-gantt-map`,
  `lark-whiteboard`, or `sequence-diagram`.
- The account-skills package is installed into a runtime that only has this
  repository's `skills/` directory.
- A future agent scans top-level skill directories with
  `find skills -maxdepth 2 -name SKILL.md`.

### RED Baseline

The prior branch version mentioned these visual workers in `visual-agent` but
bundled only `svg-flow-diagram`. That meant a future agent could claim a child
route that was not actually shipped by account-skills. `sequence-diagram` also
had its `SKILL.md` nested under `skills/sequence-diagram/skills/`, so ordinary
top-level skill discovery missed it.

### GREEN Result

The repository now bundles ordinary visual workers as top-level skill
directories: `knowledge-article-visual`, `infographic-onepager`,
`visual-knowledge-onepager`, `svg-flow-diagram`, `sequence-diagram`,
`architecture-diagram`, `frontend-visual-governor`,
`project-weekly-report-gantt-map`, and `lark-whiteboard`.

`imagegen` is explicitly documented as a runtime/system image tool, and
`public-report-quality-gate` is explicitly documented as a host-repo parent
gate. Neither is falsely presented as an account-skills worker.

### Evidence

- `find skills -maxdepth 2 -name SKILL.md` includes all bundled visual workers.
- Fixed-phrase trigger scan over the visual controller and bundled workers no
  longer finds route-controlling colloquial trigger rows.
- `git diff --check` passes.

### Residual Risks

Copied worker internals may still contain style examples or scene references
that mention visual vocabulary. Those references are not route triggers; future
localization can shrink them if account-skills needs a smaller package.

## 2026-06-22 Repo-Local Runtime Closure

### Pressure Scenarios

- This repository's runtime loads `.codex/skills` directly and receives a
  visual request that routes through `visual-agent`.
- The controller names a child worker such as `knowledge-article-visual`,
  `infographic-onepager`, `visual-knowledge-onepager`, `architecture-diagram`,
  `frontend-visual-governor`, `project-weekly-report-gantt-map`,
  `lark-whiteboard`, or `sequence-diagram`.
- The user expects the current report-wiki runtime to behave like the
  account-skills visual package branch.

### RED Baseline

Before the repo-local repair, this command found only the controller:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'visual|infographic|knowledge|architecture|frontend|project-weekly|lark|sequence|svg'
```

The installed `.codex/skills/visual-agent/SKILL.md` still described only
`svg-flow-diagram` as bundled and treated the other visual workers as runtime
companions.

### GREEN Result

The repo-local `.codex/skills` surface now includes the controller and ordinary
visual child workers:

- `visual-agent`
- `knowledge-article-visual`
- `infographic-onepager`
- `visual-knowledge-onepager`
- `svg-flow-diagram`
- `sequence-diagram`
- `architecture-diagram`
- `frontend-visual-governor`
- `project-weekly-report-gantt-map`
- `lark-whiteboard`

The controller now distinguishes bundled visual workers from runtime/system
`imagegen` and host-gate `public-report-quality-gate`.

### Evidence

- Repo-local discovery lists all visual worker `SKILL.md` files under
  `.codex/skills`.
- Fixed-trigger scan over the repo-local visual runtime surface finds no
  route-controlling old colloquial trigger rows and no old channel-specific
  visual one-pager skill name.
- Remaining visual-word hits are style-reference wording inside
  `lark-whiteboard`, not route rules.

### Residual Risks

This closes the current repo runtime surface. Account-skills package README and
integration-kit cleanup remains a separate branch phase.
