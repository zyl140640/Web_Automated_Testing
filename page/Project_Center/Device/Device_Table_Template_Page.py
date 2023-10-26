import re

from common.BasePages import BasePage


class DeviceTableTemplatePage(BasePage):

    def add_table_template(self, name):
        self.click(self.page.get_by_role("button", name="点表模板"), "点表模板按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="新增"), "新增点表模板")
        self.input_data(self.page.get_by_placeholder("请输入模板名称，40字内"), f"{name}", "输入模板名称")
        self.click(
            self.page.locator("div").filter(has_text=re.compile(r"^模板名称：端口类别：网口串口$")).get_by_placeholder(
                "请选择"), "选择端口类别")
        self.click(self.page.locator("li").filter(has_text="网口"), "选择端口")
        self.click(self.page.get_by_placeholder("请选择").nth(2), "协议类别")
        self.click(self.page.locator("li").filter(has_text="标准"), "标准")
        self.click(self.page.get_by_placeholder("请选择").nth(3), "协议名称")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP"), "tcp协议")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")

    def get_table_template(self, name):
        self.click(self.page.get_by_role("button", name="点表模板"), "点表模板按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_placeholder("请输入模板名称", exact=True), "输入")
        self.input_data(self.page.get_by_placeholder("请输入模板名称", exact=True), f"{name}", "输入模板名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def delete_table_template(self):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="删除"), "删除点表模板按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确认"), "确认删除点表模板按钮")
