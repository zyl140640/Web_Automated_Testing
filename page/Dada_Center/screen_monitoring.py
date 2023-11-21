from common.BasePages import BasePage


class ScreenMonitoring(BasePage):

    def add_screen_monitoring(self, name):
        with self.page.expect_popup() as page1_info:
            self.click(self.page.get_by_role("button", name="新增"), "新增大屏监控")
        page1 = page1_info.value
        self.click(page1.get_by_placeholder("请输入 大屏名称"), "大屏监控名称")
        self.input_data(page1.get_by_placeholder("请输入 大屏名称"), f"{name}", "大屏监控名称")
        self.click(page1.get_by_role("button", name=" 创建大屏"), "创建大屏")
        self.click(page1.get_by_role("menuitem", name=" ").locator("div").first.first, "新增翻牌器")
        self.click(page1.get_by_role("menuitem", name="翻牌器").get_by_role("img"), "选择翻牌器")
        self.click(page1.locator("div:nth-child(3) > div > .el-tooltip").first, "点击保存")
        self.asserts_result(page1.get_by_role("alert").inner_text(), "=", "大屏配置保存成功")

    def get_screen_monitoring(self, name):
        self.click(self.page.get_by_placeholder("请输入所属租户"), "选择所属租户查询条件")
        self.input_data(self.page.get_by_placeholder("请输入所属租户"), name, "选择所属租户查询条件")
        self.click(self.page.locator("li").filter(has_text=f"{name}"), f"选择[{name}]")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def delete_screen_monitoring(self, name):
        self.list_row(1)
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="删除"), "删除大屏监控")
