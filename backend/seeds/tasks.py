from backend.models import db, Task, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_tasks():
    # Tasks for Creative Hub
    task1 = Task(
        id=1,
        title="Logo Design",
        workspace_id=1,
        description="Create a new logo for the upcoming art exhibition.",
        creator_id=1,  # Assuming there are 10 different users
        due_date=datetime(2024, 2, 10),
        status="Incomplete"
    )

    task2 = Task(
        id=2,
        title="Website Redesign",
        workspace_id=1,
        description="Redesign the Creative Hub's website for better user engagement.",
        creator_id=2,
        due_date=datetime(2024, 3, 15),
        status="In Progress"
    )

    # Tasks for Tech Innovators
    task3 = Task(
        id=3,
        title="App Development",
        workspace_id=2,
        description="Develop a mobile app for smart home management.",
        creator_id=3,
        due_date=datetime(2024, 4, 20),
        status="Incomplete"
    )

    task4 = Task(
        id=4,
        title="Cybersecurity Update",
        workspace_id=2,
        description="Implement new cybersecurity protocols for our software.",
        creator_id=4,
        due_date=datetime(2024, 5, 25),
        status="Complete"
    )

    # Tasks for Eco Warriors
    task5 = Task(
        id=5,
        title="Recycling Initiative",
        workspace_id=3,
        description="Plan a community-based recycling and awareness program.",
        creator_id=5,
        due_date=datetime(2024, 6, 30),
        status="In Progress"
    )

    task6 = Task(
        id=6,
        title="Green Energy Workshop",
        workspace_id=3,
        description="Organize a workshop on renewable energy sources.",
        creator_id=6,
        due_date=datetime(2024, 7, 5),
        status="Incomplete"
    )

    # Tasks for Finance Gurus
    task7 = Task(
        id=7,
        title="Investment Strategy Meeting",
        workspace_id=4,
        description="Host a meeting to discuss the Q2 investment strategies.",
        creator_id=7,
        due_date=datetime(2024, 8, 10),
        status="Complete"
    )

    task8 = Task(
        id=8,
        title="Quarterly Financial Report",
        workspace_id=4,
        description="Prepare the Q1 financial report for review.",
        creator_id=8,
        due_date=datetime(2024, 9, 15),
        status="In Progress"
    )

    # Tasks for Health & Wellness
    task9 = Task(
        id=9,
        title="Yoga Workshop Organization",
        workspace_id=5,
        description="Organize a weekend yoga and meditation workshop.",
        creator_id=9,
        due_date=datetime(2024, 10, 20),
        status="Incomplete"
    )

    task10 = Task(
        id=10,
        title="Health Blog Update",
        workspace_id=5,
        description="Update the blog with latest health and nutrition tips.",
        creator_id=10,
        due_date=datetime(2024, 11, 25),
        status="Complete"
    )


    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)
    db.session.add(task6)
    db.session.add(task7)
    db.session.add(task8)
    db.session.add(task9)
    db.session.add(task10)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tasks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tasks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tasks"))

    db.session.commit()
