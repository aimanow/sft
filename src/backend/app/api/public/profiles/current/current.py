from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ProfileModel
from app.api.namespaces import profiles


@profiles.route('/current')
class ProfileCurrent(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @profiles.marshal_with(ProfileModel)
    def get(self):
        """
        Get current authenticated user profile info
        """

        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message='User is anonymous')

        return current_user
