from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, reqparse, abort

from app.api.models import ProfilePaginationModel
from app.api.namespaces import profiles
from database.models import User, FavoriteUser, Pagination


@profiles.route('')
class ProfileList(Resource):
    profile_filter_parser = reqparse.RequestParser()
    profile_filter_parser.add_argument('q', location='args', type=str, help="Profile search keyword")
    profile_filter_parser.add_argument('location', type=str, location='args', help="Search location", **dict(
        choices=['all', 'favorites'], default='all',
    ))
    profile_filter_parser.add_argument('page', location='args', type=int, default=1, help="Result page number")

    @profiles.expect(profile_filter_parser)
    @profiles.marshal_with(ProfilePaginationModel)
    def get(self):
        """
        Filter profiles

        * User can view **their favorite** profiles
        * User can view **all** profiles
        * View with filtration and pagination
        """
        args = self.profile_filter_parser.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        if args['location'] == 'all':
            items_query = User.query
        else:
            if current_user.is_anonymous:
                return Pagination(items_per_page=items_per_page, items=[])
            items_query = User.query.join(User.favorite_by_backref).filter(
                FavoriteUser.user_id == current_user.id
            )

        if args['q'] is not None:
            items_query = items_query.filter(User.fullname.ilike(f"%{args['q']}%"))

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )
