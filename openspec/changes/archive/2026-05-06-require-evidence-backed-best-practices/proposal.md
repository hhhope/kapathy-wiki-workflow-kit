## Why

Recent governance work repeatedly captured external articles and best-practice
signals, but the signals did not reliably constrain implementation. The failure
mode was clear: an article-derived idea could be summarized in wiki or
evaluation text, then still be applied as a vague preference rather than a
verifiable gate.

This change makes the missing rule repo-visible: reusable learnings and best
practices do not become behavior constraints until they have evidence.

## What Changes

- Add a repo `AGENTS.md` constraint under example-driven capture: article,
  README, external repo, or in-chat example learnings may be captured freely,
  but promotion into behavior assets requires evidence.
- Define the accepted evidence shapes:
  external-document excerpt, local demo/fixture, or git-like project
  comparison.
- Update the `example-driven-wiki-capture` spec so candidate learning and
  adopted practice have different gates.

## Capabilities

### Modified Capabilities

- `example-driven-wiki-capture`: distinguish capture of reusable learning from
  adoption of behavior-asset rules.

## Impact

- Edits repo `AGENTS.md`.
- Adds an OpenSpec delta for `example-driven-wiki-capture`.
- Does not edit root `~/.codex/AGENTS.md`.
- Does not create or edit skills.
- Does not create a new wiki method page.
