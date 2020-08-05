# WDT Django psu-base extension template

This template is used to start a new reusable app (plugin) to extend psu_base

## How to use

```bash
$ django-admin.py startproject \
  --template=https://github.com/PSU-OIT-ARC/django-psu-base-template/archive/master.zip \
  --extension=py,md,txt,in \
  project_name
$ cd project_name
$ pip install -r requirements.txt
$ python manage.py migrate
```