import datetime

from flask import url_for
from flask_restplus import fields
from app.api.namespaces import api


PermissionModel = api.model('Permission', {
    'name': fields.String(required=True, example="create_arguments", description="Permission name"),
    'is_allowed': fields.Boolean(required=True, default=False, description="Does the user have this permission?"),
})


ProfilePermissionsModel = api.model('ProfilePermissions', {
    'permissions': fields.List(fields.Nested(PermissionModel))
})


ProfileModel = api.model('Profile', {
    'id': fields.Integer(readonly=True, example=1, description="Profile identifier"),
    'fullname': fields.String(example="John Dorian", description="Profile display name"),
    'is_confirmed': fields.Boolean(readonly=True, description="Is the profile confirmed?"),
    'is_favorite': fields.Boolean(readonly=True, default=False, description="Is profile in current user favorites?"),
    'avatar_url': fields.String(readonly=True, description="Avatar image url", attribute=(
        lambda user: None if user.avatar_path is None else url_for('api.profile_avatar', profile_id=user.id)
    ), example="http://.../profiles/1/avatar"),
    'total_likes': fields.Integer(readonly=True, example=1337, description="Total likes on the profile"),
    'i_like': fields.Boolean(readonly=True, example=False, description="Did the current user like the profile?"),
})


ProfileEducationModel = api.model('Education', {
    'country': fields.String(required=True, example="Russia", description="Country of education"),
    'city': fields.String(required=True, example="Omsk", description="City of education"),
    'high_school': fields.String(required=True, example="OmSU", description="High school title"),
    'faculty': fields.String(required=True, example="Computer Science", description="Faculty title"),
    'speciality': fields.String(required=True, example="Information Security", description="Speciality title"),
    'graduation_date': fields.Date(required=True, description="Graduation date", example=(
        datetime.date(2019, 1, 1).isoformat()
    )),
    'scan_url': fields.String(readonly=True, description="Scan image of the certificate", attribute=(
        lambda education: education.scan_path and url_for('api.education_scan', profile_id=education.user_id)
    ), example="http://.../profiles/1/education/scan"),
    'is_verified': fields.Boolean(readonly=True, description="Is the education verified?"),
})


AbstractPaginationModel = api.model('AbstractPagination', {
    'page': fields.Integer(example=1, description='Number of this page of results'),
    'total_pages': fields.Integer(example=1, description='Total number of pages of results'),
    'total_items': fields.Integer(example=1, description='Total number of results'),
    'items_per_page': fields.Integer(example=20, description='Number of items per page of results'),
})


ProfilePaginationModel = api.inherit('ProfilePagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(ProfileModel))
})


AspectModel = api.model('Aspect', {
    'id': fields.Integer(readonly=True, example=1, description="Aspect identifier"),
    'title': fields.String(required=True, example="Physics", description="Aspect display title"),
    'image_url': fields.String(readonly=True, description="Aspect image url", attribute=(
        lambda aspect: None if aspect.image_path is None else url_for('api.aspect_image', aspect_id=aspect.id)
    ), example="http://.../aspects/1/image"),
    'is_general': fields.Boolean(readonly=True, description="Is the aspect in the general list of aspects?"),
    'is_favorite': fields.Boolean(readonly=True, default=False, description="Is aspect in current user favorites?"),
})


AspectPaginationModel = api.inherit('AspectPagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(AspectModel))
})


DiscussionVotesModel = api.model('DiscussionVotes', {
    'true': fields.Integer(readonly=True, example=80, description="Percentage of 'for' votes"),
    'false': fields.Integer(readonly=True, example=20, description="Percentage of 'against' votes"),
    'my_vote': fields.Boolean(required=True, description="Current user position (true ≈ 'for'; false ≈ 'against')")
})


DiscussionModel = api.model('Discussion', {
    'id': fields.Integer(readonly=True, example=1, description="Discussion identifier"),
    'lang': fields.String(required=True, example="ru", description="Discussion language"),
    'title': fields.String(required=True, example="Есть ли жизнь на марсе?", description="Discussion display title"),
    'description': fields.String(required=False, example="Описание дискуссии", description="Discussion display description"),
    'created_at': fields.DateTime(readonly=True, example=datetime.datetime(2019, 1, 5, 8, 2).isoformat(), description=(
        "Discussion creation datetime"
    )),
    'view_count': fields.Integer(readonly=True, example=37, description="Discussion view count"),
    'author': fields.Nested(ProfileModel, readonly=True),
    'image_url': fields.String(readonly=True, attribute=(
        lambda discussion: discussion.image_path and url_for('api.discussion_image', discussion_id=discussion.id)
    ), example="http://.../discussions/1/image"),
    'rating': fields.Integer(readonly=True, example=1000, description="Discussion rating score"),
    'votes': fields.Nested(DiscussionVotesModel, readonly=True),
    'is_frozen': fields.Boolean(readonly=True, description="Is discussion frozen by the moderator?"),
    'is_favorite': fields.Boolean(readonly=True, default=False, description="Is discussion in current user favorites?"),
    'aspects': fields.List(fields.Nested(AspectModel), readonly=True),
})


