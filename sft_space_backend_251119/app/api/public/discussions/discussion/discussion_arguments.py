import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort

from app.api.models import ArgumentPaginationModel, ArgumentModel
from app.api.namespaces import discussions
from app.authorization.permissions import CreateThesisPermission, CreateArgumentPermission
from database import db
from database.models import Argument, Thesis, Discussion, Aspect, ArgumentAspect, Pagination, ArgumentThesis


@discussions.route('/<int:{}>/arguments'.format('discussion_id'))
@discussions.param('discussion_id', description='Discussion identifier')
class DiscussionArgumentList(Resource):
    arguments_filter = reqparse.RequestParser()
    arguments_filter.add_argument('aspects', location='args', type=int, action='append', help="Argument aspects")
    arguments_filter.add_argument('page', default=1, location='args', type=int, help="Result page number")

    @discussions.expect(arguments_filter)
    @discussions.marshal_with(ArgumentPaginationModel)
    def get(self, discussion_id):
        """
        Filter discussion arguments

        * User can view discussion arguments filtered by aspects
        * View with filtration and pagination
        """

        args = self.arguments_filter.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        items_query = Argument.query.filter_by(discussion_id=discussion_id).order_by(Argument.created_at.asc())

        if args['aspects'] is not None:
            items_query = items_query.join(Argument.aspects_backref).filter(
                ArgumentAspect.aspect_id.in_(args['aspects'])
            )

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )

    @discussions.expect(ArgumentModel, validate=True)
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the argument")
    @discussions.marshal_with(ArgumentModel)
    def post(self, discussion_id):
        """
        Create a new discussion argument

        * User with permission to **"create theses"** and **"create arguments"** can create a new argument
        """

        if not CreateArgumentPermission.can() or not CreateThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to create the argument")

        payload = request.json

        discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message="Discussion not found")
        elif discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        aspects = Aspect.query.filter(Aspect.id.in_(payload['aspect_ids'])).limit(3).all()

        created_at = datetime.datetime.now()

        thesis = Thesis(
            author=current_user,
            position=payload['thesis']['position'],
            message=payload['thesis']['message'],
            created_at=created_at
        )

        argument = Argument(
            thesis=thesis,
            discussion_id=discussion_id,
            title=payload['title'],
            created_at=created_at,
            aspects_backref=[ArgumentAspect(aspect=aspect) for aspect in aspects],
        )

        db.session.add(ArgumentThesis(thesis=thesis, argument=argument))
        db.session.commit()

        return argument
