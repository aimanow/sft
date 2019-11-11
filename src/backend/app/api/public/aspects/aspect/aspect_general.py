from http import HTTPStatus

from flask_restplus import Resource, abort

from app.api.models import AspectModel
from app.api.namespaces import aspects
from app.authorization.permissions import EditAspectPermission
from database import db
from database.models import Aspect, AspectGeneral


@aspects.route('/<int:{}>/general'.format('aspect_id'))
@aspects.param('aspect_id', description='Aspect identifier')
class AspectGeneralResource(Resource):
    @aspects.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the aspect")
    @aspects.marshal_with(AspectModel)
    def post(self, aspect_id):
        """
        Toggle aspect "is_general"

        * User with permission **"edit aspects"** can add the aspect to the general list of aspects
        * User with permission **"edit aspects"** can remove the aspect from the general list of aspects
        """

        if not EditAspectPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the aspect")

        if not AspectGeneral.query.filter_by(aspect_id=aspect_id).delete():
            db.session.add(AspectGeneral(
                aspect_id=aspect_id
            ))

        db.session.commit()
        return Aspect.query.get(aspect_id)
