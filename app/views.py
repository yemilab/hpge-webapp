import os
import time
import datetime
from pathlib import Path
import re
import shutil
import glob

from flask import request, session, g, redirect, url_for, abort, render_template, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict

from app import app

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/webcam')
def webcam():
    imgs = glob.glob(os.path.join(app.config['UPLOAD_FOLDER'], 'webcam', '*.jpg'))
    cams = dict()
    for path in imgs:
        fname = os.path.basename(path)
        tag = fname.split('.')[0]
        cams[tag] = fname
    return render_template(
        'webcam.html', cams=cams
    )

@app.route('/webcam', methods=['POST'])
def webcam_upload():
    '''
    $ curl -F 'tag=@filename.jpg' http://localhost:5000/webcam
    '''
    regexp = re.compile('[^0-9a-zA-Z]+') # Find special characters
    for tag, f in request.files.items():
        if regexp.search(tag):
            return 406
        filename = secure_filename(f.filename)
        # Create plots folder
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'webcam', tag)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir, exist_ok=True)
        f.save(os.path.join(upload_dir, filename))
        shutil.copyfile(os.path.join(upload_dir, filename), os.path.join(app.config['UPLOAD_FOLDER'], 'webcam', f'{tag}.jpg'))
        return '', 204

@app.route('/webcam/<filename>')
def webcam_download(filename):
    print(app.config['UPLOAD_FOLDER'])
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], 'webcam'), filename)
