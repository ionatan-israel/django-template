## Plantilla de proyectos Django 1.5.x en Heroku + Amazon S3

django-template

### Uso:

```shell
$ mkvirtualenv tu_env
$ pip install django==1.5.2
$ django-admin.py startproject --template=https://github.com/jrperdomoz/django-template/archive/heroku-as3.zip 
--extension=py,conf,rst,bat nombre_proyecto
$ cd nombre_proyecto
$ pip install -r requirements.txt
$ git init
$ git add .
$ git commit -m 'init app django'
$ heroku create
$ git push heroku master
$ heroku ps:scale web=1
$ heroku ps
$ heroku open
```

- Renombrar config-sample.json
- mv config-sample.json config.json
