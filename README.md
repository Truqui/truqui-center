# TruquiCenter

Personal web application to centralise personal content and projects.

[![MIT License](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

---

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2, Python 3.12 |
| Database | PostgreSQL 16 |
| Frontend | HTMX, Alpine.js, Tailwind CSS |
| Auth | django-allauth (email + 2FA) |
| Logging | Loguru |
| Linter / formatter | Ruff |
| Type checker | mypy (strict) |

---

## Architecture

Layered architecture with a strict dependency direction:

```
interface → application → domain → infrastructure
```

| Layer | Path | Responsibility |
|---|---|---|
| Interface | `src/interface/<module>/` | HTTP handlers, webhooks |
| Application | `src/application/<module>/` | Use cases (`<verb>_<noun>.py`) |
| Domain | `src/domain/<module>/` | Business logic |
| Infrastructure | `src/infrastructure/database/<module>/` | Models, querysets, queries, operations |
| External | `src/infrastructure/external/` | Third-party integrations (e.g. Telegram) |

The ORM is allowed at all layers as a pragmatic exception.

---

## Local development with Docker

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose

### Setup

1. Copy the environment template and fill in the values:

   ```bash
   cp .env.example .env
   ```

2. Build and start the services:

   ```bash
   docker compose up --build
   ```

3. Run database migrations:

   ```bash
   docker compose exec app python manage.py migrate
   ```

4. Open the app at [http://localhost:8000](http://localhost:8000).

---

## Environment variables

| Variable | Default | Required | Description |
|---|---|---|---|
| `SECRET_KEY` | — | Yes | Django secret key |
| `DEBUG` | `False` | No | Enable Django debug mode |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | No | Comma-separated allowed hosts |
| `POSTGRES_DB` | — | Yes | Database name |
| `POSTGRES_USER` | — | Yes | Database user |
| `POSTGRES_PASSWORD` | — | Yes | Database password |
| `POSTGRES_HOST` | `localhost` | No | Database host (`db` inside Docker) |
| `POSTGRES_PORT` | `5432` | No | Database port |

---

## Code quality

Run the linter and formatter with Ruff:

```bash
docker compose exec app ruff check .
docker compose exec app ruff format --check .
```

Run the type checker:

```bash
docker compose exec app mypy .
```

Pre-commit hooks (Ruff check + format) run automatically on every commit. To install them locally:

```bash
pip install pre-commit
pre-commit install
```

---

## Testing

Tests are organised in three tiers mirroring `src/`:

| Tier | Path | Database |
|---|---|---|
| Unit | `tests/unit/` | No |
| Integration | `tests/integration/` | Yes |
| End-to-end | `tests/e2e/` | Yes |

Run the full test suite:

```bash
docker compose exec app python manage.py test
```

---

## Contributing

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/). Every commit body must include three paragraphs:

```
<type>: <description>

Prior this change, ...

This change ...

Assistant-model: <model name or N/A>
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.

---

## Licence

[MIT](LICENSE) © Sergio González Cruz