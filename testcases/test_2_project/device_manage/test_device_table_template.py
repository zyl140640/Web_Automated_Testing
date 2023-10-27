import allure
import pytest

from page.Project_Center.Device.Device_Page import DevicePage
from page.Project_Center.Device.Device_Table_Template_Page import DeviceTableTemplatePage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("设备管理-点表模板")
class TestDeviceTableTemplate:
    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.tabletemplate = DeviceTableTemplatePage(page)
        self.project = ProjectPage(page)

    @allure.title("设备管理-点表模板-添加点表模板")
    @allure.description("测试添加点表模板-点位功能是否正常")
    def test_add_table_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.tabletemplate.add_table_template("云平台点表模板")

    @allure.title("设备管理-点表模板-查询点表模板")
    @allure.description("测试查询点表模板-点位功能是否正常")
    def test_get_table_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.tabletemplate.get_table_template("云平台点表模板")

    @allure.title("设备管理-点表模板-删除点表模板")
    @allure.description("测试删除点表模板-点位功能是否正常")
    def test_delete_table_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.tabletemplate.get_table_template("云平台点表模板")
        self.tabletemplate.delete_table_template()
