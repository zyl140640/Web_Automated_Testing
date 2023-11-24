import allure
import pytest

from page.Project_Center.Device.Device_PT_Page import DevicePTPage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("设备管理-点表配置")
class TestDevicePT:
    device_pt_name = "测试设设备-点表-点位"
    divice_name = "测试主流程-新增设备"

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.sidebar = SidebarPage(page)
        self.device_pt = DevicePTPage(page)

    @allure.title("设备管理-点表配置-添加点位信息")
    @allure.description("测试添加点表-点位功能是否正常")
    def test_device_add_device_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_add_device_pt(self.device_pt_name, "2")

    @allure.title("设备管理-点表配置-查询点位信息")
    @allure.description("测试查询点表-点位功能是否正常")
    def test_device_get_device_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_get_device_pt(self.device_pt_name)

    @allure.title("设备管理-点表配置-修改点位信息")
    @allure.description("测试修改点表-点位功能是否正常")
    def test_device_update_device_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_get_device_pt(self.device_pt_name)
        self.device_pt.device_update_device_pt(self.device_pt_name)

    @allure.title("设备管理-点表配置-点表下发")
    @allure.description("测试点表配置-点表下发功能是否正常")
    def test_device_pt_send(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_pt_send()

    @allure.title("设备管理-点表配置-删除点位信息")
    @allure.description("测试删除点表-点位功能是否正常")
    def test_device_delete_device_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_get_device_pt(self.device_pt_name)
        self.device_pt.device_delete_device_pt()

    @allure.title("设备管理-点表配置-批量新增")
    @allure.description("测试点表配置-批量新增功能是否正常")
    def test_device_batch_addition_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_batch_addition_pt("121", "111", "2")

    @allure.title("设备管理-点表配置-批量修改从站号")
    @allure.description("测试批量修改从站号功能是否正常")
    def test_device_batch_update_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_batch_update_pt("112")

    @allure.title("设备管理-点表配置-保存为模板")
    @allure.description("测试保存为模板功能是否正常")
    def test_device_save_as_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_save_as_template("测试点表模板", "测试点表模板描述信息")

    @allure.title("设备管理-点表配置-批量删除点位信息")
    @allure.description("测试批量删除点表-点位功能是否正常")
    @pytest.mark.skip("不需要批量删除点位信息")
    def test_device_batch_device_pt(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_delete_device_pt()
        self.device_pt.device_delete_device_pt()

    @allure.title("设备管理-点表配置-引用模板")
    @allure.description("测试引用模板功能是否正常")
    def test_device_yinyong_template(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_yinyong_template("默认引用模板")

    @allure.title("设备管理-点表配置-模板下载")
    @allure.description("测试模板下载功能是否正常")
    def test_device_template_download(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.device_template_download()

    @allure.title("设备管理-点表配置-关联点表")
    @allure.description("测试关联点表功能是否正常")
    def test_link_table(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_device_name(self.divice_name)
        self.sidebar.click_more_functions("点表配置")
        self.device_pt.link_table()
