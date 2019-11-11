import os
from flask_testing import TestCase

from app.factory import app_factory
from config import ConfigType


class TestTestingConfig(TestCase):
    def create_app(self):
        return app_factory(ConfigType.TestingConfig)

    def test_is_app_in_testing_mode(self):
        self.assertTrue(self.app.config['DEBUG'], msg=(
            "DEBUG must be True in Testing mode"
        ))
        self.assertTrue(self.app.config['TESTING'], msg=(
            "TESTING must be True in Testing mode"
        ))


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        return app_factory(ConfigType.DevelopmentConfig)

    def test_is_app_in_development_mode(self):
        self.assertTrue(self.app.config['DEBUG'], msg=(
            "DEBUG must be True in Development mode"
        ))
        self.assertFalse(self.app.config['TESTING'], msg=(
            "TESTING must be False in Development mode"
        ))


class TestProductionConfig(TestCase):
    SECRET_KEY = "PRODUCTION_TEST_SECRET_KEY"
    DATABASE_URI = "sqlite:///test_db.db"
    UPLOAD_FOLDER = 'test_upload'
    SERVER_NAME = 'http://sft.crank.ru:5000'

    MAIL_DEFAULT_SENDER = 'noreply@testing.com'
    MAIL_SERVER = 'smtp.anything.com'
    MAIL_PORT = '1337'
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'

    FRONTEND_URL = 'http://localhost:9090'
    FRONTEND_EMAIL_CONFIRM_URL = '/confirm_the_email'
    FRONTEND_PASSWORD_RESET_URL = '/reset_the_password'

    def create_app(self):
        os.environ['SECRET_KEY'] = self.SECRET_KEY
        os.environ['DATABASE_URI'] = self.DATABASE_URI
        os.environ['UPLOAD_FOLDER'] = self.UPLOAD_FOLDER
        os.environ['SERVER_NAME'] = self.SERVER_NAME

        os.environ['MAIL_DEFAULT_SENDER'] = self.MAIL_DEFAULT_SENDER
        os.environ['MAIL_SERVER'] = self.MAIL_SERVER
        os.environ['MAIL_PORT'] = self.MAIL_PORT
        os.environ['MAIL_USERNAME'] = self.MAIL_USERNAME
        os.environ['MAIL_PASSWORD'] = self.MAIL_PASSWORD

        os.environ['FRONTEND_URL'] = self.FRONTEND_URL
        os.environ['FRONTEND_EMAIL_CONFIRM_URL'] = self.FRONTEND_EMAIL_CONFIRM_URL
        os.environ['FRONTEND_PASSWORD_RESET_URL'] = self.FRONTEND_PASSWORD_RESET_URL

        return app_factory(ConfigType.ProductionConfig)

    def test_is_app_in_production_mode(self):
        self.assertFalse(self.app.config['DEBUG'], msg=(
            "DEBUG must be False in Production mode"
        ))
        self.assertFalse(self.app.config['TESTING'], msg=(
            "TESTING must be False in Production mode"
        ))
        self.assertEqual(self.app.config['SECRET_KEY'], self.SECRET_KEY, msg=(
            "SECRET_KEY must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], self.DATABASE_URI, msg=(
            "SQLALCHEMY_DATABASE_URI must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['UPLOAD_FOLDER'], self.UPLOAD_FOLDER, msg=(
            "UPLOAD_FOLDER must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['SERVER_NAME'], self.SERVER_NAME, msg=(
            "SERVER_NAME must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['MAIL_DEFAULT_SENDER'], self.MAIL_DEFAULT_SENDER, msg=(
            "MAIL_DEFAULT_SENDER must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['MAIL_SERVER'], self.MAIL_SERVER, msg=(
            "MAIL_SERVER must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['MAIL_PORT'], self.MAIL_PORT, msg=(
            "MAIL_PORT must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['MAIL_USERNAME'], self.MAIL_USERNAME, msg=(
            "MAIL_USERNAME must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['MAIL_PASSWORD'], self.MAIL_PASSWORD, msg=(
            "MAIL_PASSWORD must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['FRONTEND_URL'], self.FRONTEND_URL, msg=(
            "FRONTEND_URL must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['FRONTEND_EMAIL_CONFIRM_URL'], self.FRONTEND_EMAIL_CONFIRM_URL, msg=(
            "FRONTEND_EMAIL_CONFIRM_URL must be loaded from environment variables"
        ))
        self.assertEqual(self.app.config['FRONTEND_PASSWORD_RESET_URL'], self.FRONTEND_PASSWORD_RESET_URL, msg=(
            "FRONTEND_PASSWORD_RESET_URL must be loaded from environment variables"
        ))
