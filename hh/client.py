from core.settings import config
from direction.applicant.applicant import ApplicantDirection
from direction.common.common import CommonDirection
from direction.employer.employer import EmployerDirection


class HHClient:

    def __init__(
        self,
        client_id: str,
        client_secret: str,
    ):
        """
        HHClient - client for HH API.

        :param client_id: ID obtained when creating the application
        :param client_secret: Secure key obtained when creating the application
        """
        config.client_id = client_id
        config.client_secret = client_secret

    @property
    def applicant(self) -> ApplicantDirection:
        return ApplicantDirection()

    @property
    def employer(self) -> EmployerDirection:
        return EmployerDirection()

    @property
    def common(self) -> CommonDirection:
        return CommonDirection()
