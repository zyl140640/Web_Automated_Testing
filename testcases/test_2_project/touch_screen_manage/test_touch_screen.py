import allure

from page.Project_Center.TouchScreen.Touch_Screen_Page import TouchScreenPage
from page.SideBar.SidebarPage import SidebarPage


@allure.feature("触摸屏管理")
class TestTouchScreenPage:

    @allure.title("触摸屏管理-新增触摸屏")
    @allure.description("测试新增触摸屏功能是否正常")
    def test_add_touch_screen(self, init, page):
        self.sidebar = SidebarPage(page)
        self.touch_screen = TouchScreenPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_touch_screen()
        self.touch_screen.add_touch_screen("触摸屏测试")

    @allure.title("触摸屏管理-查询触摸屏")
    @allure.description("测试查询触摸屏功能是否正常")
    def test_get_touch_screen(self, init, page):
        self.sidebar = SidebarPage(page)
        self.touch_screen = TouchScreenPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_touch_screen()
        self.touch_screen.get_touch_screen("触摸屏测试")

    @allure.title("触摸屏管理-修改触摸屏")
    @allure.description("测试修改触摸屏功能是否正常")
    def test_update_touch_screen(self, init, page):
        self.sidebar = SidebarPage(page)
        self.touch_screen = TouchScreenPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_touch_screen()
        self.touch_screen.get_touch_screen("触摸屏测试")
        self.touch_screen.update_touch_screen("修改触摸屏测试")

    @allure.title("触摸屏管理-删除触摸屏")
    @allure.description("测试删除触摸屏功能是否正常")
    def test_delete_touch_screen(self, init, page):
        self.sidebar = SidebarPage(page)
        self.touch_screen = TouchScreenPage(page)
        self.sidebar.click_project_max()
        self.sidebar.click_touch_screen()
        self.touch_screen.get_touch_screen("修改触摸屏测试")
        self.touch_screen.delete_touch_screen()
