import httpx
import pytest
from pytest_httpx import HTTPXMock

from core.settings import config
from hh import HHClient


@pytest.mark.asyncio
async def test_get_resume(client: HHClient, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url=httpx.URL(
            url=f"{config.api_url}/resumes",
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
        json={},
    )
    resume = await client.employer.resume.search(text="python")
    assert resume is not None
