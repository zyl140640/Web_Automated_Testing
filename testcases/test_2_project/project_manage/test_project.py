import random

import allure

from page.Project_Page import ProjectPage
from page.SidebarPage import SidebarPage


@allure.feature("项目管理")
class TestProject:
    @allure.title("复制项目信息")
    @allure.description("测试复制项目功能是否正常")
    @allure.severity("critical")
    def test_copy_project(self, init, page):
        a = random.randint(5400000000000000, 5499999999999999)
        self.project = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.sidebar.click_more_functions("复制")
        self.project.copy_project("Copy_不允许删除pro", f"{a}")

    @allure.title("上传项目材料")
    @allure.description("测试上传材料功能是否正常")
    @allure.severity("critical")
    def test_file_project(self, init, page):
        self.project = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.sidebar.click_more_functions("上传资料")
        self.project.update_date()

    @allure.title("项目-相关资料")
    @allure.description("测试项目-相关资料功能是否正常")
    @allure.severity("critical")
    def test_update_relevant_date(self, init, page):
        self.project = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.sidebar.click_more_functions("相关资料")
        self.project.update_relevant_date()
