from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_url: str = ""
    client_id: str = ""
    realm_name: str = ""


settings = Settings()
