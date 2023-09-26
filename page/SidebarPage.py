import re

from playwright.sync_api import Page

from common.BasePages import BasePage


class SidebarPage(BasePage):

    def click_project_max(self):
        # self.page.locator("div").filter(has_text=re.compile(r"^项目中心$")).click()
        self.click(self.page.locator("div").filter(has_text=re.compile(r"^项目中心$")), "项目中心")

    def click_project(self):
        # self.page.get_by_role("link", name="项目管理").click()
        self.click(self.page.get_by_role("link", name="项目管理"), "项目管理")

    def click_gateway(self):
        # self.page.get_by_role("link", name="网关管理").click()
        self.click(self.page.get_by_role("link", name="网关管理"), "网关管理")

    def click_device(self):
        # self.page.get_by_role("link", name="设备管理").click()
        self.click(self.page.get_by_role("link", name="设备管理"), "设备管理")

    def click_device_id(self):
        # self.page.get_by_role("link", name="点表管理").click()
        self.click(self.page.get_by_role("link", name="点表管理"), "点表管理")
