# Medical Agent MOC Temperature Review Design

> Supports a future OpenSpec change. This Superpowers design is not
> authoritative lifecycle state until it is copied into OpenSpec and reviewed
> there.

## Context

The MOC temperature reading-board change repaired an important lower-level
failure: raw graph relation types no longer become generated relation MOC pages
by default. `derived_from` and `related_objects` are blocked unless a complete
temperature review explicitly admits them.

That was necessary, but it did not finish the user-facing workflow. The current
normal surface still exposes too much implementation detail:

```text
Python dry-run
temperature_admission JSON
review JSON
admitted_relations
```

The repo already defines `wiki-medical-agent` as the single normal user-facing
entry point for wiki medical-loop status, diagnosis, confirmation, treatment,
surgery, recovery, archive checks, and MOC-sensitive findings. Therefore the
next requirement is not another MOC tool. It is a medical-agent MOC temperature
review mode that turns the existing `temperature_admission` payload into a
readable diagnosis.

## Goal

When the user asks:

```text
medical-agent 看一下当前 MOC 温度线索，先不要写
```

the agent should answer through medical-agent, not by asking the user to run
Python or hand-write JSON.

The output should help the user see:

- which relations are structural noise;
- which relations are real clue candidates;
- why a clue may be high or low temperature;
- which orphan relation MOC pages need surgery review;
- what decision still requires human confirmation.

## Recommended Approach

Add a medical-agent read-only interpretation layer above the existing MOC
temperature payload:

```text
user natural language
-> wiki-medical-agent intent classification
-> build MOC temperature preview
-> readable temperature diagnosis
-> confirmation points
-> later review/surgery/apply flow
```

This keeps the recently built Python pieces as bounded workers. It does not
make them the user experience.

## Intent Model

Add or refine a medical-agent intent such as:

```text
moc_temperature_review
```

It should trigger for requests like:

- `看当前 MOC 温度线索`
- `medical-agent 看一下 MOC，不要写`
- `MOC 哪些关系值得进图`
- `这些 relation MOC 有什么价值`
- `看一下 derived_from / related_objects 是不是噪音`

If the existing `moc_surgery_preview` intent remains the route, the response
must still include the readable temperature review before any surgery action.

## Required Response Shape

Every response keeps the fixed medical-agent fields:

```text
Intent
Case
State
Allowed action
Blocked action, when blocked
Next action
```

For MOC temperature review, add these sections:

### Current Overview

Summarize:

- MOC candidate count;
- admitted / blocked / needs-review relation-window counts;
- orphan relation MOC count;
- write boundary: no files written.

### Blocked Mechanical Relations

Explain relation types such as:

- `derived_from`
- `related_objects`

The output must say why they are blocked by default: they are source/proximity
structure, not navigation value by themselves.

### Review-Needed Clues

Surface the most useful relation clue candidates, especially non-mechanical
types such as:

- `formalizes`
- `validates`

Each item should include:

- relation type;
- source object and page;
- target object;
- evidence refs;
- temperature candidate;
- rationale;
- question for the user.

The agent may make a read-only AI judgment, but it must not mark the clue as
admitted without user confirmation.

### Orphan Relation MOC Pages

When old generated relation MOC pages now appear as orphan state, surface them
as surgery candidates, not as active generated value.

### Confirmation Points

End with explicit choices the user can confirm later:

- admit a specific clue into review;
- block a relation family;
- route orphan relation MOC pages to cleanup surgery;
- expand one object chain for deeper diagnosis.

## Data Flow

```text
scripts/build_wiki_medical_agent.py
  -> build_status_payload(...)
  -> build_moc_surgery_preview_payload(...)
  -> temperature_admission
  -> readable MOC temperature diagnosis
```

The readable diagnosis is derived from existing payload fields:

- `temperature_admission.counts`;
- `blocked_relations`;
- `review_needed_relations`;
- `clue_windows`;
- `surgery_preview.sample_items`;
- `moc_projection`.

## Boundaries

Medical-agent may:

- run read-only MOC temperature preview;
- summarize and rank clue candidates;
- explain why mechanical relation families are blocked;
- recommend next actions;
- ask for confirmation.

Medical-agent must not:

- write `wiki/moc`;
- write relation frontmatter;
- generate admitted review JSON automatically;
- mutate OpenSpec state;
- mark a clue admitted without user confirmation.

## Approaches Considered

### Recommended: Medical-Agent Readable Diagnosis

Keep medical-agent as the single normal entry point and add a readable diagnosis
layer above the existing payload.

Pros:

- Matches the repo skill contract.
- Keeps Python/JSON as internal worker surfaces.
- Solves the user's actual usage problem.
- Preserves the safety gate already implemented.

Cons:

- Requires another small OpenSpec change before implementation.
- Needs careful output shaping so large payloads do not flood the response.

### Alternative: Separate MOC Review Skill

Create a new skill or command for MOC temperature review.

Pros:

- The MOC review behavior can be isolated.

Cons:

- Splits the user-facing entry point.
- Weakens the medical-agent ownership model.
- Recreates the drift where users face tool internals.

### Alternative: Keep CLI/JSON As The Interface

Document how to run the Python dry-run and author review JSON.

Pros:

- No additional implementation work.

Cons:

- Fails the user need.
- Makes AI judgment and medical-agent orchestration optional.
- Keeps the workflow too close to implementation details.

## Testing Strategy

Tests should prove:

- natural language MOC temperature requests route through medical-agent;
- output includes fixed medical-agent fields;
- output includes readable overview, blocked mechanical relations,
  review-needed clues, orphan relation MOC pages, and confirmation points;
- no `wiki/moc` files are written;
- no review JSON is generated without confirmation;
- huge `clue_windows` payloads are summarized into bounded readable output.

## Non-Goals

- Rebuild the MOC temperature engine.
- Add a new public entry point outside medical-agent.
- Auto-admit relation MOC pages.
- Clean existing orphan relation MOC pages in this change.
- Build a human HTML board.

## Spec Self-Review

- No implementation is included in this design.
- The design corrects the user-facing entrypoint drift while preserving the
  completed lower-level safety gate.
- OpenSpec remains read-only until the user reviews this written spec.
- The next step after approval is an implementation plan, not direct code.
