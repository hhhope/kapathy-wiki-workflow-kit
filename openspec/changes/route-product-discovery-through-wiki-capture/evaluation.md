# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| positive: `$pm-product-discovery ...` followed by `这个看下skill要记录wiki，我们要改造下` | Route: repair-workflow -> OpenSpec change; then use product-discovery wiki capture for the current durable note | `tests.test_product_discovery_wiki_capture` and `wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md` |
| positive: `把这次机会树和假设记录到 wiki，后面写 PRD 用` | Load `.codex/skills/product-discovery-wiki-capture/SKILL.md`; create or update `wiki/ops/` record with opportunity, assumptions, experiments, and next step | `tests.test_product_discovery_wiki_capture` |
| negative: `帮我快速判断这个产品机会怎么样` with no wiki, durable-memory, reuse, or follow-up intent | Answer in chat; do not create durable wiki output by default | `tests.test_product_discovery_wiki_capture` |
| parent gate preserve: product discovery cites external articles, repos, papers, READMEs, or examples as reusable learning | `learning-capture` remains the parent gate for source learning before product-discovery capture references the result | `tests.test_product_discovery_wiki_capture` |
| parent gate preserve: captured output is prepared as a reader-facing report, Feishu draft, H5, README, docs, examples, or published template | `public-report-quality-gate` still applies | `tests.test_product_discovery_wiki_capture` |
| parent gate preserve: capture creates wiki frontmatter | `wiki-frontmatter-taxonomy` still applies before completion claims | `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md` |

## RED Baseline

- Before this change, the available PM plugin skills could save substantial
  product-discovery output as markdown, but no repo-local route required wiki
  capture when the user expected durable repository memory.
- Before this change, `AGENTS.md` did not list a high-frequency route for
  PM/product-discovery analysis with wiki, durable-memory, reuse, or follow-up
  intent.
- The RED test run failed with missing
  `.codex/skills/product-discovery-wiki-capture/SKILL.md` and missing
  `openspec/changes/route-product-discovery-through-wiki-capture/evaluation.md`.

## GREEN Result

- Added `.codex/skills/product-discovery-wiki-capture/SKILL.md`.
- Added the product-discovery wiki-capture route to the `AGENTS.md`
  High-Frequency Skills table.
- Added OpenSpec requirements covering positive trigger, negative one-off
  behavior, source-learning parent gate preservation, and reader-facing parent
  gate preservation.
- Added a current wiki capture note:
  `wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md`.
- Targeted replay command:

```bash
python3 -m unittest tests.test_product_discovery_wiki_capture -v
```

- OpenSpec validation passed:

```bash
openspec validate route-product-discovery-through-wiki-capture --strict
```

- Wiki frontmatter precheck for the new note produced `target.entry_count = 0`,
  so the new page was not listed as frontmatter drift. The overall frontmatter
  gate still failed because of pre-existing unrelated `wiki/reports/*`
  README/MANIFEST pages missing `layer` and `domain`.
- `python3 scripts/check_behavior_assets.py` and
  `python3 scripts/repo_health_check.py` still fail on the pre-existing active
  change `openspec/changes/initialize-llm-wiki-seed-repo`; no reported behavior
  asset error referenced this change.

## Prior-Art / Common-Rule Dedupe

- Scanned: `AGENTS.md`, `PROJECT.md`, `openspec/specs/learning-capture-routing/spec.md`, `openspec/specs/behavior-replay-gate/spec.md`, `openspec/specs/article-learning-capture/spec.md`, `openspec/specs/example-driven-wiki-capture/spec.md`, `.codex/skills/learning-capture/SKILL.md`, `.codex/skills/public-report-quality-gate/SKILL.md`, `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`, `wiki/ops/learning-capture-routing.md`, and `wiki/ops/behavior-replay-gate.md`.
- Owns: repo-local bridge behavior for PM/product-discovery analysis that has explicit wiki, durable-memory, reuse, follow-up, or missing-capture repair intent.
- References: OpenSpec remains required for workflow repair; `learning-capture` owns source learning; `public-report-quality-gate` owns reader-facing and repo-public output; `wiki-frontmatter-taxonomy` owns wiki frontmatter compliance; behavior replay evidence owns future route claims.
- Rejects: editing external `$pm-product-discovery` plugin cache; turning all PM analysis into wiki output; using product-discovery capture as evidence to promote market claims into hard repo rules.

## Behavior Replay Evidence

| Replay Field | Evidence |
|---|---|
| input or situation shape | PM/product-discovery analysis is requested or has just happened, and the user asks for wiki recording, durable memory, reuse in later product work, or repair of a missed capture. |
| trigger condition | `AGENTS.md` High-Frequency Skills maps PM/product-discovery analysis with explicit wiki, durable-memory, reuse, or follow-up intent to `.codex/skills/product-discovery-wiki-capture/SKILL.md`. |
| expected route | Load the product-discovery wiki-capture skill, preserve any stricter parent gate, then create or update the lowest correct wiki record, normally under `wiki/ops/`. |
| repo-visible artifact | `AGENTS.md`, `.codex/skills/product-discovery-wiki-capture/SKILL.md`, `openspec/changes/route-product-discovery-through-wiki-capture/specs/product-discovery-wiki-capture/spec.md`, and `wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md`. |
| expected output | Durable product-discovery notes include source prompt or situation, route used, target segment or ICP, opportunity framing, assumptions and risks, validation experiments, what was not formalized, and next step. One-off PM answers have no durable wiki output by default. |
| promotion or non-promotion boundary | The wiki note remains working product-discovery memory. It does not promote market claims into repo rules, global guidance, OpenSpec `SHALL`, or archive-ready claims without separate evidence. |
| proof boundary | Tests and manual replay prove repo-visible routing behavior for this repository. They do not prove external plugin behavior changes or multi-session client compliance unless future clients load repo `AGENTS.md` and skills. |

## Residual Risks

- Future agents may still answer a PM plugin request directly if they ignore repo
  `AGENTS.md` or the local skill list.
- Whole-repo health checks remain blocked by pre-existing active-change and wiki
  frontmatter debt outside this change.
- The boundary between a useful one-off answer and durable discovery memory may
  require judgment when the user does not say "wiki" or "reuse" explicitly.
- Captured discovery notes can preserve weak market assumptions; the skill keeps
  them as working memory, not validated market facts.
