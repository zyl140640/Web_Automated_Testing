import re

from common.BasePages import BasePage


class DevicePage(BasePage):

    def add_device(self, project, device):
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="新增"), "新增设备按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_placeholder("请选择", exact=True).nth(1), "所属租户")
        self.wait_for_timeouts(2000)
        self.click(self.page.locator("li").filter(has_text="张氏家族企业").nth(1), "选择所属租户")
        self.click(self.page.get_by_placeholder("请选择项目名称").first, "选择项目名称")
        self.wait_for_timeouts(1000)
        self.input_data(self.page.get_by_placeholder("请选择项目名称").first, f"{project}", "项目名称输入框")
        self.wait_for_timeouts(2000)
        self.click(self.page.locator("li").filter(has_text=re.compile(r"^测试主流程项目$")), "选择测试主流程项目")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^项目名称设备名称$")).get_by_role("textbox").nth(
                1), f"{device}", "设备输入框")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^设备别名序列号$")).get_by_role("textbox").first,
            "设备别名", "设备别名输入框")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^设备别名序列号$")).get_by_role("textbox").nth(1),
            "123456", "序列号输入框")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^安装位置联系电话$")).get_by_role("textbox").first,
            "山东省青岛市李沧区", "安装位置输入框")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^安装位置联系电话$")).get_by_role("textbox").nth(1),
            "15533065391", "联系电话输入框")
        self.click(self.page.get_by_role("button", name="确 定"), "保存按钮")
        self.asserts_result(self.get_alert("设备管理-新增设备"), "=", "新增成功")

    def update_device(self, project):
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_placeholder("请输入项目名称"), "项目名称输入框")
        self.input_data(self.page.get_by_placeholder("请输入项目名称"), f"{project}", "项目名称输入框")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
        self.click(self.page.get_by_role("cell", name="   ").locator("i").nth(1), "编辑按钮")
        self.page.get_by_role("button", name="确 定").click()
        self.asserts_result(self.get_alert("点表管理-修改设备"), "=", "编辑设备成功")

    def delete_device(self):
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("row", name="1", exact=True).locator("label span").nth(1), "勾选设备")
        self.click(self.page.get_by_role("button", name="删除"), "删除按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认删除设备按钮")
        self.asserts_result(self.get_alert("设备管理-删除设备"), "=", "删除设备成功")
