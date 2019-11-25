"""empty message

Revision ID: 185b3417fa80
Revises: 825c54ec76e9
Create Date: 2019-04-27 16:32:52.844506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '185b3417fa80'
down_revision = '825c54ec76e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attachments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thesis_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=False),
    sa.Column('payload', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['thesis_id'], ['theses.id'], name='attachments__thesis__fk'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attachments')
    # ### end Alembic commands ###