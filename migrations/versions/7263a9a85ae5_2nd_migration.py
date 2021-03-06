"""2nd migration

Revision ID: 7263a9a85ae5
Revises: 0aaccb72f765
Create Date: 2020-12-11 14:51:52.589662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7263a9a85ae5'
down_revision = '0aaccb72f765'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tags_customer_id_fkey', 'tags', type_='foreignkey')
    op.drop_column('tags', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('tags_customer_id_fkey', 'tags', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###
