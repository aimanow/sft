from flask import Blueprint, url_for, current_app
import flask_restplus

blueprint = Blueprint(name='api', import_name=__name__, url_prefix='/api/public', template_folder='../../templates')


class Api(flask_restplus.Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme=current_app.config['SCHEME'])


api = Api(blueprint, title='SFT Public API', version='0.2.0', doc='/docs')

# Namespaces
access = api.namespace('access')
profiles = api.namespace('profiles')
aspects = api.namespace('aspects')
discussions = api.namespace('discussions')
arguments = api.namespace('arguments')
theses = api.namespace('theses')
attachments = api.namespace('attachments')
claims = api.namespace('claims')
feedback = api.namespace('feedback')
