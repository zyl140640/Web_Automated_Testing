import re

from common.BasePages import BasePage


class TouchScreenPage(BasePage):
    def add_touch_screen(self, name):
        """
         触摸屏管理-添加触摸屏
        Args:
            name: 触摸屏名称
        """
        self.click(self.page.get_by_role("button", name="新增"), "新增触摸屏")
        self.input_data(self.page.get_by_placeholder("请输入触摸屏名称").last, f"{name}", "触摸屏名称")
        self.click(self.page.get_by_placeholder("请选择网关"), "选择所属网关")
        self.click(self.page.locator("li").filter(has_text="测试主流程项目-网关"),"选择项目流程自带网关")
        # self.click(self.page.locator("li").filter(has_text="714005F36924F9C7").first, "选择所属网关")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^触摸屏Ip\.\.\.触摸屏端口$")).get_by_role(
            "textbox").first, "192", "")
        self.input_data(self.page.get_by_label("触摸屏新增").locator("form div").filter(
            has_text="触摸屏Ip... 请输入IP地址 触摸屏端口").get_by_role("textbox").nth(1), "186", "触摸屏输入框")
        self.input_data(self.page.get_by_label("触摸屏新增").locator("form div").filter(
            has_text="触摸屏Ip... 请输入IP地址 触摸屏端口").get_by_role("textbox").nth(2), "122", "触摸屏输入框")
        self.input_data(self.page.get_by_label("触摸屏新增").locator("form div").filter(
            has_text="触摸屏Ip... 请输入IP地址 触摸屏端口").get_by_role("textbox").nth(3), "33", "触摸屏输入框")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.asserts_result(self.get_alert("触摸屏管理-新增"), "=", "保存成功")

    def get_touch_screen(self, name):
        self.input_data(self.page.get_by_placeholder("请输入触摸屏名称"), f"{name}", "查询条件-触摸屏名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def update_touch_screen(self, name):
        self.click(self.page.get_by_role("cell", name="  ").locator("i").nth(1), "编辑触摸屏")
        self.input_data(self.page.get_by_placeholder("请输入触摸屏名称").last, f"{name}", "触摸屏名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.asserts_result(self.get_alert("触摸屏管理-修改"), "=", "保存成功")

    def delete_touch_screen(self):
        self.list_row("1")
        self.click(self.page.get_by_role("button", name="删除"), "删除按钮")
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        self.asserts_result(self.get_alert("触摸屏管理-删除"), "=", "删除成功")
