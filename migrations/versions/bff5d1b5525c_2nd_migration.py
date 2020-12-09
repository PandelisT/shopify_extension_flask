"""2nd migration

Revision ID: bff5d1b5525c
Revises: a8d251533f91
Create Date: 2020-12-09 14:06:30.007353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff5d1b5525c'
down_revision = 'a8d251533f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.drop_column('tags', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('notes', 'customer_id')
    # ### end Alembic commands ###