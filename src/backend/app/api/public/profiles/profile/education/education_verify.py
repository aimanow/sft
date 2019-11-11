import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import ProfileEducationModel
from app.api.namespaces import profiles
from app.authorization.permissions import VerifyEducationPermission
from database import db
from database.models import Education, EducationVerified


@profiles.route('/<int:{}>/education/verify'.format('profile_id'))
@profiles.param('profile_id', description="Profile identifier")
class ProfileEducationVerifyResource(Resource):
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to verify the education")
    @profiles.marshal_with(ProfileEducationModel)
    def post(self, profile_id):
        """
        Verify education

        * User with permission to **"verify education"** can verify the education
        """

        if not VerifyEducationPermission.can():
            return abort(HTTPStatus.FORBIDDEN, "User is not authorized to verify the education")

        education = Education.query.get(profile_id)
        if education is None:
            return abort(HTTPStatus.NOT_FOUND, "Education is not found")

        if not education.is_verified:
            education.verified_backref = EducationVerified(
                reviewer=current_user,
                verified_at=datetime.datetime.now()
            )
            db.session.commit()

        return education
