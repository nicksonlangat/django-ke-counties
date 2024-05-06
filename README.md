
![test workflow](https://github.com/nicksonlangat/django-ke-counties/actions/workflows/tests.yml/badge.svg)

### django-ke-counties
django-ke-counties is a Django app to get all
Kenyan counties, sub counties and wards.

#### INSTALLATION & SETUP
Setting this module is a walk in the park.
Ensure you are in a virtual environment in your Django project then Simply run 
`pip install https://github.com/nicksonlangat/django-ke-counties/releases/download/v1.0.0/django-ke-counties-0.1.tar.gz`
That will download and install an app called `django_ke_counties` in your environment. 

Next, add `django_ke_counties` to the list of `INSTALLED_APPS` in your `settings.py` as follows:
```python
INSTALLED_APPS = [
...
"django_ke_counties"
...
]
```
At this point, you will need to run a migrate command to create the models; `County`, `SubCounty` and `Ward` and populate them with data. 
Run:
`python manage.py migrate`
Your project is now ready to use what the module provides.

### USAGE
