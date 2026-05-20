# wiki-medical-agent MOC Read-only Prediagnosis Design

> Supports a future OpenSpec change. This Superpowers design is not
> authoritative lifecycle state until it is copied into OpenSpec and reviewed
> there.

## Re-anchor

This design replaces the earlier framing of a "medical-agent MOC temperature
review mode". That wording was too close to creating another MOC tool.

The correct framing is:

```text
wiki-medical-agent is the normal user-facing entry point and lifecycle
controller. MOC temperature is a read-only prediagnosis section inside the
existing MOC-sensitive medical-agent route.
```

The user-facing need is not to run Python, author review JSON, or inspect raw
`temperature_admission` payloads. The need is to ask the medical-agent what the
current MOC clues mean, see which lines have value, and confirm the next
decision without granting write authority.

## Existing Authority

`wiki-medical-agent` already owns the normal medical-loop surface:

- classify user intent;
- resolve the active medical case;
- validate state;
- route to bounded workers;
- preserve case-file authority;
- report fixed fields and the next action.

Its authority model still applies:

- the case file is the only authority;
- `Confirmed Decisions` is the only executable decision surface;
- `Proposed Decisions` and prediagnosis are not executable;
- relation, governance, ADR, MOC, and OpenSpec-sensitive findings route to
  `surgery_required`, `awaiting_confirmation`, or `blocked`.

## Goal

When the user asks through the medical-agent surface, for example:

```text
$report-wiki-portfolio:wiki-medical-agent 看一下当前 MOC 温度线索，先不要写
```

the answer should be a bounded medical-agent response that shows:

- the fixed medical-agent fields;
- the script result summary;
- the interpreted live intent;
- a read-only MOC temperature prediagnosis;
- the specific confirmation point required before any admission or cleanup.

The response must help the user see real clues rather than generated relation
MOC noise.

## Route

Do not add a new normal user entry point.

Use the existing MOC-sensitive medical-agent route:

```text
user natural language
-> wiki-medical-agent intent classification
-> intent: moc_surgery_preview
-> active case / state validation
-> bounded read-only MOC worker
-> read-only prediagnosis, kind: moc_temperature
-> confirmation point
```

If implementation needs an internal subtype, it may use a field such as:

```text
prediagnosis.kind = moc_temperature
```

That subtype must not become a separate lifecycle authority and must not bypass
`moc_surgery_preview`, the active case resolver, or case-file authority.

## Required Response Shape

Every response keeps the fixed medical-agent fields:

```text
Intent
Case
State
Allowed action
Blocked action, when blocked
Next Action
```

For MOC prediagnosis, add these bounded sections.

### Script Result Summary

Summarize the worker output without dumping raw payloads:

- MOC candidate count;
- create / update / noop / orphan counts;
- admitted / blocked / needs-review relation-window counts;
- admitted relation families;
- blocked mechanical relation families;
- review-needed relation families;
- write boundary: no files written.

### Interpreted Live Intent

State what the user is trying to decide in plain language, such as:

```text
You are asking whether the current MOC graph has real reading clues, not asking
to apply MOC writes.
```

This prevents the response from collapsing into a CLI help screen.

### Read-only Prediagnosis

Surface the useful judgment layer:

- which relation families look structural and should stay blocked by default;
- which relation families may contain clue value;
- which specific clue windows deserve human review;
- which orphan relation MOC pages look like surgery cleanup candidates;
- what question the user must answer before anything becomes executable.

Each clue candidate should be compact and include:

- relation type;
- source object and page;
- target object;
- evidence refs;
- candidate temperature band or score;
- rationale;
- confirmation question.

The agent may provide a read-only temperature candidate and rationale. It must
not mark the clue as admitted.

### Mechanical Relation Families

Relation families such as:

```text
derived_from
related_objects
```

are blocked by default as standalone relation MOC pages because they usually
represent source lineage or proximity structure. They do not create reading
value by themselves.

They may still appear as evidence inside a higher-value clue, but that is not
the same as admitting the relation family into MOC.

### Review-needed Clue Families

Non-mechanical relation families such as:

```text
formalizes
validates
```

can be presented as review-needed clue families when the payload contains
evidence windows. They still require user confirmation before admission.

### Orphan Relation MOC Pages

Existing generated relation MOC pages that now appear as orphan state should be
shown as surgery candidates:

```text
relation-derived_from
relation-related_objects
relation-formalizes
relation-validates
```

