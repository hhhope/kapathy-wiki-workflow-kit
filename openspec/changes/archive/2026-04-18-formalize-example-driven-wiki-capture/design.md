## Context

The repository already improved live conversation handling through `handoff mode`.

But that change solved only one part of the problem: recognizing when a conversation has become a coherent thread. It did not yet define what to do when the user supplies outside examples and the discussion has already produced reusable learning.

Today exposed the exact gap:

- the user shared external repos
- the discussion extracted reusable takeaways
- the repository still needed an explicit reminder before the learning became a wiki record

That means the current workflow still treats example-driven learning as optional capture rather than default capture.

## Goals / Non-Goals

**Goals**

- Make reusable learning from external examples a default wiki-capture path
- Remove the need for an extra reminder when the discussion already extracted stable takeaways
- Preserve the adaptation boundary: what was reused, what was changed, and what is still missing
- Route those records to the correct repository layer

**Non-Goals**

- Do not require a wiki page for every pasted link or external reference
- Do not auto-promote every captured learning into a skill or template
- Do not force external source ingestion into `wiki/sources/` when the learning is workflow-oriented rather than source-oriented
- Do not replace the existing `handoff mode` logic

## Decisions

### Decision: Trigger on extracted reusable learning, not on raw link presence

The repository should not create a wiki record for every external link.

The trigger should be stricter: the conversation must already have extracted a reusable method, workflow pattern, or adaptation insight from the example.

That means the trigger is:

- an external repo, README, article, or concrete in-chat example is introduced
- the discussion identifies what should be reused, modified, rejected, or followed up
- the result is useful beyond the exact line-by-line source summary

Alternative considered:

- Capture every external link automatically.
  - Rejected because it would flood the wiki with low-signal stubs.

### Decision: Record adaptation, not just summary

The useful part of example-driven capture is not the source summary by itself.

The record must preserve:

- what we reused
- what we changed
- what we rejected
- what is still not formalized

Otherwise the wiki cannot answer the follow-up question:

`what did we actually learn from this example, and what changed in our repository because of it?`

Alternative considered:

- Store only a generic summary of the external source.
  - Rejected because it loses the repository-specific adaptation boundary.

### Decision: Default route goes to project wiki first

Even when the learning looks reusable, it should first land in the project wiki.

Default routing:

- `wiki/ops/retro`
  - when the example changed repository workflow understanding, governance, or operating behavior
- `wiki/examples`
  - when the value is a validated output example for future reuse
- `wiki/team-lore-candidates.md`
  - only after a project-local page already exists and the learning looks generalizable across projects

Alternative considered:

- Send reusable external learnings directly to team lore candidates.
  - Rejected because the repository boundary says project wiki is the first durable layer.

### Decision: The capture should happen in the same turn by default

When the learning is already extracted and the correct route is clear, the agent should write the record in the same turn.

The user should not have to add a second instruction such as:

- "write this down"
- "put this in wiki"
- "remember this"

Alternative considered:

- Wait for explicit user reminder before writing the record.
  - Rejected because it leaves the exact failure mode the user called out.

## Minimum Record Shape

An example-driven learning record should preserve at least:

- time
- source reference
- what we reused
- what we modified
- what we rejected or left unformalized
- repository target
- next step

Optional but recommended:

- short original quote
- why this matters for current repo workflow
- whether the learning should later become a skill, template, ADR, or team-lore candidate

## Evaluation Plan

### Baseline scenario A: external example is discussed but not captured

- Before change: the user shares a repo or README, the conversation extracts useful adaptation insight, and the agent stops at chat summary unless reminded to create a wiki page.
- Expected failure: learning remains in chat history only.

### Baseline scenario B: capture loses the adaptation boundary

- Before change: a record may summarize the source, but it does not clearly say what the repository reused, changed, or still has not formalized.
- Expected failure: the next session has to reconstruct the practical takeaway.

### After-change expectation

- Scenario A resolves because extracted reusable learning now defaults to repo-visible capture.
- Scenario B resolves because the record shape explicitly requires reuse / modify / not-formalized boundaries.

## Open Questions

- Should example-driven capture eventually create `wiki/sources/` pages for some external repos, or stay workflow-first?
- When does an example-driven retro become strong enough to graduate into a formal skill or template?
