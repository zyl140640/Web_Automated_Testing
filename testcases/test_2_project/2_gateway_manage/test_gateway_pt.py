import allure
import pytest

from page.Project_Center.Gateway.Gateway_PT_Page import GatewayPTPage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("网关管理-点表配置")
class TestGatewayPT:
    gateway_pt_value = "测试主流程-网关-点位"
    project_name = "测试主流程项目"

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.gateway_pt = GatewayPTPage(page)

    @allure.title("网关管理-点表配置-添加点位信息")
    @allure.description("测试添加点表-点位功能是否正常")
    def test_add_gateway_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.add_gateway_pt(self.gateway_pt_value, "1011")

    @allure.title("网关管理-点表配置-查询点位信息")
    @allure.description("测试查询点表-点位功能是否正常")
    def test_get_gateway_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.get_gateway_pt(self.gateway_pt_value)

    @allure.title("网关管理-点表配置-修改点位信息")
    @allure.description("测试修改点表-点位功能是否正常")
    def test_update_gateway_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.get_gateway_pt(self.gateway_pt_value)
        self.gateway_pt.update_gateway_pt(self.gateway_pt_value)

    @allure.title("网关管理-点表配置-点表下发")
    @allure.description("测试点表配置-点表下发功能是否正常")
    def test_pt_send(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.pt_send()

    @allure.title("网关管理-点表配置-删除点位信息")
    @allure.description("测试删除点表-点位功能是否正常")
    def test_delete_gateway_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.get_gateway_pt(self.gateway_pt_value)
        self.gateway_pt.delete_gateway_pt()

    @allure.title("网关管理-点表配置-批量新增")
    @allure.description("测试点表配置-批量新增功能是否正常")
    def test_batch_addition_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.batch_addition_pt("101", "11", "2")

    @allure.title("网关管理-点表配置-批量修改从站号")
    @allure.description("测试批量修改从站号功能是否正常")
    def test_batch_update_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.batch_update_pt("112")

    @allure.title("网关管理-点表配置-保存为模板")
    @allure.description("测试保存为模板功能是否正常")
    def test_save_as_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.save_as_template("测试点表模板", "测试点表模板描述信息")

    @allure.title("网关管理-点表配置-批量删除点位信息")
    @allure.description("测试批量删除点表-点位功能是否正常")
    def test_batch_gateway_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.delete_gateway_pt()
        self.gateway_pt.delete_gateway_pt()

    @allure.title("网关管理-点表配置-引用模板")
    @allure.description("测试引用模板功能是否正常")
    def test_yinyong_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.yinyong_template("云平台模板")

    @allure.title("网关管理-点表配置-模板下载")
    @allure.description("测试模板下载功能是否正常")
    def test_template_download(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(self.project_name)
        self.sidebar.click_more_functions("点表配置")
        self.gateway_pt.template_download()
