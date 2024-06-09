from flask import request, g
from functools import wraps
from keycloak import KeycloakOpenID
import consts


keycloak_openid = KeycloakOpenID(
    server_url=consts.KEYCLOAK_SERVER_URL,
    client_id=consts.KEYCLOAK_CLIENT_ID,
    realm_name=consts.KEYCLOAK_USER_REALM_NAME,
    client_secret_key=consts.KEYCLOAK_CLIENT_SECRET_KEY
)


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Authentication required"}, 401

        token = auth_header.split(" ")[1]
        print(token)

        try:
            token_info = keycloak_openid.introspect(token)
            print(token_info)
            if not token_info.get("active"):
                print("Invalid token active")
                return {"message": "Invalid token"}, 401
        except Exception as e:
            print("Auth error:", e)
            return {"message": "Invalid token"}, 401

        g.user_id = token_info["sub"]
        g.user_name = token_info["preferred_username"]

        return func(*args, **kwargs)

    return wrapper
