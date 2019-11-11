import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import DiscussionVotesModel
from app.api.namespaces import discussions
from app.authorization.permissions import VoteForAttachmentPermission
from database import db
from database.models import Discussion, DiscussionVote


@discussions.route('/<int:{}>/votes'.format('discussion_id'))
@discussions.param('discussion_id', description='Discussion identifier')
class DiscussionVotes(Resource):
    @discussions.expect(DiscussionVotesModel, validate=True)
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to vote for the discussion")
    @discussions.marshal_with(DiscussionVotesModel)
    @discussions.deprecated
    def patch(self, discussion_id):
        """
        Vote in the discussion

        * User with permission to **"vote for discussions"** can vote for the not frozen discussion
        """

        discussion: Discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message='Discussion is not found')

        if not VoteForAttachmentPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to vote for the discussion")
        elif discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        discussion_vote: DiscussionVote = discussion.votes_backref.filter(DiscussionVote.user == current_user).first()
        if discussion_vote is not None:
            if discussion_vote.vote == payload['my_vote']:
                return discussion.votes
            db.session.delete(discussion_vote)

        discussion.votes_backref.append(DiscussionVote(
            user=current_user,
            vote=payload['my_vote'],
            created_at=datetime.datetime.now(),
        ))

        db.session.commit()
        return discussion.votes
