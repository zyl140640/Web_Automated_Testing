import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.Device_id_Page import DeviceIdPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestAddDeviceId:

    @allure.title("创建设备点表")
    @pytest.mark.run(order=6)
    def test_add_device_id(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        with allure.step("进入电表管理页面"):
            self.sidebar.click_project_max()
            self.sidebar.click_device_id()
        with allure.step("添加设备点表信息"):
            self.device_id.add_device_id()
