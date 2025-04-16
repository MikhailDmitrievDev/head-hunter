import uuid

import httpx
import pytest

from hh.client import HHClient
from hh.core.settings import settings


@pytest.fixture(scope="session")
def _client_secret() -> str:
    return str(uuid.uuid4().hex)


@pytest.fixture(scope="session")
def _client_id() -> str:
    return str(uuid.uuid4().hex)


@pytest.fixture(scope="session")
def _application_token() -> str:
    return str(uuid.uuid4().hex)


@pytest.fixture(scope="function")
async def auth(httpx_mock, _client_secret, _client_id):
    httpx_mock.add_response(
        url=httpx.URL(
            url=f"{settings.api_url}/token",
            params={
                "client_id": _client_id,
                "client_secret": _client_secret,
                "grant_type": settings.grant_type.CLIENT.value,
            },
        ),
        json={"access_token": str(uuid.uuid4().hex), "expires_in": 3600},
    )


@pytest.fixture(scope="session")
def client(_client_id, _client_secret, _application_token):
    return HHClient(client_secret=_client_secret, client_id=_client_id, application_token=_application_token)