DiscussionPaginationModel = api.inherit('DiscussionPagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(DiscussionModel))
})


AttachmentVoteModel = api.model('AttachmentVote', {
    'true': fields.Integer(readonly=True, example=1, description="Total count of 'for' votes"),
    'false': fields.Integer(readonly=True, example=0, description="Total count of 'against' votes"),
    'my_vote': fields.Boolean(required=True, description=(
        "Current user attachment vote (true ≈ ✔; false ≈ x, null ≈ no vote)"
    )),
})


AttachmentModel = api.model('Attachment', {
    'id': fields.Integer(readonly=True, example=1, description="Attachment identifier"),
    'type': fields.String(required=True, example='link', description='Attachment type (link/file/...)'),
    'payload_url': fields.String(readonly=True, example='https://www.google.com/search?q=a+cat'),
    'votes': fields.Nested(AttachmentVoteModel, readonly=True),
    'rating': fields.Integer(readonly=True, example=42, description="Total attachment rating")
})

ThesisAttachmentsModel = api.model('ThesisAttachments', {
    'attachments': fields.List(fields.Nested(AttachmentModel), readonly=True),
})


UserThesisVoteModel = api.model('UserThesisVote', {
    'x': fields.Integer(required=True, example=2, description='Current user vote X axis value'),
    'y': fields.Integer(required=True, example=6, description='Current user vote Y axis value'),
})


ThesisVotesModel = api.model('ThesisVotes', {
    'mean_x': fields.Integer(readonly=True, example=2, description='Mean vote X axis value'),
    'mean_y': fields.Integer(readonly=True, example=6, description='Mean vote Y axis value'),
    'total_votes': fields.Integer(readonly=True, example=1, description="Number of votes"),
    'my_vote': fields.Nested(UserThesisVoteModel, allow_null=True, readonly=True, description=(
        'Current user vote. Can be NULL'
    )),
})


ThesisModel = api.model('Thesis', {
    'id': fields.Integer(readonly=True, example=1, description="Thesis identifier"),
    'author': fields.Nested(ProfileModel, readonly=True),
    'position': fields.Boolean(required=True, description="Position (true ≈ 'supplement'; false ≈ 'refutation')"),
    'message': fields.String(required=True, description="Content message", example=(
        "Попыткам обнаружить жизнь на Марсе уже больше 40 лет. До сих пор ничего не нашли."
    )),
    'attachments': fields.List(fields.Nested(AttachmentModel), readonly=True),
    'total_comments': fields.Integer(readonly=True, example=1, description="Number of comments on this thesis"),
    'votes': fields.Nested(ThesisVotesModel, readonly=True, description='Average values'),
    'rating': fields.Integer(readonly=True, example=sum([(2 * 6) / 1]), description="Thesis rating"),
    'created_at': fields.DateTime(readonly=True, example=datetime.datetime(2019, 1, 5, 8, 6).isoformat(), description=(
        "Thesis creation datetime"
    )),
})


ThesisPaginationModel = api.inherit('ThesisPagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(ThesisModel))
})


ArgumentOpinionRatioModel = api.model('ArgumentOpinionRatio', {
    'true': fields.Integer(readonly=True, example=80, description="Percentage of 'for' theses"),
    'false': fields.Integer(readonly=True, example=20, description="Percentage of 'against' theses"),
})

ArgumentModel = api.model('Argument', {
    'id': fields.Integer(readonly=True, example=1, description="Argument identifier"),
    'title': fields.String(required=True, description="Argument display title", example=(
        "Поиски жизни не привели к успеху."
    )),
    'aspect_ids': fields.List(fields.Integer(required=True, example=1, description='Aspect identifier')),
    'aspects': fields.List(fields.Nested(AspectModel), readonly=True, required=False),
    'thesis': fields.Nested(ThesisModel, required=True),
    'opinion_ratio': fields.Nested(ArgumentOpinionRatioModel, readonly=True)
})


ArgumentPaginationModel = api.inherit('ArgumentPagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(ArgumentModel))
})


ClaimStatusModel = api.model('ClaimStatus', {
    'title': fields.String(required=True, example="Отклонено", description="Short status title like"),
    'reason': fields.String(required=True, description="Claim status reason message", example=(
        "Оскорбительные высказывания не обнаружены"
    )),
    'created_at': fields.DateTime(readonly=True, description="When the status was created", example=(
        datetime.datetime(2019, month=4, day=26, hour=16, minute=19, second=33).isoformat()
    ))
})


ClaimModel = api.model('Claim', {
    'id': fields.Integer(readonly=True, example=1, description="Claim identifier"),
    'user_id': fields.Integer(readonly=True, example=1, description="Thesis identifier"),
    'thesis_id': fields.Integer(readonly=True, example=1, description="Thesis identifier"),
    'message': fields.String(required=True, example="Тезис содержит оскорбительные высказывания!"),
    'status': fields.Nested(ClaimStatusModel, readonly=True),
})


ClaimPaginationModel = api.inherit('ClaimPagination', AbstractPaginationModel, {
    'items': fields.List(fields.Nested(ClaimModel), readonly=True)
})
