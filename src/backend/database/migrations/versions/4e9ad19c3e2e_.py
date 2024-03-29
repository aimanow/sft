"""empty message

Revision ID: 4e9ad19c3e2e
Revises: 37875abb00c7
Create Date: 2019-04-28 12:47:22.223513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e9ad19c3e2e'
down_revision = '37875abb00c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attachments_votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('attachment_id', sa.Integer(), nullable=False),
    sa.Column('vote', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['attachment_id'], ['attachments.id'], name='attachments_votes__attachment__fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='attachments_votes__user__fk'),
    sa.PrimaryKeyConstraint('user_id', 'attachment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attachments_votes')
    # ### end Alembic commands ###
