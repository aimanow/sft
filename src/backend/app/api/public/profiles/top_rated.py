from flask import request
from flask_restplus import Resource
from sqlalchemy import desc

from app.api.models import ProfilePaginationModel
from app.api.namespaces import profiles
from database.models import Pagination, User


@profiles.route('/top_rated')
class ProfileTopRated(Resource):
    TOP_COUNT = 3

    @profiles.marshal_with(ProfilePaginationModel)
    def get(self):
        """
        Get top rated user profiles
        """
        top_filter = request.args.get('top')
        top = None
        if top_filter == '1':
            top = User.query.order_by(desc(User.total_likes)).limit(self.TOP_COUNT).all()
        else:
            top = User.query.order_by(desc(User.rating)).limit(self.TOP_COUNT).all()
        # top = User.query.order_by(desc(User.total_likes)).limit(self.TOP_COUNT).all()

        return Pagination(
            page=1,
            total_items=len(top),
            items_per_page=self.TOP_COUNT,
            items=top
        )
