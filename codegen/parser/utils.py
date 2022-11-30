import re
import builtins
from typing import List
from keyword import iskeyword

from bs4 import BeautifulSoup

from . import get_api, get_config
from .consts import PARAM_REGEX_MAP, TABLE_HEADER_MAP

FEISHU_TYPES = {"float", "string", "int", "boolean", "map", "file", "object", "list"}

RESERVED_WORDS = (
    set(dir(builtins)) | {"self", "true", "false", "datetime", "validate"}
) - {
    "type",
    "id",
}

TYPE_MAPPING = {"string": "str", "boolean": "bool"}


def remap_type(type_: str):
    return TYPE_MAPPING.get(type_, type_)


def fix_reserved_words(value: str) -> str:
    """
    Using reserved Python words as identifiers in generated code causes problems, so this function renames them.
    Args:
        value: The identifier to-be that should be renamed if it's a reserved word.
    Returns:
        `value` suffixed with `_` if it was a reserved word.
    """
    return f"{value}_" if value in RESERVED_WORDS or iskeyword(value) else value


def remap_field(field: str):
    return TABLE_HEADER_MAP.get(field, field)


def parse_table_header(soup: BeautifulSoup) -> List[str]:
    table_headers = soup.find_all("md-dt-th") or soup.find_all("md-th")

    return [remap_field(table_header.text.strip()) for table_header in table_headers]


def parse_simple_table(soup: BeautifulSoup, column_names: List[str]):
    rows = []
    for item in soup.find_all("md-tr"):
        if item.find("md-th"):
            continue

        row = {}
        depth: int = 0
        for index, column in enumerate(item.find_all("md-td")):
            if column_names[index] == "name":
                depth = column.text.count("\u2003") + column.text.count("∟")
            row[column_names[index]] = column.text.strip()

        row["_depth"] = depth
        rows.append(row)

    return rows


def get_parent(root, depth):
    parent = root
    for _ in range(depth):
        parent = parent[-1]["children"]

    return parent


def parse_simple_tree_table(soup: BeautifulSoup, column_names: List[str]):
    parsed_table = parse_simple_table(soup, column_names)
    tree_table = []

    depth_state = {
        "_depth": 0,
        "depth": 0,
    }
    for index in range(len(parsed_table)):
        row = parsed_table[index]
        overrides = get_config().depth_overrides
        name = get_api().name
        depth = overrides.get(name, {}).get(row["desc"], row.pop("_depth"))

        row["children"] = []
        if depth != depth_state["depth"]:
            if depth > depth_state["depth"]:
                depth_state["_depth"] += 1
            elif depth < depth_state["depth"]:
                depth_state["_depth"] -= 1
        depth_state["depth"] = depth

        parent = get_parent(tree_table, depth_state["_depth"])
        row["name"] = row["name"].replace("∟", "").strip()
        parent.append(row)

    return tree_table


def _parse_tree_table(soup: BeautifulSoup, column_names: List[str]):
    rows = []
    for item in soup.find_all("md-dt-tr"):
        if item.find("md-dt-th"):
            continue

        row = {}
        for index, column in enumerate(item.find_all("md-dt-td")):
            row[column_names[index]] = column.text.strip()

        row["_depth"] = int(item.attrs["level"])
        rows.append(row)

    return rows


def parse_tree_table(soup: BeautifulSoup, column_names: List[str]):
    rows = _parse_tree_table(soup, column_names)
    tree_table = []

    for index in range(len(rows)):
        row = rows[index]
        depth = row.pop("_depth")

        row["name"] = row["name"].strip()
        row["children"] = []
        if depth > 0:
            parent = tree_table
            for _ in range(depth):
                parent = parent[-1]["children"]
            parent.append(row)
        else:
            tree_table.append(row)

    return tree_table


def parse_doc_table(content: str, type_: str):
    doc = re.search(PARAM_REGEX_MAP[type_], content, re.S)
    if doc:
        soup = BeautifulSoup(doc.group(1), "lxml")
        column_names = parse_table_header(soup)
        if soup.find("md-dt-tr"):
            return parse_tree_table(soup, column_names)
        elif "∟" in soup.text:
            return parse_simple_tree_table(soup, column_names)
        else:
            return parse_simple_table(soup, column_names)

    else:
        return []


def build_request_header(content: str):
    return parse_doc_table(content, "request_header")


def build_request_query(content: str):
    return parse_doc_table(content, "query")


def build_request_path(content: str):
    return parse_doc_table(content, "path")


def build_request_body(content: str):
    return parse_doc_table(content, "request_body")


def build_response_body(content: str):
    return parse_doc_table(content, "response_body")
