from config import ConfigBase


class TestingConfig(ConfigBase):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "TESTING_SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    LIVESERVER_PORT = 0
