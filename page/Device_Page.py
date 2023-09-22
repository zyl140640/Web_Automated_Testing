import re
import time

import allure
from playwright.sync_api import Page


class DevicePage:
    def __init__(self, page: Page):
        self.page = page

    def add_device(self, project, device):
        time.sleep(4)
        with allure.step("进行新增设备操作"):
            self.page.get_by_role("button", name="新增").click()
        time.sleep(2)
        with allure.step("输入设备信息"):
            self.page.get_by_placeholder("请选择项目名称").first.click()
            time.sleep(1)
            self.page.get_by_placeholder("请选择项目名称").fill(f"{project}")
            time.sleep(2)
            self.page.locator("li").filter(has_text=project).click()
            self.page.locator("div").filter(has_text=re.compile(r"^项目名称设备名称$")).get_by_role("textbox").nth(
                1).fill(
                device)
        # self.page.get_by_placeholder("请选择组织").click()
        # self.page.locator("div:nth-child(2) > .el-tree-node__content").first.click()
        # self.page.get_by_placeholder("请选择区域").click()
        # self.page.get_by_role("treeitem", name=" 区域").locator("div").first.click()
        self.page.locator("div").filter(has_text=re.compile(r"^设备别名序列号$")).get_by_role("textbox").first.fill(
            "设备别名")
        self.page.locator("div").filter(has_text=re.compile(r"^设备别名序列号$")).get_by_role("textbox").nth(1).fill(
            "123456")
        self.page.locator("div").filter(has_text=re.compile(r"^安装位置联系电话$")).get_by_role("textbox").first.fill(
            "山东省青岛市李沧区")
        self.page.locator("div").filter(has_text=re.compile(r"^安装位置联系电话$")).get_by_role("textbox").nth(1).fill(
            "15533065391")
        with allure.step("保存设备信息"):
            self.page.get_by_role("button", name="确 定").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)

    def delete_device(self):
        time.sleep(2)
        self.page.get_by_role("row", name="1", exact=True).locator("label span").nth(1).click()
        self.page.get_by_role("button", name="删除").click()
        self.page.get_by_role("button", name="确认").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)


    def update_device(self, project):
        time.sleep(2)
        self.page.get_by_role("menu").get_by_role("link", name="设备管理").click()
        self.page.get_by_placeholder("请输入项目名称").click()
        self.page.get_by_placeholder("请输入项目名称").fill(f"{project}")
        self.page.get_by_role("button", name=" 查询").click()
        self.page.locator(
            '//*[@id="app"]/div/div[2]/section/div[1]/div[2]/div[5]/div[1]/div[5]/div[2]/table/tbody/tr/td[16]/div/div/i[2]').first.click()

        self.page.locator(
            "div:nth-child(3) > .el-dialog > .el-dialog__body > .el-form > div > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner").first.fill(
            "修改测试设备")
        self.page.get_by_role("button", name="确 定").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)
