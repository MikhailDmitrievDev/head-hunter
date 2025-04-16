from core.http import api_client, ApiGatewayClient


class Category:
    def __init__(self) -> None:
        self.api_client: ApiGatewayClient = api_client
