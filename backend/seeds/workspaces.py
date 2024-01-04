from backend.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from backend.models import Workspace


# Adds a demo user, you can add other users here if you want
def seed_workspaces():
    workspace1 = Workspace(
    id=1,
    name="Creative Hub",
    description="A vibrant space for artists and designers to collaborate and innovate.",
    owner_id=1,
    visibility="public",
    workspace_image_url=""
    )

    workspace2 = Workspace(
        id=2,
        name="Tech Innovators",
        description="Focused on cutting-edge technology and software development projects.",
        owner_id=2,
        visibility="private",
        workspace_image_url=""
    )

    workspace3 = Workspace(
        id=3,
        name="Eco Warriors",
        description="Dedicated to environmental projects and sustainable practices.",
        owner_id=3,
        visibility="public",
        workspace_image_url=""
    )

    workspace4 = Workspace(
        id=4,
        name="Finance Gurus",
        description="A hub for finance professionals to discuss market trends and strategies.",
        owner_id=4,
        visibility="private",
        workspace_image_url=""
    )

    workspace5 = Workspace(
        id=5,
        name="Health & Wellness",
        description="Focused on healthcare, fitness, and overall well-being discussions.",
        owner_id=5,
        visibility="public",
        workspace_image_url=""
    )

    db.session.add(workspace1)
    db.session.add(workspace2)
    db.session.add(workspace3)
    db.session.add(workspace4)
    db.session.add(workspace5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_workspaces():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.workspaces RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM workspaces"))

    db.session.commit()
