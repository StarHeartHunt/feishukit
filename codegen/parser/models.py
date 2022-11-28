from typing import List

from pydantic import BaseModel


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
