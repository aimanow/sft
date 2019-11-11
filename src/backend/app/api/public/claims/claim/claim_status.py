import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ClaimStatusModel, ClaimModel
from app.api.namespaces import claims
from app.authorization.permissions import ReviewClaimPermission
from database import db
from database.models import ClaimStatus


@claims.route('/<int:{}>/status'.format('claim_id'))
@claims.param('claim_id', description='Claims identifier')
class ClaimStatusResource(Resource):
    @claims.expect(ClaimStatusModel, validate=True)
    @claims.response(HTTPStatus.FORBIDDEN, description="User is not authorized to update the claim status")
    @claims.marshal_with(ClaimModel)
    def put(self, claim_id):
        """
        Update claim status

        * User with permission to **"review claims"** can update the claim status
        """

        if not ReviewClaimPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to update the claim status")

        payload = request.json

        ClaimStatus.query.filter(ClaimStatus.claim_id == claim_id).delete()
        status = ClaimStatus(
            reviewer=current_user,
            claim_id=claim_id,
            title=payload['title'],
            reason=payload['reason'],
            created_at=datetime.datetime.now()
        )
        db.session.add(status)
        db.session.commit()

        return status.claim
