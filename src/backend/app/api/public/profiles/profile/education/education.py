from http import HTTPStatus

from flask import request
from flask_principal import Permission, UserNeed
from flask_restplus import Resource, abort

from app.api.models import ProfileEducationModel
from app.api.namespaces import profiles
from app.authorization.permissions import VerifyEducationPermission
from database import db
from database.models import Education


@profiles.route('/<int:{}>/education'.format('profile_id'))
@profiles.param('profile_id', description="Profile identifier")
class ProfileEducationResource(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to view this profile education")
    @profiles.marshal_with(ProfileEducationModel)
    def get(self, profile_id):
        """
        Get profile education info

        * User can view **their education** info
        * User with permission to **"verify education"** can view education info
        """

        if not Permission(UserNeed(profile_id)).can():
            if not VerifyEducationPermission.can():
                return abort(HTTPStatus.FORBIDDEN, "User is not authorized to view this profile education")

        education = Education.query.get(profile_id)
        if education is None:
            return abort(HTTPStatus.NOT_FOUND, "Education is not found")

        return education

    @profiles.expect(ProfileEducationModel, validate=True)
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to edit this profile education")
    @profiles.marshal_with(ProfileEducationModel)
    def put(self, profile_id):
        """
        Update profile education info

        * User can edit **their education** info
        * User with permission to **"verify education"** can edit the info
        """

        if not Permission(UserNeed(profile_id)).can():
            if not VerifyEducationPermission.can():
                return abort(HTTPStatus.FORBIDDEN, "User is not authorized to edit this profile education")

        payload = request.json

        # Save old scan if it exists
        education = Education.query.get(profile_id)
        if education is not None:
            scan_path = education.scan_path
            db.session.delete(education)
        else:
            scan_path = None

        education = Education(
            user_id=profile_id,
            country=payload['country'],
            city=payload['city'],
            high_school=payload['high_school'],
            faculty=payload['faculty'],
            speciality=payload['speciality'],
            graduation_date=None if payload['graduation_date'] == '' else payload['graduation_date'],
            scan_path=scan_path
        )
        db.session.add(education)
        db.session.commit()

        return education
