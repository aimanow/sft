import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ProfileModel
from app.api.namespaces import profiles
from database import db
from database.models import LikedUser, User


@profiles.route('/<int:{}>/likes'.format('profile_id'))
@profiles.param('profile_id', description="Profile identifier")
class ProfileLikes(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @profiles.marshal_with(ProfileModel)
    def post(self, profile_id):
        """
        Toggle like on the profile
        """
        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        profile = User.query.get(profile_id)
        if profile is None:
            return abort(HTTPStatus.NOT_FOUND, message="Profile is not found")

        if not current_user.liked_users_backref.filter_by(liked_user=profile).delete():
            current_user.liked_users_backref.append(LikedUser(
                liked_user=profile,
                liked_at=datetime.datetime.now()
            ))

        db.session.commit()
        return profile
