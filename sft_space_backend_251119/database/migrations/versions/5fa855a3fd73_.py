"""empty message

Revision ID: 5fa855a3fd73
Revises: 7868dd125fb7
Create Date: 2019-04-26 13:32:31.495693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa855a3fd73'
down_revision = '7868dd125fb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('arguments_aspects__aspect__fk', 'arguments_aspects', type_='foreignkey')
    op.drop_constraint('arguments_aspects__argument__fk', 'arguments_aspects', type_='foreignkey')
    op.create_foreign_key('arguments_aspects__argument__fk', 'arguments_aspects', 'arguments', ['argument_id'], ['thesis_id'], ondelete='CASCADE')
    op.create_foreign_key('arguments_aspects__aspect__fk', 'arguments_aspects', 'aspects', ['aspect_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('arguments_aspects__aspect__fk', 'arguments_aspects', type_='foreignkey')
    op.drop_constraint('arguments_aspects__argument__fk', 'arguments_aspects', type_='foreignkey')
    op.create_foreign_key('arguments_aspects__argument__fk', 'arguments_aspects', 'arguments', ['argument_id'], ['thesis_id'])
    op.create_foreign_key('arguments_aspects__aspect__fk', 'arguments_aspects', 'aspects', ['aspect_id'], ['id'])
    # ### end Alembic commands ###