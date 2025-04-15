import uuid

import pytest

from hh.client import HHClient


@pytest.fixture(scope="session")
def _client_secret() -> str:
    return str(uuid.uuid4().hex)


@pytest.fixture(scope="session")
def _client_id() -> str:
    return str(uuid.uuid4().hex)


@pytest.fixture(scope="session")
def client(_client_id, _client_secret):
    return HHClient(client_secret=_client_secret, client_id=_client_id, )
