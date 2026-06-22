---
name: code-simplifier
description: Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Applies project standards and avoids over-simplification. Use when the user asks to simplify, refactor, or clean up code, or when refining recently modified code.
---

# Code Simplifier

Refine code for clarity and maintainability without changing behavior. Focus on **recently modified** code unless the user specifies a broader scope.

## Principles

1. **Preserve functionality**  
   Change only how the code works, not what it does. All features, outputs, and behavior stay the same.

2. **Apply project standards**  
   Follow project conventions (e.g. from `CLAUDE.md` or `.cursor/rules` when present):
   - ES modules, import order and extensions
   - Prefer `function` over arrow functions for top-level logic
   - Explicit return types for top-level functions
   - React: explicit `Props` types and standard patterns
   - Error handling: prefer project patterns (e.g. avoid try/catch when not needed)
   - Consistent naming

3. **Enhance clarity**
   - Reduce unnecessary complexity and nesting
   - Remove redundant code and unhelpful abstractions
   - Use clear names for variables and functions
   - Group related logic
   - Remove comments that only restate obvious code
   - **Avoid nested ternaries** — use `switch` or if/else for multiple conditions
   - Prefer explicit, readable code over brevity

4. **Maintain balance**  
   Do **not**:
   - Sacrifice clarity or maintainability for “simplicity”
   - Use clever, hard-to-follow solutions
   - Put too many concerns in one function or component
   - Remove abstractions that improve structure
   - Optimize for fewer lines (e.g. nested ternaries, dense one-liners)
   - Make code harder to debug or extend

## Process

1. **Identify scope** — Recently modified or user-specified code.
2. **Analyze** — Find ways to improve clarity and consistency.
3. **Apply** — Use project standards and the principles above.
4. **Verify** — Behavior unchanged; code is simpler and more maintainable.
5. **Document** — Only note changes that affect understanding.

## When to run

- User asks to simplify, refactor, or clean up code.
- User asks to apply project standards or improve readability.
- After writing or modifying code, you may refine it proactively unless the user asked not to.

## Scope

- **Default**: Only refine code that was recently modified or touched in the session.
- **Broader**: Refine a file, directory, or feature only when the user explicitly asks (e.g. “simplify this file” or “refactor the auth module”).
