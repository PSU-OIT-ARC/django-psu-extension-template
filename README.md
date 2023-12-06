# WDT Django psu-base extension template

This template is used to start a new reusable app (plugin) to extend psu_base

## How to Create a New Reusable App

Step 1 (start new project):  
*Note: Do **not** include "psu_" in the name of your project*
```bash
$ django-admin.py startproject \
  --template=https://github.com/PSU-OIT-ARC/django-psu-extension-template/archive/main.zip \
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

## Publishing Your New Reusable App
Once you have developed some usable functionality, and tested it using the included Demo app, 
you can deploy it to PyPi (assuming you have a PyPi account, and your access keys are set up).

Here is the script that I use to deploy to PyPi:
```buildoutcfg
if [ -f "MANIFEST.in" ]
then
        export DJANGO_SETTINGS_MODULE="demo/settings"
        python setup.py sdist bdist_wheel --universal
        twine upload --repository testpypi dist/*
        twine upload dist/*
        rm dist/*
        unset DJANGO_SETTINGS_MODULE
else
        echo "You must be in your project's root directory to publish to PyPi"
fi
```