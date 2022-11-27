from typing import List, Optional

from pydantic import Field, BaseModel, root_validator


class BasicRateLimit(BaseModel):
    tier: int


class Property(BaseModel):
    defaultValue: str
    description: str
    example: str
    format: str
    name: str
    ref: str
    required: bool
    type: str


class Body(BaseModel):
    defaultValue: str
    description: str
    example: str
    format: str
    name: str
    properties: Optional[List[Property]]
    ref: str
    required: bool
    type: str


class Request(BaseModel):
    body: Optional[Body]
    contentType: str


class Response(BaseModel):
    body: Optional[Body]
    contentType: str


class Definition(BaseModel):
    apiName: str
    apiPath: str
    basicRateLimit: BasicRateLimit
    description: str
    httpMethod: str
    pagination: bool
    project: str
    request: Request
    resource: str
    response: Response
    scopesOfDebugRequired: List
    scopesOfFieldRequired: List
    supportFileDownload: bool
    supportFileUpload: bool
    version: str


class Meta(BaseModel):
    name: str = Field(..., alias="Name")
    project: str = Field(..., alias="Project")
    resource: str = Field(..., alias="Resource")
    type: int = Field(..., alias="Type")
    version: str = Field(..., alias="Version")


class Api(BaseModel):
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

    definition: Optional[Definition]

    @root_validator(pre=True)
    def set_definition(cls, values):
        if values["definition"] == {}:
            values["definition"] = None
        return values


class BizInfo(BaseModel):
    desc: str
    name: str


class ApiList(BaseModel):
    apis: List[Api]
    bizInfos: List[BizInfo]
