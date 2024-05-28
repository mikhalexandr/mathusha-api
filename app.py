from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os

from data import db_session
from resources import *


load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def check_work():
    return "OK"


def add_resources():
    api = Api(app)


def main():
    if not os.path.isdir("db"):
        os.mkdir("db")
    db_session.global_init("db/MathGenerator.db")
    add_resources()
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))


if __name__ == "__main__":
    main()
