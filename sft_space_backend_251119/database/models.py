import datetime

from flask_login import current_user
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import not_, and_, cast, Float, case
from sqlalchemy.sql import functions

from app.api import file_storage
from app.extensions import db, bcrypt


class Pagination:
    def __init__(self, page=1, total_items=0, items_per_page=20, *, items):
        self.page = page
        self.total_items = total_items
        self.items_per_page = items_per_page
        self.total_pages = max(1, (total_items + items_per_page - 1) // items_per_page)
        self.items = items


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    registered_at = db.Column(db.DateTime, nullable=False)

    fullname = db.Column(db.String(64), nullable=False)
    avatar_path = db.Column(db.String)

    credentials_backref = db.relationship(
        lambda: UserCredentials, foreign_keys=lambda: UserCredentials.user_id,
        uselist=False
    )

    # For the Flask-Login
    def get_id(self):
        return str(self.id)

    is_authenticated = True
    is_anonymous = False

    deleted_backref = db.relationship(
        lambda: UserDeleted, foreign_keys=lambda: UserDeleted.user_id,
        uselist=False
    )

    @hybrid_property
    def is_active(self):
        return self.deleted_backref is None

    @is_active.expression
    def is_active(self):
        return not_(self.deleted_backref.has())

    permissions_backref = db.relationship(
        lambda: ProfilePermission, foreign_keys=lambda: ProfilePermission.user_id,
        lazy='dynamic'
    )

    @property
    def allowed_actions(self):
        return (p.name for p in self.permissions_backref if p.is_allowed)

    @property
    def denied_actions(self):
        return (p.name for p in self.permissions_backref if not p.is_allowed)

    favorite_by_backref = db.relationship(
        lambda: FavoriteUser, foreign_keys=lambda: FavoriteUser.favorite_id,
        lazy='dynamic'
    )

    @property
    def is_favorite(self):
        return not current_user.is_anonymous and self.favorite_by_backref.filter(
            FavoriteUser.user_id == current_user.id
        ).count() > 0

    favorite_users_backref = db.relationship(
        lambda: FavoriteUser, foreign_keys=lambda: FavoriteUser.user_id,
        lazy='dynamic'
    )

    confirmed_backref = db.relationship(
        lambda: UserConfirmed, foreign_keys=lambda: UserConfirmed.user_id,
        uselist=False
    )

    @hybrid_property
    def is_confirmed(self):
        return self.confirmed_backref is not None

    @is_confirmed.expression
    def is_confirmed(self):
        return self.confirmed_backref.has()

    favorite_aspects_backref = db.relationship(
        lambda: FavoriteAspect, foreign_keys=lambda: FavoriteAspect.user_id,
        lazy='dynamic'
    )

    favorite_discussions_backref = db.relationship(
        lambda: FavoriteDiscussion, foreign_keys=lambda: FavoriteDiscussion.user_id,
        lazy='dynamic'
    )

    liked_users_backref = db.relationship(
        lambda: LikedUser, foreign_keys=lambda: LikedUser.user_id,
        lazy='dynamic'
    )

    liked_by_backref = db.relationship(
        lambda: LikedUser, foreign_keys=lambda: LikedUser.liked_user_id,
        lazy='dynamic'
    )

    @hybrid_property
    def total_likes(self):
        return self.liked_by_backref.count()

    @total_likes.expression
    def total_likes(self):
        return LikedUser.query.filter(LikedUser.liked_user_id == self.id).with_entities(
            functions.count(LikedUser.liked_at)
        ).as_scalar()
        # functions.count(self.liked_by_backref)

    @property
    def i_like(self):
        return not current_user.is_anonymous and self.liked_by_backref.filter(
            LikedUser.user_id == current_user.id
        ).count() > 0

    claims_backref = db.relationship(
        lambda: Claim, foreign_keys=lambda: Claim.user_id,
        lazy='dynamic'
    )

    @hybrid_property
    def rating(self):
        return DiscussionVote.query.join(Discussion).filter(Discussion.author_id == self.id).count()

    @rating.expression
    def rating(self):
        return DiscussionVote.query.join(Discussion).filter(Discussion.author_id == self.id).with_entities(
            functions.count(DiscussionVote.discussion_id)
        ).as_scalar()


class UserCredentials(db.Model):
    __tablename__ = 'users_credentials'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_credentials__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    email = db.Column(db.String(64), nullable=False)
    is_email_confirmed = db.Column(db.Boolean, nullable=False, server_default='FALSE', default=False)

    password_hash = db.Column(db.LargeBinary(256), nullable=False)

    @property
    def password(self):
        raise ValueError("Can't read the plaintext password. Use 'password_hash' instead.")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password, rounds=10)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    __table_args__ = (
        db.UniqueConstraint(email, name='users_credentials__email__uc'),
    )


