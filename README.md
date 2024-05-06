
![test workflow](https://github.com/nicksonlangat/django-ke-counties/actions/workflows/tests.yml/badge.svg)

### django-ke-counties
django-ke-counties is a Django app to get all
Kenyan counties, sub counties and wards in a tree like structure.  
This allows you to build table relationships(FK, M2M) with the models
defined within the scope of the app.

#### INSTALLATION & SETUP
Setting this module is a walk in the park.
Ensure you are in a virtual environment in your
Django project then Simply run
```bash
pip install https://github.com/nicksonlangat/django-ke-counties/releases/download/v1.0.0/django-ke-counties-0.1.tar.gz
```
That will download and install an app called `django_ke_counties` in your environment. 

Next, add `django_ke_counties` to the list of `INSTALLED_APPS` in your `settings.py` as follows:
```python
INSTALLED_APPS = [
...
"django_ke_counties"
...
]
```
At this point, you will need to run a migrate command to create the models;
```python
County
SubCounty
Ward
```
and populate them with appropriate data. To apply this migration, run:
`python manage.py migrate`

Finally, add to your project's `urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path("", include("django_ke_counties.urls")),
]

```
Your project is now ready to use what the module provides. See usage below.

### USAGE
Out of the box, the module exposes 3 endpoints but you can always extend or even write your own.
The three endpoints provided are:

```python
/counties
/sub-counties
/wards
```
If they do not suffice for your needs, feel free to import the models and extend as you deem fit.

```python
from django_ke_counties.models import County, SubCounty, Ward
```

### SUPPORT & CONTRIBUTING
There are a couple ways of supporting this effort:
- Star the repo
- Help test it on your projects
- Share with fellow builders
- Report issues
- Buy me coffee :) ☕️
  
To contribute to this project,
Fork the repo, dance with some code and raise those PRS. I look forward to merging `em.
