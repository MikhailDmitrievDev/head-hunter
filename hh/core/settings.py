import enum


class GrantType(enum.Enum):
    CLIENT = "client_credentials"
    REFRESH = "refresh_token"
    CODE = "authorization_code"


class Settings:
    client_id: str | None = None
    client_secret: str | None = None
    application_token: str | None = None
    grant_type: GrantType = GrantType.CLIENT
    timeout: float = 10.0
    api_url: str = "https://api.hh.ru"


settings = Settings()