The medical-agent should describe why each orphan is likely cleanup, review, or
blocked. It must not clean them up in this prediagnosis step.

## Data Flow

Use the existing worker surfaces as bounded evidence, not as the user
experience:

```text
scripts/build_wiki_medical_agent.py
  -> build_status_payload(...)
  -> intent: moc_surgery_preview
  -> build_moc_surgery_preview_payload(...)
  -> moc_projection summary
  -> temperature_admission summary
  -> read-only prediagnosis
```

The prediagnosis can read from:

- `moc_projection.candidate_count`;
- create / update / noop / orphan counts;
- `temperature_admission.counts`;
- `blocked_relations`;
- `review_needed_relations`;
- bounded samples from `clue_windows`;
- `surgery_preview.sample_items`.

Large `clue_windows` arrays must be summarized into a small number of ranked or
representative candidates.

## Boundaries

Medical-agent may:

- run one read-only local check through the bounded worker;
- summarize and interpret MOC temperature evidence;
- provide candidate temperature and rationale as prediagnosis;
- recommend the next confirmation point;
- route orphan relation MOC pages as surgery candidates.

Medical-agent must not:

- write `wiki/moc`;
- write relation frontmatter;
- generate admitted review JSON automatically;
- mark a clue admitted;
- mutate OpenSpec state;
- mutate ADRs, AGENTS, skills, or taxonomy config;
- execute cleanup surgery from the prediagnosis response.

## Confirmation Points

End with explicit choices the user may confirm later:

- admit a specific clue candidate into review;
- block a relation family;
- route orphan relation MOC pages to cleanup surgery;
- expand one object chain for deeper diagnosis;
- keep everything read-only and do nothing.

These choices are proposed decision points. They are not executable until
confirmed in the case-file authority path.

## Approaches Considered

### Recommended: Read-only Prediagnosis Inside `moc_surgery_preview`

Keep `wiki-medical-agent` as the single normal entry point and add a readable
prediagnosis section above existing MOC evidence.

Pros:

- Matches the `wiki-medical-agent` skill contract.
- Reuses the existing MOC surgery preview route.
- Keeps Python/JSON as internal worker evidence.
- Solves the actual user problem: seeing clue value and next confirmation.
- Preserves the safety gate already implemented for relation MOC admission.

Cons:

- Requires careful output shaping so raw `clue_windows` do not flood the user.
- Requires a small OpenSpec change before implementation.

### Alternative: New `moc_temperature_review` Intent

Add a new top-level intent for MOC temperature review.

Pros:

- The classifier can name the request directly.

Cons:

- Risks splitting the medical-agent lifecycle surface.
- Encourages a separate MOC tool mental model.
- Makes admission and surgery authority easier to blur.

Decision: do not use this as a normal user-facing route. If a subtype is needed,
keep it internal as `prediagnosis.kind`.

### Alternative: Keep CLI/JSON As The Interface

Document how to run the Python dry-run and author review JSON.

Pros:

- No additional implementation work.

Cons:

- Fails the user need.
- Hides AI judgment behind tooling mechanics.
- Keeps the workflow too close to implementation details.

## Testing Strategy

Tests should prove:

- natural language MOC-sensitive requests route through
  `intent: moc_surgery_preview`;
- the response includes fixed medical-agent fields;
- the response includes `prediagnosis.kind: moc_temperature` or equivalent
  bounded section label;
- script results are summarized rather than dumped as huge payloads;
- mechanical relation families such as `derived_from` and `related_objects` are
  blocked by default;
- review-needed clue families can show temperature candidates and questions;
- orphan relation MOC pages are surfaced only as surgery candidates;
- no `wiki/moc` files are written;
- no review JSON is generated without confirmation;
- no clue is admitted without case-file confirmation.

## Non-Goals

- Rebuild the MOC temperature engine.
- Add a new public entry point outside `wiki-medical-agent`.
- Add an independent MOC review skill.
- Auto-admit relation MOC pages.
- Clean existing orphan relation MOC pages in this change.
- Build a human HTML reading board.
- Change OpenSpec lifecycle state from this Superpowers spec.

## Spec Self-Review

- Placeholder scan: no placeholders remain.
- Consistency check: route, authority, boundaries, and tests all use
  `moc_surgery_preview` plus read-only prediagnosis.
- Scope check: this is one implementation-plannable change after OpenSpec
  proposal/review.
- Ambiguity check: `moc_temperature_review` is rejected as a normal route; any
  subtype is internal and non-authoritative.
