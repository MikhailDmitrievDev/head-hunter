import enum
from dataclasses import dataclass

from hh.direction.applicant.applicant import ApplicantDirection
from hh.direction.employer.employer import EmployerDirection

DIRECTION = {"applicant": ApplicantDirection, "employer": EmployerDirection()}


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
