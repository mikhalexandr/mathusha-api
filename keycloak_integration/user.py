from flask import request, g
from functools import wraps

import consts


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Authentication required"}, 401

        token = auth_header.split(" ")[1]

        try:
            token_info = consts.keycloak_openid.introspect(token)
            if not token_info.get("active"):
                return {"message": "Invalid token"}, 401
        except Exception as e:
            return {"message": f"Invalid token with error [{e}]"}, 401

        g.user_id = token_info["sub"]
        g.user_name = token_info["preferred_username"]

        return func(*args, **kwargs)

    return wrapper
