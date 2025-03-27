from hh.core.settings import config
from hh.direction.applicant.applicant import ApplicantDirection
from hh.direction.common.common import CommonDirection
from hh.direction.employer.employer import EmployerDirection


class HHClient:

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str = config.default_grant_type,
    ):
        """
        HHClient - client for HH API.

        :param client_id: ID obtained when creating the application
        :param client_secret: Secure key obtained when creating the application
        :param grant_type: Token request method
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def applicant(self) -> ApplicantDirection:
        return ApplicantDirection()

    @property
    def employer(self) -> EmployerDirection:
        return EmployerDirection()

    @property
    def common(self) -> CommonDirection:
        return CommonDirection()
