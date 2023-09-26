import random

import allure
import pytest

from page.Gateway_Page import GatewayPage
from page.SidebarPage import SidebarPage


@allure.feature("御控工业云平台")
# @allure.story("主流程")
class TestAddGateway:

    @allure.title("创建网关")
    @pytest.mark.run(order=2)
    def test_add_gateway(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        a = random.randint(1000000000000000, 9999999999999999)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.gateway.add_gateway("云平台项目", "云平台网关别名", f"{a}")
