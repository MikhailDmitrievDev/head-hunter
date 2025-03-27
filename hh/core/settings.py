from dataclasses import dataclass

from hh.direction.applicant.applicant import ApplicantDirection
from hh.direction.employer.employer import EmployerDirection

DIRECTION = {"applicant": ApplicantDirection, "employer": EmployerDirection()}


@dataclass
class Config:
    """
    Configuration class.
    """

    default_grant_type: str = "client_credentials"


config = Config()
