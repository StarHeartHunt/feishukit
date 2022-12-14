"""DO NOT EDIT THIS FILE!

This file is auto generated by feishu rest api description.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

if TYPE_CHECKING:
    from feishukit.response import Response


class HireClient:
    def __init__(self, feishu):
        self._feishu = feishu

    def get_job(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get

        根据职位 ID 获取职位信息
        """
        ...

    def get_job_manager(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job-manager/get

        根据职位 ID 获取职位上的招聘人员信息，如招聘负责人、用人经理
        """
        ...

    def get_talent(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent/get

        根据人才 ID 获取人才信息
        """
        ...

    def get_attachment(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/get

        获取招聘系统中附件的元信息，比如文件名、创建时间、文件url等
        """
        ...

    def preview_attachment(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/attachment/preview

        根据附件 ID 获取附件预览信息
        """
        ...

    def list_resume_source(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/resume_source/list

        获取简历来源列表
        """
        ...

    def create_note(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/note/create

        创建备注信息
        """
        ...

    def patch_note(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/note/patch

        根据备注 ID 更新备注信息
        """
        ...

    def get_note(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/note/get

        根据备注 ID 获取备注信息
        """
        ...

    def list_note(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/note/list

        获取备注列表
        """
        ...

    def get_by_application_referral(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/referral/get_by_application

        根据投递 ID 获取内推信息
        """
        ...

    def list_job_process(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job_process/list

        获取全部招聘流程信息
        """
        ...

    def create_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/create

        根据人才 ID 和职位 ID 创建投递
        """
        ...

    def terminate_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/terminate

        根据投递 ID 修改投递状态为「已终止」
        """
        ...

    def get_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/get

        根据投递 ID 获取单个投递信息
        """
        ...

    def list_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/list

        根据限定条件获取投递列表信息
        """
        ...

    def transfer_onboard_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/transfer_onboard

        根据投递 ID 操作候选人入职并创建员工。投递须处于「待入职」阶段，可通过「转移阶段」接口变更投递状态
        """
        ...

    def patch_employee(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/employee/patch

        根据员工 ID 更新员工转正、离职状态
        """
        ...

    def get_by_application_employee(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/employee/get_by_application

        通过投递 ID 获取入职信息
        """
        ...

    def get_employee(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/employee/get

        通过员工 ID 获取入职信息
        """
        ...

    def offer_application(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application/offer

        根据投递 ID 获取 Offer 信息
        """
        ...

    def list_application_interview(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/application-interview/list

        根据投递 ID 获取面试记录列表
        """
        ...

    def get_offer_schema(
        self,
    ):
        """
        https://open.feishu.cn/document/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/offer_schema/get

        根据 Offer 申请表 ID，获取 Offer 申请表的详细信息
        """
        ...
