from http import HTTPStatus

from flask import request
from flask_restplus import Resource, abort

from app.api.models import AspectModel
from app.api.namespaces import aspects
from app.authorization.permissions import EditAspectPermission
from database import db
from database.models import Aspect


@aspects.route('/<int:{}>'.format('aspect_id'))
@aspects.param('aspect_id', description='Aspect identifier')
class AspectResource(Resource):
    @aspects.marshal_with(AspectModel)
    def get(self, aspect_id):
        """
        Get aspect info
        """

        return Aspect.query.get(aspect_id)

    @aspects.expect(AspectModel, validate=True)
    @aspects.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the aspect")
    @aspects.marshal_with(AspectModel)
    def patch(self, aspect_id):
        """
        Edit aspect info

        * User with permission **"edit aspects"** can edit the aspect
        """

        if not EditAspectPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the aspect")

        aspect = Aspect.query.get(aspect_id)
        if aspect is None:
            return abort(HTTPStatus.NOT_FOUND, message="Aspect is not found")

        payload = request.json

        aspect.title = payload['title']
        db.session.commit()
        return aspect

    @aspects.response(HTTPStatus.FORBIDDEN, description="User is not authorized to delete the aspect")
    @aspects.response(HTTPStatus.OK, description="Aspect successfully deleted")
    def delete(self, aspect_id):
        """
        Delete aspect

        * User with permission **"edit aspects"** can delete the aspect
        """

        if not EditAspectPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to delete the aspect")

        Aspect.query.filter_by(id=aspect_id).delete()
        db.session.commit()

        return "Aspect successfully deleted"
