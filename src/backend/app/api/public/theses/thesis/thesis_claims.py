import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ClaimModel
from app.api.namespaces import theses
from app.authorization.permissions import CreateClaimPermission
from database import db
from database.models import Claim, Thesis


@theses.route('/<int:{}>/claims'.format('thesis_id'))
@theses.param('thesis_id', description="Thesis identifier")
class ThesisClaimsResource(Resource):
    @theses.expect(ClaimModel, validate=True)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the claim")
    @theses.marshal_with(ClaimModel)
    def post(self, thesis_id):
        """
        Create a new claim

        * User with permission to **"create claims"** can create the claim
        """

        thesis: Thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message="Thesis is not found")

        if not CreateClaimPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to create the claim")
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        claim = Claim(
            user=current_user,
            thesis=thesis,
            message=payload['message'],
            created_at=datetime.datetime.now()
        )
        db.session.add(claim)
        db.session.commit()

        return claim
