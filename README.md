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

https://docxtpl.readthedocs.io/en/latest/ -- this is working so far!!
http://pbpython.com/python-word-template.html 


Copy form format of the following: https://www.lawdepot.ca/ (a good short form with the basics)
Good detailed questions: https://www.rocketlawyer.com/

homepage template: https://themeforest.net/item/borial-bootstrap-4-business-agency-template/21996760?irgwc=1&clickid=Tpy0-ewFQWW9Q%3An0YAy1rznNUkgXc0RbEXuwxI0&iradid=275988&irpid=1267846&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&mp_value1=&utm_campaign=af_impact_radius_1267846&utm_medium=affiliate&utm_source=impact_radius
 - there are some more links in it which could be explored. I just need the github style login form at the front page. Keep in mind this is the marketing frontend page we are talking about. The rest would have a login page to sign in from or they could use this page as well.


Things to implement in wills 2.0

1) If a couple wants to write a will for each the system should be able to handle that.
