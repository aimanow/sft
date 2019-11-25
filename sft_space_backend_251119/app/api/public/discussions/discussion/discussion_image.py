from http import HTTPStatus

from werkzeug.datastructures import FileStorage
from flask_restplus import Resource, reqparse, abort

from app.api import file_storage
from app.api.namespaces import discussions
from app.authorization.permissions import UserNeedPermission, EditDiscussionPermission
from database import db
from database.models import Discussion


@discussions.route('/<int:{}>/image'.format('discussion_id'), endpoint='discussion_image')
@discussions.param('discussion_id', description='Discussion identifier')
class DiscussionImageResource(Resource):
    @discussions.produces(['image/png'])
    def get(self, discussion_id):
        """
        Get discussion cover image
        """

        discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message='Discussion is not found')

        if discussion.image_path is None:
            return abort(HTTPStatus.NOT_FOUND, message='Discussion cover image is not found')

        return file_storage.download(file_storage.FileCategory.DiscussionImage, discussion.image_path)

    image_payload = reqparse.RequestParser()
    image_payload.add_argument('image', required=True, type=FileStorage, location='files', help="New discussion image")

    @discussions.expect(image_payload)
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the discussion")
    @discussions.response(HTTPStatus.OK, description="Discussion cover image successfully changed")
    def put(self, discussion_id):
        """
        Replace discussion cover image

        * User can replace the image of **their discussion**
        * User with permission to **"edit discussions"** can replace the image
        """

        discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message='Discussion is not found')

        if not UserNeedPermission(discussion.author_id).can():
            if not EditDiscussionPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the discussion")
        elif discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        args = self.image_payload.parse_args()
        token = file_storage.upload(file_storage.FileCategory.DiscussionImage, args['image'])
        discussion.image_path = token.path
        db.session.commit()

        return "Discussion cover image successfully changed"
