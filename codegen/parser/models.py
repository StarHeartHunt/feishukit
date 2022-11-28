from typing import List, Optional

from pydantic import Extra, Field, BaseModel, root_validator


class BasicRateLimit(BaseModel, extra=Extra.allow):
    tier: int


class Property(BaseModel, extra=Extra.allow):
    defaultValue: str
    description: str
    example: str
    format: str
    name: str
    properties: Optional[List["Property"]]
    ref: str
    required: bool
    type: str


Property.update_forward_refs()


class Body(Property, extra=Extra.allow):
    ...


class Query(Property, extra=Extra.allow):
    ...


class Path(Property, extra=Extra.allow):
    ...


class Request(BaseModel, extra=Extra.allow):
    body: Optional[Body]
    query: Optional[Query]
    path: Optional[Path]
    contentType: str


class Response(BaseModel, extra=Extra.allow):
    body: Optional[Body]
    contentType: str


class Definition(BaseModel, extra=Extra.allow):
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


class Meta(BaseModel, extra=Extra.allow):
    name: str = Field(..., alias="Name")
    project: str = Field(..., alias="Project")
    resource: str = Field(..., alias="Resource")
    type: int = Field(..., alias="Type")
    version: str = Field(..., alias="Version")


class Api(BaseModel, extra=Extra.allow):
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
