# TruquiCenter

## Project
Personal web application to centralize personal content and projects.

## Architecture
Layered architecture: interface → application → domain → infrastructure
ORM is allowed at all layers as a pragmatic exception.

## Stack
- Backend: Django + Python
- Database: PostgreSQL
- Frontend: HTMX + Alpine.js + Tailwind CSS
- Auth: django-allauth (email + 2FA)
- Logging: Loguru

## Structure
- src/interface/<module>/ → HTTP, webhooks
- src/application/<module>/ → use cases
- src/domain/<module>/ → business logic
- src/infrastructure/database/<module>/ → models, querysets, queries, operations
- src/infrastructure/external/ → Telegram
- tests/unit/application/<module>/ → without database
- tests/integration/<module>/ → with database
- tests/e2e/ → end-to-end tests

## Conventions
- Use cases go in application/<module>/<verb>_<noun>.py (e.g. create_post.py)
- Complex queries → infrastructure/database/<module>/queries.py
- Complex writes → infrastructure/database/<module>/operations.py
- HTMX → server communication
- Alpine.js → local UI interactivity only
- Tailwind CSS → all styling, no custom CSS unless strictly necessary

## Python conventions
- Formatter and linter: Ruff
- Type checking: mypy
- Always add type hints to all functions and methods
- No function or method without return type annotation

## Environment
- Docker for both local development and production
- Python version controlled via Dockerfile
- Each project has its own docker-compose.yml for local development
- Production orchestration is handled externally via a global docker-compose.yml

## Git
- Never commit directly to `main` — always create a feature branch, open a PR, and merge
- Use Conventional Commits for all commit messages
- Format: <type>: <description>
- Types: feat, fix, refactor, docs, test, chore
- Commit body must include three paragraphs:
  1. `Prior this change ...` — what the situation was before
  2. `This change ...` — what the commit does and why
  3. `Assistant-model: <model name>` — e.g. `Assistant-model: Claude Sonnet 4.6`

## GitHub
- When creating a PR, always follow the structure in `.github/PULL_REQUEST_TEMPLATE.md`

## Testing
- Mirror src/ structure inside tests/unit/, tests/integration/ and tests/e2e/
- Test files are named test_<source_filename>.py
- unit/ → without database
- integration/ → with database
- e2e/ → full flows