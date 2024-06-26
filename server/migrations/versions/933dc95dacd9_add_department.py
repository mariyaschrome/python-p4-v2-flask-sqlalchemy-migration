"""add Department

Revision ID: 933dc95dacd9
Revises: 1b6a6dc461e6
Create Date: 2024-06-26 11:29:47.575770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933dc95dacd9'
down_revision = '1b6a6dc461e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
