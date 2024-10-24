"""Make organization names unique

Revision ID: 5f2db2436c6f
Revises: 1f58a379c779
Create Date: 2024-10-24 04:46:09.379998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f2db2436c6f'
down_revision: Union[str, None] = '1f58a379c779'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'organizations', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'organizations', type_='unique')
    # ### end Alembic commands ###
