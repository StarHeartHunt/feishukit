"""DO NOT EDIT THIS FILE!

This file is auto generated by feishu rest api description.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

if TYPE_CHECKING:
    from feishukit.response import Response


class OkrClient:
    def __init__(self, feishu):
        self._feishu = feishu

    def list_period(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/period/list

        获取OKR周期列表
        """
        ...

    def batch_get_okr(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/okr/batch_get

        根据OKR id批量获取OKR
        """
        ...

    def list_user_okr(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/user-okr/list

        根据用户的id获取OKR列表
        """
        ...

    def delete_progress_record(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/delete

        根据ID删除OKR进展记录
        """
        ...

    def update_progress_record(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/update

        根据OKR进展记录ID更新进展详情
        """
        ...

    def get_progress_record(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/get

        根据ID获取OKR进展记录详情
        """
        ...

    def create_progress_record(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/progress_record/create

        创建OKR进展记录
        """
        ...

    def upload_image(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/image/upload

        上传图片
        """
        ...

    def query_review(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/review/query

        根据周期和用户查询复盘信息。
        """
        ...

    def list_metric_source(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source/list

        获取租户下全部 OKR 指标库（仅限 OKR 企业版使用）
        """
        ...

    def list_metric_source_table(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source-table/list

        获取指定指标库下有哪些指标表（仅限 OKR 企业版使用）
        """
        ...

    def batch_update_metric_source_table_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source-table-item/batch_update

        - 该接口用于批量更新多项指标，单次调用最多更新 100 条记录。接口仅限 OKR 企业版使用。

          更新成功后 OKR 系统会给以下人员发送消息通知：

            - 首次更新目标值的人员

            - 已经将指标添加为 KR、且本次目标值/起始值/支撑的上级有变更的人员，不包含仅更新了进度值的人员
        """
        ...

    def patch_metric_source_table_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source-table-item/patch

        - 该接口用于更新某项指标，接口仅限 OKR 企业版使用。

            更新成功后 OKR 系统会给以下人员发送消息通知：

            - 首次更新目标值的人员

            - 已经将指标添加为 KR、且本次目标值/起始值/支撑的上级有变更的人员，不包含仅更新了进度值的人员
        """
        ...

    def get_metric_source_table_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source-table-item/get

        获取某项指标的具体内容（仅限 OKR 企业版使用）
        """
        ...

    def list_metric_source_table_item(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/okr-v1/metric_source-table-item/list

        获取指定指标表下的所有指标项（仅限 OKR 企业版使用）
        """
        ...
