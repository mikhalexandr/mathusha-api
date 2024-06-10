from flask import Flask
from flask_restful import Api
from flask_cors import CORS
# from flask_ngrok import run_with_ngrok
import os

# from misc import create_default_data
from data import db_session
from resources import *
import consts


app = Flask(__name__)
CORS(app, supports_credentials=True)
# run_with_ngrok(app)

app.config.update({
    "SECRET_KEY": consts.SECRET_KEY,
    "JSON_AS_ASCII": False,
    "UPLOAD_FOLDER": "assets",
    "MAX_CONTENT_LENGTH": consts.MAX_CONTENT_LENGTH,
    "ALLOWED_EXTENSIONS": consts.ALLOWED_EXTENSIONS
})


@app.route("/")
def check_work():
    return "OK"


if not os.path.isdir("db"):
    os.mkdir("db")
db_session.global_init("db/Mathusha.db")


api = Api(app)
api.add_resource(UserResource, '/api/user')
api.add_resource(UserPhotoResource, '/api/user/photo')
api.add_resource(TopicsResource, '/api/user/topics')
api.add_resource(TopicPhotoResource, '/api/user/topic_photo/<int:topic_id>')
api.add_resource(TopicDescriptionResource, '/api/user/topic_description/<int:topic_id>')
api.add_resource(TopicsForMixResource, '/api/user/topics_for_mix')
api.add_resource(TaskResource, '/api/user/task/<int:topic_id>')
api.add_resource(SolvedTaskResource, '/api/user/solved_task/<int:topic_id>')
api.add_resource(AchievementsResource, '/api/user/achievements')
api.add_resource(AchievementPhotoResource, '/api/user/achievement_photo/<int:achievement_id>')
api.add_resource(ProgressResource, '/api/user/progress')
api.add_resource(RatingResource, '/api/user/rating')
api.add_resource(LeaderPhotoResource, '/api/user/leader_photo/<leader_id>')

api.add_resource(AdminTopicsResource, '/api/admin/topics')
api.add_resource(AdminTopicResource, '/api/admin/topic/<int:topic_id>')
api.add_resource(AdminTopicPhotoResource, '/api/admin/topic/photo/<int:topic_id>')
api.add_resource(AdminAddTopicResource, '/api/admin/topic/add')
api.add_resource(AdminAchievementsResource, '/api/admin/achievements')
api.add_resource(AdminAchievementResource, '/api/admin/achievement/<int:achievement_id>')
api.add_resource(AdminAchievementPhotoResource, '/api/admin/achievement/photo/<int:achievement_id>')
api.add_resource(AdminStatisticsResource, '/api/admin/statistics')


def main():
    # create_default_data()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
