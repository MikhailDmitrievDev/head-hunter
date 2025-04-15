from datetime import datetime, timedelta
from functools import wraps

from core.exceptions import AuthTokenError
from core.http import api_client
from core.paths import CommonDirectionPath
from core.settings import config


def check_expires(expires_in: int):
    if not expires_in:
        raise AuthTokenError
    now = datetime.now()
    if now < now + timedelta(seconds=expires_in):
        return True
    return False


x_www_formcontent_type = {"Content-Type": "application/x-www-form-urlencoded"}


class Authorization:
    _path: str | None = CommonDirectionPath.auth.value
    _access_token: str | None = None
    _refresh_token: str | None = None
    _expires_in: int | None = None
    _application_token: str | None = None

    async def login(self):
        if not config.client_id or not config.client_secret:
            raise AuthTokenError
        body = await api_client.post(
            path=self._path,
            params=dict(
                client_id=config.client_id,
                client_secret=config.client_secret,
                grant_type=config.grant_type.CLIENT.value,
            ),
            headers=x_www_formcontent_type,
        )
        self.set_state(body)

    async def refresh(self):
        body = await api_client.post(
            path=self._path,
            params=dict(
                refresh_token=self._refresh_token,
                grant_type=config.grant_type.REFRESH.value,
            ),
        )
        self.set_state(body)

    @classmethod
    def set_state(cls, body: dict):
        cls._access_token = body.get("access_token", cls._access_token)
        cls._refresh_token = body.get("refresh_token", cls._refresh_token)
        cls._expires_in = body.get("expires_in", cls._expires_in)

    async def auth_headers(self) -> dict:
        """
        Dict representation of authorization credentials.
        :return:
        """
        if not self._access_token:
            await self.login()
            return await self.auth_headers()
        return dict(Authorization=f"Bearer {self._access_token}")


_auth = Authorization()


def authorization(func):
    """
    Decorator inserts authorization credentials to request headers.

    Exmaple:
    @authorization
    async def get_employer_info(headers):
        return await api_client.get(
            path=CommonDirectionPath.employer_info.value,
            headers=headers
        )
    :param func: coroutine
    :return:
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        headers = await _auth.auth_headers()
        return await func(headers=headers, *args, **kwargs)

    return wrapper
