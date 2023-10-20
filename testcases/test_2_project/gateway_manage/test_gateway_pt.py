import allure

from page.Gateway_PT_Page import GatewayPTPage
from page.SidebarPage import SidebarPage


@allure.feature("网关管理")
class TestGatewayXieYi:

    @allure.title("网关-点表配置-添加点位信息")
    @allure.description("测试添加点表-点位功能是否正常")
    def test_add_gateway_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.add_gateway_pt("云平台点位")

    @allure.title("网关-点表配置-查询点位信息")
    @allure.description("测试查询点表-点位功能是否正常")
    def test_get_gateway_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.get_gateway_pt("云平台点位")

    @allure.title("网关-点表配置-修改点位信息")
    @allure.description("测试修改点表-点位功能是否正常")
    def test_update_gateway_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.update_gateway_pt("云平台点位")

    @allure.title("网关-点表配置-删除点位信息")
    @allure.description("测试删除点表-点位功能是否正常")
    def test_delete_gateway_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.delete_gateway_pt()

    @allure.title("网关-点表配置-点表下发")
    @allure.description("测试点表配置-点表下发功能是否正常")
    def test_pt_send(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.pt_send()

    @allure.title("网关-点表配置-批量新增")
    @allure.description("测试点表配置-批量新增功能是否正常")
    def test_batch_addition_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.batch_addition_pt("10", "11", "2")

    @allure.title("网关-点表配置-批量修改从站号")
    @allure.description("测试批量修改从站号功能是否正常")
    def test_batch_update_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.batch_update_pt("112")

    @allure.title("网关-点表配置-批量删除点位信息")
    @allure.description("测试批量删除点表-点位功能是否正常")
    def test_batch_gateway_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.gateway_pt = GatewayPTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.delete_gateway_pt()
