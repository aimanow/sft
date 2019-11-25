from config import ConfigBase

try:
    from .config import LocalConfig
    assert issubclass(LocalConfig, ConfigBase)
except ImportError:
    LocalConfig = ConfigBase


class DevelopmentConfigMixin:
    DEBUG = True
    TESTING = False


class DevelopmentConfig(DevelopmentConfigMixin, LocalConfig):
    """
        <!> DO NOT EDIT THIS CLASS FOR YOUR LOCAL CONFIGURATION
        Create your local configuration in "config/development/config.py" like this:

        >>> from config import ConfigBase
        >>> class LocalConfig(ConfigBase):
        ...    SECRET_KEY = "DEVELOPMENT_SECRET_KEY"
        ...    SQLALCHEMY_DATABASE_URI = 'postgresql://...'
        ...
        ...    MAIL_DEFAULT_SENDER = 'noreply@sft.space'
        ...    MAIL_SERVER, MAIL_PORT = "smtp.mailtrap.io", 2525
        ...    MAIL_USERNAME = '<your_mailtrap_username>'
        ...    MAIL_PASSWORD = '<your_mailtrap_password>'
        ...
        ...    # If you are using a frontend application
        ...    FRONTEND_URL = 'http://localhost:8000/'
        ...    FRONTEND_EMAIL_CONFIRM_URL = '/email_confirmation'
        ...    FRONTEND_PASSWORD_RESET_URL = '/password_reset'
    """
