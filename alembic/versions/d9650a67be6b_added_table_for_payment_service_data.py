"""added_table_for_payment_service_data

Revision ID: d9650a67be6b
Revises: fe33a13e5b73
Create Date: 2024-06-02 10:14:29.227190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd9650a67be6b'
down_revision: Union[str, None] = 'fe33a13e5b73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_service_data',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('claim_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('net_fees', sa.DOUBLE_PRECISION(precision=53),
                              server_default=sa.text("'0'::double precision"), autoincrement=False, nullable=False),
                    sa.Column("notifying_status", sa.String(), nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='payment_service_data_pkey')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_service_data')
    # ### end Alembic commands ###
