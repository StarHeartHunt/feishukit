from contextlib import contextmanager, asynccontextmanager
from typing import Any, Union, Optional, Generator, AsyncGenerator

import httpx

from .config import Config, get_config
from .exception import RequestError, RequestTimeout
from .typing import (
    URLTypes,
    CookieTypes,
    HeaderTypes,
    ContentTypes,
    RequestFiles,
    QueryParamTypes,
)


class FeishuCore:
    def __init__(
        self,
        *,
        config: Optional[Config] = None,
        base_url: Optional[Union[str, httpx.URL]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
    ):
        self.config = config or get_config(
            base_url, user_agent, follow_redirects, timeout
        )
        self.__sync_client: Optional[httpx.Client] = None
        self.__async_client: Optional[httpx.AsyncClient] = None

    # default args for creating client
    def _get_client_defaults(self):
        return {
            "auth": "",
            "base_url": self.config.base_url,
            "headers": {
                "User-Agent": self.config.user_agent,
            },
            "timeout": self.config.timeout,
            "follow_redirects": self.config.follow_redirects,
        }

    # create sync client
    def _create_sync_client(self) -> httpx.Client:
        return httpx.Client(**self._get_client_defaults())

    # get or create sync client
    @contextmanager
    def get_sync_client(self) -> Generator[httpx.Client, None, None]:
        if self.__sync_client:
            yield self.__sync_client
        else:
            client = self._create_sync_client()
            try:
                yield client
            finally:
                client.close()

    # create async client
    def _create_async_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(**self._get_client_defaults())

    # get or create async client
    @asynccontextmanager
    async def get_async_client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        if self.__async_client:
            yield self.__async_client
        else:
            client = self._create_async_client()
            try:
                yield client
            finally:
                await client.aclose()

    # sync request
    def _request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        with self.get_sync_client() as client:
            try:
                return client.request(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=json,
                    headers=headers,
                    cookies=cookies,
                )
            except httpx.TimeoutException as e:
                raise RequestTimeout(e.request) from e
            except Exception as e:
                raise RequestError(repr(e)) from e

    # async request
    async def _arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        async with self.get_async_client() as client:
            try:
                return await client.request(
                    method,
                    url,
                    params=params,
                    content=content,
                    data=data,
                    files=files,
                    json=json,
                    headers=headers,
                    cookies=cookies,
                )
            except httpx.TimeoutException as e:
                raise RequestTimeout(e.request) from e
            except Exception as e:
                raise RequestError(repr(e)) from e
