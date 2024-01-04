from backend.models import db, Notification, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_notifications():
    # Notification for a new task assignment in Creative Hub
    notification1 = Notification(
        id=1,
        user_id=1,  # Assuming this user is assigned the task
        title="New Task Assigned: Logo Design",
        message="You have been assigned a new task 'Logo Design' in the Creative Hub workspace.",
        status="unread",
        link=""
    )

    # Notification for project kickoff in Tech Innovators
    notification2 = Notification(
        id=2,
        user_id=3,  # User associated with the Tech Innovators workspace
        title="Project Kickoff: Smart Home Ecosystem",
        message="The 'Smart Home Ecosystem' project in Tech Innovators is starting. Check the project details and upcoming tasks.",
        status="read",
        link=""
    )

    # Notification for a new task in Eco Warriors
    notification3 = Notification(
        id=3,
        user_id=5,
        title="New Task: Green Energy Workshop",
        message="A new task 'Green Energy Workshop' has been created in the Eco Warriors workspace.",
        status="unread",
        link=""
    )

    # Notification for completion of a task in Finance Gurus
    notification4 = Notification(
        id=4,
        user_id=8,
        title="Task Completed: Quarterly Financial Report",
        message="The 'Quarterly Financial Report' task in Finance Gurus has been marked as complete.",
        status="read",
        link=""
    )

    # Notification for being added to a project in Health & Wellness
    notification5 = Notification(
        id=5,
        user_id=9,
        title="Added to Project: Wellness and Mindfulness Series",
        message="You have been added to the 'Wellness and Mindfulness Series' project in the Health & Wellness workspace.",
        status="unread",
        link=""
    )

    # Notification for task deadline reminder in Creative Hub
    notification6 = Notification(
        id=6,
        user_id=2,
        title="Task Deadline Approaching: Website Redesign",
        message="The deadline for the 'Website Redesign' task in Creative Hub is approaching.",
        status="unread",
        link=""
    )

    # Notification for new project in Tech Innovators
    notification7 = Notification(
        id=7,
        user_id=4,
        title="New Project: AI Development",
        message="A new project 'AI Development' has been created in the Tech Innovators workspace.",
        status="read",
        link=""
    )

    # Notification for task update in Eco Warriors
    notification8 = Notification(
        id=8,
        user_id=6,
        title="Task Update: Recycling Initiative",
        message="There is an important update on the 'Recycling Initiative' task in Eco Warriors.",
        status="unread",
        link=""
    )

    # Notification for project completion in Finance Gurus
    notification9 = Notification(
        id=9,
        user_id=7,
        title="Project Completed: Financial Planning and Reporting",
        message="The 'Financial Planning and Reporting' project in Finance Gurus is now complete.",
        status="read",
        link=""
    )

    # Notification for workshop reminder in Health & Wellness
    notification10 = Notification(
        id=10,
        user_id=10,
        title="Workshop Reminder: Yoga Workshop Organization",
        message="Reminder: The 'Yoga Workshop Organization' event is happening this weekend in Health & Wellness.",
        status="unread",
        link=""
    )

    # Notification for new team member in Creative Hub
    notification11 = Notification(
        id=11,
        user_id=1,
        title="New Team Member in Creative Hub",
        message="A new member has joined your team in the Creative Hub workspace.",
        status="read",
        link=""
    )

    # Notification for software update in Tech Innovators
    notification12 = Notification(
        id=12,
        user_id=3,
        title="Software Update Required",
        message="Please update your software to the latest version in the Tech Innovators workspace.",
        status="unread",
        link=""
    )

    # Notification for event participation in Eco Warriors
    notification13 = Notification(
        id=13,
        user_id=5,
        title="Event Participation: Eco Conference",
        message="You are invited to participate in the upcoming Eco Conference in the Eco Warriors workspace.",
        status="read",
        link=""
    )

    # Notification for new investment opportunity in Finance Gurus
    notification14 = Notification(
        id=14,
        user_id=8,
        title="New Investment Opportunity",
        message="A new investment opportunity has been identified in the Finance Gurus workspace.",
        status="unread",
        link=""
    )

    # Notification for health challenge in Health & Wellness
    notification15 = Notification(
        id=15,
        user_id=9,
        title="Health Challenge: 30 Days Fitness",
        message="Join the '30 Days Fitness' challenge starting next week in Health & Wellness.",
        status="read",
        link=""
    )


    db.session.add(notification1)
    db.session.add(notification2)
    db.session.add(notification3)
    db.session.add(notification4)
    db.session.add(notification5)
    db.session.add(notification6)
    db.session.add(notification7)
    db.session.add(notification8)
    db.session.add(notification9)
    db.session.add(notification10)
    db.session.add(notification11)
    db.session.add(notification12)
    db.session.add(notification13)
    db.session.add(notification14)
    db.session.add(notification15)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_notifications():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.notifications RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM notifications"))

    db.session.commit()
