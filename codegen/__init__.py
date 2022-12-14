import json
import shutil
from pathlib import Path
from typing import Any, Dict

import httpx
import tomli
from jinja2 import Environment, PackageLoader, select_autoescape

from .log import logger
from .config import Config
from .source import get_source
from .parser import parse_api_list
from .models import APIList, APIListResponse
from .utils import sanitize, kebab_case, snake_case, pascal_case

env = Environment(loader=PackageLoader("codegen"), autoescape=select_autoescape())
env.globals.update(
    {
        "sanitize": sanitize,
        "snake_case": snake_case,
        "pascal_case": pascal_case,
        "kebab_case": kebab_case,
    }
)
dict_apis = {}


def load_config() -> Config:
    pyproject = tomli.loads(Path("./pyproject.toml").read_text(encoding="utf-8"))
    config_dict: Dict[str, Any] = pyproject.get("tool", {}).get("codegen", {})
    config_dict = {
        k.replace("--", "").replace("-", "_"): v for k, v in config_dict.items()
    }
    return Config.parse_obj(config_dict)


def build():
    config = load_config()
    logger.info(f"Loaded config: {config!r}")

    logger.info("Start getting API list...")
    api_list: APIList = get_source(
        httpx.URL(config.api_list_source), APIListResponse
    ).data
    Path(config.api_list_output).write_text(
        json.dumps(api_list.dict(), indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info(f"Write API list to {config.api_list_output}")

    client_path = Path(config.client_output)
    # shutil.rmtree(client_path)
    client_path.mkdir(parents=True, exist_ok=True)

    logger.info("Parsing api list...")
    endpoints = parse_api_list(api_list, config)
    logger.info("Parsing api list done!")

    dict_biz_api = {endpoint.api.bizTag: [] for endpoint in endpoints}
    for endpoint in endpoints:
        dict_biz_api[endpoint.api.bizTag].append(endpoint)

    for biz in list(dict_biz_api.keys()):
        if len(dict_biz_api[biz]) == 0:
            del dict_biz_api[biz]

    for scope, endpoints in dict_biz_api.items():
        client_template = env.get_template("client/client.py.jinja")
        logger.info(f"Building endpoints for {scope}...")
        tag_path = client_path / f"{scope}.py"
        tag_path.write_text(
            client_template.render(
                project=scope,
                endpoints=endpoints,
            ),
            encoding="utf-8",
        )
        logger.info(f"Successfully built endpoints for {scope}!")
    logger.info("Successfully built endpoints!")

    logger.info("Building namespace...")
    namespace_template = env.get_template("namespace/namespace.py.jinja")
    namespace_path = client_path / "__init__.py"
    namespace_path.write_text(
        namespace_template.render(tags=dict_biz_api.keys()), encoding="utf-8"
    )
    logger.info("Successfully built namespace!")

    logger.info("Successfully generated rest api codes!")
