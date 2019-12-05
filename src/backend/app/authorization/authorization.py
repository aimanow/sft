from flask_login import current_user, LoginManager
from flask_principal import Identity, UserNeed, ActionNeed, Principal
from flask_principal import identity_loaded


class Authorization:
    def __init__(self, app=None):
        from .permissions import DEFAULT_ACTIONS, SPECIAL_ACTIONS
        self.default_actions = set(DEFAULT_ACTIONS)
        self.special_actions = set(SPECIAL_ACTIONS)
        self.init_app(app)

    def init_app(self, app):
        if app is None:
            return
        Principal(app)
        login_manager = LoginManager(app)

        from database.models import User

        @login_manager.user_loader
        def __user_loader(user_id):
            user = User.query.get(user_id)
            if user is not None and user.is_active:
                return user

        @identity_loaded.connect_via(app)
        def __authorize(sender, identity: Identity):
            if current_user.is_anonymous or not current_user.is_active:
                return

            # Permission for *their resources*
            identity.provides.add(UserNeed(current_user.id))

            # Not denied default permissions
            identity.provides.update(self.default_actions.difference(map(ActionNeed, current_user.denied_actions)))

            # Explicitly allowed special permissions
            identity.provides.update(self.special_actions.intersection(map(ActionNeed, current_user.allowed_actions)))
