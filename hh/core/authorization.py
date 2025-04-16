from datetime import datetime, timedelta
from typing import Any, Coroutine, Callable

from core.exceptions import AuthTokenError
from core.http import api_client
from core.paths import CommonDirectionPath
from core.settings import settings


def check_expires(expires_in: int) -> bool:
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

    async def login(self) -> None:
        if not settings.client_id or not settings.client_secret:
            raise AuthTokenError
        body = await api_client.post(
            path=self._path,
            params=dict(
                client_id=settings.client_id,
                client_secret=settings.client_secret,
                grant_type=settings.grant_type.CLIENT.value,
            ),
            headers=x_www_formcontent_type,
        )
        self.set_state(body)

    async def refresh(self) -> None:
        body = await api_client.post(
            path=self._path,
            params=dict(
                refresh_token=self._refresh_token,
                grant_type=settings.grant_type.REFRESH.value,
            ),
        )
        self.set_state(body)

    @classmethod
    def set_state(cls, body: dict[str, Any]) -> None:
        cls._access_token = body.get("access_token", cls._access_token)
        cls._refresh_token = body.get("refresh_token", cls._refresh_token)
        cls._expires_in = body.get("expires_in", cls._expires_in)

    async def auth_headers(self) -> dict[str, Any]:
        """
        Dict representation of authorization credentials.
        :return:
        """
        if not self._access_token:
            await self.login()
            return await self.auth_headers()
        return dict(Authorization=f"Bearer {self._access_token}")


_auth = Authorization()


def authorization(func: Callable[..., Coroutine]) -> Callable[..., Coroutine]:
    """
    Decorator inserts authorization credentials to request headers.
    Example:
    @authorization
    async def get_employer_info(headers):
        return await api_client.get(
            path=CommonDirectionPath.employer_info.value,
            headers=headers
        )
    :param func: coroutine
    :return:
    """

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        headers = await _auth.auth_headers()
        kwargs["headers"] = headers
        return await func(*args, **kwargs)

    return wrapper
