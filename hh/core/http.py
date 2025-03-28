import httpx

from hh.core.settings import config


class ApiGatewayClient:

    def __init__(self, domain: str):
        self.domain = domain

    def make_url(self, path: str):
        return self.domain + path

    async def get(self, path: str, params: dict, headers: dict | None = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.make_url(path), headers=headers, params=params
            )
            return response

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
                params=params,
                data=data,
                json=json,
                files=files,
                timeout=config.TIMEOUT,
            )
            return response

    async def update(self, path: str, params: dict, headers: dict | None = None):
        pass

    async def delete(self, path: str, params: dict, headers: dict | None = None):
        pass
