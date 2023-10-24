import allure

from page.Project_Center.Device.Device_PT_Page import DevicePTPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("设备管理-点表配置")
class TestDevicePT:

    @allure.title("设备管理-点表配置-添加点位信息")
    @allure.description("测试添加点表-点位功能是否正常")
    def test_device_add_device_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_add_device_pt("云平台点位", "2")

    @allure.title("设备管理-点表配置-查询点位信息")
    @allure.description("测试查询点表-点位功能是否正常")
    def test_device_get_device_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_get_device_pt("云平台点位")

    @allure.title("设备管理-点表配置-修改点位信息")
    @allure.description("测试修改点表-点位功能是否正常")
    def test_device_update_device_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_update_device_pt("云平台点位")

    @allure.title("设备管理-点表配置-删除点位信息")
    @allure.description("测试删除点表-点位功能是否正常")
    def test_device_delete_device_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_delete_device_pt()

    @allure.title("设备管理-点表配置-点表下发")
    @allure.description("测试点表配置-点表下发功能是否正常")
    def test_device_pt_send(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_pt_send()

    @allure.title("设备管理-点表配置-批量新增")
    @allure.description("测试点表配置-批量新增功能是否正常")
    def test_device_batch_addition_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_batch_addition_pt("10", "11", "2")

    @allure.title("设备管理-点表配置-批量修改从站号")
    @allure.description("测试批量修改从站号功能是否正常")
    def test_device_batch_update_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_batch_update_pt("112")

    @allure.title("设备管理-点表配置-保存为模板")
    @allure.description("测试保存为模板功能是否正常")
    def test_device_save_as_template(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_save_as_template("测试点表模板", "测试点表模板描述信息")

    @allure.title("设备管理-点表配置-批量删除点位信息")
    @allure.description("测试批量删除点表-点位功能是否正常")
    def test_device_batch_device_pt(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_delete_device_pt()
        self.device_pt.device_delete_device_pt()

    @allure.title("设备管理-点表配置-引用模板")
    @allure.description("测试引用模板功能是否正常")
    def test_device_yinyong_template(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_yinyong_template("云平台项目")

    @allure.title("设备管理-点表配置-模板下载")
    @allure.description("测试模板下载功能是否正常")
    def test_device_template_download(self, init, page):
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_gateway_sn("714005F36924F9C7")
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_template_download()
