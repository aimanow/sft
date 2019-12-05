import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort
from sqlalchemy import desc

from app.api.models import AspectPaginationModel, AspectModel
from app.api.namespaces import aspects
from app.authorization.permissions import CreateAspectPermission
from database import db
from database.models import Pagination, Aspect, FavoriteAspect, ArgumentAspect, Argument


@aspects.route('')
class AspectList(Resource):
    aspect_filter_parser = reqparse.RequestParser()
    aspect_filter_parser.add_argument('q', location='args', type=str, help="Aspect search keyword")
    aspect_filter_parser.add_argument('discussion', location='args', type=int, help="Discussion id")
    aspect_filter_parser.add_argument('location', type=str, location='args', help="Search location", **dict(
        choices=['all', 'favorites'], default='all',
    ))
    aspect_filter_parser.add_argument('page', location='args', type=int, default=1, help="Result page number")

    @aspects.expect(aspect_filter_parser)
    @aspects.marshal_with(AspectPaginationModel)
    def get(self):
        """
        Filter aspects

        * User can view **their favorite** aspects
        * User can view **all available** aspects
        * View with filtration and pagination
        """

        args = self.aspect_filter_parser.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        if args['location'] == 'all':
            items_query = Aspect.query
        else:
            if current_user.is_anonymous:
                return Pagination(items_per_page=items_per_page, items=[])
            items_query = Aspect.query.join(Aspect.favorite_by_backref).filter(
                FavoriteAspect.user_id == current_user.id
            )

        if args['q'] is not None:
            items_query = items_query.filter(Aspect.title.ilike(f"%{args['q']}%"))

        if args['discussion'] is not None:
            items_query = items_query.join(ArgumentAspect).join(Argument).filter(
                Argument.discussion_id == args['discussion']
            )

        count_query = items_query

        if current_user.is_anonymous:
            items_query = items_query.order_by(
                desc(Aspect.is_general),
                Aspect.title.asc()
            )
        else:
            items_query = items_query.outerjoin(Aspect.favorite_by_backref).order_by(
                FavoriteAspect.user_id == current_user.id,
                desc(Aspect.is_general),
                Aspect.title.asc()
            )

        total_items = count_query.order_by(Aspect.id).distinct(Aspect.id).count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )

    @aspects.expect(AspectModel, validate=True)
    @aspects.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the aspect")
    @aspects.marshal_with(AspectModel)
    def post(self):
        """
        Create a new aspect

        * User with permission to **"create aspects"** can create a new aspect
        * **Don't forget** to set the aspect image on frontend using `PUT http://.../aspects/{aspect_id}/image`
        """

        if not CreateAspectPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to create the aspect")

        payload = request.json

        aspect = Aspect(
            title=payload['title'],
            created_at=datetime.datetime.now()
        )
        db.session.add(aspect)
        db.session.commit()

        return aspect
