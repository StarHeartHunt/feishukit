"""DO NOT EDIT THIS FILE!

This file is auto generated by feishu rest api description.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

if TYPE_CHECKING:
    from feishukit.response import Response


class HumanAuthenticationClient:
    def __init__(self, feishu):
        self._feishu = feishu

    def create_identity(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/human_authentication-v1/identity/create

        该接口用于录入实名认证的身份信息，在唤起有源活体认证前，需要使用该接口进行实名认证。
        """
        ...