import time

import allure
from playwright.sync_api import Page


class GatewayPage:
    def __init__(self, page: Page):
        self.page = page

    def add_gateway(self, project, gateway, gatewayid):
        time.sleep(4)
        with allure.step("进行新增网关操作"):
            self.page.get_by_role("button", name="新增").click()
        with allure.step("输入网关信息"):
            self.page.get_by_role("textbox", name="请选择项目名称").click()
            self.page.get_by_label("选择项目").get_by_placeholder("请选择项目名称").fill(project)
            self.page.get_by_label("选择项目").get_by_role("button", name=" 查询").click()
            self.page.get_by_role("radio").click()
            self.page.get_by_label("选择项目").get_by_role("button", name="确 定").click()
            self.page.get_by_placeholder("请输入网关别名").fill(gateway)
            self.page.get_by_role("textbox", name="请输入网关SN").fill(gatewayid)
            self.page.get_by_placeholder("请选择网关类型").click()
            # self.page.get_by_placeholder("请选择组织").click()
            # self.page.locator("div").filter(has_text=re.compile(r"^宁波高新区安立特电气科技有限公司$")).first.click()
            # self.page.get_by_placeholder("请选择区域").click()
            self.page.get_by_placeholder("请输入负责人").fill("负责人")
            self.page.get_by_placeholder("请输入地址").fill("山东省青岛市李沧区九水东路东李新苑")
            self.page.get_by_placeholder("请选择状态").click()
        with allure.step("点击确定按钮，进行保存"):
            self.page.get_by_role("button", name="确 定").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)

    def delete_gateway(self):
        time.sleep(5)
        self.page.get_by_role("row", name="1", exact=True).locator("label span").nth(1).click()
        self.page.get_by_role("button", name="删除").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)
        self.page.get_by_role("button", name="确认").click()

    def update_gateway(self, project):
        time.sleep(2)
        self.page.get_by_role("link", name="网关管理").click()
        self.page.get_by_role("textbox", name="请输入项目名称").click()
        self.page.get_by_role("textbox", name="请输入项目名称").fill(f"{project}")
        self.page.get_by_role("button", name=" 查询").click()
        self.page.locator(
            '//*[@id="app"]/div/div[2]/section/div[1]/div[2]/div[5]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[15]/div/div/i[2]').first.click()
        self.page.get_by_placeholder("请输入网关别名").fill("修改测试网关")
        self.page.get_by_label("网关编辑窗口").get_by_role("spinbutton").fill("6")
        self.page.get_by_role("button", name="确 定").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)
