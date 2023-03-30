"""Added column teacher in books

Revision ID: 75033f740793
Revises: 71ca8eb9da33
Create Date: 2023-03-30 02:35:10.671244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75033f740793'
down_revision = '71ca8eb9da33'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('teacher', sa.String(), nullable=False))
    op.drop_column('books', 'professor')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('professor', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('books', 'teacher')
    # ### end Alembic commands ###
