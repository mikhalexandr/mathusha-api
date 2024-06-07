from flask import Flask
from flask_restful import Api
from flask_cors import CORS
# from flask_ngrok import run_with_ngrok
from dotenv import load_dotenv
import os

from misc import create_base_things
from data import db_session
from resources import *


load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
# run_with_ngrok(app)


app.config.update({
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "JSON_AS_ASCII": False,
})


@app.route("/")
def check_work():
    return "OK"


def add_resources():
    api = Api(app)


def main():
    if not os.path.isdir("db"):
        os.mkdir("db")
    db_session.global_init("db/Mathusha.db")
    create_base_things()
    add_resources()
    app.run()


if __name__ == "__main__":
    main()
