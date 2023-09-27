import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestDevice:

    @allure.title("创建设备")
    @pytest.mark.run(order=5)
    def test_add_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.add_device("云平台项目", "云平台项目设备名称")

    @allure.title("删除设备")
    @pytest.mark.run(order=4)
    def test_delete_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.delete_device()
