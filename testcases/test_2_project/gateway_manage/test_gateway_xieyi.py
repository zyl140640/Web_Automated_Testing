import allure

from page.Project_Center.Gateway.Gateway_xieyi_Page import GatewayXieYiPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("网关管理-协议配置")
class TestGatewayXieYi:

    @allure.title("网关-协议配置-添加网关")
    @allure.description("测试添加网关功能是否正常")
    def test_add_gateway_xieyi(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_xieyi("192.186.0.1")

    @allure.title("网关-协议配置-修改网关")
    @allure.description("测试修改协议功能是否正常")
    def test_update_gateway_xieyi(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.update_chuankou()

    @allure.title("网关-协议配置-删除网关")
    @allure.description("测试删网关议功能是否正常")
    def test_delete_gateway_xieyi(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.delete_xieyi()

    @allure.title("网关-协议配置-添加串口")
    @allure.description("测试添加串口功能是否正常")
    def test_add_gateway_chuankou(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_chuangkou()

    @allure.title("网关-协议配置-修改串口")
    @allure.description("测试修改协议功能是否正常")
    def test_update_gateway_chuankou(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.update_wangkou()

    @allure.title("网关-协议配置-删除串口")
    @allure.description("测试删除协议功能是否正常")
    def test_delete_gateway_chuangkou(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.delete_xieyi()

    @allure.title("网关-协议配置-网口连接测试")
    @allure.description("测试网口连接测试功能是否正常")
    def test_lianjie_gateway_xieyi(self, page):
        self.sidebar = SidebarPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.wangkou_lianjie("192.186.0.1")
