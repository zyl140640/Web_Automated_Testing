import random
import time

import allure
import pytest

from page.Gateway_Page import GatewayPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
class TestDeleteGateway:

    @allure.title("删除网关")
    @pytest.mark.run(order=3)
    def test_delete_gateway(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        with allure.step("执行删除网关步骤"):
            self.sidebar.click_project_max()
            self.sidebar.click_gateway()
            self.gateway.delete_gateway()
