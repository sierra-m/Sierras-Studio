import time
import os
import json
from datetime import datetime

from flask import Flask, send_from_directory, redirect, send_file, request, jsonify, render_template, Markup
import requests
from PIL import Image
import markdown2

import util

app = Flask('SierrasStudio')


@app.route('/')
def root():
    return send_from_directory('static/html', 'main.html', mimetype='text/html')


@app.route('/home')
def home():
    return redirect('/')


@app.route('/projects/')
@app.route('/projects')
def projects():
    return send_file('static/html/projects.html', mimetype='text/html')


@app.route('/files')
def files():
    return send_file('static/html/files.html', mimetype='text/html')


@app.route('/about')
def about():
    return send_file('static/html/about.html', mimetype='text/html')


@app.route('/css/<stylesheet>')
def css(stylesheet):
    return send_from_directory('static/css', stylesheet, mimetype='text/css')


@app.route('/image/<img>')
def image(img):
    if img.endswith('.png'):
        mime = 'image/png'
    else:
        mime = 'image/jpeg'

    return send_from_directory('static/image', img, mimetype=mime)


@app.route('/icon/<file>')
def icon(file):
    return send_from_directory('static/image/icon', file, mimetype='image/png')


@app.route('/manifest')
def manifest():
    return send_file('static/image/icon/manifest.json', mimetype='application/json')


@app.route('/js/<script>')
def js(script):
    return send_from_directory('static/js', script, mimetype='text/javascript')


@app.route('/projects/<article_id>')
def article(article_id):
    article_id = article_id.replace("/..", "/")  # super secure

    with open('static/html/articles/{}.json'.format(article_id), 'r') as f:
        data = json.load(f)
        content = markdown2.markdown(''.join(data['content']))
        data['content'] = Markup(content)
        return render_template('article.html', **data)

# TODO: Urandom author auth


app.run(threaded=True)
