import json
from pathlib import Path
from typing import Type, Union, TypeVar

import httpx
from pydantic import parse_obj_as

T = TypeVar("T")


def get_content(source: Union[httpx.URL, Path], **kwargs):
    if isinstance(source, Path):
        return json.loads(source.read_text())
    else:
        return httpx.get(
            source,
            headers={"User-Agent": "FeishuKit Codegen"},
            follow_redirects=True,
            **kwargs,
        ).json()


def get_source(source: Union[httpx.URL, Path], response_model: Type[T], **kwargs) -> T:
    uri = httpx.URL(source.resolve().as_uri()) if isinstance(source, Path) else source
    return parse_obj_as(response_model, get_content(uri, **kwargs))
