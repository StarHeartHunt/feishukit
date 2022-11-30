from typing import Dict

PARAM_REGEX_MAP: Dict[str, str] = {
    "request_header": r"\s*请求头\s*:::html\n(.*?):::",
    "request_body": r"\s*请求体\s*:::html\n(.*?):::",
    "path": r"\s*路径参数\s*:::html\n(.*?):::",
    "query": r"\s*查询参数\s*:::html\n(.*?):::",
    "response_body": r"\s*响应体\s*:::html\n(.*?):::",
}

TABLE_HEADER_MAP = {"名称": "name", "类型": "type", "描述": "desc", "必填": "required"}
