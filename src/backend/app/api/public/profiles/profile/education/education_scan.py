from http import HTTPStatus

from flask_restplus import Resource, abort, reqparse
from werkzeug.datastructures import FileStorage

from app.api import file_storage
from app.api.namespaces import profiles
from app.authorization.permissions import UserNeedPermission, VerifyEducationPermission
from database import db
from database.models import Education


@profiles.route('/<int:{}>/education/scan'.format('profile_id'), endpoint='education_scan')
@profiles.param('profile_id', description="Profile identifier")
class ProfileEducationScanResource(Resource):
    @profiles.produces(['image/png'])
    def get(self, profile_id):
        """
        View education scan

        * User can view **their education** scan
        * User with permission to **"verify education"** can view the education scan
        """

        if not VerifyEducationPermission.can():
            if not UserNeedPermission(profile_id):
                return abort(HTTPStatus.FORBIDDEN, "User is not authorized to view the education scan")

        education = Education.query.get(profile_id)
        if education is None:
            return abort(HTTPStatus.NOT_FOUND, "Education is not found")

        if education.scan_path is None:
            return abort(HTTPStatus.NOT_FOUND, 'Education scan is not found')

        return file_storage.download(file_storage.FileCategory.EducationScan, education.scan_path)

    scan_image_parser = reqparse.RequestParser()
    scan_image_parser.add_argument('scan', required=True, type=FileStorage, location='files', help="New scan image")

    @profiles.expect(scan_image_parser)
    @profiles.response(HTTPStatus.FORBIDDEN, description="User is not authorized to verify the education")
    @profiles.response(HTTPStatus.OK, description="Education scan successfully changed")
    def put(self, profile_id):
        """
        Replace education scan image

        * User can update **their education** scan
        * User with permission to **"verify education"** can update the scan
        """

        if not VerifyEducationPermission.can():
            if not UserNeedPermission(profile_id).can():
                return abort(HTTPStatus.FORBIDDEN, "User is not authorized to edit the education")

        education = Education.query.get(profile_id)
        if education is None:
            return abort(HTTPStatus.NOT_FOUND, "Education is not found")

        args = self.scan_image_parser.parse_args()
        token = file_storage.upload(file_storage.FileCategory.EducationScan, args['scan'])
        education.scan_path = token.path

        if education.is_verified:
            db.session.delete(education.verified_backref)

        db.session.commit()
        return 'Education scan successfully changed'
