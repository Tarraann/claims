"""add_tables_for_claims

Revision ID: fe33a13e5b73
Revises: 
Create Date: 2024-06-01 20:52:54.604451

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe33a13e5b73'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "providers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("npi", sa.Integer(), nullable=False),
        sa.CheckConstraint("npi >= 1000000000 AND npi <= 9999999999", name="npi_ten_digit_check"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "procedures",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("code", sa.String(), nullable=False),
        sa.CheckConstraint("code LIKE 'D%'", name="code_starts_with_d"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "plans",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("plan_group", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "subscribers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("subscribers", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_table(
        "claims",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("service_date", sa.DateTime(), nullable=False),
        sa.Column("quadrant", sa.String(), nullable=True),
        sa.Column("provider_id", sa.Integer(), nullable=False),
        sa.Column("procedure_id", sa.Integer(), nullable=False),
        sa.Column("plan_id", sa.Integer(), nullable=False),
        sa.Column("subscriber_id", sa.Integer(), nullable=False),
        sa.Column("provider_fees", sa.Float(), nullable=False, server_default="0"),
        sa.Column("allowed_fees", sa.Float(), nullable=False, server_default="0"),
        sa.Column("member_coinsurance", sa.Float(), nullable=False, server_default="0"),
        sa.Column("member_copay", sa.Float(), nullable=False, server_default="0"),
        sa.Column("net_fees", sa.Float(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id")
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("claims")
    op.drop_table("subscribers")
    op.drop_table("plans")
    op.drop_table("procedures")
    op.drop_table("providers")
    # ### end Alembic commands ###
