# Design: OpenSpec User-Scope Skills

## Runtime Finding

Using a temporary `HOME` with only project trust and no plugin marketplace still
returned:

```json
{
  "name": "report-wiki-portfolio:openspec-explore",
  "scope": "repo",
  "path": "/mnt/d/cloud/account-meeting-lore/.codex/skills/openspec-explore/SKILL.md"
}
```

Therefore the prefix is not introduced by plugin registration. It comes from
the repo-local skill namespace.

## Shape

Repo source:

```text
plugins/report-wiki-portfolio/skills/openspec-*/SKILL.md
```

Runtime install:

```text
/home/yan/.codex/skills/openspec-*/SKILL.md
```

Repo-local blocked location:

```text
.codex/skills/openspec-*/SKILL.md
```

The blocked location must stay absent to avoid duplicate namespaced entries.

## Verification

- Unit tests assert that `openspec-*` source files exist outside
  `.codex/skills`.
- Real `codex app-server` `skills/list` confirms user-scope `openspec-*` names
  are present and repo-scope `report-wiki-portfolio:openspec-*` names are
  absent.
