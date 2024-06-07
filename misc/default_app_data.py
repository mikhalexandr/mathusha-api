from data import db_session
from data.users import User
from data.user_progress import UserProgress
from data.topics import Topic


def create_default_data():
    session = db_session.create_session()
    u1 = User(id='1', username='Alex')
    u2 = User(id='2', username='NeAlex')
    session.add(u1)
    session.add(u2)

    t1 = Topic(name='Math', description='Mathhhh', image='math.png')
    t2 = Topic(name='English', description='English', image='english.png')
    session.add(t1)
    session.add(t2)

    p1 = UserProgress(user_id='1', topic_id='1')
    p2 = UserProgress(user_id='1', topic_id='2')
    p3 = UserProgress(user_id='2', topic_id='1')
    p4 = UserProgress(user_id='2', topic_id='2')
    session.add(p1)
    session.add(p2)
    session.add(p3)
    session.add(p4)

    session.commit()
