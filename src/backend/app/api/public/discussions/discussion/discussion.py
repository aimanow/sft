from http import HTTPStatus

from flask import request
from flask_principal import Permission, UserNeed
from flask_restplus import Resource, abort

from app.api.models import DiscussionModel, ArgumentModel
from app.api.namespaces import discussions
from app.authorization.permissions import EditDiscussionPermission
from database import db
from database.models import Discussion, Argument, Aspect, ArgumentAspect


@discussions.route('/<int:{}>'.format('discussion_id'))
@discussions.param('discussion_id', description='Discussion identifier')
class DiscussionItem(Resource):
    @discussions.marshal_with(DiscussionModel)
    def get(self, discussion_id):
        """
        Get discussion info

        * This action **increases the views count**
        """

        discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message='Discussion is not found')

        discussion.view_count += 1
        db.session.commit()
        return discussion

    @discussions.expect(DiscussionModel)
    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit the discussion")
    @discussions.marshal_with(DiscussionModel)
    def patch(self, discussion_id):
        """
        Edit discussion info

        * User can edit **their discussion** (not frozen)
        * User with permission to **"edit discussions"** can edit the discussion (with frozen discussions)
        """

        discussion = Discussion.query.get(discussion_id)
        if discussion is None:
            return abort(HTTPStatus.NOT_FOUND, message="Discussion is not found")

        if not Permission(UserNeed(discussion.author_id)).can():
            if not EditDiscussionPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to edit the discussion")
        elif discussion.is_frozen:
            return abort(HTTPStatus.FORBIDDEN, message="Discussion is frozen")

        payload = request.json

        if 'lang' in payload:
            discussion.lang = payload['lang']
        if 'title' in payload:
            discussion.title = payload['title']

        if 'aspects' in payload:
            argument = Argument.query.get(payload['argument_id'])
            aspects = Aspect.query.filter(Aspect.id.in_(payload['aspects'])).limit(3).all()
            ArgumentAspect.query.filter_by(argument_id=payload['argument_id']).delete()
            for aspect in aspects:
                db.session.add(ArgumentAspect(
                    argument_id=payload['argument_id'],
                    aspect_id=aspect.id
                ))
        db.session.commit()
        discussion = Discussion.query.get(discussion_id)

        return discussion

    @discussions.response(HTTPStatus.FORBIDDEN, description="User is not authorized to delete the discussion")
    @discussions.response(HTTPStatus.OK, description="Discussion successfully deleted")
    def delete(self, discussion_id):
        """
        Delete the discussion

        * User with permission to **"edit discussions"** can delete the discussion
        """

        if not EditDiscussionPermission.can():
            return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to delete the discussion")

        Discussion.query.filter_by(id=discussion_id).delete()
        db.session.commit()

        return "Discussion successfully deleted"
