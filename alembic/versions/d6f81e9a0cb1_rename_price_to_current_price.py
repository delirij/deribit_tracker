"""rename_price_to_current_price

Revision ID: d6f81e9a0cb1
Revises: 40f2c862f630
Create Date: 2026-03-13 13:37:07.606553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6f81e9a0cb1'
down_revision: Union[str, Sequence[str], None] = '40f2c862f630'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('crypto_prices', 'current_price', new_column_name='price')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('crypto_prices', 'price', new_column_name='current_price')
