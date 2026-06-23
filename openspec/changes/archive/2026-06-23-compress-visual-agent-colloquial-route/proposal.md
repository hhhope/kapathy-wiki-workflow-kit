# Compress visual-agent colloquial route

## Why

The previous hardening made visual-agent harder to bypass, but the runtime
`SKILL.md` became too thick for frequent use. That creates a new failure mode:
the agent loads the right skill but has to scan governance wording instead of
immediately seeing the operating rule.

The trigger wording is also too example-driven. It lists terms such as 制图,
出图, 配图, and 一图流, but the real class is broader: colloquial requests to
make, draw, add, polish, convert, or generate a visual artifact.

## What Changes

- Compress `.codex/skills/visual-agent/SKILL.md` into a short runtime card.
- Generalize visual triggers to formal or colloquial visual-deliverable asks.
- Keep only runtime-critical route, mode, and stop rules in the skill body.
- Move proof burden into this change and the skill evaluation file.
- Align AGENTS and public-report wording so they reference colloquial visual
  requests as a class, not only fixed trigger words.

## Out of Scope

- Changing global worker skills.
- Producing visual assets.
- Changing the public-report scoring model beyond visual trigger wording.
