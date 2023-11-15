import allure
import pytest

from page.Project_Center.Gateway.Gateway_xieyi_Page import GatewayXieYiPage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("网关管理-协议配置")
class TestGatewayXieYi:
    project_name = "测试主流程项目"

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.gatewayxieyi = GatewayXieYiPage(page)

    @allure.title("网关-协议配置-添加网关")
    @allure.description("测试添加网关功能是否正常")
    def test_add_gateway_xieyi(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_xieyi("192.186.0.1")

    @allure.title("网关-协议配置-修改网关")
    @allure.description("测试修改协议功能是否正常")
    def test_update_gateway_xieyi(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.update_chuankou()

    @allure.title("网关-协议配置-删除网关")
    @allure.description("测试删网关议功能是否正常")
    def test_delete_gateway_xieyi(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.delete_xieyi()

    @allure.title("网关-协议配置-添加串口")
    @allure.description("测试添加串口功能是否正常")
    def test_add_gateway_chuankou(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.add_chuangkou()

    @allure.title("网关-协议配置-修改串口")
    @allure.description("测试修改协议功能是否正常")
    def test_update_gateway_chuankou(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.update_wangkou()

    @allure.title("网关-协议配置-删除串口")
    @allure.description("测试删除协议功能是否正常")
    def test_delete_gateway_chuangkou(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.delete_xieyi()

    @allure.title("网关-协议配置-网口连接测试")
    @allure.description("测试网口连接测试功能是否正常")
    def test_lianjie_gateway_xieyi(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("协议配置")
        self.gatewayxieyi.wangkou_lianjie("192.168.50.97")
