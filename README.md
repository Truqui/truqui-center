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

## Modules

### Pages

Static pages are available at:

| URL | View | Description |
|---|---|---|
| `/<slug>/` | `PageDetailView` | Full page detail |

Pages are managed via the Django admin (`/admin/` → **Pages**). A page only appears on the site when `is_published` is set to `True`.

#### Adding a Page to the navigation menu

To expose a page in the navigation bar, create a `MenuItem` entry via the Django admin:

1. Go to `/admin/` → **Menu items** → **Add menu item**.
2. Set **Label** to the text you want in the nav (e.g. `About`).
3. Set **URL** to `/<slug>/` matching the page slug.
4. Set **Order** to control its position relative to other items.
5. Make sure **Is active** is checked.
6. Save.

---

### Blog

Published posts are available at:

| URL | View | Description |
|---|---|---|
| `/blog/` | `PostListView` | Paginated list of all published posts |
| `/blog/<slug>/` | `PostDetailView` | Full post detail |

Posts are managed via the Django admin (`/admin/` → **Posts**). A post only appears on the site when `is_published` is set to `True`.

#### Adding the Blog to the navigation menu

The navigation bar is driven by `MenuItem` records. To expose the blog page in the menu, create an entry manually via the Django admin:

1. Go to `/admin/` → **Menu items** → **Add menu item**.
2. Set **Label** to the text you want in the nav (e.g. `Blog`).
3. Set **URL** to `/blog/`.
4. Set **Order** to control its position relative to other items.
5. Make sure **Is active** is checked.
6. Save.

---

### Teams

A registry of football teams is available at:

| URL | View | Description |
|---|---|---|
| `/teams/` | `TeamListView` | Card-based listing of teams, grouped into Active and Inactive |

Teams are managed via the Django admin (`/admin/` → **Teams**). Name, coach, crest and status (**Is active**) are required; stadium, motto, fans name and country are optional and simply omitted from the card when left blank.

#### Adding Teams to the navigation menu

To expose the teams page in the navigation bar, create a `MenuItem` entry via the Django admin:

1. Go to `/admin/` → **Menu items** → **Add menu item**.
2. Set **Label** to the text you want in the nav (e.g. `Teams`).
3. Set **URL** to `/teams/`.
4. Set **Order** to control its position relative to other items.
5. Make sure **Is active** is checked.
6. Save.

---

## CSS development

Tailwind CSS is compiled ahead of time — the project does **not** use the Tailwind CDN. The compiled stylesheet is committed to the repository at `src/interface/web/static/css/styles.css`.

### When to rebuild

Rebuild `styles.css` whenever you:

- Add a new Tailwind utility class to a template.
- Change the `@theme` color tokens in `input.css`.
- Add custom CSS or import a third-party CSS library.

### How to rebuild

```bash
make css        # single build (minified)
make css-watch  # watch mode — rebuilds automatically on every change
```

The first run downloads the Tailwind CLI binary to `/tmp/` automatically. No Node.js required.

### Adding custom CSS

All CSS goes through `src/interface/web/static/css/input.css`. Add hand-written styles or `@import` statements for third-party libraries below the `@theme` block — they will be included in the compiled output.

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
| `SITE_NAME` | `My Site` | No | Site name shown in the nav and page title |
| `THEME_BACKGROUND` | `#ffffff` | No | Background colour |
| `THEME_FOREGROUND` | `#111827` | No | Default text colour |
| `THEME_MUTED` | `#6b7280` | No | Muted text colour |
| `THEME_BORDER` | `#e5e7eb` | No | Border colour |
| `THEME_PRIMARY` | `#111827` | No | Primary/brand colour |
| `THEME_BANNER` | `#555555` | No | Page banner background colour |
| `THEME_BANNER_FG` | `#ffffff` | No | Page banner title text colour |
| `THEME_MAIN_BG` | `#ffffff` | No | Main content box background colour |
| `THEME_MAIN_BORDER` | `#e5e7eb` | No | Main content box border colour |
| `THEME_NAV_ACTIVE` | `#111827` | No | Active nav item background colour |
| `THEME_CARD` | `#ffffff` | No | Card background colour (e.g. team listing cards) |

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