"""create pets table

Revision ID: 39a8c15ab1ee
Revises: 
Create Date: 2025-09-20 22:34:47.070701

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import CHAR, ENUM, TINYINT

# revision identifiers, used by Alembic.
revision: str = '39a8c15ab1ee'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: create pets table."""
    op.create_table(
        'pets',
        sa.Column('id', CHAR(36), primary_key=True, nullable=False),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('data_nascimento', sa.Date(), nullable=False),
        sa.Column('tipo', ENUM('Gato', 'Cachorro', 'Cavalo', 'Lagarto'), nullable=False),
        sa.Column('raca', ENUM(
            'Siamese', 'Persian', 'Maine Coon', 'Labrador', 'Bulldog', 'Poodle',
            'Andaluz', 'Árabe', 'Quarto de Milha', 'Iguana', 'Dragão Barbado', 'Gecko', 'SRD'
        ), nullable=False),
        sa.Column('cor', ENUM('Branco', 'Preto', 'Cinza', 'Marrom', 'Amarelo', 'Laranja', 'Rajado'), nullable=False),
        sa.Column('castrado', TINYINT(display_width=1), nullable=True, default=0),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )


def downgrade() -> None:
    """Downgrade schema: drop pets table."""
    op.drop_table('pets')
