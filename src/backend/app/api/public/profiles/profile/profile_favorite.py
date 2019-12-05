import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ProfileModel
from app.api.namespaces import profiles
from database import db
from database.models import FavoriteUser, User


@profiles.route('/<int:{}>/favorite'.format("profile_id"))
@profiles.param('profile_id', description="Profile identifier")
class ProfileFavorite(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @profiles.marshal_with(ProfileModel)
    def post(self, profile_id):
        """
        Toggle profile in current user favorites (add / remove)

        * User can add profile to **their favorites**
        * User can remove profile from **their favorites**
        """
        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        if not current_user.favorite_users_backref.filter_by(favorite_id=profile_id).delete():
            current_user.favorite_users_backref.append(FavoriteUser(
                favorite_id=profile_id,
                created_at=datetime.datetime.now()
            ))

        db.session.commit()
        return User.query.get(profile_id)
