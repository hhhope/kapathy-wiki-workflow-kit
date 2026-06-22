# req-agent kit README sync evidence - 2026-06-04

## Source

- External source repo: `/mnt/d/cloud/account-meeting-lore`
- Local kit: `req-agent-kit/req-agent`
- Task: sync the local kit with the changed req-agent material and explain
  taxonomy, requirement review flow, AGI collaboration, quality gates, and known
  gaps in the kit README.

## RED Baseline

Before edits, `req-agent-kit/req-agent/README.md` did not contain the requested
sections:

```text
missing: Domain Taxonomy
missing: Requirement Review Flow
missing: AGI collaboration
missing: Known Gaps
```

The payload also missed the newly required domain-analysis and DDD readiness
surface:

```text
req-domain-analysis=1
missing: payload/scripts/requirements_ddd_analysis.py
missing: payload/scripts/requirements_ddd_readiness.py
missing: payload/scripts/requirements_domain_coverage.py
missing: payload/scripts/check_requirements_ddd_taxonomy.py
missing: payload/tests/test_requirements_ddd_analysis_agent.py
missing: payload/tests/test_requirements_ddd_readiness_gate.py
missing: payload/tests/test_requirements_domain_coverage_gate.py
missing: payload/tests/test_requirements_ddd_taxonomy.py
```

The previous controller skill also had no matches for:

```text
req-domain-analysis
domain_coverage_gate
detailed_design_gate
requirements_ddd
```

## GREEN Evidence

After the first sync, the kit README included:

- `Domain Taxonomy`
- `Requirement Review Flow`
- `How We Collaborate With AGI`
- `Quality Gates`
- `Known Gaps`

After the follow-up localization, the kit README is Chinese-first and includes:

- `Taxonomy 和 DDD 模型`
- `需求评审流程`
- `我们如何识别需求`
- `我们如何进行需求分析`
- `我们如何与 AGI 协作`
- `质量门`
- `还有什么未做`
- ASCII diagrams for taxonomy boundaries, DDD taxonomy layers, review flow,
  requirement analysis layers, AGI collaboration, and quality gates
- Follow-up taxonomy update explains current payment ecosystem decomposition
  from the taxonomy data: 8 payment subdomains plus 5 adjacent Agent service
  subdomains.
- The README now states the collaboration thesis: classify -> model ->
  standard -> discuss -> reuse, and adds maintenance rules for subdomains,
  bounded contexts, aggregate roots, fact owners, and trigger rules.

The payload now includes:

- `.codex/skills/req-domain-analysis/SKILL.md`
- `scripts/check_requirements_ddd_taxonomy.py`
- `scripts/requirements_ddd_analysis.py`
- `scripts/requirements_ddd_readiness.py`
- `scripts/requirements_domain_coverage.py`
- `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
- DDD/domain coverage unittest modules

The installer `--verify` path was updated to include the new unittest modules.

Post-change verification:

```text
python3 -m unittest tests.test_req_agent_skills ...
Ran 65 tests
OK
```

```text
bash req-agent-kit/req-agent/install.sh "$tmp/target" --mode codex-repo --update-agents --verify
req-agent installed into /tmp/req-agent-kit-verify.OGaKv9/target
installed=53 overwritten=0 skipped=0
Ran 65 tests
OK
Change 'req-agent' is valid
```

The OpenSpec command emitted a PostHog telemetry network flush error after
validation because the sandbox has restricted network access. The command exit
status was `0`, and the local validation line was present.

## Residual Risk

This is package-level sync evidence. Passing fixture and unittest verification
proves the bundled payload shape and local checker behavior; it does not prove
future live-agent sessions will always make perfect domain-coverage judgments
without human review.
