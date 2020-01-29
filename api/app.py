import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(basedir, '../version.txt')

app = Flask(__name__)

@app.route('/')
def app_home():
    return 'Launch Darkly!!!'

@app.route('/version')
def app_version():
    with open(version_file, 'r') as file:
        version_str = file.read().replace('\n', '')
    return "app_version: {}".format(version_str)
