import re
import time

import allure
from playwright.sync_api import Page


class ProjectPage:
    def __init__(self, page: Page):
        self.page = page

    def add_project(self, project, project_id, gateway):
        time.sleep(2)
        with allure.step("点击新增"):
            self.page.get_by_role("button", name="新增").click()
        with allure.step("输入项目名称"):
            self.page.get_by_label("新增项目").get_by_placeholder("请输入项目名称").fill(f"{project}")
        with allure.step("输入项目编码"):
            self.page.get_by_placeholder("请输入项目编码").fill(project_id)
        with allure.step("使用地图选择位置"):
            self.page.get_by_placeholder("请点击地图选择位置").click()
            time.sleep(3)
            self.page.locator(".BMap_mask").click()
            self.page.get_by_role("button", name="确 定").click()
        with allure.step("输入负责人信息"):
            self.page.get_by_placeholder("请输入负责人").fill("张三")
        with allure.step("输入电话信息"):
            self.page.get_by_placeholder("请输入电话").fill("15533065391")
        # self.page.get_by_placeholder("请选择组织").click()
        # self.page.get_by_text("宁波高新区安立特电气科技有限公司").nth(3).click()
        # self.page.get_by_placeholder("请选择区域").click()
        # self.page.get_by_text("区域", exact=True).click()
        with allure.step("点击下一步"):
            self.page.get_by_role("button", name="下一步").click()
        with allure.step("输入网关别名"):
            self.page.get_by_placeholder("请输入网关别名").fill("测试项目网关")
        with allure.step("输入网关SN"):
            self.page.get_by_placeholder("请输入网关SN").fill(gateway)
            self.page.get_by_text("添加网口").click()
            self.page.get_by_role("textbox", name="请选择", exact=True).nth(2).click()
            self.page.get_by_text("Modbus TCP").click()
            self.page.get_by_placeholder("请输入设备IP").fill("198.180.16.11")
        with allure.step("进入选择自定义模板页面"):
            self.page.get_by_role("button", name="下一步").click()
            time.sleep(3)
            self.page.get_by_role("button", name="下一步").click()
        with allure.step("选择模板并保存"):
            self.page.locator("label").filter(has_text="0905自定义模板").locator("span").nth(1).click()
            self.page.get_by_role("button", name="保 存").click()
            allure.attach(self.page.screenshot(timeout=2000), "用例执行结果图", allure.attachment_type.PNG)
            self.page.get_by_role("button", name="关闭").click()

    def detect_project(self):
        time.sleep(5)
        self.page.get_by_role("textbox", name="请输入项目名称").click()
        self.page.get_by_role("textbox", name="请输入项目名称").fill("测试dome1")
        self.page.get_by_role("button", name=" 查询").click()
        self.page.get_by_role("cell", name="   ").locator("i").nth(2).click()
        allure.attach(self.page.screenshot(timeout=2000), "用例执行结果图", allure.attachment_type.PNG)
        self.page.get_by_role("button", name="确认").click()

    def update_project(self, project):
        self.page.get_by_role("textbox", name="请输入项目名称").click()
        self.page.get_by_role("textbox", name="请输入项目名称").fill(f"{project}")
        self.page.get_by_role("button", name=" 查询").click()
        self.page.get_by_role("cell", name="   ").locator("i").nth(1).click()
        self.page.get_by_placeholder("请输入负责人").fill("李四")
        self.page.get_by_placeholder("请输入电话").fill("15533065392")
        self.page.get_by_role("button", name="结束并保存").click()
        allure.attach(self.page.screenshot(timeout=2000), "用例执行结果图", allure.attachment_type.PNG)
        self.page.get_by_role("button", name="确定").click()
