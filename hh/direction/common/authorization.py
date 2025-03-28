from datetime import datetime, timedelta
from functools import wraps

from hh.core import api_client
from hh.core.exceptions import AuthTokenError
from hh.core.paths import CommonDirectionPath
from hh.core.settings import config


def check_expires(expires_in: int):
    if not expires_in:
        raise AuthTokenError
    now = datetime.now()
    if now < now + timedelta(seconds=expires_in):
        return True
    return False


x_www_formcontent_type = {"Content-Type": "application/x-www-form-urlencoded"}


class Authorization:
    _path = CommonDirectionPath.auth.value
    _access_token = None
    _refresh_token = None
    _expires_in = None

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
        cls._access_token = body.get("access_token")
        cls._refresh_token = body.get("refresh_token")
        cls._expires_in = body.get("expires_in")

    async def dict(self) -> dict:
        """
        Dict representation of authorization credentials.
        :return:
        """
        if not self._access_token:
            await self.login()
        if not check_expires(self._expires_in):
            await self.refresh()
        return dict(access_token=self._access_token, refresh_token=self._refresh_token)


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
        headers = await _auth.dict()
        return await func(headers=headers, *args, **kwargs)

    return wrapper
