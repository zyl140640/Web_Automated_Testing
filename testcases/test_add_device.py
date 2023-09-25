import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestAddDevice:

    @allure.title("创建设备")
    @pytest.mark.run(order=5)
    def test_add_device(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        with allure.step("进入设备管理页面"):
            self.sidebar.click_project_max()
            self.sidebar.click_device()
        with allure.step("添加设备"):
            self.device.add_device("云平台项目", "云平台项目设备名称")
