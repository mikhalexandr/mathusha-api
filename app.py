from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_oidc import OpenIDConnect
from dotenv import load_dotenv
import os

from data import db_session
from resources import *


load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config.update({
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "JSON_AS_ASCII": False,
    # "OIDC_CLIENT_SECRETS": "client_secrets.json",
    # "OIDC_CALLBACK_ROUTE": "/oidc/callback",
    # "OIDC_SCOPES": ["openid", "email", "profile"]
})

# oidc = OpenIDConnect(app)


@app.route("/")
def check_work():
    return "OK"


def add_resources():
    api = Api(app)
    api.add_resource(RatingResource, "api/rating")


def main():
    if not os.path.isdir("db"):
        os.mkdir("db")
    db_session.global_init("db/MathGenerator.db")
    add_resources()
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))


if __name__ == "__main__":
    main()
