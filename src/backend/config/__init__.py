import os
from enum import Enum


class ConfigBase:
    # SERVER
    SERVER_NAME = None
    SCHEME = 'http'

    # BASICS
    DEBUG = False
    TESTING = False

    # SECURITY
    SECRET_KEY = "SECRET_KEY"

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SWAGGER
    ERROR_404_HELP = False

    # USER UPLOADS
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'upload')

    FRONTEND_URL = 'http://localhost:8000/'
    FRONTEND_EMAIL_CONFIRM_URL = '/email_confirmation'
    FRONTEND_PASSWORD_RESET_URL = '/password_reset'

    # Mails
    MAIL_FEEDBACK = 'info@sft.space'
    MAIL_DEFAULT_SENDER = 'noreply@sft.space'
    MAIL_SERVER, MAIL_PORT = "smtp.mailtrap.io", 2525
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''


class ConfigType(Enum):
    DevelopmentConfig = 'config.development.DevelopmentConfig'
    ProductionConfig = 'config.production.ProductionConfig'
    TestingConfig = 'config.testing.TestingConfig'
