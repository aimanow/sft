import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort
from sqlalchemy import desc

from app.api.models import DiscussionPaginationModel, DiscussionModel
from app.api.namespaces import discussions
from database import db
from database.models import FavoriteDiscussion, Discussion, Pagination
from app.authorization.permissions import CreateArgumentPermission, CreateThesisPermission


@discussions.route('')
class DiscussionList(Resource):
    discussions_filter = reqparse.RequestParser()
    discussions_filter.add_argument('q', type=str, location='args', help="Discussion search keyword")
    discussions_filter.add_argument('author', type=int, location='args', help="Discussion author id")
    discussions_filter.add_argument('location', type=str, location='args', help="Search location", **dict(
        choices=['all', 'favorites'], default='all',
    ))
    discussions_filter.add_argument('sort', type=str, location='args', help="Result sort type", **dict(
        choices=['last', 'popular', 'popular_today'], default='last',
    ))
    discussions_filter.add_argument('page', default=1, location='args', type=int, help="Result page number")

    @discussions.expect(discussions_filter)
    @discussions.marshal_with(DiscussionPaginationModel)
    def get(self):
        """
        Filter discussions

        * User can view **their favorite** discussions
        * User can view all discussions
        * User can view **discussions of the day** with sort=popular_today
        * View with filtration and pagination
        """

        args = self.discussions_filter.parse_args()

        items_per_page = 20
        total_items = 0
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        if args['location'] == 'all' and args['q'] is not None:
            # Discussion.reindex()

            items_query, total_items = Discussion.search(args['q'], int(page_number), items_per_page)

            if args['sort'] == 'popular':
                items_query = items_query.order_by(desc(Discussion.rating))
            elif args['sort'] == 'popular_today':
                items_query = items_query.order_by(desc(Discussion.today_rating))
            else:
                items_query = items_query.order_by(Discussion.created_at.desc())
        elif args['location'] == 'all':
            items_query = Discussion.query
        else:
            if current_user.is_anonymous:
                return Pagination(items_per_page=items_per_page, items=[])
            items_query = Discussion.query.join(Discussion.favorite_by_backref).filter(
                FavoriteDiscussion.user_id == current_user.id
            )

        if args['author'] is not None:
            items_query = items_query.filter(Discussion.author_id == args['author'])

        if args['sort'] == 'popular':
            items_query = items_query.order_by(desc(Discussion.rating))
        elif args['sort'] == 'popular_today':
            items_query = items_query.order_by(desc(Discussion.today_rating))
        else:
            items_query = items_query.order_by(Discussion.created_at.desc())

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )

    @discussions.expect(DiscussionModel, validate=True)
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the discussion")
    @discussions.marshal_with(DiscussionModel)
    def post(self):
        """
        Create a new discussion

        * User with permission to **"create arguments"** and **"create theses"** can create a new discussion
        """

        if not CreateArgumentPermission.can() or not CreateThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to create the discussion")

        payload = request.json

        discussion = Discussion(
            author=current_user,
            lang=payload['lang'],
            title=payload['title'],
            created_at=datetime.datetime.now()
        )
        db.session.add(discussion)
        db.session.commit()

        return discussion
