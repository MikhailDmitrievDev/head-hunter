from core.settings import settings
from direction.applicant.applicant import ApplicantDirection
from direction.common.common import CommonDirection
from direction.employer.employer import EmployerDirection


class HHClient:

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        application_token: str,
    ):
        """
        HHClient - client for HH API.

        :param client_id: ID obtained when creating the application
        :param client_secret: Secure key obtained when creating the application
        :param client_secret: Secret token, make request:
        curl -X POST "https://api.hh.ru/oauth/token" -H "Content-Type: application/x-www-form-urlencoded"
        -d "client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=client_credentials"
        """
        settings.client_id = client_id
        settings.client_secret = client_secret
        settings.application_token = application_token

    @property
    def applicant(self) -> ApplicantDirection:
        return ApplicantDirection()

    @property
    def employer(self) -> EmployerDirection:
        return EmployerDirection()

    @property
    def common(self) -> CommonDirection:
        return CommonDirection()
