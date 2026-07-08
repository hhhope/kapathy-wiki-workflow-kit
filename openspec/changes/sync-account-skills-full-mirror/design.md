# Design

## Source And Target

Source:

```text
/mnt/d/skills/account-skills/
```

Target:

```text
skills-drafts/account-skills/
```

The target remains a repo-visible draft/reference mirror, not active runtime
registration.

## Copy Policy

Sync ordinary source content and reusable kits while excluding local, generated,
or plugin packaging state:

- `.git/`
- `.claude-plugin/`
- `.codex-plugin/`
- `.idea/`
- `.agents/`
- `graphify-out/`
- `__pycache__/`
- `tests/test_cr_agent_plugin_marketplace.py`

Preserve repo-specific mirror boundary files:

- `skills-drafts/account-skills/README.md`
- `skills-drafts/account-skills/account-cr-agent/README.md`

These README files intentionally differ from the source package so the repo
mirror remains documented as a non-plugin, non-runtime draft/reference copy.
The plugin marketplace test is excluded because it requires the plugin
manifests that this mirror intentionally excludes.

## Validation

- Diff source and target with the same exclusions plus preserved README
  exceptions.
- Confirm excluded directories are absent from the target.
- Run representative account-skills tests for CR and visual skill packaging
  when available.
- Run OpenSpec strict validation for this change.
- Run behavior-asset checker and record unrelated active-change blockers.
