"""empty message

Revision ID: a201ce93fc6c
Revises: 8f735328be19
Create Date: 2019-05-02 11:33:48.222933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a201ce93fc6c'
down_revision = '8f735328be19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('discussions', sa.Column('view_count', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('discussions', 'view_count')
    # ### end Alembic commands ###
