import allure
import pytest

from page.Dada_Center.screen_monitoring import ScreenMonitoring
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("可视化管理")
class TestScreenMonitoring:

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.screen_monitoring = ScreenMonitoring(page)

    def test_add_screen_monitoring(self):
        self.sidebar.click_data_max()
        self.sidebar.click_screen_monitoring()
        self.screen_monitoring.add_screen_monitoring("测试大屏哦")
