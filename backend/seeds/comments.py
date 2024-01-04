from backend.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_comments():
    # Comment on Task 1 (Logo Design in Creative Hub)
    comment1 = Comment(
        id=1,
        task_id=1,
        comment_id=1,  # Self-referencing for top-level comment
        author_id=2,  # User commenting on the task
        body="I've started sketching some initial concepts for the logo. Feedback is welcome!"
    )

    # Comment on Task 2 (Website Redesign in Creative Hub)
    comment2 = Comment(
        id=2,
        task_id=2,
        comment_id=2,
        author_id=1,
        body="Let's ensure the new design aligns with our exhibition themes. I'll post some layout ideas soon."
    )

    # Comment on Task 3 (App Development in Tech Innovators)
    comment3 = Comment(
        id=3,
        task_id=3,
        comment_id=3,
        author_id=4,
        body="I've implemented the first set of features in the app. Check it out and let me know your thoughts."
    )

    # Comment on Task 4 (Cybersecurity Update in Tech Innovators)
    comment4 = Comment(
        id=4,
        task_id=4,
        comment_id=4,
        author_id=3,
        body="The security protocols are updated. Please review the documentation and provide feedback."
    )

    # Comment on Task 5 (Recycling Initiative in Eco Warriors)
    comment5 = Comment(
        id=5,
        task_id=5,
        comment_id=5,
        author_id=6,
        body="I have some ideas to increase community engagement in our recycling program. Let's discuss."
    )

    # Comment on Task 6 (Green Energy Workshop in Eco Warriors)
    comment6 = Comment(
        id=6,
        task_id=6,
        comment_id=6,
        author_id=5,
        body="I've contacted a few experts in renewable energy to speak at our workshop."
    )

    # Comment on Task 7 (Investment Strategy Meeting in Finance Gurus)
    comment7 = Comment(
        id=7,
        task_id=7,
        comment_id=7,
        author_id=8,
        body="The meeting agenda is set. I've emailed the topics we'll cover, including new investment areas."
    )

    # Comment on Task 8 (Quarterly Financial Report in Finance Gurus)
    comment8 = Comment(
        id=8,
        task_id=8,
        comment_id=8,
        author_id=7,
        body="The draft of the financial report is ready. I need inputs on the forecast section."
    )

    # Comment on Task 9 (Yoga Workshop Organization in Health & Wellness)
    comment9 = Comment(
        id=9,
        task_id=9,
        comment_id=9,
        author_id=10,
        body="Can someone update on the status of the venue booking for the yoga workshop?"
    )

    # Comment on Task 10 (Health Blog Update in Health & Wellness)
    comment10 = Comment(
        id=10,
        task_id=10,
        comment_id=10,
        author_id=9,
        body="I've added a new article on nutrition tips. It would be great if someone could review it."
    )

    # Comment on Task 1 (Logo Design in Creative Hub) - Follow-up
    comment11 = Comment(
        id=11,
        task_id=1,
        comment_id=1,  # Related to the first comment on this task
        author_id=3,
        body="I love the initial concepts! Maybe we can try integrating more vibrant colors?"
    )

    # Comment on Task 3 (App Development in Tech Innovators) - Additional Feedback
    comment12 = Comment(
        id=12,
        task_id=3,
        comment_id=3,  # Follow-up on the app development
        author_id=2,
        body="The app's interface is user-friendly, but we need to work on faster response times."
    )

    # Comment on Task 7 (Investment Strategy Meeting in Finance Gurus) - Query
    comment13 = Comment(
        id=13,
        task_id=7,
        comment_id=7,  # Related to the meeting agenda
        author_id=10,
        body="Are we also discussing the impact of recent market fluctuations on our investments?"
    )

    # Comment on Task 5 (Recycling Initiative in Eco Warriors) - Suggestion
    comment14 = Comment(
        id=14,
        task_id=5,
        comment_id=5,  # Regarding the recycling program
        author_id=9,
        body="Perhaps we could partner with local schools to broaden the reach of our recycling program."
    )

    # Comment on Task 10 (Health Blog Update in Health & Wellness) - Appreciation
    comment15 = Comment(
        id=15,
        task_id=10,
        comment_id=10,  # Related to the health blog update
        author_id=6,
        body="Great article on nutrition! I've added a few comments on recent dietary research trends."
    )


    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)
    db.session.add(comment6)
    db.session.add(comment7)
    db.session.add(comment8)
    db.session.add(comment9)
    db.session.add(comment10)
    db.session.add(comment11)
    db.session.add(comment12)
    db.session.add(comment13)
    db.session.add(comment14)
    db.session.add(comment15)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
