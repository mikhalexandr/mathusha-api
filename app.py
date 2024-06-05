from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_oidc import OpenIDConnect
# from flask_ngrok import run_with_ngrok
from keycloak import KeycloakOpenID
from dotenv import load_dotenv
import os

from data import db_session
from resources import *


load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
# run_with_ngrok(app)

oidc = OpenIDConnect(app)

keycloak_openid = KeycloakOpenID(server_url=os.getenv("SERVER_URL"),
                                 client_id=os.getenv("CLIENT_ID"),
                                 realm_name=os.getenv("REALM_NAME"),
                                 client_secret_key=os.getenv("CLIENT_SECRET_KEY"))

app.config.update({
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "JSON_AS_ASCII": False,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'login-app',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
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
    add_resources()
    app.run()


if __name__ == "__main__":
    main()
