# Finance-app (mywallet)

An unfinished Django personal-finance app: a landing page with a spending chart, plus the start of a user-profile model.

## Context

I started this in late 2020 while teaching myself Django, before I knew its conventions for apps, routing and settings. It was meant to include a payment-system integration, which I never got working, partly because I wasn't managing package versions. I keep it public as a record of how I learned.

## Stack

- Python 3.8.2 (from the `tutorial-env/` virtualenv that was committed)
- Django 3.1.3, Django REST framework 3.12.2, asgiref 3.3.1, pytz 2020.4, sqlparse 0.4.1
- pylint 2.6.0 and its dependencies were also installed; they're editor tools, not runtime dependencies
- SQLite; Google Charts loaded from a CDN
- The page markup started as my `FinanceApp` repository

## Running it

It does not start as committed (see Known gaps). Once the two missing imports in `urls.py` are added, these steps work (I checked them with Python 3.8):

    cd mywallet
    python3.8 -m venv venv && source venv/bin/activate
    pip install -r ../requirements.txt
    python manage.py migrate
    python manage.py runserver

`DJANGO_SECRET_KEY` and `DJANGO_DEBUG` are optional locally; see `.env.example`.

## Status

Not finished. The payment integration was never committed, so nothing in this repo calls an external service. With the two missing imports added, the home page renders; the Login, Sign Up and planning buttons go nowhere. The first commit is from February 2021; in February 2023 I fixed syntax errors in `views.py` and `admin.py` and added the home route through GitHub's web editor.

## Known gaps

- `mywallet/mywallet/urls.py:16-21`: `admin` and `path` are used but never imported, so `manage.py` fails with `NameError: name 'path' is not defined`. The 2021 version had the imports but no route to the app; the 2023 edit added the route and lost them.
- `mywallet/money/models.py:2`: `from __future__ import unicode_literals` comes after another import, which is a `SyntaxError`. Line 13 has `max_lenght`, a `TypeError`. `ssn` and `zipcode` are `IntegerField`s with `max_length`, which Django ignores. Several imports on lines 4-9 are unused.
- `mywallet/mywallet/settings.py:34-44`: the `money` app is not in `INSTALLED_APPS`, so it has no migrations and its model isn't in the admin. `'mywallet'`, the project package, is listed instead.
- `settings.py:24`: the secret key was hardcoded. It now comes from `DJANGO_SECRET_KEY`. The original key is still in git history; it was a development key.
- `settings.py:27`: `DEBUG` was hardcoded to `True`. It now reads `DJANGO_DEBUG` and still defaults to `True`. `ALLOWED_HOSTS` (line 29) is empty, and there is no `STATIC_ROOT`.
- `settings.py:36, 54, 127`: CORS is half set up. `corsheaders` is commented out, so `CORS_ORIGIN_ALLOW_ALL` does nothing. `CommonMiddleware` is listed twice (lines 49 and 55). `rest_framework` is installed (line 35), but nothing uses it.
- Routing: there is no `money/urls.py`; the project `urls.py` imports the view directly, and only `/` and `/admin/` exist. The page links to `login.html` and loads `style.css`, but neither is routed or served, so both 404 and the page has no styling.
- `money/views.py`: the page is a Python string returned with `HttpResponse`, not a template.
- The model stores Social Security numbers as plain integers with no encryption. Integers would also drop leading zeros from SSNs and ZIP codes.
- No requirements file was committed, and no payment or banking library is installed in `tutorial-env/`, so the integration's dependencies aren't recorded anywhere. The new `requirements.txt` is pinned from what is in `tutorial-env/`.
- No tests (`money/tests.py` is empty). `tutorial-env/` and `__pycache__` were committed; they're untracked now but remain in history.

## What I'd do differently now

- Get the basic routes and models running end to end before adding an integration.
- Pin dependencies in `requirements.txt` from the start and use the provider's sandbox.
- Not store SSNs at all unless required, and encrypt them if they are.
