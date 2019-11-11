from http import HTTPStatus

from flask_restplus import Resource, reqparse, abort
from werkzeug.datastructures import FileStorage

from app.api import file_storage
from app.api.models import ThesisAttachmentsModel
from app.api.namespaces import theses
from app.authorization.permissions import UserNeedPermission, EditThesisPermission
from database import db
from database.models import Thesis, Attachment


@theses.route('/<int:{}>/attachments/files'.format('thesis_id'))
@theses.param('thesis_id', description='Thesis identifier')
class ThesisFileAttachmentResource(Resource):
    attachment_parser = reqparse.RequestParser()
    attachment_parser.add_argument('files[]', required=True, type=FileStorage, location='files', help=(
        'File attachments'
    ))

    real_attachment_parser = reqparse.RequestParser()
    real_attachment_parser.add_argument('files[]', required=True, type=FileStorage, location='files', action='append')

    @theses.expect(attachment_parser)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the thesis")
    @theses.marshal_with(ThesisAttachmentsModel)
    def post(self, thesis_id):
        """
        Add file attachment to the thesis

        * User can add new file attachment to **their thesis**
        * User with permission to **"edit theses"** can add new attachment

        **NOTICE: Swagger UI contains a bug.
        If you send several files via Swagger UI, then the strings '[object File]' come to the server, not the files.
        Sending multiple files tested via Postman.**
        """

        thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message='Thesis is not found')

        if not UserNeedPermission(thesis.author_id).can():
            if not EditThesisPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the thesis")
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        args = self.real_attachment_parser.parse_args()

        attachments = []
        for file in args['files[]']:
            attachments.append(Attachment(
                type='file',
                payload=file_storage.upload(file_storage.FileCategory.Attachment, file).path
            ))

        thesis.attachments.extend(attachments)
        db.session.commit()

        return {
            'attachments': attachments
        }
