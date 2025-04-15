from typing import Any

import httpx

from core.exceptions import HTTPErrorResponse
from core.settings import config


class ApiGatewayClient:

    def __init__(self, domain: str):
        self.domain = domain

    def make_url(self, path: str):
        return self.domain + path

    async def get(self, path: str, params: dict, headers: dict | None = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.make_url(path), headers=headers, params=self.delete_none_params(params))
            if response.is_client_error:
                raise HTTPErrorResponse(response)
            return response.json()

    async def post(
            self,
            path: str,
            params: dict,
            headers: dict | None = None,
            data: dict | None = None,
            json: dict | None = None,
            files: dict | None = None,
    ):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.make_url(path),
                headers=headers,
                params=self.delete_none_params(params),
                data=self.delete_none_params(data),
                json=self.delete_none_params(json),
                files=files,
            )
            if response.is_client_error:
                raise HTTPErrorResponse(response)
            return response.json()

    async def update(self, path: str, params: dict, headers: dict | None = None):
        pass

    async def delete(self, path: str, params: dict, headers: dict | None = None):
        pass

    @classmethod
    def delete_none_params(cls, params: dict[Any, Any] | None) -> dict[Any, Any] | None:
        if not params:
            return None
        return {key: value for key, value in params.items() if value is not None}


api_client = ApiGatewayClient(domain=config.api_url)
