import re

from common.BasePages import BasePage


class TouchScreenPage(BasePage):
    def add_touch_screen(self, name):
        self.click(self.page.get_by_role("button", name="新增"), "新增触摸屏")
        self.input_data(self.page.get_by_placeholder("请输入触摸屏名称"), f"{name}", "触摸屏名称")
        self.click(self.page.get_by_placeholder("请选择网关"), "选择所属网关")
        self.click(self.page.locator("li").filter(has_text="张三").first, "选择所属网关")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^触摸屏Ip\.\.\.触摸屏端口$")).get_by_role(
            "textbox").first, "192", "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^触摸屏Ip\.\.\.触摸屏端口$")).get_by_role(
            "textbox").first, "186", "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^触摸屏Ip\.\.\.触摸屏端口$")).get_by_role(
            "textbox").first, "221", "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^触摸屏Ip\.\.\.触摸屏端口$")).get_by_role(
            "textbox").first, "221", "11")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")

    def get_touch_screen(self, name):
        self.input_data(self.page.get_by_placeholder("请选触摸屏名称"), f"{name}", "查询条件-触摸屏名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def update_touch_screen(self, name):
        self.click(self.page.get_by_role("cell", name="  ").locator("i").nth(1), "编辑触摸屏")
        self.input_data(self.page.get_by_placeholder("请输入触摸屏名称"), f"{name}", "触摸屏名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")

    def delete_touch_screen(self):
        self.click(self.page.get_by_role("button", name="删除"), "删除按钮")
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
