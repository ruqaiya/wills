# wills
Automatic will generation software

## Local setup

### instal requirements

the system should have python 3.7.2 and pipenv installed.
Run: pipenv install

### setup db and run migrations

create a postgres db. Add those credentials to wills/settings.py
run: python manage.py migrate

### create superuser

run: python manage.py createsuperuser

### run local server

run: python manage.py runserver

### access admin panel

go to 127.0.0.1:8000/admin/ and use the superuser credentials you created above.








Try these for document building:

https://docxtpl.readthedocs.io/en/latest/
http://pbpython.com/python-word-template.html (trying this right now)
