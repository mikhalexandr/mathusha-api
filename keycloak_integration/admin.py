from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
from flask import request
from functools import wraps
import requests

import consts


keycloak_connection = KeycloakOpenIDConnection(
    server_url=consts.KEYCLOAK_SERVER_URL,
    username=consts.KEYCLOAK_ADMIN_USERNAME,
    password=consts.KEYCLOAK_ADMIN_PASSWORD,
    realm_name=consts.KEYCLOAK_REALM_NAME,
    user_realm_name=consts.KEYCLOAK_USER_REALM_NAME,
    client_id=consts.KEYCLOAK_CLIENT_ID,
    client_secret_key=consts.KEYCLOAK_CLIENT_SECRET_KEY,
    verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return "Authorization header is missing", 401

        if not auth_header.startswith('Bearer '):
            return "Invalid authorization header", 401

        token = auth_header.split(' ')[1]

        headers = {
            "Authorization": f"client_id={consts.KEYCLOAK_CLIENT_ID}, "
                             f"client_secret={consts.KEYCLOAK_CLIENT_SECRET_KEY}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"token": token}
        response = requests.post(f"{consts.KEYCLOAK_SERVER_URL}/realms/{consts.KEYCLOAK_USER_REALM_NAME}"
                                 f"/protocol/openid-connect/token/introspect",
                                 headers=headers, data=data)

        if response.status_code == 200:
            if response.json().get('active') and response.json().get('client_id') == consts.KEYCLOAK_CLIENT_ID:
                return func(*args, **kwargs)
            else:
                return "Unauthorized", 401
        else:
            return "Unauthorized", 401

    return wrapper
