import allure

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
