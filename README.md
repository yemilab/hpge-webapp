# HPGe web app

## Requirements

```
$ python3 -m venv python3
$ source python3/bin/activate
```

```
$ pip install -r requirements.txt
```

## Developments

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
export HPGEWEBAPP_SETTINGS=$PREFIX/hpgeapp.cfg
cd $PREFIX
$PREFIX/python3/bin/gunicorn hpgeapp:app
```

Settings example,

```
SECRET_KEY = 'somekey'
```

Apache settings,

```
    <Location "/webapp">
        ProxyPreserveHost On
        ProxyPass http://localhost:8000/
        ProxyPassReverse http://localhost:8000/
        #RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set X-SCRIPT-NAME /app
    </Location>
```