class UserDeleted(db.Model):
    __tablename__ = 'users_deleted'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_deleted__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)
    deleted_at = db.Column(db.DateTime, nullable=True)


class UserConfirmed(db.Model):
    __tablename__ = 'users_confirmed'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_confirmed__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    reviewer_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_confirmed__reviewer__fk'),
        nullable=False
    )
    reviewer = db.relationship(User, foreign_keys=reviewer_id)

    confirmed_at = db.Column(db.DateTime, nullable=False)


class ProfilePermission(db.Model):
    __tablename__ = 'users_permissions'

    name = db.Column(db.String(50), primary_key=True)

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_permissions__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    is_allowed = db.Column(db.Boolean, default=False)
    granted_at = db.Column(db.DateTime, nullable=False)


class FavoriteUser(db.Model):
    __tablename__ = 'users_favorites_users'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_favorites_users__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    favorite_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_favorites_users__favorite__fk'),
        primary_key=True
    )
    favorite = db.relationship(User, foreign_keys=favorite_id)

    created_at = db.Column(db.DateTime, nullable=False)


class Aspect(db.Model):
    __tablename__ = 'aspects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False)

    general_backref = db.relationship(
        lambda: AspectGeneral, foreign_keys=lambda: AspectGeneral.aspect_id,
        uselist=False
    )

    @hybrid_property
    def is_general(self):
        return self.general_backref is not None

    @is_general.expression
    def is_general(self):
        return self.general_backref.has()

    favorite_by_backref = db.relationship(
        lambda: FavoriteAspect, foreign_keys=lambda: FavoriteAspect.favorite_id,
        lazy='dynamic'
    )

    @property
    def is_favorite(self):
        return not current_user.is_anonymous and self.favorite_by_backref.filter(
            FavoriteAspect.user_id == current_user.id
        ).count() > 0


class AspectGeneral(db.Model):
    __tablename__ = 'aspects_general'

    aspect_id = db.Column(
        db.Integer, db.ForeignKey(Aspect.id, name='aspects_general__aspect__fk', ondelete='CASCADE'),
        primary_key=True
    )
    aspect = db.relationship(Aspect, foreign_keys=aspect_id)


class FavoriteAspect(db.Model):
    __tablename__ = 'users_favorites_aspects'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_favorites_aspects__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    favorite_id = db.Column(
        db.Integer, db.ForeignKey(Aspect.id, name='users_favorites_aspects__favorite__fk', ondelete='CASCADE'),
        primary_key=True
    )
    favorite = db.relationship(Aspect, foreign_keys=favorite_id)

    created_at = db.Column(db.DateTime, nullable=False)


