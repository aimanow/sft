import os
import pathlib
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

DEBUG = os.getenv("DEBUG", 'False') == 'True'
SQL_DEBUG = os.getenv("SQL_DEBUG", DEBUG) == 'True'

BASE_PATH = pathlib.Path(__file__).parent

APP_HOST = os.getenv("ADMIN_APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("ADMIN_APP_PORT", 1414))
APP_TITLE = "SFT SPACE"
APP_LOGO = "<strong>SFT SPACE ADMIN</strong>"
# DATABASE ONLY FOR ADMIN_APP USERS, NOT PRODUCTION DB
APP_DSN = "sqlite:///godmode/database/godmode.sqlite"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simpleFormatter": {
            "format": "%(asctime)s %(levelname)-8s %(module)s : %(message)s"
        },
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "formatter": "simpleFormatter",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["consoleHandler"]
        },
    }
}
