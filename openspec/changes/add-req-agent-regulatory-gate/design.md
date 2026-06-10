# Design

## Gate Shape

The checker evaluates a new `regulatory_gate` in addition to existing
`domain_model_gate`, `domain_coverage_gate`, `requirement_delivery_gate`, and
`detailed_design_gate`.

The gate is triggered when either condition is true:

- `domain.confirmed`, `domain_model.subdomains`, or `domain_coverage` includes
  `risk_compliance`;
- source-derived case text contains explicit regulatory signals in domain
  candidates, open questions, soft evidence, stories, acceptance functions,
  roles, blockers, or proof-boundary notes.

The signal scan is intentionally narrow and explicit. It should catch terms
such as:

- compliance, regulation, regulatory, law, legal, KYC, KYB, AML;
- 合规, 法规, 监管, 法务, 法人, 核身, 身份, 真实意愿, 授权, 同意, 个人信息;
- SMS link, 短信链接, URL, token, consent, evidence.

## Obligation Model

Triggered cases must provide `soft_evidence.regulatory_obligations` as a list.
Each obligation is a case-local evidence object:

```json
{
  "id": "REG-001",
  "status": "confirmed",
  "owner_refs": ["R-compliance-owner"],
  "source_basis": "payment regulation / legal review / product confirmation",
  "obligation": "Confirm legal representative identity binding before consent.",
  "acceptance_function_ids": ["AF-019", "AF-020"],
  "evidence_anchor": {
    "source_section": "human review regulatory gap"
  }
}
```

Minimum required fields:

- `id`
- `status`
- `owner_refs`
- `source_basis`
- `obligation`
- `acceptance_function_ids`
- evidence anchor, using the existing object-aware evidence convention

Accepted statuses:

- `confirmed`
- `waived`

Blocked statuses:

- missing
- `missing`
- `candidate`
- `unresolved`
- `review_prompt`

Waivers must include `waiver_reason` or `waiver_ref`.

## Readiness Behavior

If the gate is not triggered, it reports `passed: true` with mode
`not_triggered`.

If the gate is triggered and obligations are missing or unresolved, it adds
blockers to the normal requirements blocker list. That means the summary status
is `blocked`, not `requirements_ready`.

This differs from `detailed_design_gate`. Detailed-design inputs can block API,
DDL, state-machine, and engineering breakdown while leaving a requirement
skeleton reviewable. Regulatory obligations can determine whether stories and
acceptance criteria are valid, so missing obligations block requirement
readiness.

## Worker Guidance

- `req-domain-analysis`: detect regulatory triggers and emit open questions /
  obligations for `risk_compliance` or explicit regulatory source signals.
- `req-scope`: assign each obligation to concrete case-local owners or keep it
  blocked.
- `req-acceptance`: convert confirmed obligations into observable acceptance
  functions.
- `req-human-review`: verify that regulatory demand facts are synchronized back
  into machine case data before handoff.
- `req-agent`: report `regulatory_gate` in every normal readiness response.

## Compatibility

Legacy cases that do not trigger the gate remain unchanged.

Historical cases that trigger the gate but lack obligations may become blocked
when rechecked. That is intentional for safety-sensitive requirements and
should be resolved by adding case-local obligations or explicit waivers, not by
weakening the signal scan.
