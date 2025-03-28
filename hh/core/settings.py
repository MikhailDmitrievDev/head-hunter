import enum
from dataclasses import dataclass


class GrantType(enum.Enum):
    CLIENT = "client_credentials"
    REFRESH = "refresh_token"
    CODE = "authorization_code"


@dataclass
class Config:
    """
    Configuration class.
    """

    client_id: str | None = None
    client_secret: str | None = None
    grant_type: GrantType = GrantType.CLIENT
    timeout: float = 10.0


config = Config()
