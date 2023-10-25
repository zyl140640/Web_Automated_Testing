import re
import time

import allure

from common.BasePages import BasePage


class DeviceIdPage(BasePage):

    def add_device_id(self, name):
        self.click(self.page.get_by_role("button", name="新增", exact=True), "新增点表按钮")
        self.click(self.page.get_by_role("dialog").locator("form").filter(
            has_text="所属租户xing0011009child1012qitest11009qi0921newa0921child0921qi09210010905qi泉州市德宝机电").get_by_placeholder(
            "请选择", exact=True), "选择租户")
        self.click(self.page.locator("li").filter(has_text="xing001").nth(1), "")
        self.click(self.page.get_by_role("dialog", name="新增点位").get_by_placeholder("请选择", exact=True).nth(2), "")
        self.click(self.page.locator("ul").filter(has_text="Modbus TCPOPC").locator("span").first, "")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), "189.123.22.11", "")
        self.click(self.page.get_by_role("button", name="下一步"), "")
        self.click(self.page.get_by_role("button", name="添加点表"), "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox"),
                        f"{name}", "")
        self.input_data(self.page.locator(
            "div:nth-child(2) > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"),
            "1", "")
        self.click(self.page.get_by_role("button", name="确 定"), "")
        self.click(self.page.get_by_role("button", name="保存", exact=True), "")

    def update_device_id(self):
        self.page.get_by_role("cell", name="   ").locator("i").nth(1).click()
        self.page.get_by_placeholder("请输入设备IP").fill("192.180.1.1")
        self.page.get_by_placeholder("请输入端口").fill("501")
        self.page.get_by_role("button", name="下一步").click()
        self.wait_for_timeouts(1000)
        self.page.get_by_role("button", name="保存", exact=True).click()

    def get_device_id(self, name):
        self.click(self.page.get_by_role("textbox", name="请输入参数名称"), "参数名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入参数名称"), f"{name}", "输入点表参数名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def delete_device_id(self):
        self.list_row(1)
        self.wait_for_timeouts(1000)
        self.page.get_by_role("button", name="删除").click()
        self.wait_for_timeouts(1000)
        self.page.get_by_role("button", name="确认").click()
