# -*- coding:utf-8 -*-
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

__author__ = 'MiracleWong'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        return dict(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.modules.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')

    register_blueprints(app)
    register_plugin(app)
    return app