"""Add DatasetRow only

Revision ID: 28fa6a6c63d0
Revises: 
Create Date: 2025-06-25 15:28:30.776455

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '28fa6a6c63d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key(
        constraint_name='fk_auditlog_user_id',
        source_table='audit_log',
        referent_table='users',
        local_cols=['user_id'],
        remote_cols=['id']
    )

def downgrade():
    op.drop_constraint(
        constraint_name='fk_auditlog_user_id',
        table_name='audit_log',
        type_='foreignkey'
    )