# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| `readMe写一下` | Agent Intent Routing -> repo-public artifact -> public gate lightweight path -> README constraint scan | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| `把这个 wiki/ops 改成飞书文章` | Full public report gate because an internal ops note becomes reader-facing Feishu content | `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` Agent Intent Routing Replay |
| `这个外部 README 学一下能不能复用` | `learning-capture` and README learning module, not repo-public artifact edit | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| `改一下 wiki frontmatter` | `wiki-frontmatter-taxonomy` gate remains responsible | `tests/test_agent_intent_routing.py::test_pressure_scenarios_replay_agent_intent_routing` |
| Small README typo fix | Public gate lightweight path applies without default gate-review artifact requirement | `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` Agent Intent Routing Replay |

## Behavior Replay Evidence

| Replay Field | Evidence |
|---|---|
| Input or situation shape | User asks the agent to write, rewrite, polish, prepare, or update a repo-public artifact such as `README.md`, `docs/*`, `examples/*`, or a published template. |
| Trigger condition | Repo `AGENTS.md` contains `Agent Intent Routing` requiring intent classification before acting and routing repo-public artifacts to `.codex/skills/public-report-quality-gate/SKILL.md` lightweight path. |
| Expected route or stop behavior | Agent loads the public gate lightweight path, identifies reader/job-to-be-done, scans relevant artifact-specific constraints, then drafts. If the work is actually frontmatter, semantic skill editing, external learning, OpenSpec lifecycle, or full reader-facing publication, the specialized gate wins. |
| repo-visible trigger artifacts | `AGENTS.md`, `.codex/skills/public-report-quality-gate/SKILL.md`, `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`, and `openspec/changes/route-repo-public-artifacts-through-agent-intent/specs/agent-intent-routing/spec.md`. |
| Expected output or non-output | Repo-public drafts are not treated as ordinary Markdown edits. Small repo-public edits do not create gate-review artifacts by default. Review-ready, publish, Feishu sync, complex, reference-shaped, or drift-corrected outputs still require stronger gate evidence. |
| Promotion or non-promotion boundary | This change adds repo-local routing only. It does not promote the rule to global AGENTS, team lore, or root-scope skills. |
| Proof Boundary | Tests prove repo-visible routing text and pressure scenarios. They do not prove every future AI client will load the correct skill unless that client honors repo `AGENTS.md` and skill routing. |

## RED Baseline

- Before this change, `public-report-quality-gate` covered public materials and
  reader-facing outputs but did not explicitly name repo-public artifacts such
  as `README.md`, `docs/*`, `examples/*`, or published templates.
- Before this change, `AGENTS.md` did not include an entry-layer `Agent Intent
  Routing` section requiring intent classification before acting.
- Before this change, the README incident showed that a repo-public artifact
  could be rewritten before the agent explicitly routed through the public gate
  lightweight path or scanned README-specific constraints.
- The RED test run failed because `AGENTS.md`, `public-report-quality-gate`, and
  pressure scenarios did not contain the required repo-public routing terms, and
  `evaluation.md` did not exist.

## GREEN Result

- `AGENTS.md` contains `Agent Intent Routing` with a compact parent-gate map.
- `.codex/skills/public-report-quality-gate/SKILL.md` includes repo-public
  artifact trigger semantics and a lightweight path.
- `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
  includes Agent Intent Routing replay scenarios.
- The OpenSpec change contains requirements for intent classification,
  repo-public lightweight routing, specialized-gate preservation, and behavior
  replay evidence.
- Targeted tests pass:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

## Residual Risks

- Very small repo-public wording edits may feel heavy if the lightweight path is
  interpreted as the full report gate. The skill text states the lightweight
  path and gate-review artifact boundary to keep this bounded.
- README constraint scans can surface unrelated references. The design and gate
  text require relevant artifact-specific scanning rather than opening every
  hit.
- Future AI clients still need to honor repo `AGENTS.md` and skill routing.
  This change creates repo-visible routing evidence, not automatic enforcement
  across all clients.
