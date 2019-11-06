# Helpful Info

## Migrations

Steps to updating database

1. Change your models (in models.py).
2. Run `python manage.py makemigrations` to create migrations for those changes
3. Run `python manage.py migrate` to apply those changes to the database.

## Remaining

1. Add some basic tests
2. Describe missing features:
    - better input validation
    - Viewsets rather than views
    - discomfort with `POST theatres/2/showings/3/tickets` to purchase tickets
    - ticket model with unique ID that can be recognized and revoked
    - update methods
