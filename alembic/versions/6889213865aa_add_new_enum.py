"""add new enum

Revision ID: 6889213865aa
Revises: 5fbba5385e6c
Create Date: 2025-09-15 19:45:39.333520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = '6889213865aa'
down_revision: Union[str, Sequence[str], None] = '5fbba5385e6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE pets MODIFY COLUMN cor "
        "ENUM('branco','preto','cinza','marrom','amarelo','laranja','rajado') NOT NULL"
    )


def downgrade() -> None:
    op.execute(
        "ALTER TABLE pets MODIFY COLUMN cor "
        "ENUM('branco','preto','cinza','marrom','amarelo','laranja') NOT NULL"
    )
