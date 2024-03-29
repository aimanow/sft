"""empty message

Revision ID: 8f735328be19
Revises: 6935ac723f40
Create Date: 2019-05-01 15:25:30.641089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f735328be19'
down_revision = '6935ac723f40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_credentials', sa.Column('is_email_confirmed', sa.Boolean(), server_default='FALSE', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_credentials', 'is_email_confirmed')
    # ### end Alembic commands ###
