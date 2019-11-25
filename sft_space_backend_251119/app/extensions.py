from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

from app.authorization import Authorization

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
authorization = Authorization()


def register_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    authorization.init_app(app)
    CORS(app, supports_credentials=True)
