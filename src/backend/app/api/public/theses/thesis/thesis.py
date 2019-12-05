from http import HTTPStatus

from flask import request
from flask_principal import Permission, UserNeed
from flask_restplus import Resource, abort

from app.api.models import ThesisModel
from app.api.namespaces import theses
from app.authorization.permissions import EditThesisPermission
from database import db
from database.models import Thesis


@theses.route('/<int:{}>'.format('thesis_id'))
@theses.param('thesis_id', description='Thesis identifier')
class ThesisResource(Resource):
    @theses.marshal_with(ThesisModel)
    def get(self, thesis_id):
        """
        Get thesis
        """
        return Thesis.query.get(thesis_id)

    @theses.expect(ThesisModel, validate=True)
    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the thesis")
    @theses.marshal_with(ThesisModel)
    def patch(self, thesis_id):
        """
        Edit thesis

        * User can edit **their thesis**
        * User with permission to **"edit theses"** can edit the thesis
        """

        thesis: Thesis = Thesis.query.get(thesis_id)
        if thesis is None:
            return abort(HTTPStatus.NOT_FOUND, message="Thesis is not found")

        if not Permission(UserNeed(thesis.author_id)):
            if not EditThesisPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the thesis")
        elif thesis.argument_thesis.argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        thesis.position = payload['position']
        thesis.message = payload['message']

        db.session.commit()
        return thesis

    @theses.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the thesis")
    @theses.response(HTTPStatus.OK, description="Thesis successfully deleted")
    def delete(self, thesis_id):
        """
        Delete thesis

        * User with permission to **"edit theses"** can delete the thesis
        """

        if not EditThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the thesis")

        if not Thesis.query.filter_by(id=thesis_id).delete():
            return abort(HTTPStatus.NOT_FOUND, message="Thesis is not found")

        db.session.commit()
        return "Thesis successfully deleted"
