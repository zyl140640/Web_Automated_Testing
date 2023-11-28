import allure
import pytest

from page.Dada_Center.configuration_management import ConfigurationManagement
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("可视化管理")
class TestConfiguration:

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.configuration = ConfigurationManagement(page)

    @allure.title("组态管理-新增")
    @allure.description("测试复制项目功能是否正常")
    @allure.severity("critical")
    def test_add_configuration(self):
        self.sidebar.click_data_max()
        self.sidebar.click_configuration()
        self.configuration.add_configuration("自动化-测试组态管理")

    @allure.title("组态管理-查询")
    @allure.description("测试复制项目功能是否正常")
    @allure.severity("critical")
    def test_get_configuration(self):
        self.sidebar.click_data_max()
        self.sidebar.click_configuration()
        self.configuration.get_configuration("测试主流程项目")

    @allure.title("组态管理-删除")
    @allure.description("测试复制项目功能是否正常")
    @allure.severity("critical")
    def test_delete_configuration(self):
        self.sidebar.click_data_max()
        self.sidebar.click_configuration()
        self.configuration.get_configuration("测试主流程项目")
        self.configuration.delete_configuration()

