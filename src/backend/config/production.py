import os
from config import ConfigBase
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')


class ProductionConfig(ConfigBase):
    DEBUG = False
    TESTING = False

    SERVER_NAME = os.getenv('SERVER_NAME')

    SCHEME = os.getenv('SCHEME', ConfigBase.SCHEME)

    SECRET_KEY = os.getenv('SECRET_KEY')
    if SECRET_KEY is None:
        raise EnvironmentError("SECRET_KEY env variable is not set")

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    if SQLALCHEMY_DATABASE_URI is None:
        raise EnvironmentError("DATABASE_URI env variable is not set")

    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL', 'http://192.168.100.1:9200')
    if ELASTICSEARCH_URL is None:
        raise EnvironmentError("ELASTICSEARCH_URL env variable is not set")

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    if SQLALCHEMY_DATABASE_URI is None:
        raise EnvironmentError("UPLOAD_FOLDER env variable is not set")

    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    if MAIL_DEFAULT_SENDER is None:
        raise EnvironmentError("MAIL_DEFAULT_SENDER env variable is not set")

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    if MAIL_SERVER is None:
        raise EnvironmentError("MAIL_SERVER env variable is not set")

    MAIL_PORT = os.getenv('MAIL_PORT')
    if MAIL_PORT is None:
        raise EnvironmentError("MAIL_PORT env variable is not set")

    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', False)
    if MAIL_USE_TLS == 'True' or MAIL_USE_TLS == '1':
        MAIL_USE_TLS = True

    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', False)
    if MAIL_USE_SSL == 'True' or MAIL_USE_SSL == '1':
        MAIL_USE_SSL = True

    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    if MAIL_USERNAME is None:
        raise EnvironmentError("MAIL_USERNAME env variable is not set")

    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    if MAIL_PASSWORD is None:
        raise EnvironmentError("MAIL_PASSWORD env variable is not set")

    FRONTEND_URL = os.getenv('FRONTEND_URL')
    if FRONTEND_URL is None:
        raise EnvironmentError("FRONTEND_URL env variable is not set")

    FRONTEND_EMAIL_CONFIRM_URL = os.getenv('FRONTEND_EMAIL_CONFIRM_URL')
    if FRONTEND_EMAIL_CONFIRM_URL is None:
        raise EnvironmentError("FRONTEND_EMAIL_CONFIRM_URL env variable is not set")

    FRONTEND_PASSWORD_RESET_URL = os.getenv('FRONTEND_PASSWORD_RESET_URL')
    if FRONTEND_PASSWORD_RESET_URL is None:
        raise EnvironmentError("FRONTEND_PASSWORD_RESET_URL env variable is not set")

    OAUTH_VK_ID = os.getenv('OAUTH_VK_ID', False)
    OAUTH_VK_SECRET = os.getenv('OAUTH_VK_SECRET', False)
    OAUTH_VK_REDIRECT = os.getenv('OAUTH_VK_REDIRECT', False)

    OAUTH_GOOGLE_ID = os.getenv('OAUTH_GOOGLE_ID', False)
    OAUTH_GOOGLE_SECRET = os.getenv('OAUTH_GOOGLE_SECRET', False)
    OAUTH_GOOGLE_REDIRECT = os.getenv('OAUTH_GOOGLE_REDIRECT', False)

    OAUTH_FACEBOOK_ID = os.getenv('OAUTH_FACEBOOK_ID', False)
    OAUTH_FACEBOOK_SECRET = os.getenv('OAUTH_FACEBOOK_SECRET', False)
    OAUTH_FACEBOOK_REDIRECT = os.getenv('OAUTH_FACEBOOK_REDIRECT', False)