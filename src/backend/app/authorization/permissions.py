from flask import current_app
from flask_principal import Permission, Identity, ActionNeed, identity_changed, UserNeed


def update_user_permissions(user_id):
    # noinspection PyProtectedMember
    identity_changed.send(current_app._get_current_object(), identity=Identity(user_id))


class UserNeedPermission(Permission):
    def __init__(self, user_id):
        super().__init__(UserNeed(user_id))


CreateArgumentAction = ActionNeed('create_arguments')
CreateArgumentPermission = Permission(CreateArgumentAction)

CreateThesisAction = ActionNeed('create_theses')
CreateThesisPermission = Permission(CreateThesisAction)

CreateAspectAction = ActionNeed('create_aspects')
CreateAspectPermission = Permission(CreateAspectAction)

CreateClaimAction = ActionNeed('create_claims')
CreateClaimPermission = Permission(CreateClaimAction)

VoteForAttachmentAction = ActionNeed('vote_for_attachments')
VoteForAttachmentPermission = Permission(VoteForAttachmentAction)

VoteForThesisAction = ActionNeed('vote_for_theses')
VoteForThesisPermission = Permission(VoteForThesisAction)

VoteForDiscussionAction = ActionNeed('vote_for_discussions')
VoteForDiscussionPermission = Permission(VoteForDiscussionAction)


DEFAULT_ACTIONS = [
    CreateArgumentAction,
    CreateThesisAction,
    CreateAspectAction,
    CreateClaimAction,
    VoteForAttachmentAction,
    VoteForThesisAction,
    VoteForDiscussionAction,
]


DeleteUserAction = ActionNeed('delete_users')
DeleteUserPermission = Permission(DeleteUserAction)

ConfirmUserAction = ActionNeed('confirm_users')
ConfirmUserPermission = Permission(ConfirmUserAction)

VerifyEducationAction = ActionNeed('verify_educations')
VerifyEducationPermission = Permission(VerifyEducationAction)

EditDiscussionAction = ActionNeed('edit_discussions')
EditDiscussionPermission = Permission(EditDiscussionAction)

EditAspectAction = ActionNeed('edit_aspects')
EditAspectPermission = Permission(EditAspectAction)

EditThesisAction = ActionNeed('edit_theses')
EditThesisPermission = Permission(EditThesisAction)

ReviewClaimAction = ActionNeed('review_claims')
ReviewClaimPermission = Permission(ReviewClaimAction)

EditDefaultRightAction = ActionNeed('edit_default_rights')
EditDefaultRightPermission = Permission(EditDefaultRightAction)

EditSpecialRightAction = ActionNeed('edit_special_rights')
EditSpecialRightPermission = Permission(EditSpecialRightAction)

SPECIAL_ACTIONS = [
    EditDiscussionAction,
    DeleteUserAction,
    ConfirmUserAction,
    EditAspectAction,
    EditThesisAction,
    ReviewClaimAction,
    EditDefaultRightAction,
    EditSpecialRightAction,
    VerifyEducationAction,
]
