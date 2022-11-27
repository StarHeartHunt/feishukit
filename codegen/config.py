from pathlib import Path

from pydantic import BaseModel


class Config(BaseModel):
    client_output: str

    api_list_source: str
    api_definition_source: str

    api_list_output: str
    api_definition_output: str
