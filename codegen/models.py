from typing import List

from pydantic import BaseModel, root_validator


class Meta(BaseModel):
    Name: str
    Project: str
    Resource: str
    Type: int
    Version: str


class API(BaseModel):
    bizTag: str
    detail: str
    fullDose: bool
    fullPath: str
    id: str
    meta: Meta
    name: str
    orderMark: str
    supportAppTypes: List[str]
    tags: List[str]
    updateTime: int
    url: str

    http_method: str
    api_path: str

    @root_validator(pre=True)
    def split_url(cls, values):
        values["http_method"], values["api_path"] = values["url"].split(":", 1)

        return values


class BizInfo(BaseModel):
    desc: str
    name: str


class APIList(BaseModel):
    apis: List[API]
    bizInfos: List[BizInfo]

    @root_validator(pre=True)
    def remove_old_api(cls, values):
        values["apis"] = [
            api for api in values["apis"] if api["meta"]["Version"] != "old"
        ]
        return values


class BaseResponse(BaseModel):
    code: int
    msg: str


class APIListResponse(BaseResponse):
    data: APIList
