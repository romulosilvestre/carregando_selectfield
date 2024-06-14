"""adicionando telefone na escola

Revision ID: 3e75c31ec399
Revises: b5be3feda246
Create Date: 2024-06-14 15:25:36.460494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e75c31ec399'
down_revision = 'b5be3feda246'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('escola', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telefone', sa.String(length=25), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('escola', schema=None) as batch_op:
        batch_op.drop_column('telefone')

    # ### end Alembic commands ###
