import json
from pathlib import Path
from typing import Any, Union
from dataclasses import dataclass

import httpx
from jsonpointer import JsonPointer


@dataclass(frozen=True)
class Source:
    uri: httpx.URL
    root: Any

    @property
    def pointer(self) -> JsonPointer:
        return JsonPointer(self.uri.fragment)

    @property
    def data(self) -> Any:
        return self.pointer.resolve(self.root)

    def get_root(self) -> "Source":
        return Source(uri=self.uri.copy_with(fragment=""), root=self.root)

    def resolve_ref(self, ref: str) -> "Source":
        uri_ref = httpx.URL(ref)
        if uri_ref.scheme and uri_ref.host:
            return get_source(uri_ref)
        return Source(uri=self.uri.copy_with(fragment=uri_ref.fragment), root=self.root)

    def __truediv__(self, other: Union[str, int]) -> "Source":
        parts = self.pointer.get_parts() + [other]
        fragment = JsonPointer.from_parts(parts).path
        return self.resolve_ref(str(httpx.URL(fragment=fragment)))


def get_content(source: Union[httpx.URL, Path], **kwargs):
    if isinstance(source, Path):
        return json.loads(source.read_text())
    else:
        data = httpx.get(
            source,
            headers={"User-Agent": "FeishuKit Codegen"},
            follow_redirects=True,
            **kwargs,
        ).json()

        return data


def get_source(source: Union[httpx.URL, Path], **kwargs) -> Source:
    uri = httpx.URL(source.resolve().as_uri()) if isinstance(source, Path) else source
    return Source(uri=uri, root=get_content(source, **kwargs))
