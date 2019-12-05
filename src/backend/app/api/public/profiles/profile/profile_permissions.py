import datetime
from http import HTTPStatus

from flask import request
from flask_login import current_user
from flask_principal import ActionNeed
from flask_restplus import Resource, abort

from app.api.models import PermissionModel, ProfilePermissionsModel
from app.api.namespaces import profiles
from app.authorization.permissions import DEFAULT_ACTIONS, SPECIAL_ACTIONS
from app.authorization.permissions import EditDefaultRightPermission, EditSpecialRightPermission
from database import db
from database.models import User, ProfilePermission


@profiles.route('/<int:{}>/permissions'.format('profile_id'))
@profiles.param('profile_id', description="Profile identifier")
class ProfilePermissionResource(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to view the permissions")
    @profiles.marshal_with(ProfilePermissionsModel)
    def get(self, profile_id):
        """
        Get profile permissions

        * User can view all **their allowed** permissions
        * User with permission to **"edit default rights"** can view user permissions from **default list**
        * User with permission to **"edit special rights"** can view user permissions from **special list**
        """

        if not EditDefaultRightPermission.can() and not EditSpecialRightPermission.can():
            if current_user.id == profile_id:
                # View all default permissions and only allowed special permissions
                permissions = {action.value: True for action in DEFAULT_ACTIONS}
                permissions.update({
                    p.name: p.is_allowed for p in current_user.permissions_backref.all()
                    if p.is_allowed or ActionNeed(p.name) in DEFAULT_ACTIONS
                })
            else:
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to view the permissions")
        else:
            permissions = {}
            profile = User.query.get(profile_id)
            if not profile:
                return abort(HTTPStatus.NOT_FOUND, message='Profile is not found')

            profile_permissions = profile.permissions_backref.all()

            if EditDefaultRightPermission.can():
                # Add all default permissions to the result
                permissions.update({
                    action.value: True
                    for action in DEFAULT_ACTIONS
                })
                permissions.update({
                    p.name: p.is_allowed
                    for p in profile_permissions if ActionNeed(p.name) in DEFAULT_ACTIONS
                })

            if EditSpecialRightPermission.can():
                # Add all special permissions to the result
                permissions.update({
                    action.value: False
                    for action in SPECIAL_ACTIONS
                })
                permissions.update({
                    p.name: p.is_allowed
                    for p in profile_permissions if ActionNeed(p.name) in SPECIAL_ACTIONS
                })

        return {
            'permissions': [
                {'name': name, 'is_allowed': is_allowed}
                for name, is_allowed in permissions.items()
            ]
        }

    @profiles.expect(PermissionModel, validate=True)
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to manage the permission")
    @profiles.marshal_with(PermissionModel)
    def post(self, profile_id):
        """
        Allow or deny profile permissions

        * User with permission to **"edit default rights"** can allow / deny user permissions from **default list**
        * User with permission to **"edit special rights"** can allow / deny user permissions from **special list**
        """

        profile = User.query.get(profile_id)
        if not profile:
            return abort(HTTPStatus.NOT_FOUND, message='Profile is not found')

        payload = request.json
        need = ActionNeed(payload['name'])

        if need in DEFAULT_ACTIONS:
            is_special = False
            if not EditDefaultRightPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to manage the permission")

        elif need in SPECIAL_ACTIONS:
            is_special = True
            if not EditSpecialRightPermission.can():
                return abort(HTTPStatus.FORBIDDEN, message="User is not authorized to manage the permission")

        else:
            return abort(HTTPStatus.BAD_REQUEST, message="Undefined permission name")

        profile.permissions_backref.filter(ProfilePermission.name == need.value).delete()
        if is_special is payload['is_allowed']:
            profile.permissions_backref.append(ProfilePermission(
                name=need.value,
                user_id=profile_id,
                is_allowed=payload['is_allowed'],
                granted_at=datetime.datetime.now()
            ))

        db.session.commit()
        return {
            'name': need.value,
            'is_allowed': payload['is_allowed']
        }
