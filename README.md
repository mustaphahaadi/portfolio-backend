# Portfolio Backend (Django REST API)

Backend API for a personal portfolio website, built with Django and Django REST Framework.

## Stack

- Python 3.12
- Django 5
- Django REST Framework
- django-filter
- django-cors-headers
- PostgreSQL (production), SQLite (local default)
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

### Free Profile Photo Option (No S3 Needed)

If you only need one profile image, use the `profile_picture_url` field on the Profile model/admin.

- Put any public image URL there (for example from Cloudinary free tier, Imgur, GitHub raw URL, or another public CDN).
- The API will return this URL as `profile_picture`.
- If `profile_picture_url` is empty, it falls back to the uploaded `profile_picture` file.

This allows you to avoid object storage services for a small portfolio setup.

## Production Notes

- Set `DJANGO_DEBUG=False`.
- Use a strong `DJANGO_SECRET_KEY`.
- Set explicit `DJANGO_ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS`.
- Set `CSRF_TRUSTED_ORIGINS` to your frontend domain.
- Provide a production `DATABASE_URL`.
- Run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn portbackend.wsgi:application --bind 0.0.0.0:$PORT
```

### Production Environment File

Use `.env.production.example` as the template for production variables.

Required minimum in production:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `DATABASE_URL`
- `CORS_ALLOWED_ORIGINS`
- `CSRF_TRUSTED_ORIGINS`

If `DATABASE_URL` is missing in production, the app now fails fast during startup instead of silently falling back to SQLite.

## Deployment (Railway)

`railway.toml` uses:

```text
python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn portbackend.wsgi:application --bind 0.0.0.0:$PORT
```

Make sure required environment variables are configured in Railway.

If remote migrations still do not apply:

- Confirm `DATABASE_URL` points to Railway Postgres (not a placeholder value).
- Confirm the latest migration files are pushed (including `portfolio_api/migrations/0011_profile_profile_picture_url.py`).
- Run a one-off Railway command: `python manage.py migrate --noinput`.
- Check deploy logs for `Applying portfolio_api.0011_profile_profile_picture_url... OK`.

### Persistent Storage for Media Files

Railway has an ephemeral filesystem — files uploaded to `/media/` disappear after each deploy. The `railway.toml` now configures a persistent volume mounted at `/app/media` to preserve profile pictures and resumes across deployments.

**First time only:** After pushing this update, redeploy and run a one-off Django shell command to re-upload your files through the admin interface, or:

1. In Railway, use a one-off command to create the media directory:
   ```
   mkdir -p /app/media/profile_pics /app/media/resumes
   ```
2. Access admin at `/admin/` and re-upload your resume and profile picture.
3. They will now persist across future deployments.

**Alternative (free, no uploads needed):** Use `profile_picture_url` in admin to link a free hosted image (GitHub raw URL, Imgur, etc.), and use `resume` URL field if you host the file elsewhere.

### Admin Login

This backend does not expose a custom user login API.

- Admin login is available at `/admin/`
- Create the admin user with `python manage.py createsuperuser`
- Run that only after Railway Postgres is attached and `DATABASE_URL` is set correctly

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
