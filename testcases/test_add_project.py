import random
import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.Device_id_Page import DeviceIdPage
from page.Gateway_Page import GatewayPage
from page.Project_Page import ProjectPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
# @allure.story("主流程")
class TestAddProject:

    @allure.title("创建项目")
    @pytest.mark.run(order=1)
    def test_add_project(self, page):
        a = random.randint(1000000000000000, 9999999999999999)
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        with allure.step("从首页进入项目中心"):
            self.sidebar.click_project_max()
            self.sidebar.click_project()
        with allure.step("添加项目"):
            self.project.add_project("云平台项目", "00100", f"{a}")
