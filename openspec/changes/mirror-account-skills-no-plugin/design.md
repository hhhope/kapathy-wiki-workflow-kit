# Design: account-skills mirror without plugin mode

## Target

Target directory:

```text
skills-drafts/account-skills/
```

This keeps the imported content visible in the repo but outside active
`.codex/skills` runtime loading. Future work can promote individual skills
through a separate OpenSpec change and skill evaluation gate.

## Copy Policy

Mirror from:

```text
/mnt/d/skills/account-skills
```

Include ordinary repo content and reusable kits. Exclude:

- `.git/`
- `.claude-plugin/`
- `.idea/`
- `graphify-out/`

Rationale:

- `.claude-plugin/` is excluded because the user explicitly requested not to use
  plugin mode.
- `.git/` and `.idea/` are local state.
- `graphify-out/` is generated/cache output, not source material.

## README Policy

The target README is newly written for this repo. It must:

- state that the mirror is not plugin mode;
- describe included content at a high level;
- explain how to use direct skill folders manually;
- warn that individual skills are draft/reference until promoted;
- avoid plugin marketplace commands.

## Validation

Minimum validation:

- target directory exists;
- excluded directories are absent;
- expected source directories exist in target;
- target README contains no plugin marketplace install commands;
- OpenSpec validation passes.
