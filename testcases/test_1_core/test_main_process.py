import random

import allure
import pytest

from page.Project_Center.Device.Device_Page import DevicePage
from page.Project_Center.Device_id.Device_id_Page import DeviceIdPage
from page.Project_Center.Gateway.Gateway_Page import GatewayPage
from page.Project_Center.Project.Project_Page import ProjectPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("主流程")
class TestMainProcess:
    project_name = "测试主流程项目"
    device_id_name = "测试主流程项目-点表"
    gateway_sn = random.randint(1000000000000000, 9999999999999999)

    @pytest.fixture(scope="function", autouse=True)
    def global_init(self, page):
        self.sidebar = SidebarPage(page)
        self.project = ProjectPage(page)
        self.gateway = GatewayPage(page)
        self.device = DevicePage(page)
        self.device_id = DeviceIdPage(page)

    @allure.title("创建项目信息")
    @allure.description("测试创建项目功能是否正常")
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    def test_main_add_project(self):
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.add_project(f"{self.project_name}", "00100", "测试主流程项目网关", f"{self.gateway_sn}")

    @allure.title("查询项目信息")
    @allure.description("测试查询项目功能是否正常")
    def test_main_git_project(self):
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.sidebar.get_project_name(f"{self.project_name}")

    @allure.title("修改项目信息")
    @allure.description("测试修改项目功能是否正常")
    @allure.severity("critical")
    def test_main_update_project(self):
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.update_project(f"{self.project_name}")

    @allure.title("删除网关信息")
    @allure.description("测试删除网关功能是否正常")
    @allure.severity("minor")
    def test_main_delete_gateway(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_project_name(f"{self.project_name}")
        self.gateway.delete_gateway()

    @allure.title("创建网关信息")
    @allure.description("测试创建网关功能是否正常")
    @allure.severity("critical")
    def test_main_add_gateway(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        a = random.randint(1000000000000000, 9999999999999999)
        self.gateway.add_gateway(f"{self.project_name}", "测试主流程网关别名", f"{a}")

    @allure.title("修改网关信息")
    @allure.description("测试修改网关功能是否正常")
    def test_main_update_gateway(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_name(f"{self.project_name}")
        self.gateway.update_gateway()

    @allure.title("查询网关信息")
    @allure.description("测试查询网关功能是否正常")
    def test_main_get_gateway(self):
        self.sidebar.click_project_max()
        self.sidebar.click_gateway()
        self.sidebar.get_gateway_name(f"{self.project_name}")

    @allure.title("删除设备信息")
    @allure.description("测试删除设备功能是否正常")
    @allure.severity("trivial")
    def test_main_delete_device(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_project_name(f"{self.project_name}")
        self.device.delete_device()

    @allure.title("创建设备信息")
    @allure.description("测试创建设备功能是否正常")
    @allure.severity("critical")
    def test_main_add_device(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.add_device(f"{self.project_name}", "测试主流程设备名称")

    @allure.title("修改设备信息")
    @allure.description("测试修改设备功能是否正常")
    @allure.severity("trivial")
    def test_main_update_device(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.device.update_device(f"{self.project_name}")

    @allure.title("查询设备信息")
    @allure.description("测试查询设备功能是否正常")
    @allure.severity("trivial")
    def test_main_get_device(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device()
        self.sidebar.get_project_name(f"{self.project_name}")

    @allure.title("创建点表信息")
    @allure.severity("critical")
    @allure.description("测试创建点表功能是否正常")
    def test_main_add_device_id(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.add_device_one()
        self.device_id.add_device_id(f"{self.device_id_name}")

    @allure.title("查询点表信息")
    @allure.severity("critical")
    @allure.description("测试查询点表功能是否正常")
    def test_main_get_device_id(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id(f"{self.device_id_name}")

    @allure.title("修改点表信息")
    @allure.severity("critical")
    @allure.description("测试点表信息功能是否正常")
    def test_main_update_device_id(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id(f"{self.device_id_name}")
        self.device_id.update_device_id()

    @allure.title("删除点表信息")
    @allure.severity("critical")
    @allure.description("测试删除点表功能是否正常")
    @pytest.mark.run(order=-2)
    def test_main_delete_device_id(self):
        self.sidebar.click_project_max()
        self.sidebar.click_device_id()
        self.device_id.get_device_id(f"{self.device_id_name}")
        self.device_id.delete_device_id()

    @allure.title("删除项目信息")
    @allure.description("测试删除项目功能是否正常")
    @allure.severity("normal")
    @pytest.mark.run(order=-1)
    def test_main_detect_project(self):
        self.sidebar.click_project_max()
        self.sidebar.click_project()
        self.project.detect_project(f"{self.project_name}")
