import random

import allure
import pytest

from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("项目管理")
class TestMainProject:

    @allure.title("创建项目")
    @allure.description("测试创建项目功能是否正常")
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_add_project(self, page):
        a = random.randint(1000000000000000, 9999999999999999)
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.add_project("云平台项目", "00100", f"{a}")

    @allure.title("修改项目信息")
    @pytest.mark.run(order=3)
    @allure.description("测试修改项目功能是否正常")
    @allure.severity("critical")
    def test_update_project(self, page):
        self.update = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.update.update_project("云平台项目")

    @allure.title("删除项目")
    @allure.description("测试删除项目功能是否正常")
    @pytest.mark.run(order=-1)
    @allure.severity("normal")
    def test_detect_project(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.detect_project("云平台项目")

    @allure.title("查询项目信息")
    @pytest.mark.run(order=2)
    @allure.description("测试查询项目功能是否正常")
    def test_git_project(self, page):
        self.project = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.sidebar.get_project_name("云平台项目")
