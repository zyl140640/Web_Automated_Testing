import allure

from page.Project_Center.Device.Device_PT_Page import DevicePTPage
from page.Project_Center.Device_id.Device_id_Page import DeviceIdPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("点表管理")
class TestMainDeviceId:

    @allure.title("创建点表")
    @allure.severity("critical")
    @allure.description("测试创建点表功能是否正常")
    def test_add_device_id(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.add_device_id("云平台测试点位")

    @allure.title("查询点表")
    @allure.severity("critical")
    @allure.description("测试查询点表功能是否正常")
    def test_get_device_id(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")

    @allure.title("修改设备点表")
    @allure.severity("critical")
    @allure.description("测试修改点表功能是否正常")
    def test_update_device_id(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")
        self.device_id.update_device_id()

    @allure.title("点表管理-保存为模板")
    @allure.description("测试点表管理-保存为模板功能是否正常")
    def test_device_id_template(self, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")
        self.device_pt.device_save_as_template("测试点表模板", "测试点表模板描述信息")

    @allure.title("绑定网关")
    @allure.severity("critical")
    @allure.description("测试绑定网关功能是否正常")
    def test_bind_device(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")
        self.device_id.bind_gateway()

    @allure.title("绑定设备")
    @allure.severity("critical")
    @allure.description("测试绑定设备功能是否正常")
    def test_bind_device(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")
        self.device_id.bind_device()

    @allure.title("创建点表-创建点位")
    @allure.severity("critical")
    @allure.description("测试创建点位功能是否正常")
    def test_add_device_dianwei(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.add_device_dianwei("云平台测试点位")

    @allure.title("点表管理-点位-批量新增")
    @allure.severity("critical")
    @allure.description("测试批量新增点位功能是否正常")
    def test_device_addition_pt(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_addition_pt("112", "22", "1")

    @allure.title("点表管理-点位-引用模板")
    @allure.severity("critical")
    @allure.description("测试点位-引用模板功能是否正常")
    def test_device_pt_yinyong(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_pt_yinyong()

    @allure.title("点表管理-点位-下载模板")
    @allure.severity("critical")
    @allure.description("测试点位-下载模板功能是否正常")
    def test_device_xiazai_moban(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.device_xiazai_moban()

    @allure.title("删除设备点表")
    @allure.severity("critical")
    @allure.description("测试删除点表功能是否正常")
    def test_delete_device_id(self, page):
        self.sidebar = SidebarPage(page)
        self.device_id = DeviceIdPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id("云平台测试点位")
        self.device_id.delete_device_id()
