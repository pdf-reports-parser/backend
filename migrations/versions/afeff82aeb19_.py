"""

Revision ID: afeff82aeb19
Revises: f7e42dbb3bd6
Create Date: 2022-04-12 17:55:13.931359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afeff82aeb19'
down_revision = 'f7e42dbb3bd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trials', 'measure_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trials', 'measure_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
