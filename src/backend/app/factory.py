import os

from flask import Flask
from flask_migrate import Migrate

from config import ConfigType
from elasticsearch import Elasticsearch
from app.api import api_blueprint
from commands.superuser import superuser_cli

from app.extensions import db, register_extensions


def register_blueprints(app):
    app.register_blueprint(api_blueprint)


def register_commands(app):
    Migrate(app, db, directory=os.path.join('database', 'migrations'))
    app.cli.add_command(superuser_cli)


def app_factory(config_type: ConfigType):
    app = Flask(__name__)
    app.config.from_object(config_type.value)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app
