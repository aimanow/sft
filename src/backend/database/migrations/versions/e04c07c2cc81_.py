"""empty message

Revision ID: e04c07c2cc81
Revises: ceb2d761f97d
Create Date: 2019-04-26 12:44:08.781736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e04c07c2cc81'
down_revision = 'ceb2d761f97d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('theses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('position', sa.Boolean(), nullable=False),
    sa.Column('message', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name='theses__author___fk'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arguments',
    sa.Column('thesis_id', sa.Integer(), nullable=False),
    sa.Column('discussion_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['discussion_id'], ['discussions.id'], name='arguments__discussion__fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['thesis_id'], ['theses.id'], name='arguments__thesis__fk'),
    sa.PrimaryKeyConstraint('thesis_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arguments')
    op.drop_table('theses')
    # ### end Alembic commands ###
