import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.Device_id_Page import DeviceIdPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestDeviceId:

    @allure.title("创建设备点表")
    @pytest.mark.run(order=6)
    def test_add_device_id(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_id()
