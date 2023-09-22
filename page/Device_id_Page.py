import re
import time

import allure
from playwright.sync_api import Page


class DeviceIdPage:
    def __init__(self, page: Page):
        self.page = page

    def add_device_id(self):
        time.sleep(4)
        with allure.step("新增点表操作"):
            self.page.get_by_role("button", name="新增", exact=True).click()
            self.page.get_by_placeholder("请选择", exact=True).nth(3).click()
        with allure.step("选择协议"):
            self.page.locator("li").filter(has_text="Modbus TCP").locator("span").click()
        with allure.step("输入设备IP"):
            self.page.get_by_placeholder("请输入设备IP").fill("198.120.1.1")
        with allure.step("点击下一步按钮"):
            self.page.get_by_role("button", name="下一步").click()
        with allure.step("添加点表信息"):
            self.page.get_by_role("button", name="添加点表").click()
            self.page.locator(
                "div:nth-child(2) > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner").fill(
                "1")
            self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox").click()
            self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox").fill(
                "测试点位1")
        with allure.step("进行点表保存操作"):
            self.page.get_by_role("button", name="确 定").click()
            self.page.get_by_role("button", name="保存", exact=True).click()
            allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)

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
