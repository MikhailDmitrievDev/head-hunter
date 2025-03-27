import httpx


class ApiGatewayClient:

    def __init__(
        self,
        domain: str,
    ):
        self.domain = domain

    async def get(self, path: str, params: dict):
        url = self.domain + path
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            return response

    async def post(self, params: dict):
        pass

    async def update(self, params: dict):
        pass

    async def delete(self, params: dict):
        pass
