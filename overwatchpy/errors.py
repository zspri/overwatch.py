class errors:
    class ClientError:
        def __init__(self, code, message):
            super(errors.ServerError, self).__init__(message)
            self.code = code
            self.message = message
    class ServerError:
        def __init__(self, code, message):
            super(errors.ServerError, self).__init__(message)
            self.code = code
            self.message = message
    class RateLimitReached:
        pass