class Discussion(db.Model):
    __tablename__ = 'discussions'

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(3), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False)

    author_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='discussions__author___fk'), nullable=False
    )
    author = db.relationship(User, foreign_keys=author_id)

    view_count = db.Column(db.Integer, nullable=False, server_default="0")

    frozen_backref = db.relationship(
        lambda: DiscussionFrozen, foreign_keys=lambda: DiscussionFrozen.discussion_id,
        uselist=False
    )

    @hybrid_property
    def is_frozen(self):
        return self.frozen_backref is not None

    @is_frozen.expression
    def is_frozen(self):
        return self.frozen_backref.has()

    favorite_by_backref = db.relationship(
        lambda: FavoriteDiscussion, foreign_keys=lambda: FavoriteDiscussion.favorite_id,
        lazy='dynamic'
    )

    @property
    def is_favorite(self):
        return not current_user.is_anonymous and self.favorite_by_backref.filter(
            FavoriteDiscussion.user_id == current_user.id
        ).count() > 0

    arguments_backref = db.relationship(
        lambda: Argument, foreign_keys=lambda: Argument.discussion_id,
        lazy='dynamic'
    )

    @hybrid_property
    def rating(self):
        return Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.rating), 0.0)
        ).scalar()

    @rating.expression
    def rating(self):
        return Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.rating), 0.0)
        ).as_scalar()

    @hybrid_property
    def today_rating(self):
        return Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.today_rating), 0.0)
        ).scalar()

    @today_rating.expression
    def today_rating(self):
        return Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.today_rating), 0.0)
        ).as_scalar()

    # DEPRECATED
    votes_backref = db.relationship(
        lambda: DiscussionVote, foreign_keys=lambda: DiscussionVote.discussion_id,
        lazy='dynamic'
    )

    @property
    def votes(self):
        positive = Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.positive_rating_sum), 0.0)
        ).scalar()
        negative = Argument.query.filter(Argument.discussion_id == self.id).with_entities(
            functions.coalesce(functions.sum(Argument.negative_rating_sum), 0.0)
        ).scalar()

        if positive + negative < 0.001:
            positive = 1
            negative = 1

        ratio = positive / (positive + negative)
        return {
            'true': round(ratio * 100),
            'false': 100 - round(ratio * 100),
            'my_vote': None
        }

    @property
    def aspects(self):
        # todo: remove the property 'aspects' from discussion model
        # Use `GET /aspects` with "discussion" argument to filter aspects by discussion
        return Aspect.query.join(ArgumentAspect).join(Argument).filter(
            Argument.discussion_id == self.id
        ).distinct(Aspect.id).limit(20).all()


class DiscussionFrozen(db.Model):
    __tablename__ = 'discussions_frozen'

    discussion_id = db.Column(
        db.Integer, db.ForeignKey(Discussion.id, name='discussions_frozen__discussion__fk'),
        primary_key=True
    )
    discussion = db.relationship(Discussion, foreign_keys=discussion_id)

    frozen_at = db.Column(db.DateTime, nullable=False)


class FavoriteDiscussion(db.Model):
    __tablename__ = 'users_favorites_discussions'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_favorites_discussions__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    favorite_id = db.Column(
        db.Integer, db.ForeignKey(Discussion.id, name='users_favorites_discussions__favorite__fk', ondelete='CASCADE'),
        primary_key=True
    )
    favorite = db.relationship(Discussion, foreign_keys=favorite_id)

    created_at = db.Column(db.DateTime, nullable=False)


class Thesis(db.Model):
    __tablename__ = 'theses'

    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='theses__author___fk'), nullable=False
    )
    author = db.relationship(User, foreign_keys=author_id)

    position = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    argument_thesis = db.relationship(
        lambda: ArgumentThesis, foreign_keys=lambda: ArgumentThesis.thesis_id,
        uselist=False
    )

    thesis_comments_backref = db.relationship(
        lambda: ThesisComment, foreign_keys=lambda: ThesisComment.thesis_id,
        lazy='dynamic'
    )

    comment_backref = db.relationship(
        lambda: ThesisComment, foreign_keys=lambda: ThesisComment.comment_id,
        uselist=False
    )

    @hybrid_property
    def is_comment(self):
        return self.comment_backref is not None

    @is_comment.expression
    def is_comment(self):
        return self.comment_backref.has()

    @hybrid_property
    def total_comments(self):
        return self.thesis_comments_backref.count()

    @total_comments.expression
    def total_comments(self):
        return functions.count(self.thesis_comments_backref)

    attachments = db.relationship(
        lambda: Attachment, foreign_keys=lambda: Attachment.thesis_id,
        lazy='joined'
    )

    votes_backref = db.relationship(
        lambda: ThesisVote, foreign_keys=lambda: ThesisVote.thesis_id,
        lazy='dynamic'
    )

    @property
    def votes(self):
        total_votes, total_x, total_y = self.votes_backref.with_entities(
            functions.count(ThesisVote.thesis_id),
            functions.coalesce(functions.sum(ThesisVote.value_x) / functions.count(ThesisVote.thesis_id), 0),
            functions.coalesce(functions.sum(ThesisVote.value_y) / functions.count(ThesisVote.thesis_id), 0),
        ).one()

        return {
            'total_votes': total_votes,
            'mean_x': total_x,
            'mean_y': total_y,
            'my_vote': self.my_vote
        }

    @property
    def my_vote(self):
        if current_user.is_anonymous:
            return None
        thesis_vote: ThesisVote = self.votes_backref.filter(ThesisVote.user_id == current_user.id).first()
        return None if thesis_vote is None else {
            'x': thesis_vote.value_x,
            'y': thesis_vote.value_y
        }

    @hybrid_property
    def rating(self):
        return self.votes_backref.with_entities(
            functions.coalesce(functions.sum(ThesisVote.score), 0)
        ).scalar()

    @rating.expression
    def rating(self):
        return ThesisVote.query.filter(ThesisVote.thesis_id == self.id).with_entities(
            functions.coalesce(functions.sum(ThesisVote.score), 0)
        ).as_scalar()

    @hybrid_property
    def today_rating(self):
        return self.votes_backref.filter(ThesisVote.created_at > datetime.datetime.today().date()).with_entities(
            functions.coalesce(functions.sum(ThesisVote.score), 0)
        ).scalar()

    @today_rating.expression
    def today_rating(self):
        return ThesisVote.query.filter(
            ThesisVote.thesis_id == self.id,
            ThesisVote.created_at > datetime.datetime.today().date()
        ).with_entities(
            functions.coalesce(functions.sum(ThesisVote.score), 0)
        ).as_scalar()


