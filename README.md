# COSINE Run Catalog

## Flask

http://flask.pocoo.org/

## Requirements

```
$ pip install -r requirements.txt
```

## Developments

Initialize database

```
$ sqlite3 cosine.db < schema.sql
```

Test run

```
$ FLASK_APP=hpge.py FLASK_DEBUG=1 flask run
```

```
$ export FLASK_APP=hpge
$ export FLASK_DEBUG=1
$ python -m flask run
```

## Deployments

Gunicorn example

```
#!/bin/bash
PREFIX=/opt/hpgeapp
export COSINEWEBAPP_SETTINGS=$PREFIX/cosine.cfg
cd $PREFIX
$PREFIX/miniconda3/bin/gunicorn COSINEApp:app
```

Settings example,

```
SECRET_KEY = 'somekey'
```

Apache settings,

```
    <Location "/webapp">
        ProxyPass http://localhost:8000/
        ProxyPassReverse http://localhost:8000/
        #RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set X-SCRIPT-NAME /webapp
    </Location>
```
