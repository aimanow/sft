import datetime
from http import HTTPStatus

from flask_restplus import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from app.api.namespaces import access
from app.mails import send_registration_email
from app.tokens import EmailConfirmationToken, EmailConfirmationType
from database import db
from database.models import User, UserCredentials


@access.route('/registration')
class Registration(Resource):
    register_parser = reqparse.RequestParser()
    register_parser.add_argument('fullname', required=True, type=str, location='form', help=(
        "Fullname like 'John Dorian'"
    ))
    register_parser.add_argument('email', required=True, type=str, location='form', help="Email address")
    register_parser.add_argument('password', required=True, type=str, location='form', help="Password")

    @access.expect(register_parser)
    @access.response(HTTPStatus.CONFLICT, description='User is already exists')
    @access.response(HTTPStatus.OK, description='User successfully registered')
    def post(self):
        """
        Registration with email and password
        """

        args = self.register_parser.parse_args()

        user = User(
            fullname=args['fullname'],
            registered_at=datetime.datetime.now(),
            credentials_backref=UserCredentials(
                email=args['email'].lower(),
                password=args['password'],
            )
        )
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "User is already exists", HTTPStatus.CONFLICT

        registration_token = EmailConfirmationToken(EmailConfirmationType.Registration, user.id, args['email'])

        send_registration_email(
            email=args['email'],
            fullname=args['fullname'],
            token=registration_token.encode()
        )

        return "User successfully registered", HTTPStatus.OK