class Argument(db.Model):
    __tablename__ = 'arguments'

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='arguments__thesis__fk'),
        primary_key=True
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    discussion_id = db.Column(
        db.Integer, db.ForeignKey(Discussion.id, name='arguments__discussion__fk', ondelete='CASCADE'),
        nullable=False
    )
    discussion = db.relationship(Discussion, foreign_keys=discussion_id)

    @hybrid_property
    def id(self):
        return self.thesis_id

    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    aspects_backref = db.relationship(
        lambda: ArgumentAspect, foreign_keys=lambda: ArgumentAspect.argument_id,
        lazy='joined'
    )

    @property
    def aspect_ids(self):
        return [argument_aspect.aspect_id for argument_aspect in self.aspects_backref]

    arguments_theses_backref = db.relationship(
        lambda: ArgumentThesis, foreign_keys=lambda: ArgumentThesis.argument_id,
        lazy='dynamic'
    )

    @hybrid_property
    def theses(self):
        return [argument_thesis.thesis for argument_thesis in self.arguments_theses_backref]

    @theses.expression
    def theses(self):
        return Thesis.query.join(Thesis.argument_thesis).filter(
            ArgumentThesis.argument_id == self.id
        )

    @hybrid_property
    def rating(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).scalar()

    @rating.expression
    def rating(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).as_scalar()

    @hybrid_property
    def today_rating(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.today_rating), 0.0)
        ).scalar()

    @today_rating.expression
    def today_rating(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.today_rating), 0.0)
        ).as_scalar()

    @hybrid_property
    def positive_rating_sum(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id,
            Thesis.position
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).scalar()

    @positive_rating_sum.expression
    def positive_rating_sum(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id,
            Thesis.position
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).as_scalar()

    @hybrid_property
    def negative_rating_sum(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id,
            not_(Thesis.position)
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).scalar()

    @negative_rating_sum.expression
    def negative_rating_sum(self):
        return Thesis.query.join(ArgumentThesis).filter(
            ArgumentThesis.argument_id == self.id,
            not_(Thesis.position)
        ).with_entities(
            functions.coalesce(functions.sum(Thesis.rating), 0.0)
        ).as_scalar()

    @property
    def opinion_ratio(self):
        positive = self.positive_rating_sum
        negative = self.negative_rating_sum

        if positive + negative < 0.001:
            positive = 1
            negative = 1

        ratio = positive / (positive + negative)
        return {
            'true': round(ratio * 100),
            'false': 100 - round(ratio * 100),
        }


