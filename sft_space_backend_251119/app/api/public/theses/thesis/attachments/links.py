from http import HTTPStatus

from flask_restplus import Resource, reqparse, abort

from app.api.models import ThesisAttachmentsModel
from app.api.namespaces import theses
from app.authorization.permissions import UserNeedPermission, EditThesisPermission
from database import db
from database.models import Thesis, Attachment


@theses.route('/<int:{}>/attachments/links'.format('thesis_id'))
@theses.param('thesis_id', description='Thesis identifier')
class ThesisLinkAttachments(Resource):
    attachment_parser = reqparse.RequestParser()
    attachment_parser.add_argument('links[]', required=True, type=str, location='form', action='append', help=(
        'Link attachments'
    ))

    @theses.expect(attachment_parser)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the thesis")
    @theses.marshal_with(ThesisAttachmentsModel)
    def post(self, thesis_id):
        """
        Add link attachment to the thesis

        * User can add new link attachment to **their thesis**
        * User with permission to **"edit theses"** can add new attachment
        """

        thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message='Thesis is not found')

        if not UserNeedPermission(thesis.author_id).can():
            if not EditThesisPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the thesis")
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        args = self.attachment_parser.parse_args()

        attachments = []
        for link in args['links[]']:
            attachments.append(Attachment(
                type='link',
                payload=link
            ))

        thesis.attachments.extend(attachments)
        db.session.commit()

        return {
            'attachments': attachments
        }
