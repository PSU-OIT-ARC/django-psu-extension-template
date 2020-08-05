# WDT Django psu-base extension template

This template is used to start a new reusable app (plugin) to extend psu_base

## How to use

Step 1 (start new project):
```bash
$ django-admin.py startproject \
  --template=https://github.com/PSU-OIT-ARC/django-psu-extension-template/archive/master.zip \
  --extension=py,md,txt,in \
  project_name
```

Step 2 (provide secrets):  

* Open project_name/demo/local_settings.py 
  * You MUST enter the appropriate Finti token.  
  * If your plugin will send emails, you will also need to provide the email password in order to test sending emails.  

Step 3 (install dependencies):
```bash
$ cd project_name
$ pip install -r requirements.txt
$ python manage.py migrate
```

Step 4 (initialize Git):
```bash
$ git init
$ git add .
$ git commit -m "New reusable psu-base extension"
```