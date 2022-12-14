"""DO NOT EDIT THIS FILE!

This file is auto generated by feishu rest api description.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

if TYPE_CHECKING:
    from feishukit.response import Response


class SearchClient:
    def __init__(self, feishu):
        self._feishu = feishu

    def create_data_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/create

        创建一个数据源
        """
        ...

    def get_data_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/get

        获取已经创建的数据源
        """
        ...

    def patch_data_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/patch

        更新一个已经存在的数据源
        """
        ...

    def list_data_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/list

        批量获取创建的数据源信息
        """
        ...

    def delete_data_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source/delete

        删除一个已存在的数据源
        """
        ...

    def create_data_source_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source-item/create

        索引一条数据记录
        """
        ...

    def get_data_source_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source-item/get

        获取单个数据记录
        """
        ...

    def delete_data_source_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/data_source-item/delete

        删除数据项
        """
        ...

    def patch_schema(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/patch

        修改数据范式
        """
        ...

    def delete_schema(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/delete

        删除已存在的数据范式
        """
        ...

    def get_schema(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/get

        获取单个数据范式
        """
        ...

    def create_schema(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/search-v2/schema/create

        创建一个数据范式
        """
        ...
