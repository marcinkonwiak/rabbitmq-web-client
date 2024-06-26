"""Initial migration

Revision ID: e382c3bed0f5
Revises: 
Create Date: 2024-03-23 21:39:28.821770+00:00

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision: str = 'e382c3bed0f5'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('amqp_url', sa.String(), nullable=True),
    sa.Column('routing_key', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.Column('content_encoding', sa.String(), nullable=True),
    sa.Column('headers', sqlite.JSON(), nullable=True),
    sa.Column('delivery_mode', sa.Enum('Transient', 'Persistent', name='deliverymode'), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('correlation_id', sa.String(), nullable=True),
    sa.Column('reply_to', sa.String(), nullable=True),
    sa.Column('expiration', sa.String(), nullable=True),
    sa.Column('amqp_message_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.String(length=10), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('app_id', sa.String(), nullable=True),
    sa.Column('cluster_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.Column('inherit_settings', sa.Boolean(), nullable=False),
    sa.Column('amqp_url', sa.String(), nullable=True),
    sa.Column('routing_key', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.Column('content_encoding', sa.String(), nullable=True),
    sa.Column('headers', sqlite.JSON(), nullable=True),
    sa.Column('delivery_mode', sa.Enum('Transient', 'Persistent', name='deliverymode'), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('correlation_id', sa.String(), nullable=True),
    sa.Column('reply_to', sa.String(), nullable=True),
    sa.Column('expiration', sa.String(), nullable=True),
    sa.Column('amqp_message_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.String(length=10), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('app_id', sa.String(), nullable=True),
    sa.Column('cluster_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('collection')
    # ### end Alembic commands ###