class ArgumentAspect(db.Model):
    __tablename__ = 'arguments_aspects'

    argument_id = db.Column(
        db.Integer, db.ForeignKey(Argument.id, name='arguments_aspects__argument__fk', ondelete='CASCADE'),
        primary_key=True
    )
    argument = db.relationship(Argument, foreign_keys=argument_id)

    aspect_id = db.Column(
        db.Integer, db.ForeignKey(Aspect.id, name='arguments_aspects__aspect__fk', ondelete='CASCADE'),
        primary_key=True
    )
    aspect = db.relationship(Aspect, foreign_keys=aspect_id)


class ArgumentThesis(db.Model):
    __tablename__ = 'arguments_theses'

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='arguments_theses__thesis__fk', ondelete='CASCADE'),
        primary_key=True
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    argument_id = db.Column(
        db.Integer, db.ForeignKey(Argument.id, name='arguments_theses__argument__fk', ondelete='CASCADE'),
        nullable=False
    )
    argument = db.relationship(Argument, foreign_keys=argument_id)


class ThesisComment(db.Model):
    __tablename__ = 'theses_comments'

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='theses_comments__thesis__fk', ondelete='CASCADE'),
        primary_key=True
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    comment_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='theses_comments__comment__fk', ondelete='CASCADE'),
        primary_key=True
    )
    comment = db.relationship(Thesis, foreign_keys=comment_id)


class Claim(db.Model):
    __tablename__ = 'claims'

    id = db.Column(db.Integer, primary_key=True)

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='claims__thesis__fk', ondelete='CASCADE'),
        nullable=False
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='claims__user__fk'),
        nullable=False
    )
    user = db.relationship(User, foreign_keys=user_id)

    message = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    status = db.relationship(
        lambda: ClaimStatus, foreign_keys=lambda: ClaimStatus.claim_id,
        uselist=False
    )


class ClaimStatus(db.Model):
    __tablename__ = 'claims_statuses'

    claim_id = db.Column(
        db.Integer, db.ForeignKey(Claim.id, name='claims_statuses__claim__fk', ondelete='CASCADE'),
        primary_key=True
    )
    claim = db.relationship(Claim, foreign_keys=claim_id)

    reviewer_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='claims_statuses__reviewer__fk'), nullable=False
    )
    reviewer = db.relationship(User, foreign_keys=reviewer_id)

    title = db.Column(db.String(32), nullable=False)
    reason = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


class LikedUser(db.Model):
    __tablename__ = 'users_likes_users'

    # Who created this "like"
    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_likes__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    liked_user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='users_likes__liked_user__fk'),
        primary_key=True
    )
    liked_user = db.relationship(User, foreign_keys=liked_user_id)

    liked_at = db.Column(db.DateTime, nullable=False)


class Education(db.Model):
    __tablename__ = 'educations'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='educations__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    high_school = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    graduation_date = db.Column(db.Date, nullable=False)
    scan_path = db.Column(db.String)

    verified_backref = db.relationship(
        lambda: EducationVerified, foreign_keys=lambda: EducationVerified.education_id,
        uselist=False
    )

    @hybrid_property
    def is_verified(self):
        return self.verified_backref is not None

    @is_verified.expression
    def is_verified(self):
        return self.verified_backref.has()


class EducationVerified(db.Model):
    __tablename__ = 'educations_verified'

    education_id = db.Column(
        db.Integer, db.ForeignKey(Education.user_id, name='educations_verified__education__fk', ondelete='CASCADE'),
        primary_key=True
    )
    education = db.relationship(Education, foreign_keys=education_id)

    reviewer_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='educations_verified__reviewer__fk'), nullable=False
    )
    reviewer = db.relationship(User, foreign_keys=reviewer_id)

    verified_at = db.Column(db.DateTime, nullable=False)


