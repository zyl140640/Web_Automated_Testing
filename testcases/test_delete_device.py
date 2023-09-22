import time

import allure
import pytest

from page.Device_Page import DevicePage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestDeleteDevice:

    @allure.title("删除设备")
    @pytest.mark.run(order=4)
    def test_delete_device(self, page):
        self.sidebar = SidebarPage(page)
        self.device = DevicePage(page)
        with allure.step("执行删除设备步骤"):
            self.sidebar.click_project_max()
            self.sidebar.click_device()
            self.device.delete_device()
