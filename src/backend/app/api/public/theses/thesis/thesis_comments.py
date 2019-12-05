import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_restplus import Resource, reqparse, abort

from app.api.models import ThesisPaginationModel, ThesisModel
from app.api.namespaces import theses
from app.authorization.permissions import CreateThesisPermission
from database import db
from database.models import ThesisComment, Thesis, Pagination, ArgumentThesis


@theses.route('/<int:{}>/comments'.format('thesis_id'))
@theses.param('thesis_id', description='Thesis identifier')
class ThesisComments(Resource):
    comments_filter = reqparse.RequestParser()
    comments_filter.add_argument('page', default=1, location='query', type=int, help="Result page number")

    @theses.expect(comments_filter)
    @theses.marshal_with(ThesisPaginationModel)
    def get(self, thesis_id):
        """
        Get comments of the thesis

        * User can view comments of thesis
        * View with pagination
        """

        args = self.comments_filter.parse_args()

        items_per_page = 20
        page_number = args['page']

        if page_number < 1:
            return abort(HTTPStatus.BAD_REQUEST, message="'page' must be > 0")

        items_query = Thesis.query.join(Thesis.comment_backref).filter(
            ThesisComment.thesis_id == thesis_id
        ).order_by(Thesis.created_at.asc())

        total_items = items_query.count()
        items_query = items_query.offset(items_per_page * (page_number - 1)).limit(items_per_page)

        return Pagination(
            page=page_number,
            total_items=total_items,
            items_per_page=items_per_page,
            items=items_query.all()
        )

    @theses.expect(ThesisModel, validate=True)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to create the comment")
    @theses.response(HTTPStatus.BAD_REQUEST, description="User is trying to create a comment on a comment")
    @theses.marshal_with(ThesisModel)
    def post(self, thesis_id):
        """
        Create a new thesis comment

        * User with permission to **"create theses"** can create a new comment
        * **Comment is a thesis**, but user **CANNOT** create a comment on a comment
        """

        thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message="Thesis is not found")

        if not CreateThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message='User is not authorized to create the comment')
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        if thesis.is_comment:
            return abort(HTTPStatus.BAD_REQUEST, message="User is trying to create a comment on a comment")

        payload = request.json

        comment = Thesis(
            author=current_user,
            position=payload['position'],
            message=payload['message'],
            created_at=datetime.datetime.now(),
            comment_backref=ThesisComment(thesis=thesis)
        )
        db.session.add(ArgumentThesis(argument=thesis.argument_thesis.argument, thesis=comment))
        db.session.commit()

        return comment
