from http import HTTPStatus

from flask_restplus import Resource, reqparse
from werkzeug.datastructures import FileStorage

from app.api.namespaces import feedback
from app.mails import send_feedback


@feedback.route('')
class Feedback(Resource):
    feedback_parser = reqparse.RequestParser()
    feedback_parser.add_argument('name', required=True, type=str, location='form', help='Name')
    feedback_parser.add_argument('email', required=True, type=str, location='form', help='Reply email')
    feedback_parser.add_argument('topic', required=True, choices=['offer', 'claim', 'wish'], location='form', help=(
        'Feedback topic'
    ))
    feedback_parser.add_argument('message', required=True, type=str, location='form', help="Feedback message")
    feedback_parser.add_argument('file', type=FileStorage, location='files', help="Attachment")

    @feedback.expect(feedback_parser)
    @feedback.response(HTTPStatus.OK, description='Feedback successfully sent')
    def post(self):
        """
        Feedback form

        * Send feedback to info@sft.space
        """

        args = self.feedback_parser.parse_args()
        send_feedback(
            from_email=args['email'],
            name=args['name'],
            topic=args['topic'],
            message=args['message'],
            attachment=args['file']
        )

        return "Feedback successfully sent"
