"""empty message

Revision ID: 181542925b5e
Revises: b7166eaba029
Create Date: 2018-12-14 09:16:54.116978

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '181542925b5e'
down_revision = 'b7166eaba029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'c_time',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.add_column('user', sa.Column('u_head', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'u_head')
    op.alter_column('comment', 'c_time',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
