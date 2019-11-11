import datetime
from http import HTTPStatus

from flask import request
from flask_principal import UserNeed, Permission
from flask_restplus import Resource, abort
from sqlalchemy.exc import IntegrityError

from app.api.models import ProfileModel
from app.api.namespaces import profiles
from app.authorization.permissions import DeleteUserPermission
from database import db
from database.models import User, UserDeleted


@profiles.route('/<{}>'.format("int:profile_id"))
@profiles.param('profile_id', description="Profile identifier")
class ProfileItem(Resource):
    @profiles.marshal_with(ProfileModel)
    def get(self, profile_id):
        """
        Get profile info
        """

        return User.query.get(profile_id)

    @profiles.expect(ProfileModel, validate=True)
    @profiles.response(HTTPStatus.NOT_FOUND, description="Profile is not found")
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit this profile")
    @profiles.marshal_with(ProfileModel)
    def patch(self, profile_id):
        """
        Update profile info

        * User can update **their profile** information
        """

        if not Permission(UserNeed(profile_id)).can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit this profile")

        profile: User = User.query.get(profile_id)
        if profile is None:
            return abort(HTTPStatus.NOT_FOUND, message="Profile is not found")

        payload = request.json
        profile.fullname = payload['fullname']
        db.session.commit()
        return profile

    @profiles.response(HTTPStatus.FORBIDDEN, description="The current user trying to delete other profile")
    @profiles.response(HTTPStatus.OK, description="Profile successfully deleted")
    def delete(self, profile_id):
        """
        Soft delete the profile

        * User can mark their profile "deleted"
        * User with permission to "delete_users" can delete the profile
        """

        if not Permission(UserNeed(profile_id)).can():
            if not DeleteUserPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="The current user trying to delete other profile")

        db.session.add(UserDeleted(user_id=profile_id, deleted_at=datetime.datetime.now()))
        try:
            db.session.commit()
        except IntegrityError:
            pass

        return "Profile successfully deleted"
