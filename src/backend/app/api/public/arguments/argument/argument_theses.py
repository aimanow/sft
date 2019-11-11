import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort
from sqlalchemy import not_

from app.api.models import ThesisPaginationModel, ThesisModel
from app.api.namespaces import arguments
from app.authorization.permissions import CreateThesisPermission
from database import db
from database.models import Thesis, ArgumentThesis, Pagination, Argument


@arguments.route('/<int:{}>/theses'.format('argument_id'))
@arguments.param('argument_id', description="Argument identifier")
class ArgumentThesesResource(Resource):
    theses_filter = reqparse.RequestParser()
    theses_filter.add_argument('page', default=1, location='args', type=int, help="Result page number")

    @arguments.expect(theses_filter)
    @arguments.marshal_with(ThesisPaginationModel)
    def get(self, argument_id):
        """
        Get all argument theses

        * User can view theses of argument
        * View with pagination
        """

        args = self.theses_filter.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        items_query = Thesis.query.join(Thesis.argument_thesis).filter(
            ArgumentThesis.argument_id == argument_id, not_(Thesis.is_comment)
        ).order_by(Thesis.created_at.asc())

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )

    @arguments.expect(ThesisModel, validate=True)
    @arguments.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the thesis")
    @arguments.marshal_with(ThesisModel)
    def post(self, argument_id):
        """
        Create a new argument thesis

        * User with permission to **"create theses"** can create a new thesis (in argument of not frozen discussion)
        """

        argument = Argument.query.get(argument_id)
        if argument is None:
            return abort(HTTPStatus.NOT_FOUND, message='Argument is not found')

        if not CreateThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to create the thesis")
        elif argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json
        thesis = Thesis(
            author=current_user,
            position=payload['position'],
            message=payload['message'],
            created_at=datetime.datetime.now(),
        )
        db.session.add(ArgumentThesis(argument=argument, thesis=thesis))
        db.session.commit()

        return thesis
