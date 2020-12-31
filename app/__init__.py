import os

from flask import Flask

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    DEBUG = True,
    TESTING = True,
    SECRET_KEY = 'development',
    UPLOAD_FOLDER = os.path.join(basedir, '..', 'uploads'),
    MAX_CONTENT_PATH = 10485760, # 10MB
)

app.config.from_object(__name__)

try:
    app.config.from_envvar('WEBAPP_SETTINGS')
except RuntimeError:
    pass

from app import views
