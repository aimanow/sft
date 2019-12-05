from http import HTTPStatus

from flask_login import logout_user
from flask_restplus import Resource
from app.api.namespaces import access


@access.route('/logout')
class AccessLogout(Resource):
    @access.response(HTTPStatus.OK, description='User successfully logged out')
    def post(self):
        """
        Log out
        """
        logout_user()
        return "User successfully logged out"
