# Design

## Scope

This change is a mirror sync, not a semantic redesign. The adoption decision is
`mirror`: the installed `account-cr-agent` bundle is already the behavior source
for this machine, and the repo mirror should preserve it as draft/reference
material.

## Source And Target

Primary source:

```text
/home/yan/.codex/plugins/cache/account-skills/account-cr-agent/0.1.1/skills/
```

Targets:

```text
skills-drafts/account-skills/account-cr-agent/skills/
skills-drafts/account-skills/skills/
```

The first target preserves the account-cr-agent bundle mirror. The second target
preserves the root account-skills skill mirror for the same skill names when the
installed user-scope copies exist.

## Copy Policy

- Copy ordinary skill source files, references, scripts, rules, replay fixtures,
  and tests.
- Exclude transient Python bytecode caches such as `__pycache__/`.
- Do not copy plugin marketplace metadata into this repo mirror.
- Do not copy into `.codex/skills/`.

## Behavior-Asset Evidence

Although this is a mirror sync, the copied files are behavior assets. Evaluation
must record:

- pressure scenarios for missing coverage gate and report-wrapper conflict;
- RED baseline showing the old repo mirror lacked installed coverage files;
- GREEN result showing mirrored files and installed validation pass;
- Prior-Art / Common-Rule Dedupe;
- proof boundary that the mirror is not runtime activation or plugin release.

## Routing Ownership

`cr-agent` remains the high-level CR lifecycle router/gate. `cr-report` and
`release-diff-cr` remain module/helper skills under that lifecycle. This change
does not make mirrored draft skills active user-facing runtime routes in this
repository.
