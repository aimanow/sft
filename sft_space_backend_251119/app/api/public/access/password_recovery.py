from datetime import timedelta
from http import HTTPStatus

from flask_restplus import Resource, reqparse, abort
from app.api.namespaces import access
from app.mails import send_password_recovery_email
from app.tokens import PasswordRecoveryToken
from app.authorization.permissions import update_user_permissions
from database import db
from database.models import UserCredentials
from app.api.models import ProfileModel

@access.route('/password/recovery')
class PasswordRecovery(Resource):
    recovery_parser = reqparse.RequestParser()
    recovery_parser.add_argument('email', required=True, type=str, location='form', help=(
        'Email specified during registration'
    ))

    @access.expect(recovery_parser)
    @access.response(HTTPStatus.OK, description='A letter to confirm the password recovery sent to the email')
    def post(self):
        """
        Password recovery

        * User can send a request to reset **their password**
        * An **email with a token** is sent during this action
        """

        args = self.recovery_parser.parse_args()
        user_credentials: UserCredentials = UserCredentials.query.filter(UserCredentials.email == args['email']).first()
        if user_credentials is None:
            # This is a lie
            return "A letter to confirm the password recovery sent to the email"

        password_recovery_token = PasswordRecoveryToken(user_credentials.user_id).encode(exp=timedelta(minutes=10))
        send_password_recovery_email(
            email=user_credentials.email,
            fullname=user_credentials.user.fullname,
            token=password_recovery_token
        )

        return "A letter to confirm the password recovery sent to the email"


@access.route('/password/reset')
class PasswordReset(Resource):
    password_reset_parser = reqparse.RequestParser()
    password_reset_parser.add_argument('token', required=True, type=str, location='form', help=(
        "Token received by the user via email"
    ))
    password_reset_parser.add_argument('password', required=True, type=str, location='form', help="New password")

    @access.expect(password_reset_parser)
    @access.response(HTTPStatus.BAD_REQUEST, description='Bad token')
    @access.response(HTTPStatus.OK, description='Password successfully changed')
    @access.marshal_with(ProfileModel)
    def post(self):
        """
        Password changing

        * User can change **their password**
        """

        args = self.password_reset_parser.parse_args()

        token: PasswordRecoveryToken = PasswordRecoveryToken.decode(args['token'])
        if token is None:
            return abort(HTTPStatus.BAD_REQUEST, message="Bad token")

        user_credentials: UserCredentials = UserCredentials.query.get(token.user_id)
        if user_credentials is None:
            return abort(HTTPStatus.BAD_REQUEST, message="Bad token")

        user_credentials.password = args['password']

        db.session.commit()
        update_user_permissions(user_credentials.user_id)
        return user_credentials.user
