import os
import time
import datetime
from pathlib import Path
import re
import shutil

from flask import request, session, g, redirect, url_for, abort, render_template, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict

from app import app

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/gasflow')
def gasflow():
    return render_template(
        'gasflow.html',
    )

@app.route('/gasflow', methods=['POST'])
def uploader():
    '''
    $ curl -F 'gasflow=@filename.jpg' http://localhost:5000/gasflow
    '''
    for k, f in request.files.items():
        filename = secure_filename(f.filename)
        if filename == 'gasflow.jpg':
            return abort(406)
        # Create plots folder
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], k)
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
        f.save(os.path.join(upload_dir, filename))
        shutil.copyfile(os.path.join(upload_dir, filename), os.path.join(upload_dir, 'gasflow.jpg'))
        return '', 204

@app.route('/files/<category>/<filename>')
def downloader(category, filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category), filename)

