from http import HTTPStatus

from flask_principal import Permission, UserNeed
from flask_restplus import Resource, reqparse, abort
from werkzeug.datastructures import FileStorage

from app.api.namespaces import profiles
from app.api import file_storage
from database import db
from database.models import User


@profiles.param('profile_id', description="Profile identifier")
@profiles.route('/<int:{}>/avatar'.format('profile_id'), endpoint='profile_avatar')
class ProfileAvatarResource(Resource):
    @profiles.produces(['image/png'])
    def get(self, profile_id):
        """
        Get profile avatar image
        """

        profile: User = User.query.get(profile_id)
        if profile is None:
            return abort(HTTPStatus.NOT_FOUND, 'Profile is not found')

        if profile.avatar_path is None:
            return abort(HTTPStatus.NOT_FOUND, 'Avatar image is not found')

        return file_storage.download(file_storage.FileCategory.AvatarImage, profile.avatar_path)

    avatar_parser = reqparse.RequestParser()
    avatar_parser.add_argument('avatar', required=True, type=FileStorage, location='files', help="New avatar image")

    @profiles.response(HTTPStatus.FORBIDDEN, description="The current user is trying to change someone else's avatar")
    @profiles.response(HTTPStatus.OK, description="Avatar successfully changed")
    @profiles.expect(avatar_parser, validate=True)
    def put(self, profile_id):
        """
        Change profile avatar image
        """

        if not Permission(UserNeed(profile_id)).can():
            return abort(HTTPStatus.FORBIDDEN, "The current user is trying to change someone else's avatar")

        profile: User = User.query.get(profile_id)
        if profile is None:
            return abort(HTTPStatus.NOT_FOUND, 'Profile is not found')

        args = self.avatar_parser.parse_args()
        token = file_storage.upload(file_storage.FileCategory.AvatarImage, args['avatar'])
        profile.avatar_path = token.path
        db.session.commit()

        return "Avatar successfully changed"
