import os
from functools import wraps

from flask import request
from keycloak import KeycloakOpenID

KEYCLOAK_SERVER_URL = os.getenv('KEYCLOAK_SERVER_URL', 'http://localhost:9000/realms')
KEYCLOAK_REALM_NAME = os.getenv('KEYCLOAK_REALM_NAME', 'development')
KEYCLOAK_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'api_client_confidential')
KEYCLOAK_CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRET', 'ZijuR1urbsbWgU90NujioHY3gBvx33m4')

keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    realm_name=KEYCLOAK_REALM_NAME,
    client_id=KEYCLOAK_CLIENT_ID,
    client_secret_key=KEYCLOAK_CLIENT_SECRET
)


def auth_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            keycloak_openid.decode_token(request.authorization.token, True)
            return func(*args, **kwargs)
        except Exception as e:
            return "", 401

    return wrapper
