from flask.cli import AppGroup
from .users import seed_users, undo_users
from .workspaces import seed_workspaces, undo_workspaces
from .projects import seed_projects, undo_projects
from .tasks import seed_tasks, undo_tasks
from .comments import seed_comments, undo_comments
from .notifications import seed_notifications, undo_notifications

from backend.models.db import db, environment, SCHEMA

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
        undo_notifications()
        undo_comments()
        undo_tasks()
        undo_projects()
        undo_workspaces()
        undo_users()
    seed_users()
    seed_workspaces()
    seed_projects()
    seed_tasks()
    seed_comments()
    seed_notifications()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_notifications()
    undo_comments()
    undo_tasks()
    undo_projects()
    undo_workspaces()
    undo_users()
    # Add other undo functions here
