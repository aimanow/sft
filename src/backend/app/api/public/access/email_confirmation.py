from http import HTTPStatus

from flask_restplus import Resource, reqparse, abort
from app.api.namespaces import access
from app.tokens import EmailConfirmationToken, EmailConfirmationType
from database import db
from database.models import UserCredentials


@access.route('/email/confirm')
class EmailConfirmation(Resource):
    confirmation_parser = reqparse.RequestParser()
    confirmation_parser.add_argument('token', required=True, type=str, location='form', help=(
        "Token received by the user via email"
    ))

    @access.expect(confirmation_parser)
    @access.response(HTTPStatus.BAD_REQUEST, description="Bad confirm token")
    @access.response(HTTPStatus.OK, description="Email successfully confirmed")
    def post(self):
        """
        Email confirmation

        * Confirmation of email **after registration**
        * Confirmation of email **after changing email**
        """

        args = self.confirmation_parser.parse_args()
        token: EmailConfirmationToken = EmailConfirmationToken.decode(args['token'])
        if token is None:
            return abort(HTTPStatus.BAD_REQUEST, message="Bad confirm token")

        user_credentials: UserCredentials = UserCredentials.query.get(token.user_id)
        if user_credentials is None:
            return abort(HTTPStatus.BAD_REQUEST, message="Bad confirm token")

        if token.type is EmailConfirmationType.Registration:
            if user_credentials.email != token.email:
                return abort(HTTPStatus.BAD_REQUEST, message="Bad confirm token")

        elif token.type is EmailConfirmationType.Changing:
            user_credentials.email = token.email

        else:
            raise NotImplementedError

        user_credentials.is_email_confirmed = True

        db.session.commit()
        return "Email successfully confirmed"
