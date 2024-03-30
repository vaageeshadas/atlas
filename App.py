from flask import Flask, render_template, request, jsonify, abort, session
import os
from pathlib import Path
from sys import path
import json
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/globe')
def globe():
    return render_template('globe.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/united-states-of-america')
def usa_page():
    return render_template('united-states-of-america.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug = True)