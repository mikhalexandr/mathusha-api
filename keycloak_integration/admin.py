# from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
# from flask import request, jsonify
# from functools import wraps

import consts

keycloak_admin = None
# keycloak_connection = KeycloakOpenIDConnection(
#     server_url=consts.KEYCLOAK_SERVER_URL,
#     username=consts.KEYCLOAK_ADMIN_USERNAME,
#     password=consts.KEYCLOAK_ADMIN_PASSWORD,
#     realm_name=consts.KEYCLOAK_REALM_NAME,
#     user_realm_name=consts.KEYCLOAK_USER_REALM_NAME,
#     client_id=consts.KEYCLOAK_CLIENT_ID,
#     client_secret_key=consts.KEYCLOAK_CLIENT_SECRET_KEY,
#     verify=True)
#
# keycloak_admin = KeycloakAdmin(connection=keycloak_connection)


def admin_required(func):
    pass
