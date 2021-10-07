"""Updated

Revision ID: 811310f49ee2
Revises: 
Create Date: 2021-10-08 00:07:19.179988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '811310f49ee2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('isbn', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###