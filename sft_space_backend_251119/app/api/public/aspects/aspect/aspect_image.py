from http import HTTPStatus

from flask_restplus import Resource, reqparse, abort
from werkzeug.datastructures import FileStorage

from app.api import file_storage
from app.api.namespaces import aspects
from app.authorization.permissions import EditAspectPermission
from database import db
from database.models import Aspect


@aspects.route('/<int:{}>/image'.format('aspect_id'), endpoint='aspect_image')
@aspects.param('aspect_id', description='Aspect identifier')
class AspectImageResource(Resource):
    @aspects.produces(['image/png'])
    def get(self, aspect_id):
        """
        Get aspect image
        """

        aspect = Aspect.query.get(aspect_id)
        if aspect is None:
            return abort(HTTPStatus.NOT_FOUND, message='Aspect is not found')

        if aspect.image_path is None:
            return abort(HTTPStatus.NOT_FOUND, 'Aspect image is not found')

        return file_storage.download(file_storage.FileCategory.AspectImage, aspect.image_path)

    image_payload = reqparse.RequestParser()
    image_payload.add_argument('image', required=True, type=FileStorage, location='files', help="New aspect image")

    @aspects.expect(image_payload)
    @aspects.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the aspect")
    @aspects.response(HTTPStatus.OK, description="Aspect image successfully changed")
    def put(self, aspect_id):
        """
        Replace aspect image

        * User can set the aspect image **if it does not exists**.
        This is done to set the image after creating the aspect
        * User with permission to **"edit aspects"** can replace the aspect image
        """

        aspect = Aspect.query.get(aspect_id)
        if aspect is None:
            return abort(HTTPStatus.NOT_FOUND, message='Aspect is not found')

        if aspect.image_path is not None:
            if not EditAspectPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the aspect")

        args = self.image_payload.parse_args()
        token = file_storage.upload(file_storage.FileCategory.AspectImage, args['image'])
        aspect.image_path = token.path
        db.session.commit()

        return "Aspect image successfully changed"
