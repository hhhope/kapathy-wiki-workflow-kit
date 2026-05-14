# Design: wiki runtime layer contract

## Architecture

The stable wiki runtime architecture has six layers:

1. Core loop
   - Capture, Compile, Retrieve, Apply.
   - Owned by the LLM Wiki core contract.

2. Skill entrypoints
   - `wiki-react` is the explicit router and decision-trace entrypoint.
   - Domain skills such as `wiki-status`, `wiki-query`, `wiki-apply`,
     `wiki-explore`, and `wiki-scorecard` remain directly callable.

3. Decision contract
   - High-risk or ambiguous routes produce `decision_trace` before acting.
   - Domain skills do not bypass this contract; they embed it when risk
     requires it.

4. Observation tools
   - Deterministic scripts and generated artifacts provide observations:
     status, manifest, frontmatter precheck, graph, relation, scorecard,
     context, apply preview, and queue preview.
   - Python tools provide observations or validation. They do not classify
     natural-language intent.

5. Boundaries
   - Results are classified as inspect-only, candidate judgment, bounded page
     fix, requires user confirmation, or requires OpenSpec.
   - Scorecard is an observation source, not a behavior judge.

6. Eval and lifecycle gates
   - Trace eval validates agent-produced decision traces.
   - Behavior asset checker validates behavior-change evidence.
   - OpenSpec owns workflow/runtime change lifecycle.

## Documentation Shape

The README should start from the layer model before listing skills. The skill
list should explain when to use `wiki-react` versus direct domain skills.

The repo-visible architecture page should live in:

```text
wiki/ops/wiki-runtime-layer-contract.md
```

## Spec Naming

Active specs must not preserve obsolete slash-command path names when the
supported runtime is no longer slash/plugin based. Rename:

```text
openspec/specs/wiki-runtime-slash-command-surface
  -> openspec/specs/wiki-runtime-skill-surface

openspec/specs/wiki-status-slash-command
  -> openspec/specs/wiki-status-skill
```

Archive history may retain old names.

## Verification

- Tests assert the layer contract exists and names all six layers.
- Tests assert README explains `wiki-react` as router without replacing domain
  skills.
- Tests assert active spec paths no longer contain obsolete slash-command names.
- Existing wiki runtime, decision-trace, behavior-asset, and OpenSpec checks
  still pass.
