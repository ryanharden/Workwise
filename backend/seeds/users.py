from backend.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        id=1,
        first_name='demo',
        last_name= 'user',
        username='Demo',
        email='demo@gmail.com',
        password='password',
        image_url=""
    )
    ryan = User(
        id=2,
        first_name='ryan',
        last_name='harden',
        username='ryan',
        email='ryan@gmail.com',
        password='password',
        image_url=""
    )
    jason = User(
        id=3,
        first_name='jason',
        last_name='allen',
        username='jason',
        email='jason@gmail.com',
        password='password',
        image_url=""
    )

    sophia = User(
        id=4,
        first_name='sophia',
        last_name='martinez',
        username='sophia',
        email='sophia@gmail.com',
        password='password',
        image_url=""
    )

    michael = User(
        id=5,
        first_name='michael',
        last_name='johnson',
        username='michael',
        email='michael@gmail.com',
        password='password',
        image_url=""
    )

    emma = User(
        id=6,
        first_name='emma',
        last_name='lee',
        username='emma',
        email='emma@gmail.com',
        password='password',
        image_url=""
    )

    olivia = User(
        id=7,
        first_name='olivia',
        last_name='smith',
        username='olivia',
        email='olivia@gmail.com',
        password='password',
        image_url=""
    )

    william = User(
        id=8,
        first_name='william',
        last_name='davis',
        username='william',
        email='william@gmail.com',
        password='password',
        image_url=""
    )

    ava = User(
        id=9,
        first_name='ava',
        last_name='garcia',
        username='ava',
        email='ava@gmail.com',
        password='password',
        image_url=""
    )

    james = User(
        id=10,
        first_name='james',
        last_name='martin',
        username='james',
        email='james@gmail.com',
        password='password',
        image_url=""
    )


    db.session.add(demo)
    db.session.add(ryan)
    db.session.add(jason)
    db.session.add(sophia)
    db.session.add(michael)
    db.session.add(emma)
    db.session.add(olivia)
    db.session.add(william)
    db.session.add(ava)
    db.session.add(james)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
