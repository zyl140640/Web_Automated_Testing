import datetime
import random

import allure
import pytest

from page.Gateway_Page import GatewayPage
from page.SidebarPage import SidebarPage


@allure.feature("网关管理")
class TestGateway:

    @allure.title("网关-参数读取")
    @allure.description("测试参数读取功能是否正常")
    def test_read_gateway(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.gateway.get_sn_gateway("714005F36924F9C7")
        self.gateway.parm_read()

    @allure.title("网关-获取网关时间")
    @allure.description("测试网关时钟功能是否正常")
    def test_clock_gateway(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.gateway.get_sn_gateway("714005F36924F9C7")
        current_datetime = datetime.datetime.now()
        self.gateway.get_clock_gate(current_datetime.year)