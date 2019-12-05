from actions.demo_ban_user import DemoBanUserAction
from godmode.views.list_view import BaseListView
from godmode.models.base import BaseAdminModel
from godmode.widgets.base import BaseWidget
from groups.main_group import MainGroup
from database.db import User, pg_database
from widgets.boolean import BooleanReverseWidget


class NameWidget(BaseWidget):
    filterable = False

    def render_list(self, item):
        return "<b>{}</b>".format(item.fullname)


class UsersAdminModel(BaseAdminModel):
    db = pg_database
    name = "users"
    title = "Users"
    icon = "icon-user"
    group = MainGroup
    index = 100
    table = User
    # widgets = {
    #     "is_locked": BooleanReverseWidget
    # }

    class PUsersListView(BaseListView):
        title = "User list"
        # sorting = ["id", "name"]
        sorting = ["id", "fullname"]
        default_sorting = User.registered_at.desc()
        fields = [
            "id",
            "fullname",
            "registered_at",
            "avatar_path"
        ]
        # object_actions = [DemoBanUserAction]
        # batch_actions = [DemoBanUserAction]
        widgets = {
            "fullname": NameWidget
        }

    list_view = PUsersListView
