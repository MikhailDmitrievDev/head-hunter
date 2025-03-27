from hh.core.settings import config
from hh.core.settings import DIRECTION


class HHClient:

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str = config.default_grant_type,
        direction: str = "applicant",
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
        try:
            self.direction = DIRECTION[direction]
        except KeyError:
            raise ValueError(
                f"Unknown direction: {direction}, available: {list(DIRECTION.keys())}"
            )

    async def __aenter__(self):
        return self.direction

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
