from backend.models import db, Project, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_projects():
    # Project for Creative Hub
    project1 = Project(
        id=1,
        workspace_id=1,  # Creative Hub
        owner_id=1,  # Assigning a user as the owner
        name="Art and Design Expo",
        description="A comprehensive project to organize a large-scale art and design exhibition, including branding, marketing, and website development."
    )

    # Project for Tech Innovators
    project2 = Project(
        id=2,
        workspace_id=2,  # Tech Innovators
        owner_id=2,  # Assigning a different user as the owner
        name="Smart Home Ecosystem",
        description="Development of a series of interconnected tech solutions for smart homes, including app development and cybersecurity enhancements."
    )

    # Project for Eco Warriors
    project3 = Project(
        id=3,
        workspace_id=3,  # Eco Warriors
        owner_id=3,
        name="Sustainable Living Campaign",
        description="A series of initiatives aimed at promoting sustainable living practices, including recycling programs and educational workshops."
    )

    # Project for Finance Gurus
    project4 = Project(
        id=4,
        workspace_id=4,  # Finance Gurus
        owner_id=4,
        name="Financial Planning and Reporting",
        description="Focused on developing comprehensive investment strategies and financial reporting for the upcoming quarters."
    )

    # Project for Health & Wellness
    project5 = Project(
        id=5,
        workspace_id=5,  # Health & Wellness
        owner_id=5,
        name="Wellness and Mindfulness Series",
        description="Organizing events and creating content related to yoga, meditation, and overall wellness, including workshops and blog updates."
    )

    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.add(project4)
    db.session.add(project5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_projects():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.projects RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM projects"))

    db.session.commit()
