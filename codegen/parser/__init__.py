import json
from pathlib import Path
from contextvars import ContextVar

import httpx

from ..config import Config
from .models import ApiList
from ..source import Source, get_source

_config: ContextVar["Config"] = ContextVar("config")


def get_config() -> "Config":
    return _config.get()


def parse_api_list(source: Source, config: Config):
    _ct = _config.set(config)
    """
    data = source.data.get("data", {})
    for api in data.get("apis", []):
        api["definition"] = get_source(
            httpx.URL(get_config().api_definition_source),
            params={
                "project": api["meta"]["Project"],
                "version": api["meta"]["Version"],
                "resource": api["meta"]["Resource"],
                "apiName": api["meta"]["Name"],
            },
            timeout=20,
        ).data.get("data")
    Path(config.api_definition_output.replace(".json", "_raw.json")).write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    """

    data = json.loads(
        Path(config.api_definition_output.replace(".json", "_raw.json")).read_text(
            encoding="utf-8"
        )
    )

    api_list = ApiList.parse_obj(data)
    Path(config.api_definition_output).write_text(
        json.dumps(api_list.dict(by_alias=True), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return api_list
