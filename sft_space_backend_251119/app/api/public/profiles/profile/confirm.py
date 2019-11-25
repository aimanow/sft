import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ProfileModel
from app.api.namespaces import profiles
from app.authorization.permissions import ConfirmUserPermission
from database import db
from database.models import User, UserConfirmed


@profiles.route('/<{}>/confirm'.format("int:profile_id"))
@profiles.param('profile_id', description="Profile identifier")
class ProfileConfirmation(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to confirm this profile")
    @profiles.marshal_with(ProfileModel)
    def post(self, profile_id):
        """
        Confirm the profile

        * The user with the permission to **"confirm users"** can set "confirmed"
        """

        user = User.query.get(profile_id)
        if user is None:
            return abort(HTTPStatus.NOT_FOUND)

        if not ConfirmUserPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message='User is not authorized to confirm this profile')

        if not user.is_confirmed:
            db.session.add(UserConfirmed(
                user_id=profile_id,
                reviewer_id=current_user.id,
                confirmed_at=datetime.datetime.now()
            ))
            db.session.commit()
        return user
