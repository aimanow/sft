from flask import g
from sqlalchemy.exc import DataError

from godmode.models.base import BaseAdminModel
from godmode.views.view import BaseView
from godmode.acl import ACL
from database.db import pg_database


class IndexAdminModel(BaseAdminModel):
    acl = ACL.ALL
    db = pg_database
    title = "Home"
    place = None
    url_prefix = "/"

    class IndexView(BaseView):
        acl = ACL.ALL
        url = "/"
        title = "Index"
        template = "index.html"

        def get(self):
            session = self.model.session

            try:
                total_users = session.execute("select count(id) as value from users").first()[0]
            except DataError:
                total_users = 0


            context = {
                "message": "Welcome to SFT SPACE ADMIN, {}. You can customize this page.".format(g.user.login),
                "total_users": total_users,
            }
            return self.render(**context)

    list_view = IndexView
