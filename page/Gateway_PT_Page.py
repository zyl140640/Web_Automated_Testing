import re

from common.BasePages import BasePage


class GatewayPTPage(BasePage):

    def add_gateway_pt(self, name):
        self.wait_for_timeouts(3000)
        self.click(self.page.get_by_role("button", name="新增", exact=True), "新增点位按钮")
        self.click(self.page.locator("div").filter(has_text=re.compile(r"^名称标识$")).get_by_role("textbox").first,
                   "点位名称")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^名称标识$")).get_by_role("textbox").first, f"{name}",
            "点位名称")
        self.click(self.page.get_by_role("textbox", name="请选择协议"), "请选择协议")
        self.click(self.page.get_by_role("listitem").nth(1), "确定协议")
        self.input_data(self.page.get_by_label("新增点位").locator("form div").filter(
            has_text="点位地址 请输入地址 寄存器地址区0X1X3X4X").get_by_role("textbox").first, "1", "点位地址")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "新增点位成功，请及时下发点表")

    def update_gateway_pt(self, name):
        self.wait_for_timeouts(1000)
        self.click(self.page.locator(
            ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_3_column_19 > .cell > .basicTableBtnBox > .el-icon-edit-outline").first,
                   "编辑点位按钮")
        self.input_data(
            self.page.get_by_label("编辑点位").locator("div").filter(has_text=re.compile(r"^名称标识$")).get_by_role(
                "textbox").first, f"{name}",
            "点位名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "编辑点位成功，请及时下发点表")

    def delete_gateway_pt(self):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("cell", name="  ").locator("i").nth(2), "删除按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "删除成功")

    def get_gateway_pt(self, name):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请输入参数名称"), "参数名称查询框")
        self.input_data(self.page.get_by_placeholder("请输入参数名称"), f"{name}", "参数名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
