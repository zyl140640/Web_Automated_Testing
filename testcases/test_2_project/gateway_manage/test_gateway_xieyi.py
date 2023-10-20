import allure

from page.Gateway_xieyi_Page import GatewayXieYiPage
from page.SidebarPage import SidebarPage


@allure.feature("网关管理")
class TestGatewayXieYi:

    @allure.title("网关-协议配置-添加网关")
    @allure.description("测试添加网关功能是否正常")
    def test_add_gateway_xieyi(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_xieyi("192.186.0.1")

    @allure.title("网关-协议配置-添加串口")
    @allure.description("测试添加串口功能是否正常")
    def test_add_gateway_wangkou(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_chuangkou()

    @allure.title("网关-协议配置-修改协议")
    @allure.description("测试修改协议功能是否正常")
    def test_update_gateway_xieyi(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.update_chuankou()

    @allure.title("网关-协议配置-删除协议")
    @allure.description("测试删除协议功能是否正常")
    def test_delete_gateway_xieyi(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.delete_xieyi()