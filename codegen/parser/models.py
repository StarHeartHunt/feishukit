from typing import List, Optional

from pydantic import Extra, BaseModel, root_validator

from ..models import API
from .utils import remap_type, fix_reserved_words


class Definition(BaseModel, extra=Extra.allow):
    name: str
    type: str
    desc: str
    children: Optional[List["Definition"]]

    @root_validator(pre=True)
    def normalize(cls, values):
        values["type"] = values["type"].replace("\\", "")
        if values["type"].endswith("[]"):
            values["type"] = (
                "List[" + remap_type(values["type"].replace("[]", "")) + "]"
            )
        else:
            values["type"] = remap_type(values["type"])
        values["name"] = fix_reserved_words(values["name"])

        return values


Definition.update_forward_refs()


class Endpoint(BaseModel):
    api: API
    request_body: List[Definition]
    request_header: List[Definition]
    path: List[Definition]
    query: List[Definition]
    response_body: List[Definition]

    request_content_type: str = "json"

    @root_validator(pre=True)
    def set_fields(cls, values):
        for header in values["request_header"]:
            if header["name"] == "Content-Type":
                if header["desc"].count("form") > 0:
                    values["request_content_type"] = "form"

        return values


class Document(BaseModel):
    allVisible: bool
    content: str
    directoryId: str
    fullPath: str
    id: str
    keywords: List
    name: str
    subtitles: List
    title: str
    type: str
    updateTime: int


class APIDoc(BaseModel):
    document: Document


class APIDocResponse(BaseModel):
    code: int
    data: APIDoc
    msg: str
