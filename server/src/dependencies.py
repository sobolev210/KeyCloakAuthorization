from typing import Annotated

import jwcrypto
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from keycloak.exceptions import KeycloakConnectionError

from src import keycloak_client

http_bearer_dependency = HTTPBearer()


def get_user_id_from_token(
        credentials: Annotated[HTTPAuthorizationCredentials,  # token is taken from "Authorization" header
        Depends(http_bearer_dependency)]
) -> str:
    try:
        token_info = keycloak_client.decode_access_token(credentials.credentials)
    except (jwcrypto.jws.InvalidJWSObject, jwcrypto.jws.InvalidJWSSignature, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwcrypto.jwt.JWTExpired:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwcrypto.common.JWException as e:
        print("Unexpected error when validating token: ", e)
        raise HTTPException(status_code=401, detail="Token did not pass validation")
    except KeycloakConnectionError:
        raise HTTPException(status_code=500, detail="Authorization service is unavailable")
    return token_info["sub"]
