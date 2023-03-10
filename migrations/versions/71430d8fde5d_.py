"""empty message

Revision ID: 71430d8fde5d
Revises: 
Create Date: 2023-03-07 19:30:18.184248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71430d8fde5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pm_chats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('profile_img', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('chat_users',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['pm_chats.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('chat_id', 'user_id')
    )
    op.create_table('pm_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=750), nullable=True),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['chat_id'], ['pm_chats.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('server_image', sa.String(length=1000), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('server_users',
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('server_id', 'user_id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=750), nullable=True),
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['messages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message_images')
    op.drop_table('messages')
    op.drop_table('server_users')
    op.drop_table('channels')
    op.drop_table('servers')
    op.drop_table('pm_messages')
    op.drop_table('chat_users')
    op.drop_table('users')
    op.drop_table('pm_chats')
    # ### end Alembic commands ###
