from godmode.groups.base import BaseGroup
from godmode.acl import ACL


class GodModeGroup(BaseGroup):
    acl = ACL.ADMIN
    policy = "godmode_group"
    name = "ADMIN"
    index = 0
