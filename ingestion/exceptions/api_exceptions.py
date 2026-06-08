class APIError(Exception):
    pass


class APITimeoutError(APIError):
    pass


class APIConnectionError(APIError):
    pass