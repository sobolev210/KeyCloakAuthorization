from keycloak import KeycloakOpenID

from src.settings import settings

keycloak_open_id = KeycloakOpenID(
    server_url=settings.server_url,
    client_id=settings.client_id,
    realm_name=settings.realm_name
)


def decode_access_token(access_token: str):
    return keycloak_open_id.decode_token(access_token)
