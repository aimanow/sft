import requests
import json
import datetime
import random

PASSWORD_SEED = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
RANDOM_PASSWORD_LEN = 16

from http import HTTPStatus

from flask_login import login_user
from flask_restplus import Resource, reqparse, abort
from sqlalchemy.orm.exc import NoResultFound

from app.api.models import ProfileModel
from app.api.namespaces import access
from app.authorization.permissions import update_user_permissions
from database.models import UserCredentials, User
from database import db
from sqlalchemy.exc import IntegrityError

VK_ID = '7199975'
VK_SECRET = 'Mgp5TOAq2iebJkR6mm5N'
VK_REDIRECT = 'https://sft.space/oauth/vk'

GOOGLE_ID = '148084958804-dkk0uf9jai6lufivefuegtnu4oidt2cf.apps.googleusercontent.com'
GOOGLE_SECRET = 'HrezXyPrXmD85ebaXUYO55Db'
GOOGLE_REDIRECT = 'https://sft.space/oauth/google'

FACEBOOK_ID = '403797927239132'
FACEBOOK_SECRET = '05580c65057f0d91239d5f1a191ade9c'
FACEBOOK_REDIRECT = 'https://sft.space/oauth/facebook'


@access.route('/auth')
class PasswordAuthentication(Resource):
    auth_parser = reqparse.RequestParser()
    auth_parser.add_argument('email', required=False, type=str, location='form', help="User email")
    auth_parser.add_argument('password', required=False, type=str, location='form', help="User password")
    auth_parser.add_argument('oauth', required=False, type=str, location='form', help="OAuth code")
    auth_parser.add_argument('provider', required=False, type=str, location='form', help="OAuth provider")

    @access.expect(auth_parser)
    @access.response(HTTPStatus.FORBIDDEN, description='Wrong email or password')
    @access.response(HTTPStatus.OK, description='User successfully authenticated')
    @access.marshal_with(ProfileModel)
    def post(self):
        """
        Authentication with email and password
        """

        args = self.auth_parser.parse_args()
        full_name = ''
        pass_password = False

        try:
            if args['oauth'] and args['provider']:
                if args['provider'] == 'vk':
                    oauth_seed = requests.get('https://oauth.vk.com/access_token?'
                                              'client_id=' + VK_ID +
                                              '&client_secret=' + VK_SECRET +
                                              '&redirect_uri=' + VK_REDIRECT +
                                              '&code=' + args['oauth']).text
                    oauth_data = json.loads(oauth_seed)
                    user_id = oauth_data['user_id']
                    access_token = oauth_data['access_token']

                    args['email'] = oauth_data['email']
                    if args['email'] and args['email'] != '':
                        pass_password = True

                    oauth_seed = requests.get('https://api.vk.com/method/users.get?v=5.103&access_token=' + access_token).text
                    oauth_data = json.loads(oauth_seed)
                    full_name = oauth_data['first_name'] + ' ' + oauth_data['last_name']

                if args['provider'] == 'google':
                    oauth_seed = requests.post('https://www.googleapis.com/oauth2/v4/token', data={
                        'code': args['oauth'],
                        'grant_type': 'authorization_code',
                        'redirect_uri': GOOGLE_REDIRECT,
                        'client_id': GOOGLE_ID,
                        'client_secret': GOOGLE_SECRET,
                    }, headers={
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }).text
                    oauth_data = json.loads(oauth_seed)
                    access_token = oauth_data['access_token']

                    oauth_seed = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?access_token='
                                              + access_token).text
                    oauth_data = json.loads(oauth_seed)

                    args['email'] = oauth_data['email']
                    full_name = oauth_data['name']

                    if args['email'] and args['email'] != '':
                        pass_password = True

                if args['provider'] == 'facebook':
                    oauth_seed = requests.get('https://graph.facebook.com/v5.0/oauth/access_token?'
                                              'client_id=' + FACEBOOK_ID +
                                              '&redirect_uri=' + FACEBOOK_REDIRECT +
                                              '&client_secret=' + FACEBOOK_SECRET +
                                              '&code=' + args['oauth']).text
                    oauth_data = json.loads(oauth_seed)
                    access_token = oauth_data['access_token']

                    oauth_seed = requests.get('https://graph.facebook.com/me?fields=email,name&access_token='
                                              + access_token).text

                    oauth_data = json.loads(oauth_seed)
                    full_name = oauth_data['name']

                    args['email'] = oauth_data['email']
                    if args['email'] and args['email'] != '':
                        pass_password = True
        except Exception as e:
            pass

        # TODO ADD REGISTER

        try:
            user_credentials: UserCredentials = UserCredentials.query.filter(UserCredentials.email == args['email']).one()
        except NoResultFound:
            if pass_password:
                user = User(
                    fullname=full_name,
                    registered_at=datetime.datetime.now(),
                    credentials_backref=UserCredentials(
                        email=args['email'],
                        password=''.join(random.sample(PASSWORD_SEED, RANDOM_PASSWORD_LEN)),
                    )
                )
                db.session.add(user)

                try:
                    db.session.commit()
                    user_credentials: UserCredentials = UserCredentials.query.filter(UserCredentials.email == args['email']).one()
                except IntegrityError:
                    db.session.rollback()
                    return "User is already exists", HTTPStatus.CONFLICT
            else:
                return abort(HTTPStatus.FORBIDDEN, message='Wrong email or password')

        if not pass_password:
            if not user_credentials.check_password(args['password']):
                return abort(HTTPStatus.FORBIDDEN, message='Wrong email or password')

        if not login_user(user_credentials.user):
            return abort(HTTPStatus.FORBIDDEN, message='Wrong email or password')

        update_user_permissions(user_credentials.user_id)
        return user_credentials.user
