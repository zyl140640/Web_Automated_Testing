import random

import allure
import pytest

from page.Project_Page import ProjectPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
# @allure.story("主流程")
class TestProject:

    @allure.title("创建项目")
    @pytest.mark.run(order=1)
    def test_add_project(self, init, page):
        a = random.randint(1000000000000000, 9999999999999999)
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.add_project("云平台项目", "00100", f"{a}")

    @allure.title("修改项目信息")
    @pytest.mark.run(order=7)
    def test_update_project(self, init, page):
        self.update = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.update.update_project("云平台项目")

    @allure.title("删除项目")
    @pytest.mark.run(order=-1)
    def test_detect_project(self, init, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.detect_project("云平台项目")
