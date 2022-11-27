from typing_extensions import Self
from dataclasses import asdict, dataclass
from typing import Any, Dict, Union, Optional

import httpx


@dataclass(frozen=True)
class Config:
    base_url: httpx.URL
    user_agent: str
    follow_redirects: bool
    timeout: httpx.Timeout

    def dict(self) -> Dict[str, Any]:
        return asdict(self)

    def copy(self) -> Self:
        return self.__class__(**self.dict())


def build_base_url(base_url: Optional[Union[str, httpx.URL]]) -> httpx.URL:
    base_url = base_url or httpx.URL("https://open.feishu.cn")
    return base_url if isinstance(base_url, httpx.URL) else httpx.URL(base_url)


def build_user_agent(user_agent: Optional[str] = None) -> str:
    return user_agent or "FeishuKit/Python"


def build_timeout(
    timeout: Optional[Union[float, httpx.Timeout]] = None
) -> httpx.Timeout:
    return timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)


def get_config(
    base_url: Optional[Union[str, httpx.URL]] = None,
    user_agent: Optional[str] = None,
    follow_redirects: bool = True,
    timeout: Optional[Union[float, httpx.Timeout]] = None,
) -> Config:
    return Config(
        build_base_url(base_url),
        build_user_agent(user_agent),
        follow_redirects,
        build_timeout(timeout),
    )
