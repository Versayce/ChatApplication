from flask.cli import AppGroup
from .users import seed_users, undo_users
from .channels import seed_channels, undo_channels
from .messages import seed_message_images, seed_messages, undo_message_images, undo_messages
from .pm_chats import seed_pm_chats, undo_pm_chats
from .pm_messages import seed_pm_messages, undo_pm_messages
from .servers import seed_servers, undo_server

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_pm_messages
        undo_pm_chats()
        undo_message_images()
        undo_messages()
        undo_channels()
        undo_server()
        undo_users()
    seed_users()
    seed_servers()
    seed_channels()
    seed_messages()
    seed_message_images()
    seed_pm_chats()
    seed_pm_messages()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # Add other undo functions here
    undo_message_images()
    undo_messages()
    undo_channels()
    undo_server()
    undo_users()
