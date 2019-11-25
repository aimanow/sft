"""empty message

Revision ID: 37875abb00c7
Revises: 185b3417fa80
Create Date: 2019-04-27 17:46:28.669175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37875abb00c7'
down_revision = '185b3417fa80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('claims', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('claims__user__fk', 'claims', 'users', ['user_id'], ['id'])
    op.drop_constraint('claims_statuses__claim__fk', 'claims_statuses', type_='foreignkey')
    op.create_foreign_key('claims_statuses__claim__fk', 'claims_statuses', 'claims', ['claim_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('claims_statuses__claim__fk', 'claims_statuses', type_='foreignkey')
    op.create_foreign_key('claims_statuses__claim__fk', 'claims_statuses', 'claims', ['claim_id'], ['id'])
    op.drop_constraint('claims__user__fk', 'claims', type_='foreignkey')
    op.drop_column('claims', 'user_id')
    # ### end Alembic commands ###