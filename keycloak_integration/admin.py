from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
from flask import request
from functools import wraps
import requests
import os


keycloak_connection = KeycloakOpenIDConnection(
    server_url=os.getenv("KEYCLOAK_SERVER_URL"),
    username=os.getenv("KEYCLOAK_ADMIN_USERNAME"),
    password=os.getenv("KEYCLOAK_ADMIN_PASSWORD"),
    realm_name=os.getenv("KEYCLOAK_REALM_NAME"),
    user_realm_name=os.getenv("KEYCLOAK_USER_REALM_NAME"),
    client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
    client_secret_key=os.getenv("KEYCLOAK_CLIENT_SECRET_KEY"),
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
            "Authorization": f"client_id={os.getenv('KEYCLOAK_CLIENT_ID')}, "
                             f"client_secret={os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"token": token}
        response = requests.post(f"{os.getenv('KEYCLOAK_SERVER_URL')}/realms/{os.getenv('KEYCLOAK_USER_REALM_NAME')}"
                                 f"/protocol/openid-connect/token/introspect",
                                 headers=headers, data=data)

        if response.status_code == 200:
            if response.json().get('active') and response.json().get('client_id') == os.getenv("KEYCLOAK_CLIENT_ID"):
                return func(*args, **kwargs)
            else:
                return "Unauthorized", 401
        else:
            return "Unauthorized", 401

    return wrapper
