import uuid

import httpx
import pytest
from pytest_httpx import HTTPXMock

from hh import HHClient
from hh.core.settings import settings
from tests.data.const import SUCCES_RESUME_RESPONSE


@pytest.mark.asyncio
async def test_get_resume(client: HHClient, httpx_mock: HTTPXMock, _client_id, _client_secret):
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
    httpx_mock.add_response(
        url=httpx.URL(
            url=f"{settings.api_url}/resumes",
            params={
                "text": "python",
                "page": 0,
                "search_in_responses": False,
                "by_text_prefix": False,
                "per_page": 20,
                "include_all_folders": False,
                "locale": "RU",
                "host": "hh.ru"
            },
        ),
        json=SUCCES_RESUME_RESPONSE,
    )
    resume = await client.employer.resume.search(text="python")
    assert resume is not None
