from http import HTTPStatus

from flask_restplus import Resource, abort

from app.api.models import AttachmentModel
from app.api.namespaces import attachments
from app.authorization.permissions import EditThesisPermission, UserNeedPermission
from database import db
from database.models import Attachment


@attachments.route('/<int:{}>'.format('attachment_id'))
@attachments.param('attachment_id', description='Attachment identifier')
class AttachmentItem(Resource):
    @attachments.marshal_with(AttachmentModel)
    def get(self, attachment_id):
        """
        Get attachment info
        """

        attachment = Attachment.query.get(attachment_id)
        if attachment is None:
            return abort(HTTPStatus.NOT_FOUND, message='Attachment is not found')

        return attachment

    @attachments.response(HTTPStatus.FORBIDDEN, description="User is not authorized to delete the attachment")
    @attachments.response(HTTPStatus.OK, description="Attachment successfully deleted")
    def delete(self, attachment_id):
        """
        Delete attachment

        * User can delete **their attachment** if discussion is not frozen
        * User with permission to **"edit theses"** can delete the attachment
        """

        attachment = Attachment.query.get(attachment_id)
        if attachment is None:
            return abort(HTTPStatus.NOT_FOUND, message='Attachment is not found')

        if not UserNeedPermission(attachment.thesis.author_id):
            if not EditThesisPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to delete the attachment")
        elif attachment.thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        db.session.delete(attachment)
        db.session.commit()

        return "Attachment successfully deleted"
