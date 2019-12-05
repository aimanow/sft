import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import DiscussionModel
from app.api.namespaces import discussions
from database import db
from database.models import FavoriteDiscussion, Discussion


@discussions.route('/<int:{}>/favorite'.format("discussion_id"))
@discussions.param('discussion_id', description="Discussion identifier")
class DiscussionFavoriteResource(Resource):
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @discussions.marshal_with(DiscussionModel)
    def post(self, discussion_id):
        """
        Toggle discussion in current user favorites (add / remove)

        * User can add discussion to **their favorites**
        * User can remove discussion from **their favorites**
        """
        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        if not current_user.favorite_discussions_backref.filter_by(favorite_id=discussion_id).delete():
            current_user.favorite_discussions_backref.append(FavoriteDiscussion(
                favorite_id=discussion_id,
                created_at=datetime.datetime.now()
            ))

        db.session.commit()
        return Discussion.query.get(discussion_id)
