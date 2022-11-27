"""DO NOT EDIT THIS FILE!

This file is auto generated by feishu rest api description.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

if TYPE_CHECKING:
    from feishukit.response import Response


class ContactClient:
    def __init__(self, feishu):
        self._feishu = feishu

    def create_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/create

        使用该接口向通讯录创建一个用户，可以理解为员工入职。创建用户后只返回有数据权限的数据。具体的数据权限的与字段的对应关系请参照[应用权限](/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)。
        """
        ...

    def delete_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/delete

        该接口向通讯录删除一个用户信息，可以理解为员工离职。
        """
        ...

    def patch_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/patch

        该接口用于更新通讯录中用户的字段，未传递的参数不会更新。
        """
        ...

    def update_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/update

        该接口用于更新通讯录中用户的字段。
        """
        ...

    def get_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/get

        该接口用于获取通讯录中单个用户的信息。
        """
        ...

    def find_by_department_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/find_by_department

        基于部门ID获取部门直属用户列表。
        """
        ...

    def batch_get_id_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/batch_get_id

        通过该接口，可使用手机号/邮箱获取用户的 ID 信息，具体获取支持的 ID 类型包括 open_id、user_id、union_id，可通过查询参数指定。
        """
        ...

    def create_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/create

        该接口用于向通讯录中创建部门。
        """
        ...

    def delete_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/delete

        该接口用于向通讯录中删除部门。
        """
        ...

    def patch_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/patch

        该接口用于更新通讯录中部门的信息中的任一个字段。
        """
        ...

    def update_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/update

        该接口用于更新当前部门所有信息。
        """
        ...

    def unbind_department_chat_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/unbind_department_chat

        通过该接口将部门群转为普通群。
        """
        ...

    def get_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/get

        该接口用于向通讯录获取单个部门信息。
        """
        ...

    def children_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/children

        通过部门ID获取部门的子部门列表。
        """
        ...

    def parent_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/parent

        该接口用来递归获取部门父部门的信息，并按照由子到父的顺序返回有权限的父部门信息列表。
        """
        ...

    def search_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/search

        搜索部门，用户通过关键词查询可见的部门数据，部门可见性需要管理员在后台配置。
        """
        ...

    def create_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/create

        使用该接口创建用户组，请注意创建用户组时应用的通讯录权限范围需为“全部员工”，否则会创建失败，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def delete_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/delete

        通过该接口可删除企业中的用户组，请注意删除用户组时应用的通讯录权限范围需为“全部员工”，否则会删除失败，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def patch_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/patch

        使用该接口更新用户组信息，请注意更新用户组时应用的通讯录权限范围需为“全部员工”，否则会更新失败。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def get_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/get

        根据用户组 ID 查询某个用户组的基本信息，支持查询普通用户组和动态用户组。请确保应用的通讯录权限范围里包括该用户组或者是“全部员工”，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def simplelist_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/simplelist

        通过该接口可查询企业的用户组列表，可分别查询普通用户组或动态用户组。如果应用的通讯录权限范围是“全部员工”，则可获取企业全部用户组列表。如果应用的通讯录权限范围不是“全部员工”，则仅可获取通讯录权限范围内的用户组。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def member_belong_group(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group/member_belong

        通过该接口可查询该用户所属的用户组列表，可分别查询普通用户组和动态用户组。如果应用的通讯录权限范围是“全部员工”，则可获取该员工所属的全部用户组列表。如果应用的通讯录权限范围不是“全部员工”，则仅可获取通讯录权限范围内该员工所属的用户组。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def add_group_member(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/add

        向用户组中添加成员(目前成员仅支持用户，未来会支持部门)，如果应用的通讯录权限范围是“全部员工”，则可将任何成员添加到任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员添加到通讯录权限范围的用户组中，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def batch_add_group_member(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/batch_add

        向普通用户组中批量添加成员(目前仅支持添加用户，暂不支持添加部门），如果应用的通讯录权限范围是“全部员工”，则可将任何成员添加到任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员添加到通讯录权限范围的用户组中，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def remove_group_member(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/remove

        从用户组中移除成员 (目前成员仅支持用户，未来会支持部门)，如果应用的通讯录权限范围是“全部员工”，则可将任何成员移出任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员从通讯录权限范围的用户组中移除， [点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def batch_remove_group_member(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/batch_remove

        从普通用户组中批量移除成员 (目前仅支持移除用户，暂不支持移除部门）。如果应用的通讯录权限范围是“全部员工”，则可将任何成员移出任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员从通讯录权限范围的用户组中移除， [点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def simplelist_group_member(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/group-member/simplelist

        通过该接口可查询某个用户组的成员列表（支持查询成员中的用户和部门）, 本接口支持普通用户组和动态用户组。如果应用的通讯录权限范围是“全部员工”，则可查询企业内任何用户组的成员列表。如果应用的通讯录权限范围不是“全部员工”，则仅可查询通讯录权限范围中的用户组的成员列表，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。
        """
        ...

    def create_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/create

        使用该接口创建单位，需要有更新单位的权限。注意：单位功能属于旗舰版付费功能，企业需开通对应版本才可以创建单位。
        """
        ...

    def delete_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/delete

        使用该接口删除单位，需要有更新单位的权限。注意：如果单位的单位类型被其它的业务使用，不允许删除。
        """
        ...

    def patch_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/patch

        调用该接口，需要有更新单位的权限。注意：单位功能属于旗舰版付费功能，企业需开通对应版本才可以修改单位
        """
        ...

    def bind_department_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/bind_department

        通过该接口建立部门与单位的绑定关系，需更新单位的权限，需对应部门的通讯录权限。由于单位是旗舰版付费功能，企业需开通相关版本，否则会绑定失败
        """
        ...

    def unbind_department_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/unbind_department

        通过该接口解除部门与单位的绑定关系，需更新单位的权限，需对应部门的通讯录权限。由于单位是旗舰版付费功能，企业需开通相关功能，否则会解绑失败
        """
        ...

    def list_department_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/list_department

        通过该接口获取单位绑定的部门列表，需具有获取单位的权限
        """
        ...

    def get_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/get

        调用该接口获取单位信息，需有获取单位的权限
        """
        ...

    def list_unit(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/unit/list

        通过该接口获取企业的单位列表，需获取单位的权限
        """
        ...

    def create_employee_type_enum(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/create

        新增自定义人员类型
        """
        ...

    def delete_employee_type_enum(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/delete

        删除自定义人员类型
        """
        ...

    def update_employee_type_enum(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/update

        更新自定义人员类型
        """
        ...

    def list_employee_type_enum(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/employee_type_enum/list

        该接口用于获取员工的人员类型
        """
        ...

    def list_custom_attr(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/custom_attr/list

        获取企业自定义的用户字段配置信息
        """
        ...

    def list_scope(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/scope/list

        该接口用于获取应用被授权可访问的通讯录范围，包括可访问的部门列表、用户列表和用户组列表。
        授权范围为全员时，返回的部门列表为该企业所有的一级部门；否则返回的部门为管理员在设置授权范围时勾选的部门（不包含勾选部门的子部门）。
        """
        ...

    def list_user(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/user/list

        基于部门ID获取部门下直属用户列表。
        [常见问题答疑](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN)。
        """
        ...

    def list_department(
        self,
    ):
        """
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/contact-v3/department/list

        该接口用于获取当前部门子部门列表。[常见问题答疑](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN)。
        """
        ...
