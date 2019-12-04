import os
import pathlib
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

DEBUG = bool(os.environ.get("DEBUG", False))
SQL_DEBUG = os.environ.get("SQL_DEBUG", DEBUG)

BASE_PATH = pathlib.Path(__file__).parent

APP_HOST = os.environ.get("APP_HOST", "0.0.0.0")
APP_PORT = int(os.environ.get("APP_PORT", 1414))
APP_TITLE = "SFT SPACE"
APP_LOGO = "<strong>SFT SPACE ADMIN</strong>"
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
