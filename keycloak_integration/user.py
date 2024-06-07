from functools import wraps
from flask import request, g
from keycloak import KeycloakOpenID
import os


keycloak_openid = KeycloakOpenID(
    server_url=os.getenv("KEYCLOAK_SERVER_URL"),
    client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
    realm_name=os.getenv("USER_REALM_NAME"),
    client_secret_key=os.getenv("CLIENT_SECRET_KEY")
)


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Authentication required"}, 401

        token = auth_header.split(" ")[1]

        try:
            token_info = keycloak_openid.introspect(token)
            if not token_info.get("active"):
                return {"message": "Invalid token"}, 401
        except Exception as e:
            print("Auth error:", e)
            return {"message": "Invalid token"}, 401

        g.user_id = token_info["sub"]

        return func(*args, **kwargs)

    return wrapper


# def authenticate(func):
#     @wraps(func)
#     def wrapper(*args, Ⓑkwargs):
#         auth_header = request.headers.get('Authorization')
#         if not auth_header:
#             return jsonify({'message': 'Авторизация не предоставлена'}), 401
#
#         try:
#             token = auth_header.split(' ')[1]
#             payload = jwt.decode(token, KEYCLOAK_PUBLIC_KEY, algorithms=['RS256'])
#             if payload['iss'] != f'{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}' or payload['aud'] != KEYCLOAK_CLIENT_ID:
#                 return jsonify({'message': 'Недействительный токен'}), 401
#
#             # Сохранение ID пользователя в flask.g
#             g.user_id = payload['sub']
#
#         except jwt.ExpiredSignatureError:
#             return jsonify({'message': 'Токен истек'}), 401
#         except jwt.JWTClaimsError:
#             return jsonify({'message': 'Недействительный токен'}), 401
#         except Exception:
#             return jsonify({'message': 'Ошибка авторизации'}), 401
#
#         return func(*args, Ⓑkwargs)
#
#     return wrapper
