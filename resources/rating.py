from flask_restful import Resource, abort
from flask import jsonify, request

from data import db_session
from data.users import User
# from app import oidc


class RatingResource(Resource):
    @staticmethod
    # @oidc.require_login
    def get():
        name = request.json["name"]
        session = db_session.create_session()
        users = session.query(User).all()
        leaders = []
        for user in users:
            leaders.append(
                    {
                        "name": user.name,
                    }
            )
        sorted_leaders = sorted(leaders, key=lambda x: (-x["level_amount"], x["time"]))
        user_index = 0
        try:
            user_index = [x for x in range(len(sorted_leaders)) if sorted_leaders[x]["name"] == name][0]
        except IndexError:
            abort(404, message=f"User [{name}] is not found")
        result = [sorted_leaders, user_index + 1]
        return jsonify(result)
