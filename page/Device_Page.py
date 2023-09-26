import re
import time

import allure

from common.BasePages import BasePage


class DevicePage(BasePage):

    def add_device(self, project, device):
        self.wait_for_timeouts(4000)
        self.click(self.page.get_by_role("button", name="新增"), "新增设备按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_placeholder("请选择项目名称").first, "选择项目名称")
        self.wait_for_timeouts(1000)
        self.input_data(self.page.get_by_placeholder("请选择项目名称"), f"{project}", "项目名称输入框")
        self.wait_for_timeouts(2000)
        self.click(self.page.locator("li").filter(has_text=project), "项目")
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
        self.cut_out("添加设备信息")

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
