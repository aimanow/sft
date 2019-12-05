from godmode.groups.base import BaseGroup
from godmode.acl import ACL


class MainGroup(BaseGroup):
    acl = ACL.MODERATOR
    name = "MAIN"
    policy = "main_group"
    index = 1000
