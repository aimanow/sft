import os

from app.factory import app_factory
from config import ConfigType


def create_app():
    if os.environ.get('SFT_CONFIG') == 'prod':
        config_type = ConfigType.ProductionConfig
    else:
        config_type = ConfigType.DevelopmentConfig

    app = app_factory(config_type)
    return app
