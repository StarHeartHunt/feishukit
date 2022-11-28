from contextvars import ContextVar

_config: ContextVar["Config"] = ContextVar("config")


def get_config() -> "Config":
    return _config.get()


from ..config import Config
from ..models import API, APIList
from .utils import (
    get_api_doc,
    build_request_body,
    build_request_path,
    build_request_query,
    build_response_body,
    build_request_header,
)


def get_definition(api: API) -> None:
    content = get_api_doc(api).document.content
    build_request_body(content)
    build_request_header(content)
    build_request_query(content)
    build_request_path(content)
    build_response_body(content)


def set_definitions(source: APIList):
    for api in source.apis:
        get_definition(api)

    """
    Path(get_config().api_definition_output.replace(".json", "_raw.json")).write_text(
        json.dumps(source, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    """

    return source


def parse_api_list(source: APIList, config: Config):
    _ct = _config.set(config)
    set_definitions(source)

    """
    Path(config.api_definition_output).write_text(
        json.dumps(api_list.dict(by_alias=True), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return api_list
    """
