"""empty message

Revision ID: 037d00c04a7f
Revises: f27df6e867ec
Create Date: 2019-04-26 13:53:29.513221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '037d00c04a7f'
down_revision = 'f27df6e867ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('arguments_theses__thesis__uc', 'arguments_theses', ['thesis_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('arguments_theses__thesis__uc', 'arguments_theses', type_='unique')
    # ### end Alembic commands ###
