import allure
import pytest

from page.Project_Center.Device.Device_PT_Page import DevicePTPage
from page.Project_Center.Device_id.Device_id_Page import DeviceIdPage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("点表管理")
class TestDeviceId:

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.device_pt = DevicePTPage(page)
        self.device_id = DeviceIdPage(page)

    @allure.title("点表管理-保存为模板")
    @allure.description("测试点表管理-保存为模板功能是否正常")
    def test_device_id_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.sidebar.click(self.sidebar.page.get_by_role("button", name=" 展开"), "展开查询条件")
        self.sidebar.get_project_name("测试项目-主流程")
        self.device_pt.device_save_as_template("测试点表模板", "测试点表模板描述信息")

    @allure.title("绑定网关")
    @allure.severity("critical")
    @allure.description("测试绑定网关功能是否正常")
    def test_bind_gateway(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("测试项目-点表")
        self.device_id.bind_gateway("714005F36924F9C7")

    @allure.title("绑定设备")
    @allure.severity("critical")
    @allure.description("测试绑定设备功能是否正常")
    def test_bind_device(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("测试项目-点表")
        self.device_id.bind_device()

    @allure.title("创建点表-创建点位")
    @allure.severity("critical")
    @allure.description("测试创建点位功能是否正常")
    def test_add_device_dianwei(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.add_device_dianwei("测试-新增点位")

    @allure.title("点表管理-点位-批量新增")
    @allure.severity("critical")
    @allure.description("测试批量新增点位功能是否正常")
    def test_device_addition_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_addition_pt("112", "22", "1")

    @allure.title("点表管理-点位-引用模板")
    @allure.severity("critical")
    @allure.description("测试点位-引用模板功能是否正常")
    def test_device_pt_yinyong(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_pt_yinyong("测试点表模板")

    @allure.title("点表管理-点位-下载模板")
    @allure.severity("critical")
    @allure.description("测试点位-下载模板功能是否正常")
    def test_device_xiazai_moban(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_xiazai_moban()
