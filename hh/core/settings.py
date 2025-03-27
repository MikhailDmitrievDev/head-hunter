import enum
from dataclasses import dataclass

from hh.direction.employer.employer import EmployerDirection

DIRECTION = {"applicant": "applicant", "employer": EmployerDirection()}


class EmployerDirectionPath(enum.Enum):
    resumes = "/resumes"


class CommonDirectionPath(enum.Enum):
    vacancies = "/vacancies"


@dataclass
class Config:
    """
    Configuration class.
    """

    default_grant_type: str = "client_credentials"


config = Config()
