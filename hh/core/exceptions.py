from httpx import Response


class AuthTokenError(Exception):

    def __init__(self, message: str | None = None):
        self.message = message
        if message is None:
            self.message = "No auth token"
        super().__init__(self.message)


class HTTPErrorResponse(Exception):

    def __init__(self, message: Response | None = None):
        if message is None:
            self.message = "Server response error"
        else:
            self.message = f"{message.status_code} {message.reason_phrase}: {message.json()}"
        super().__init__(self.message)
