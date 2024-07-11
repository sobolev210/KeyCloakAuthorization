## Starting the server

Specify keycloak server url, client id and realm name in settings.py file.

Then run the following commands
```
cd server
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Authorization logic 

Authorization logic is located in dependencies.py and in keycloak_client.py files. To validate the token,
keycloak_client internally gets public key from Keycloak for each request


## Third-Party libraries
**(need to keep this section due to terms of LGPLv3 license)**

This project uses [jwcrypto](https://pypi.org/project/jwcrypto/) library, distributed under LGPLv3+ license.
Copy of license is included in the file licenses/LGPLv3.txt
