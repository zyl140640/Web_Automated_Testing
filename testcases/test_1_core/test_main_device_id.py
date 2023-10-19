import allure
import pytest

from page.Device_id_Page import DeviceIdPage
from page.SidebarPage import SidebarPage


@allure.feature("点表管理")
class TestDeviceId:

    @allure.title("创建设备点表")
    @pytest.mark.run(order=6)
    @allure.severity("critical")
    @allure.description("测试创建设备点表功能是否正常")
    def test_add_device_id(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_id()


    @allure.title("查询设备点表")
    @allure.severity("critical")
    @allure.description("测试查询设备点表功能是否正常")
    def test_add_device_id(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
