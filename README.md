# Portfolio Backend (Django REST API)

Backend API for a personal portfolio website, built with Django and Django REST Framework.

## Stack

- Python 3.12
- Django 5
- Django REST Framework
- django-filter
- django-cors-headers
- PostgreSQL (production / Docker), SQLite (local default)
- Gunicorn + WhiteNoise

## Features

- Profile, Projects, Tools, Experience, Education, Services, Testimonials, Certifications, and Contact APIs
- Search/filter/order support on key list endpoints
- Email notification on contact form submission
- Static file serving with WhiteNoise
- Media upload support (profile pictures and resumes)

## Project Structure

```text
portbackend/        # Django project config (settings, urls, wsgi, asgi)
portfolio_api/      # Main app (models, serializers, viewsets, routes)
manage.py
requirements.txt
Dockerfile
docker-compose.yml
```

## Requirements

- Python 3.12+
- pip
- PostgreSQL (optional for local dev; SQLite is used by default)

## Local Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root.

```env
# Django
DJANGO_SECRET_KEY=replace-me
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# Database (optional - if omitted, SQLite is used)
# DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DB_NAME

# Email (for contact form notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-password
ADMIN_EMAIL=admin@example.com
```

4. Run migrations.

```bash
python manage.py migrate
```

5. Start dev server.

```bash
python manage.py runserver
```

API base URL (local):

```text
http://127.0.0.1:8000/api/
```

## API Endpoints

All endpoints are under `/api/` and use DRF router paths with trailing slash.

| Resource | Endpoint | Notes |
|---|---|---|
| Profile | `/api/profile/` | Returns a single profile object instead of a list; GET only |
| Projects | `/api/projects/` | CRUD viewset |
| Tools | `/api/tools/` | CRUD viewset |
| Experiences | `/api/experiences/` | CRUD viewset |
| Education | `/api/education/` | CRUD viewset |
| Services | `/api/services/` | CRUD viewset |
| Testimonials | `/api/testimonials/` | Read-only |
| Contact | `/api/contact/` | POST enabled in viewset; sends email notification |
| Certifications | `/api/certifications/` | CRUD viewset |

### Query Support

The following endpoints support filtering, searching, and/or ordering:

- Projects: `filter(title)`, `search(title, description)`, `ordering(number, title)`
- Tools: `filter(name)`, `search(name)`, `ordering(name)`
- Experiences: `filter(company, position)`, `search(company, position, description)`, `ordering(year, company)`
- Education: `filter(institution)`, `search(institution, description)`, `ordering(year, institution)`
- Services: `filter(title)`, `search(title, description)`, `ordering(title)`
- Certifications: `filter(organization)`, `search(name, organization)`

Examples:

```text
GET /api/projects/?search=django
GET /api/experiences/?ordering=-year
GET /api/tools/?name=python
```

## Auth and Permissions

- Global DRF permission is `IsAuthenticatedOrReadOnly`.
- Read operations are public.
- Write operations require authentication unless endpoint-specific permissions are changed.

## Static and Media

- Static files: served from `STATIC_ROOT` (`/staticfiles` in project root after collectstatic).
- Media files: served from `/media/` in debug mode.

## Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

Services:

- `web`: Django + Gunicorn on `:8000`
- `db`: PostgreSQL on `:5432`

The compose setup runs migrations automatically before starting Gunicorn.

## Production Notes

- Set `DJANGO_DEBUG=False`.
- Use a strong `DJANGO_SECRET_KEY`.
- Set explicit `DJANGO_ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS`.
- Provide a production `DATABASE_URL`.
- Run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn portbackend.wsgi:application --bind 0.0.0.0:$PORT
```

## Deployment (Railway)

`railway.toml` uses:

```text
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portbackend.wsgi:application --bind 0.0.0.0:$PORT
```

Make sure required environment variables are configured in Railway.

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

## Admin

Admin site is available at:

```text
/admin/
```

Create a superuser to manage records through Django admin.
