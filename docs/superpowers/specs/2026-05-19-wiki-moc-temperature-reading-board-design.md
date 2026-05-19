# Wiki MOC Temperature Reading Board Design

> Supports a future OpenSpec change. This Superpowers design is not
> authoritative lifecycle state until it is copied into OpenSpec and reviewed
> there.

## Context

The current MOC projection is mechanically correct but weak as a knowledge
surface. It turns graph/frontmatter structure into Obsidian-visible Markdown
pages, including relation pages such as `relation-derived_from.md` and
`relation-related_objects.md`.

That behavior came from the archived Obsidian MOC projection design, where
`domain`, `canonical_object`, and relation fields are all valid projection
inputs. The archived evaluation already named the risk: direct application can
produce many noisy MOC files and does not prove graph layout or reading value.

The user clarified the actual goal during review:

- MOC should help reveal real wiki relationships and clues.
- Mechanical relation pages are not useful just because they have audit value.
- Python scoring alone is insufficient; AI judgment must explain why a
  relation matters.
- The missing concept is continuous temperature: relation/object value should
  be judged by evidence, chain, tension, and next action.

This is not a brand new model. The Li Xiang / Luo Yonghao interview reading
board already solved the same shape for long-form reading: ordered windows,
temperature, evidence, chain, relation, question, and keywords. The MOC repair
should reuse that pattern for wiki relations.

## Prior Art

### Obsidian MOC projection

Existing model:

```text
frontmatter / graph
-> domain, object, relation candidates
-> generated wiki/moc/*.md pages
```

Strengths:

- deterministic;
- dry-run by default;
- explicit `--apply` write mode;
- status and graph surfaces can report candidate health.

Failure mode:

- raw relation type becomes a page;
- all relation types are treated as equally navigable;
- there is no value admission gate before MOC projection;
- MOC pages can multiply without becoming better reading paths.

### Agent-readable relation reading view

`wiki/ops/agent-readable-wiki-relation-reading-view.md` already states that
the repo needs a readable layer above graph and relation analysis. It says the
problem is no longer "no graph", but that object chains are not actively pulled
into readable paths.

This design extends that idea from a static readable summary into an
agent-facing clue board.

### Interview deep reading board

The interview reading board uses `readingWindows[]` as the primary unit.
Relevant fields include:

- `temperature`
- `evidence`
- `chain`
- `relation`
- `question`
- `keywords`

Important transfer:

- Keywords are entry points, not the main structure.
- Temperature is a reading control, not a decorative label.
- Evidence follows the selected window.
- Questions preserve the next investigation path.

For MOC, raw graph edges should behave like keywords: useful as entry points,
but not sufficient as generated navigation pages.

## Design Goal

Create a value-first MOC admission model:

```text
graph/frontmatter
-> relation feature package
-> AI temperature review
-> clue windows
-> MOC admission
-> generated MOC projection
```

The goal is to make MOC pages represent high-value wiki clues instead of raw
edge dumps.

## Approaches Considered

### Recommended: Temperature Reading Board Before MOC Admission

Add an agent-facing relation reading board layer. It converts structural graph
edges into clue windows, asks AI judgment to assign continuous temperature with
evidence, and lets MOC consume only admitted windows.

Pros:

- Reuses the validated reading-board model.
- Preserves deterministic graph extraction as input.
- Makes AI judgment explicit and inspectable.
- Prevents raw relation pages like `relation-derived_from.md` from becoming
  MOC pages by default.
- Gives medical-agent a useful review surface before cleanup or write
  decisions.

Cons:

- Requires a new intermediate payload and tests.
- MOC generation must stop treating relation type as an automatic page axis.

### Alternative: Add Scores Directly To MOC Candidates

Keep the current generator and add a numeric score to each domain/object/relation
candidate.

Pros:

- Smaller patch.
- Keeps current script shape.

Cons:

- Still centers MOC pages too early.
- Turns temperature into a filter over bad candidates.
- Does not create evidence windows or next-action questions.

### Alternative: Build A Full Human Interactive Board First

Create an HTML/H5 relation board for the wiki, mirroring the interview reading
board UI.

Pros:

- Good human review surface.
- Could make relation clues visually clear.

Cons:

- Too much UI before the agent workflow is repaired.
- Does not by itself constrain MOC admission.
- Risks treating visual output as the product instead of the relation judgment
  model.

## Recommended Model

### Raw Graph Layer

Keep existing extraction:

- pages;
- canonical objects;
- domains;
- relation fields such as `related_objects`, `derived_from`, `validates`, and
  `formalizes`.

This layer remains deterministic and structural. It does not decide reading
value.

