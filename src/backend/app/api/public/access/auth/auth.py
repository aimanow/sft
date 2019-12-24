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
from flask import render_template, current_app
from database.models import UserCredentials, User
from database import db
from sqlalchemy.exc import IntegrityError


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
                if args['provider'] == 'vk' and current_app.config['OAUTH_GOOGLE_ID']:
                    oauth_seed = requests.get('https://oauth.vk.com/access_token?'
                                              'client_id=' + current_app.config['OAUTH_VK_ID'] +
                                              '&client_secret=' + current_app.config['OAUTH_VK_SECRET'] +
                                              '&redirect_uri=' + current_app.config['OAUTH_VK_REDIRECT'] +
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

                if args['provider'] == 'google' and current_app.config['OAUTH_GOOGLE_ID']:
                    oauth_seed = requests.post('https://www.googleapis.com/oauth2/v4/token', data={
                        'code': args['oauth'],
                        'grant_type': 'authorization_code',
                        'redirect_uri': current_app.config['OAUTH_GOOGLE_REDIRECT'],
                        'client_id': current_app.config['OAUTH_GOOGLE_ID'],
                        'client_secret': current_app.config['OAUTH_GOOGLE_SECRET'],
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

                if args['provider'] == 'facebook' and current_app.config['OAUTH_FACEBOOK_ID']:
                    oauth_seed = requests.get('https://graph.facebook.com/v5.0/oauth/access_token?'
                                              'client_id=' + current_app.config['OAUTH_FACEBOOK_ID'] +
                                              '&redirect_uri=' + current_app.config['OAUTH_FACEBOOK_REDIRECT'] +
                                              '&client_secret=' + current_app.config['OAUTH_FACEBOOK_SECRET'] +
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

        if args['email'] and args['email'] != '':
            args['email'] = args['email'].lower()

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
