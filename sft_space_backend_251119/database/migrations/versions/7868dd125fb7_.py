"""empty message

Revision ID: 7868dd125fb7
Revises: e04c07c2cc81
Create Date: 2019-04-26 12:58:36.147680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7868dd125fb7'
down_revision = 'e04c07c2cc81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arguments_aspects',
    sa.Column('argument_id', sa.Integer(), nullable=False),
    sa.Column('aspect_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['argument_id'], ['arguments.thesis_id'], name='arguments_aspects__argument__fk'),
    sa.ForeignKeyConstraint(['aspect_id'], ['aspects.id'], name='arguments_aspects__aspect__fk'),
    sa.PrimaryKeyConstraint('argument_id', 'aspect_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arguments_aspects')
    # ### end Alembic commands ###
