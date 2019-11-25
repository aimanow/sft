from http import HTTPStatus

from flask import request
from flask_principal import Permission, UserNeed
from flask_restplus import Resource, abort

from app.api.models import ArgumentModel
from app.api.namespaces import arguments
from app.authorization.permissions import EditThesisPermission
from database import db
from database.models import Argument, ArgumentAspect


@arguments.route('/<int:{}>'.format('argument_id'))
@arguments.param('argument_id', description='Argument identifier')
class ArgumentResource(Resource):
    @arguments.marshal_with(ArgumentModel)
    def get(self, argument_id):
        """
        Get discussion argument info
        """
        return Argument.query.get(argument_id)

    @arguments.expect(ArgumentModel, validate=True)
    @arguments.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the argument")
    @arguments.marshal_with(ArgumentModel)
    def patch(self, argument_id):
        """
        Edit argument

        * User can edit **their argument** in not frozen discussion
        * User with permission **"edit theses"** can edit the argument
        """

        argument = Argument.query.get(argument_id)
        if argument is None:
            return abort(HTTPStatus.NOT_FOUND, message="Argument is not found")

        if not Permission(UserNeed(argument.thesis.author_id)):
            if not EditThesisPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the argument")
        elif argument.discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        argument.title = payload['title']

        argument_aspect_limit = 3
        ArgumentAspect.query.filter(ArgumentAspect.argument_id == argument_id).delete()
        for aspect_id in payload['aspect_ids'][:argument_aspect_limit]:
            db.session.add(ArgumentAspect(
                argument_id=argument_id,
                aspect_id=aspect_id,
            ))

        argument.thesis.position = payload['thesis']['position']
        argument.thesis.message = payload['thesis']['message']

        db.session.commit()
        return argument

    @arguments.response(HTTPStatus.FORBIDDEN, description="User is not authorized to delete the argument")
    @arguments.response(HTTPStatus.OK, description="Argument successfully deleted")
    def delete(self, argument_id):
        """
        Delete argument

        * User with permission **"edit theses"** can delete the argument
        """

        if not EditThesisPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to delete the argument")

        Argument.query.filter_by(id=argument_id).delete()
        db.session.commit()

        return "Argument successfully deleted"
