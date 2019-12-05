import os

from app.factory import app_factory
from config import ConfigType


def create_app():
    config_type = ConfigType.ProductionConfig

    app = app_factory(config_type)
    return app
