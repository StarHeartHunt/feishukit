import httpx


class FeishuException(Exception):
    ...


class RequestError(FeishuException):
    """Simple API request failed with unknown error."""


class RequestTimeout(FeishuException):
    """Simple API request timeout."""

    def __init__(self, request: httpx.Request):
        self.request = request

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url})"
        )
