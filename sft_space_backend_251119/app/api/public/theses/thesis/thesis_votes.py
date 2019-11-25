import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ThesisVotesModel, UserThesisVoteModel
from app.api.namespaces import theses
from app.authorization.permissions import VoteForThesisPermission
from database import db
from database.models import Thesis, ThesisVote


@theses.route('/<int:{}>/votes'.format('thesis_id'))
@theses.param('thesis_id', description='Thesis identifier')
class ThesisVotesResource(Resource):
    @theses.expect(UserThesisVoteModel, validate=True)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to vote for the thesis")
    @theses.marshal_with(ThesisVotesModel)
    def patch(self, thesis_id):
        """
        Vote for the thesis

        * User with permission to **"vote for theses"** can vote for the thesis
        """

        thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message='Thesis is not found')

        if not VoteForThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message='User is not authorized to vote for the thesis')
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        now = datetime.datetime.now()

        thesis.votes_backref.filter(ThesisVote.user == current_user).delete()
        flood_divider = 1 + ThesisVote.query.filter(ThesisVote.user == current_user).filter(
            ThesisVote.created_at > now - datetime.timedelta(hours=1),
        ).count()

        thesis.votes_backref.append(
            ThesisVote(
                user=current_user,
                value_x=payload['x'],
                value_y=payload['y'],
                flood_divider=flood_divider,
                created_at=now
            )
        )

        db.session.commit()
        return thesis.votes
