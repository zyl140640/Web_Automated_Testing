import datetime
import allure

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
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("参数读取")
        self.gateway.parm_read()

    @allure.title("网关-点表下发")
    @allure.description("测试点表下发功能是否正常")
    def test_issue_device_id(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表下发")
        self.gateway.issue_device_id()

    @allure.title("网关-基础信息下发")
    @allure.description("测试基础信息下发功能是否正常")
    def test_message_send(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("基础信息下发")
        self.gateway.message_send()

    @allure.title("网关-网络信息下发")
    @allure.description("测试网络信息下发功能是否正常")
    def test_network_send(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("网络配置下发")
        self.gateway.network_send()

    @allure.title("网关-同步时钟")
    @allure.description("测试同步时钟功能是否正常")
    def test_lock_in_time(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("同步时钟")
        self.gateway.lock_in_time()

    @allure.title("网关-远程调试开关")
    @allure.description("测试远程调试开关功能是否正常")
    def test_debug_switch(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("远程调试开关")
        self.gateway.debug_switch()

    @allure.title("网关-获取网关时间")
    @allure.description("测试网关时钟功能是否正常")
    def test_clock_gateway(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway = GatewayPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("获取网关时间")
        current_datetime = datetime.datetime.now()
        self.gateway.get_clock_gate(current_datetime.year)
