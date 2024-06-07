from sqlalchemy import func

from data.topics import Topic
from data.achievements import Achievement
from data.user_progress import UserProgress
from data.user_achievements import UserAchievement


def user_data_generation(session, user_id):
    topics_count = session.query(func.count('*')).select_from(Topic).scalar()
    achievements_count = session.query(func.count('*')).select_from(Achievement).scalar()
    for i in range(1, topics_count + 1):
        user_progress = UserProgress(
            user_id=user_id,
            topic_id=i
        )
        session.add(user_progress)
    for i in range(1, achievements_count + 1):
        user_achievement = UserAchievement(
            user_id=user_id,
            achievement_id=i
        )
        session.add(user_achievement)
    session.commit()
