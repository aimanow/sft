from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, reqparse, abort
from app.api.namespaces import profiles
from database import db
from database.models import UserCredentials


@profiles.route(f'/current/security/password')
class ProfileSecurityPassword(Resource):

    security_password_parser = reqparse.RequestParser()
    security_password_parser.add_argument('old_password', location='form', required=True, type=str, help='Old password')
    security_password_parser.add_argument('new_password', location='form', required=True, type=str, help='New password')

    @profiles.expect(security_password_parser)
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @profiles.response(HTTPStatus.OK, description="Password successfully changed")
    def post(self):
        """
        Change profile password

        * User can change **their password**
        """

        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        args = self.security_password_parser.parse_args()

        user_credentials: UserCredentials = UserCredentials.query.get(current_user.id)
        if user_credentials is None or not user_credentials.check_password(args['old_password']):
            return abort(HTTPStatus.FORBIDDEN, message="Wrong password")

        user_credentials.password = args['new_password']

        db.session.commit()
        return "Password successfully changed"
