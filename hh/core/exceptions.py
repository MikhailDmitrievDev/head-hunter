class AuthTokenError(Exception):

    def __init__(self, message):
        self.message = message
        if message is None:
            self.message = "No auth token"
        super().__init__(self.message)
