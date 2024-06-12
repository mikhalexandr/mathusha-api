from keycloak import KeycloakOpenID
from dotenv import load_dotenv
import os


load_dotenv()

# secret keys
SECRET_KEY = os.getenv("SECRET_KEY")


# yandex gpt secrets
YANDEX_GPT_DIRECTORY_ID = os.getenv("YANDEX_GPT_DIRECTORY_ID")
YANDEX_GPT_API_KEY = os.getenv("YANDEX_GPT_API_KEY")


# keycloak secrets
KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL")
KEYCLOAK_USER_REALM_NAME = os.getenv("KEYCLOAK_USER_REALM_NAME")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET_KEY = os.getenv("KEYCLOAK_CLIENT_SECRET_KEY")

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_USER_REALM_NAME,
    client_secret_key=KEYCLOAK_CLIENT_SECRET_KEY
)


# configurations
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


# achievement triggers
solved_tasks_amount = [1000, 500, 100]
rating_amount = [200, 1000, 5000]
