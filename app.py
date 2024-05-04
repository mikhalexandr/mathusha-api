from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from data import db_session

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)


def main():
    db_session.global_init("db/MathGenerator.db")
    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()
