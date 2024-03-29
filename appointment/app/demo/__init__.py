# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import appiontment

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

def create_app():
    app = Flask(__name__, static_folder='static')
    app.after_request(after_request)
    app.register_blueprint(
        appiontment.bp,
        url_prefix='/appiontment')
    return app

if __name__ == '__main__':
    create_app().run('0.0.0.0',debug=True)