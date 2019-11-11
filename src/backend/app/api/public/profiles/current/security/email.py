from datetime import timedelta
from http import HTTPStatus

from flask import redirect
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort
from app.api.namespaces import profiles
from app.mails import send_email_changing_email
from app.tokens import EmailConfirmationToken, EmailConfirmationType


@profiles.route(f'/current/security/email')
class ProfileSecurityEmail(Resource):
    security_email_parser = reqparse.RequestParser()
    security_email_parser.add_argument('email', location='form', required=True, type=str, help='New email address')
    security_email_parser.add_argument('redirect', location='args', type=str, help='Frontend redirect url')

    @profiles.expect(security_email_parser)
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @profiles.response(HTTPStatus.FOUND, description=(
        "A confirmation letter is sent to the new email address. "
        "Redirect to `?redirect=...` from query params"
    ))
    @profiles.response(HTTPStatus.OK, description=(
        "A confirmation letter is sent to the new email address. "
        "No redirect url provided"
    ))
    def post(self):
        """
        Change profile email

        * User can change **their email**
        """

        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        args = self.security_email_parser.parse_args()

        email_changing_token = EmailConfirmationToken(EmailConfirmationType.Changing, current_user.id, args['email'])
        send_email_changing_email(
            email=args['email'],
            fullname=current_user.fullname,
            token=email_changing_token.encode(exp=timedelta(minutes=10))
        )

        if args['redirect']:
            return redirect(args['redirect'], code=HTTPStatus.FOUND)

        return "A confirmation letter is sent to the new email address"
