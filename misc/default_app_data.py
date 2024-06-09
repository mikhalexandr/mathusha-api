from data import db_session
from data.users import User
from data.achievements import Achievement
from data.topics import Topic


def create_default_data():
    session = db_session.create_session()
    u1 = User(id='test1', name='TestUser')
    u2 = User(id='test2', name='TestUser2')
    session.add(u1)
    session.add(u2)

    t1 = Topic(name='Math', description='Mathhhh', eng_name='Math', eng_description='Math', color='#00FF00')
    t2 = Topic(name='English', description='English', eng_name='English', eng_description='English', color='#FF0000')
    t3 = Topic(name='Russian', description='Russian', eng_name='Russian', eng_description='Russian', color='#0000FF')
    session.add(t1)
    session.add(t2)
    session.add(t3)

    a1 = Achievement(name='First achievement', eng_name='First achievement', description='First achievement',
                     eng_description='First achievement', type=1.1)
    a2 = Achievement(name='Second achievement', eng_name='Second achievement', description='Second achievement',
                     eng_description='Second achievement', type=2)
    a3 = Achievement(name='Third achievement', eng_name='Third achievement', description='Third achievement',
                     eng_description='Third achievement', type=3)
    session.add(a1)
    session.add(a2)
    session.add(a3)

    session.commit()
    session.close()
