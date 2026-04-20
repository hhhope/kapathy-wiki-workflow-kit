## Context

This repository has already separated the durable layers correctly:

- `OpenSpec` owns scoped implementation progress
- `wiki/ops` owns operating-layer intake and follow-through
- `ADR` owns stable decisions
- retros stay separate from ADRs

The current weakness is earlier than all of those layers. During the live conversation, the agent still behaves like a responsive note taker rather than a collaborator that can detect when the user has started repeatedly steering toward the same goal.

That means the repository is strong at storing decisions after they are obvious, but still weak at recognizing the moment when a topic needs to be carried as a coherent thread.

## Goals / Non-Goals

**Goals**

- Detect when the conversation has shifted from ordinary Q&A into repeated convergence on the same north-star goal
- Define a handoff mode for that moment
- Keep the first version lightweight and repo-compatible
- Route the resulting durable record to the correct repository layer
- Preserve enough original wording and timing to support later reconstruction

**Non-Goals**

- Do not auto-edit `.codex/skills/*`
- Do not auto-edit `AGENTS.md` from conversation-derived rules
- Do not solve the whole `archive review` closure problem in this change
- Do not add a full runtime state machine for every `wiki/ops` page type
- Do not depend on heavy cross-session analytics before the feature is useful

## Decisions

### Decision: Trigger on in-session north-star convergence, not only on post-hoc repetition

The first version should not wait for long-term statistics or future repeated sessions before it becomes useful.

The system should instead detect that a north star is actively pulling the current discussion back into the same goal. This makes the change valuable during the same conversation, which is where the current failure is happening.

Alternative considered:

- Wait for repeated occurrences across future sessions before recognizing importance.
  - Rejected because it leaves the current session unsupported and keeps important process discussion in chat too long.

### Decision: Enter a handoff mode instead of immediately mutating rules

The right first move is to switch the conversation into a structured handoff mode, not to directly mutate repo rules or skill files.

This preserves the user's stated safety constraint:

- high recall
- low drift

Alternative considered:

- Auto-promote repeated conversation findings directly into skills or repo rules.
  - Rejected because it amplifies the exact failure mode the user most wants to avoid: the agent evolving in the wrong direction.

### Decision: The handoff mode uses explicit slots

The mode should maintain at least these slots:

- `north_star`
- `constraints`
- `failure_modes`
- `preferences`
- `disagreements`
- `open_questions`
- `candidate_practices`
- `repo_targets`

These slots are small enough to keep the mode lightweight, but strong enough to stop the thread from collapsing back into loose conversation.

Alternative considered:

- Keep handoff mode as a free-form summary.
  - Rejected because free-form summaries recreate the current failure: the topic becomes hard to resume and hard to promote safely.

### Decision: Route durable outputs to the lowest correct repository layer

The system should not assume every handoff topic deserves the same level of promotion.

The first version should map outputs like this:

- `trace / intake`
  - a topic has clearly opened and needs operating-layer continuity
- `retro`
  - the conversation exposed drift, disagreement, or repeated process confusion
- `ADR`
  - the conversation produced a stable decision that should persist across changes
- `OpenSpec change`
  - the discussion has become a repository-default workflow change or scoped implementation track
- `archive-review.md`
  - the discussion specifically concerns closure reasoning for a current change

Alternative considered:

- Always create the same page type for every handoff topic.
  - Rejected because it would flatten important distinctions and make later governance noisier.

### Decision: Two-round recurrence is a strong heuristic, not the only rule

The user explicitly wants the system to treat repeated discussion of the same topic as meaningful. The repository should preserve that intuition.

But the first version should not define “importance” only as counting turns. A topic may clearly enter handoff mode because:

- the user repeatedly pulls the discussion back to the same goal
- the user explicitly says it should be remembered
- local fixes are rejected in favor of the same larger objective

So “same topic beyond two rounds” should be one strong trigger, not the sole criterion.

Alternative considered:

- Make a strict two-round counter the only trigger.
  - Rejected because it is too mechanical and misses the actual user intent: repeated gravitational pull toward the same goal.

### Decision: Implement handoff entry as a weighted in-session state transition

The first version should not implement handoff entry as a literal turn counter.

Instead, it should maintain lightweight in-session state and evaluate a set of signals after each user turn. The important shift is not “this topic appeared N times,” but “the user keeps pulling the discussion back to the same north-star goal.”

