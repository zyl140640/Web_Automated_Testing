import allure
import pytest

from page.Device_Page import DevicePage
from page.SidebarPage import SidebarPage


@allure.feature("设备管理")
class TestDevice:

    @allure.title("创建设备")
    @allure.description("测试创建设备功能是否正常")
    @pytest.mark.run(order=5)
    @allure.severity("critical")
    def test_add_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.add_device("云平台项目", "云平台项目设备名称")

    @allure.title("删除设备")
    @allure.description("测试删除设备功能是否正常")
    @pytest.mark.run(order=4)
    @allure.severity("trivial")
    def test_delete_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.delete_device()
