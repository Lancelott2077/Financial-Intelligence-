# Coding Guidelines — Financial Intelligence Platform

> **Status:** Placeholder — expand during Sprint 1.

## General Principles

- Clean Architecture: strict layer separation (API → Services → Domain → DB)
- Every module is independently testable and implementable
- Prefer explicit over implicit
- Document all public interfaces with docstrings / JSDoc

## Python (Backend)

- **Style:** PEP 8 + Black formatter (line length 88)
- **Typing:** Full type annotations on all functions (Python 3.11+)
- **Imports:** Grouped (stdlib → third-party → local), `from __future__ import annotations`
- **Docstrings:** Google-style for all public classes and functions
- **Error handling:** Use typed exceptions; never silent `except Exception: pass`
- **TODO comments:** Use `# TODO: Description.` format consistently

## TypeScript (Frontend)

- **Style:** ESLint + Prettier (configured in `.eslintrc.json`)
- **Typing:** Strict mode enabled; no implicit `any`
- **Components:** Functional components only (no class components)
- **Hooks:** Custom hooks in `hooks/` — one hook per concern
- **Services:** All API calls via `services/financialService.ts`; never call fetch() directly in components
- **Naming:** PascalCase for components, camelCase for functions/variables, SCREAMING_SNAKE_CASE for constants

## Git Conventions

- Branch naming: `feature/description`, `fix/description`, `chore/description`
- Commit messages: `feat: add X`, `fix: correct Y`, `docs: update Z`
- PR size: keep PRs focused — one feature / one fix per PR

## Testing

- Backend: pytest — test files mirror app structure
- Frontend: Vitest + React Testing Library (TODO: configure)
- Coverage target: 80% on business logic modules

<!-- TODO: Add more specific guidelines as patterns emerge. -->
