"""Renaming students to scholars

Revision ID: f35fe850ef93
Revises: ccfaf59dd4fc
Create Date: 2024-01-10 04:30:57.842065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f35fe850ef93'
down_revision: Union[str, None] = 'ccfaf59dd4fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
