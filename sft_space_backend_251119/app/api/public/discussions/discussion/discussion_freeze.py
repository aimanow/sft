import datetime
from http import HTTPStatus

from flask_restplus import Resource, abort

from app.api.models import DiscussionModel
from app.api.namespaces import discussions
from app.authorization.permissions import EditDiscussionPermission
from database import db
from database.models import Discussion, DiscussionFrozen


@discussions.route('/<int:{}>/freeze'.format("discussion_id"))
@discussions.param('discussion_id', description="Discussion identifier")
class DiscussionFreeze(Resource):
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to freeze the discussion")
    @discussions.marshal_with(DiscussionModel)
    def post(self, discussion_id):
        """
        Toggle discussion "is_frozen"

        * User with permission to **"edit discussions"** can freeze the discussion
        * User with permission to **"edit discussions"** can unfreeze the discussion
        """

        if not EditDiscussionPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to freeze the discussion")

        if not DiscussionFrozen.query.filter_by(discussion_id=discussion_id).delete():
            db.session.add(DiscussionFrozen(
                discussion_id=discussion_id,
                frozen_at=datetime.datetime.now()
            ))

        db.session.commit()
        return Discussion.query.get(discussion_id)
