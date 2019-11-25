from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, reqparse, abort

from app.api.models import ClaimPaginationModel
from app.api.namespaces import claims
from app.authorization.permissions import ReviewClaimPermission
from database.models import Claim, Pagination


@claims.route('')
class ClaimList(Resource):
    claims_filter = reqparse.RequestParser()
    claims_filter.add_argument('thesis', type=int, action='append', location='args', help="Filter claims by thesis id")
    claims_filter.add_argument('page', type=int, default=1, location='args', help="Result page number")

    @claims.expect(claims_filter)
    @claims.response(HTTPStatus.FORBIDDEN, description="User is not authorized to view the claims")
    @claims.marshal_with(ClaimPaginationModel)
    def get(self):
        """
        Get claim list

        * User can view **their claims**
        * User with permission to **"review claims"** can view the claims
        """

        args = self.claims_filter.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        if ReviewClaimPermission.can():
            items_query = Claim.query

        elif not current_user.is_anonymous:
            items_query = current_user.claims_backref

        else:
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to view the claims")

        items_query = items_query.order_by(Claim.created_at.desc())
        if args['thesis']:
            items_query = items_query.filter(Claim.thesis_id.in_(args['thesis']))

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )
