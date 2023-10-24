import re
import time

import allure

from common.BasePages import BasePage


class DeviceIdPage(BasePage):

    def add_device_id(self, name):
        self.wait_for_timeouts(4000)
        self.click(self.page.get_by_role("button", name="新增", exact=True), "新增点表按钮")
        self.click(self.page.get_by_placeholder("请选择", exact=True).nth(3), "选择协议")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP").locator("span"), "选择Modbus TCP协议")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), "198.120.1.1", "设备IP输入框")
        self.click(self.page.get_by_role("button", name="下一步"), "下一步按钮")
        self.click(self.page.get_by_role("button", name="添加点表"), "添加点表按钮")
        self.input_data(self.page.locator(
            "div:nth-child(2) > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"),
            "1", "输入地址框")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox"),
            f"{name}", "点位名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.click(self.page.get_by_role("button", name="保存", exact=True), "保存按钮")
        self.cut_out("新增点表、点位")

    def update_device_id(self, project):
        time.sleep(2)
        self.page.get_by_role("menu").get_by_role("link", name="点表管理").click()
        self.page.get_by_placeholder("请输入参数名称").click()
        self.page.get_by_placeholder("请输入参数名称").fill(f"{project}")
        self.page.get_by_role("button", name=" 查询").click()
        self.page.locator(
            '//*[@id="app"]/div/div[2]/section/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[18]/div/div/i[2]').first.click()
        self.page.get_by_placeholder("请输入设备IP").click()
        self.page.get_by_placeholder("请输入设备IP").fill("192.180.1.1")
        self.page.get_by_placeholder("请输入端口").click()
        self.page.get_by_placeholder("请输入端口").fill("501")
        self.page.get_by_role("button", name="下一步").click()
        self.page.get_by_role("button", name="保存", exact=True).click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)

    def get_device_id(self, name):
        self.click(self.page.get_by_role("textbox", name="请输入参数名称"), "参数名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入参数名称"), f"{name}", "输入点表参数名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
