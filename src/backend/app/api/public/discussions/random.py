from http import HTTPStatus

from flask_restplus import Resource, abort
from sqlalchemy import not_
from sqlalchemy.sql import functions

from app.api.models import DiscussionModel
from app.api.namespaces import discussions
from database.models import Discussion


@discussions.route('/random')
class DiscussionRandom(Resource):
    @discussions.marshal_with(DiscussionModel)
    @discussions.response(HTTPStatus.NOT_FOUND, description='No active discussions (not frozen)')
    def get(self):
        """
        Get random discussion

        * User can view a random discussion if it is not frozen
        """

        discussion = Discussion.query.filter(not_(Discussion.is_frozen)).order_by(functions.random()).first()
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message="No available discussions")

        return discussion
