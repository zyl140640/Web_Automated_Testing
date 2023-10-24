import allure
import pytest

from page.Project_Center.Device.Device_Page import DevicePage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("设备管理")
class TestMainDevice:

    @allure.title("创建设备")
    @allure.description("测试创建设备功能是否正常")
    @pytest.mark.run(order=8)
    @allure.severity("critical")
    def test_add_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.add_device("云平台项目", "云平台项目设备名称")

    @allure.title("删除设备")
    @allure.description("测试删除设备功能是否正常")
    @pytest.mark.run(order=7)
    @allure.severity("trivial")
    def test_delete_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.delete_device()

    @allure.title("修改设备")
    @allure.description("测试修改设备功能是否正常")
    @pytest.mark.run(order=9)
    @allure.severity("trivial")
    def test_update_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.update_device("云平台项目")

    @allure.title("查询设备")
    @allure.description("测试查询设备功能是否正常")
    @pytest.mark.run(order=10)
    @allure.severity("trivial")
    def test_get_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_project_name("云平台项目")
