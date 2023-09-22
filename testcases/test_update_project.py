import allure
import pytest

from page.Project_Page import ProjectPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestUpdateProject:
    @allure.title("修改项目信息")
    @pytest.mark.run(order=7)
    def test_updata_project(self, page):
        self.update = ProjectPage(page)
        with allure.step("从首页进入项目中心"):
            self.sidebar = SidebarPage(page)
            self.sidebar.click_project_max()
            self.sidebar.click_project()
        with allure.step("修改项目信息"):
            self.update.update_project("云平台项目")
