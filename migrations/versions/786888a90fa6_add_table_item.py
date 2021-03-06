"""add table Item

Revision ID: 786888a90fa6
Revises: c0023538cac0
Create Date: 2022-04-20 21:26:46.568553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '786888a90fa6'
down_revision = 'c0023538cac0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('price', sa.Numeric(precision=9, scale=2), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
