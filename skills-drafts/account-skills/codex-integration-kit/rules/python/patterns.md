# Python Patterns

## Scope

The backend stack is Python 3.11 + FastAPI + MySQL-backed repositories.

## Module Structure

- `main.py` should stay as app assembly and router wiring; business logic should live in router/service/repository/helper modules.
- If a Python file exceeds 300 lines, evaluate module extraction before adding more functionality.
- New team-facing code paths should use `team_context` and team-scoped repositories; do not spread new direct `tenant_*` argument passing through business code.

## Typing and Data Models

- New functions should have type annotations by default; avoid passing complex payloads as untyped `dict` values.
- Public request/response structures should use Pydantic models or explicit typed structures instead of implicit field contracts.
- Use enums or named constant sets for semantic states; do not scatter magic strings.

## Exceptions and Resource Management

- Do not use `except: pass`; catch specific exceptions and preserve diagnostic context.
- Use `with` or explicit lifecycle management for files, connections, and cursors.
- Avoid long blocking work inside FastAPI async routes; use background execution or the scheduler path for heavy tasks.

## Data Handling

- For large list transformations, prefer small helper functions and clear transformation steps over deep nesting.
- Before mapping raw JSON fields, verify actual field names, `None` behavior, and camelCase/snake_case differences from real payloads.
