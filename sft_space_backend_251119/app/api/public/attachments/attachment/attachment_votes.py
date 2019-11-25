import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import AttachmentVoteModel
from app.api.namespaces import attachments
from app.authorization.permissions import VoteForAttachmentPermission
from database import db
from database.models import Attachment, AttachmentVote


@attachments.route('/<int:{}>/votes'.format('attachment_id'))
@attachments.param('attachment_id', description='Attachment identifier')
class AttachmentVotesResource(Resource):
    @attachments.expect(AttachmentVoteModel, validate=True)
    @attachments.response(HTTPStatus.FORBIDDEN, description="User is not authorized to vote for the attachment")
    @attachments.marshal_with(AttachmentVoteModel)
    def patch(self, attachment_id):
        """
        Vote for the argument

        * User with permission to **"vote for attachments"** can vote for the attachment if discussion is not frozen
        """

        attachment = Attachment.query.get(attachment_id)
        if attachment is None:
            return abort(HTTPStatus.NOT_FOUND, message='Attachment is not found')

        if not VoteForAttachmentPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to vote for the attachment")
        elif attachment.thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        attachment_vote: AttachmentVote = attachment.votes_backref.filter(AttachmentVote.user == current_user).first()
        if attachment_vote is not None:
            if attachment_vote.vote == payload['my_vote']:
                return attachment.votes
            db.session.delete(attachment_vote)

        attachment.votes_backref.append(AttachmentVote(
            user=current_user,
            vote=payload['my_vote'],
            created_at=datetime.datetime.now()
        ))

        db.session.commit()
        return attachment.votes
