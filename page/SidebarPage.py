import re

from playwright.sync_api import Page

from common.BasePages import BasePage


class SidebarPage(BasePage):

    def click_project_max(self):
        self.click(self.page.locator("div").filter(has_text=re.compile(r"^项目中心$")), "项目中心")

    def click_project(self):
        self.click(self.page.get_by_role("link", name="项目管理"), "项目管理")

    def click_gateway(self):
        self.click(self.page.get_by_role("link", name="网关管理"), "网关管理")

    def click_device(self):
        self.click(self.page.get_by_role("link", name="设备管理"), "设备管理")

    def click_device_id(self):
        self.click(self.page.get_by_role("link", name="点表管理"), "点表管理")

    def click_touch_screen(self):
        self.click(self.page.get_by_role("link", name="触摸屏管理"), "点表管理")

    def get_gateway_sn(self, sn):
        """
        根据网关sn查询
        Args:
            sn:714005F36924F9C7
        """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name=" 展开"), "展开查询条件")
        self.click(self.page.get_by_role("textbox", name="请输入网关SN"), "网关别名查询框")
        self.input_data(self.page.get_by_role("textbox", name="请输入网关SN"), f"{sn}", "输入网关sn")
        self.click(self.page.get_by_role("button", name=" 收起"), "收起查询框")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询网关sn")

    def get_project_gateway(self, project):
        """
         根据项目查询网关信息
        Args:
            project: 项目名称
        """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), project, "输入项目名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def get_project_name(self, project):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), project, "输入项目名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "根据项目名称查询按钮")

    def get_gateway_name(self, sn):
        """
        根据网关别名查询
        Args:
            sn:714005F36924F9C7
        """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name=" 展开"), "展开查询条件")
        self.click(self.page.get_by_placeholder("请输入网关别名"), "网关别名查询框")
        self.input_data(self.page.get_by_placeholder("请输入网关别名"), f"{sn}", "输入网关别名")
        self.click(self.page.get_by_role("button", name=" 收起"), "收起查询框")
        self.click(self.page.get_by_role("button", name=" 查询"), "根据网关别名进行查询")

    def click_more_functions(self, functions_name):
        """
        封装页面三个点内的功能，比如参数读取xxx，那个ul/li列表
        Args:
            functions_name:
        """
        self.wait_for_timeouts(1000)
        self.click(self.page.locator(
            ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first,
                   "更多功能")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator(f"li:has-text('{functions_name}')").last, f"{functions_name}按钮")
