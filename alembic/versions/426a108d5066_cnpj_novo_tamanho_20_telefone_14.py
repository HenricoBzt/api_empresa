"""cnpj novo tamanho(20) | telefone (14)

Revision ID: 426a108d5066
Revises: 
Create Date: 2025-02-15 00:31:56.187899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '426a108d5066'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('empresas', 'cnpj',
               existing_type=sa.VARCHAR(length=14),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('empresas', 'telefone',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=14),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('empresas', 'telefone',
               existing_type=sa.String(length=14),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.alter_column('empresas', 'cnpj',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=14),
               existing_nullable=False)
    # ### end Alembic commands ###
