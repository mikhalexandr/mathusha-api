from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
import os


keycloak_connection = KeycloakOpenIDConnection(
                        server_url=os.getenv("KEYCLOAK_SERVER_URL"),
                        username=os.getenv("KEYCLOAK_ADMIN_USERNAME"),
                        password=os.getenv("KEYCLOAK_ADMIN_PASSWORD"),
                        user_realm_name=os.getenv("USER_REALM_NAME"),
                        client_id=os.getenv("KEYCLOAK_CLIENT_ID"),
                        client_secret_key=os.getenv("CLIENT_SECRET_KEY"),
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