### Relation Feature Package

Build a bounded package for review. Each candidate should carry enough facts
for judgment without requiring full wiki loading:

```json
{
  "candidate_id": "relation:<source>:<type>:<target>",
  "source_page": "wiki/ops/example.md",
  "source_object": "example-object",
  "relation_type": "derived_from",
  "target_object": "source-object",
  "source_layer": "ops",
  "target_layer": "adr",
  "evidence_refs": ["wiki/ops/example.md"],
  "structural_features": {
    "cross_layer": true,
    "has_spec_support": false,
    "has_adr_support": true,
    "fanout_count": 3,
    "recency": "active"
  }
}
```

Python may compute structural features. It must not claim semantic value by
itself.

### Temperature Review

AI reviews candidate packages and emits clue windows:

```json
{
  "window_id": "clue-001",
  "temperature": 82,
  "temperature_reason": "Connects a live workflow failure to an accepted ADR and spec.",
  "source": "wiki/ops/example.md",
  "object": "example-object",
  "relation": {
    "type": "derived_from",
    "target": "source-object"
  },
  "evidence": [
    "Frontmatter links the object to the accepted ADR.",
    "Spec page carries the runtime SHALL."
  ],
  "chain": "failure -> method -> ADR -> spec -> runtime route",
  "question": "Should this chain become the preferred context for future routing?",
  "moc_admission": "admit"
}
```

Temperature is continuous. Suggested bands:

- `80-100`: strong clue; eligible for MOC admission.
- `60-79`: supporting clue; may appear under an admitted object page.
- `40-59`: weak or context-only clue; keep in reading board, not MOC.
- `0-39`: noise or mechanical relation; do not project.

The bands are guidance, not rigid labels. The explanation and evidence are
part of the judgment.

### MOC Admission

MOC projection consumes clue windows, not raw relation types.

Admission rules:

- Domain MOC can stay structural if it is useful as a top-level entry.
- Object MOC requires admitted clue windows or strong object coverage.
- Relation MOC is not automatic. A relation type page is allowed only if the
  relation type itself has repeated high-temperature clue windows and serves a
  real navigation purpose.
- Mechanical relation types such as `derived_from` and `related_objects` are
  blocked by default as standalone MOC pages unless review admits them with
  evidence.

### Medical-Agent Integration

The medical-agent should treat MOC repair as a review/surgery surface:

```text
moc review request
-> build MOC dry-run
-> build relation feature package
-> produce temperature clue board
-> show admitted / blocked / uncertain windows
-> preview cleanup or generation actions
```

It should not write `wiki/moc` directly from diagnosis or review. Existing
medical-agent boundaries remain valid.

## Data Flow

```text
extract_wiki_graph.py
  -> graph nodes and edges

relation feature builder
  -> compact candidate packages

AI temperature reviewer
  -> clue windows with evidence, chain, relation, question

MOC admission planner
  -> admitted object/domain/relation projection plan

wiki_moc_projection.py
  -> generated MOC pages only after explicit apply
```

## Error Handling

- Missing evidence: mark candidate `blocked_missing_evidence`.
- Pure mechanical relation: mark `blocked_mechanical_relation`.
- Conflicting evidence: mark `needs_human_review`.
- Oversized candidate package: sample evidence and record truncation.
- No high-temperature windows: report "no MOC admission" instead of generating
  low-value pages.

## Testing Strategy

Unit tests should cover:

- raw relation types do not become MOC relation pages by default;
- high-temperature clue windows can admit object MOC candidates;
- repeated high-temperature relation windows can admit a relation MOC page;
- `derived_from` and `related_objects` remain blocked as standalone relation
  MOC pages without explicit temperature evidence;
- medical-agent MOC preview remains read-only;
- dry-run output reports admitted, blocked, and review-needed counts.

Behavior replay should cover:

- user asks "why is relation-derived_from useful?";
- user asks for MOC repair after noisy generated pages;
- user asks medical-agent to review MOC;
- user asks for direct `--apply` while no admitted clue windows exist.

## Non-Goals

- Build a human HTML board in the first implementation.
- Replace frontmatter graph extraction.
- Remove all generated MOC files immediately.
- Make Python scoring the final semantic judge.
- Let medical-agent or status write `wiki/moc` directly.
- Treat Superpowers design as OpenSpec lifecycle state.

## Spec Self-Review

- No empty markers or unfinished sections remain.
- Scope is one design: relation temperature before MOC admission.
- OpenSpec remains read-only until this written design is reviewed.
- The design reuses existing reading-board and relation-view prior art instead
  of inventing a separate MOC framework.
- Implementation is intentionally deferred to a later plan.
