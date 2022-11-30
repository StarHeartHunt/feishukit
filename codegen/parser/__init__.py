import json
from typing import List
from pathlib import Path
from contextvars import ContextVar

import httpx
from pydantic import parse_obj_as

_api: ContextVar["API"] = ContextVar("api")
_config: ContextVar["Config"] = ContextVar("config")


def get_config() -> "Config":
    return _config.get()


def get_api() -> "API":
    return _api.get()


from ..config import Config
from ..source import get_source
from ..models import API, APIList
from .models import Endpoint, APIDocResponse
from .utils import (
    build_request_body,
    build_request_path,
    build_request_query,
    build_response_body,
    build_request_header,
)


def get_api_doc(api: API):
    return get_source(
        httpx.URL(get_config().api_doc_source),
        APIDocResponse,
        params={"fullPath": api.fullPath.replace("/document", "", 1)},
    ).data


def get_definition(api: API):
    content = get_api_doc(api).document.content

    return Endpoint(
        api=api,
        request_body=build_request_body(content),
        request_header=build_request_header(content),
        path=build_request_path(content),
        query=build_request_query(content),
        response_body=build_response_body(content),
    )


def get_endpoints(source: APIList):
    endpoints = []
    for api in source.apis:
        _at = _api.set(api)
        definition = get_definition(api)
        endpoints.append(definition)

    Path(get_config().api_definition_output).write_text(
        json.dumps(
            [endpoint.dict() for endpoint in endpoints], indent=2, ensure_ascii=False
        ),
        encoding="utf-8",
    )

    return endpoints


def parse_api_list(source: APIList, config: Config):
    _ct = _config.set(config)
    get_endpoints(source)

    endpoints = parse_obj_as(
        List[Endpoint],
        json.loads(
            Path(get_config().api_definition_output).read_text(
                encoding="utf-8",
            )
        ),
    )

    """
    Path(config.api_definition_output).write_text(
        json.dumps(api_list.dict(by_alias=True), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    """

    return endpoints
