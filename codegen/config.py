from typing import Dict

from pydantic import BaseModel


class Config(BaseModel):
    client_output: str

    api_list_source: str
    api_definition_source: str

    api_list_output: str
    api_definition_output: str

    api_doc_source: str

    depth_overrides: Dict[str, Dict[str, int]]
