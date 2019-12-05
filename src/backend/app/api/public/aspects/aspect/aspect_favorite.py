import datetime
from http import HTTPStatus

from flask_login import current_user
from flask_restplus import Resource, abort

from app.api.models import AspectModel
from app.api.namespaces import aspects
from database import db
from database.models import FavoriteAspect, Aspect


@aspects.route('/<int:{}>/favorite'.format("aspect_id"))
@aspects.param('aspect_id', description="Aspect identifier")
class AspectFavoriteResource(Resource):
    @aspects.response(HTTPStatus.FORBIDDEN, description="User is anonymous")
    @aspects.marshal_with(AspectModel)
    def post(self, aspect_id):
        """
        Toggle aspect in current user favorites (add / remove)

        * User can add aspect to **their favorites**
        * User can remove aspect from **their favorites**
        """
        if current_user.is_anonymous:
            return abort(HTTPStatus.FORBIDDEN, message="User is anonymous")

        if not current_user.favorite_aspects_backref.filter_by(favorite_id=aspect_id).delete():
            current_user.favorite_aspects_backref.append(FavoriteAspect(
                favorite_id=aspect_id,
                created_at=datetime.datetime.now()
            ))

        db.session.commit()
        return Aspect.query.get(aspect_id)