class FileAttachment(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def dumps(self):
        return self.file_path

    @staticmethod
    def loads(payload):
        return FileAttachment(file_path=payload)

    def get_url(self):
        return file_storage.download_link(
            category=file_storage.FileCategory.Attachment,
            relative_path=self.file_path
        )


class LinkAttachment(object):
    def __init__(self, url):
        self.url = url

    def dumps(self):
        return self.url

    @staticmethod
    def loads(payload):
        return LinkAttachment(url=payload)

    def get_url(self):
        return self.url


class Attachment(db.Model):
    __tablename__ = 'attachments'

    TYPE_MAPPING = {
        'file': FileAttachment,
        'link': LinkAttachment
    }

    id = db.Column(db.Integer, primary_key=True)

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='attachments__thesis__fk'), nullable=False
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    type = db.Column(db.String(32), nullable=False)
    payload = db.Column(db.String, nullable=False)

    @property
    def payload_url(self):
        return Attachment.TYPE_MAPPING[self.type].loads(self.payload).get_url()

    votes_backref = db.relationship(
        lambda: AttachmentVote, foreign_keys=lambda: AttachmentVote.attachment_id,
        lazy='dynamic'
    )

    @hybrid_property
    def votes_true(self):
        return self.votes_backref.filter(AttachmentVote.vote.is_(True)).count()

    @hybrid_property
    def votes_false(self):
        return self.votes_backref.filter(AttachmentVote.vote.is_(False)).count()

    @property
    def votes(self):
        return {
            'true': self.votes_true,
            'false': self.votes_false,
            'my_vote': self.my_vote
        }

    @property
    def my_vote(self):
        if current_user.is_anonymous:
            return None
        attachment_vote = self.votes_backref.filter(AttachmentVote.user_id == current_user.id).first()
        return None if attachment_vote is None else attachment_vote.vote

    @hybrid_property
    def rating(self):
        votes_sum = functions.coalesce(functions.sum(AttachmentVote.score), 0.0)
        return self.votes_backref.with_entities(
            case([(votes_sum <= 0.0, 0.0)], else_=votes_sum)
        ).scalar()

    @rating.expression
    def rating(self):
        votes_sum = functions.coalesce(functions.sum(AttachmentVote.score), 0)
        return self.votes_backref.with_entities(
            case([(votes_sum <= 0.0, 0.0)], else_=votes_sum)
        ).as_scalar()


class AttachmentVote(db.Model):
    __tablename__ = 'attachments_votes'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='attachments_votes__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    attachment_id = db.Column(
        db.Integer, db.ForeignKey(Attachment.id, name='attachments_votes__attachment__fk', ondelete='CASCADE'),
        primary_key=True
    )
    attachment = db.relationship(Attachment, foreign_keys=attachment_id)

    vote = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @hybrid_property
    def score(self):
        return 1.0 if self.vote else -0.5

    @score.expression
    def score(self):
        return case([(self.vote, 1.0)], else_=-0.5)


class ThesisVote(db.Model):
    __tablename__ = 'theses_votes'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='theses_votes__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    thesis_id = db.Column(
        db.Integer, db.ForeignKey(Thesis.id, name='theses_votes__thesis__fk', ondelete='CASCADE'),
        primary_key=True
    )
    thesis = db.relationship(Thesis, foreign_keys=thesis_id)

    value_x = db.Column(db.SmallInteger, nullable=False)
    value_y = db.Column(db.SmallInteger, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False)

    # Number of votes in the last hour
    flood_divider = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint(and_(value_x >= 0, value_x <= 10), name='theses_votes__value_x__check'),
        db.CheckConstraint(and_(value_y >= 0, value_y <= 10), name='theses_votes__value_y__check'),
        db.CheckConstraint(flood_divider > 0, name='theses_votes__flood_divider__check'),
    )

    @hybrid_property
    def score(self):
        return (self.value_x * self.value_y) / self.flood_divider

    @score.expression
    def score(self):
        return cast(self.value_x * self.value_y, Float) / cast(self.flood_divider, Float)


class DiscussionVote(db.Model):
    __tablename__ = 'discussions_votes'

    user_id = db.Column(
        db.Integer, db.ForeignKey(User.id, name='discussions_votes__user__fk'),
        primary_key=True
    )
    user = db.relationship(User, foreign_keys=user_id)

    discussion_id = db.Column(
        db.Integer, db.ForeignKey(Discussion.id, name='discussions_votes__discussion__fk', ondelete='CASCADE'),
        primary_key=True
    )
    discussion = db.relationship(Discussion, foreign_keys=discussion_id)

    # true ≈ for, false ≈ against
    vote = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
