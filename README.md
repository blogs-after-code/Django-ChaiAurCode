# ChaiAurDjango

A Django project for browsing chai varieties.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set a unique `DJANGO_SECRET_KEY`, then run:

```powershell
cd chaiaurDjango
python manage.py migrate
python manage.py tailwind build
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. The local database is intentionally not versioned; create an admin user with `python manage.py createsuperuser` if needed.