This lets the repository optimize for the user's actual priorities:

- high recall
- low drift

Alternative considered:

- Trigger handoff mode only when the same topic appears beyond a hard turn threshold.
  - Rejected because it creates false positives for ordinary follow-up questions and false negatives when a single strong correction clearly reveals the real objective.

## Handoff Mode Shape

### Detection signals

The first version may use lightweight signals such as:

- the user explicitly corrects the framing and pulls the conversation back to the same goal
- the same desired end-state reappears across multiple turns even when the subtopic changes
- the user rejects local optimization and reasserts a larger intent
- the user explicitly says the topic should be remembered, recorded, or made reusable
- the topic passes a “same subject beyond two rounds” threshold

These signals should not all have equal importance.

The strongest signals are:

- `goal_repull`
  - the user explicitly pulls the discussion back to the same intended outcome
- `framing_correction`
  - the user rejects the current framing and corrects what the discussion is really about
- `local_fix_rejected`
  - the user refuses a local answer and continues steering toward the larger goal

Lower-weight but still useful signals include:

- `memory_request`
  - the user explicitly asks for durable recording or future reuse
- `process_dispute`
  - the conversation becomes about workflow, boundary, or operating behavior
- `topic_recurrence`
  - the same topic continues beyond two rounds

The design intent is clear:

- “same topic beyond two rounds” is a strong heuristic
- but “north-star pull” is the real primary condition

### In-session state model

The first version should maintain lightweight session state for the current conversation, not just emit final summaries.

That state may include:

- `north_star_candidates`
- `active_handoff_topic`
- `signal_history`
- `preferences`
- `disagreements`
- `open_questions`
- `repo_target_hint`

After each user turn, the system should:

1. extract handoff-related signals
2. update candidate north-star state
3. decide whether the conversation is still loose Q&A or has entered handoff mode
4. if handoff mode is active, update the slot structure instead of treating the next turn as isolated chat

### Mode-entry behavior

The first version should behave like a small state transition:

- default state: ordinary Q&A
- transition condition: weighted evidence that the same north-star goal is actively pulling the conversation back
- target state: handoff mode

Once in handoff mode:

- later turns should attach to the active operating context
- the system should prefer structured slot updates over fresh disconnected summaries
- durable repo-visible output may begin before the conversation is fully complete

This keeps the system conversation-native instead of archive-native.

### Minimum record contents

The durable record for a handoff topic should preserve:

- time
- enough original wording to reconstruct intent later
- the current north star
- unresolved questions
- the current next step

### Mode behavior

Once a handoff topic is recognized, the conversation should stop behaving like disconnected Q&A and start behaving like a coherent thread that can be resumed, promoted, or closed later.

More concretely:

- answering the immediate question is still allowed
- but the system must also preserve the active north star and attach new information to it
- the conversation should accumulate structured state instead of repeatedly rebuilding context from scratch

## Evaluation Plan

### Baseline scenario A: conversation keeps converging, but the repo sees only loose chat

- Before change: the user repeatedly corrects and refocuses the discussion, but the repository has no named concept for that shift.
- Expected failure: important preferences and process disagreements remain in chat until someone manually extracts them later.

### Baseline scenario B: repeated topic is recognized too late

- Before change: repo-visible artifacts are added only after the insight is already obvious.
- Expected failure: the current session still feels discontinuous and fragile.

### Baseline scenario C: early automation mutates the wrong thing

- Before change: the easiest “self-evolving” story would be to auto-edit workflow rules or skills directly.
- Expected failure: drift increases because the agent promotes the wrong abstraction too early.

### After-change expectation

- Scenario A resolves because the repository now defines a handoff mode for repeated in-session convergence.
- Scenario B resolves because the durable record can begin while the conversation is still live.
- Scenario C resolves because the first version stops at capture, structure, and correct durable routing rather than direct rule mutation.

## Open Questions

- What exact threshold should switch the mode on in practice?
- Should the first repo-visible record be created immediately on mode entry or only after a minimum slot set is filled?
- How much original wording should be preserved before pages become too noisy?
- Should `candidate_practices` live inside the same page or in a later candidate layer?
- How should a handoff topic be explicitly closed or downgraded when the user moves on?
