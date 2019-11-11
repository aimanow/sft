from http import HTTPStatus

from flask_restplus import Resource, abort

from app.api.models import ClaimModel
from app.api.namespaces import claims
from app.authorization.permissions import ReviewClaimPermission, UserNeedPermission
from database.models import Claim


@claims.route('/<int:{}>'.format('claim_id'))
@claims.param('claim_id', description='Claims identifier')
class ClaimItem(Resource):
    @claims.response(HTTPStatus.FORBIDDEN, description="User is not authorized to view the claim")
    @claims.marshal_with(ClaimModel)
    def get(self, claim_id):
        """
        Get claim info

        * User can view **their claim**
        * User with permission to **"review claims"** can view the claim
        """

        claim = Claim.query.get(claim_id)

        if not ReviewClaimPermission.can():
            if claim is None or not UserNeedPermission(claim.user_id).can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to view the claim")

        if claim is None:
            return abort(HTTPStatus.NOT_FOUND, message="Claim is not found")

        return claim
