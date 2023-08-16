"""db_criar_banco

Revision ID: 9a9748f03bf7
Revises: 2b058e3498ae
Create Date: 2023-08-16 11:45:32.274868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a9748f03bf7'
down_revision = '2b058e3498ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastro_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('sobrenome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('senha', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cadastro_model')
    # ### end Alembic commands ###