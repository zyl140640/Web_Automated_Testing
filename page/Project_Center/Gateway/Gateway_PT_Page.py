import re

from common.BasePages import BasePage


class GatewayPTPage(BasePage):

    def add_gateway_pt(self, name, path):
        """
        新增点表配置点位信息
        Args:
            path: 点位地址
            name: 点位名称
        """
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
            has_text="点位地址 请输入地址 寄存器地址区0X1X3X4X").get_by_role("textbox").first, f"{path}", "点位地址")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "新增点位成功，请及时下发点表")

    def update_gateway_pt(self, name):
        """
               编辑点表配置点位信息
               Args:
                   name: 点位名称
               """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("cell", name="  ").locator("i").nth(1),
                   "编辑点位按钮")
        self.input_data(
            self.page.locator("div").filter(has_text=re.compile(r"^名称标识$")).get_by_role("textbox").first, f"{name}",
            "点位名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "编辑点位成功，请及时下发点表")

    def delete_gateway_pt(self):
        """
       删除点表配置点位信息
       """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("cell", name="  ").locator("i").nth(2), "删除按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "删除成功")

    def get_gateway_pt(self, name):
        """
               查询点表配置点位信息
               Args:
                   name: 点位名称
               """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请输入参数名称"), "参数名称查询框")
        self.input_data(self.page.get_by_placeholder("请输入参数名称"), f"{name}", "参数名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def pt_send(self):
        """
               下发点表信息
               """
        self.click(self.page.get_by_role("button", name="点表下发"), "点表下发按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确认"), "确定按钮")
        self.wait_for_timeouts(1000)
        result = self.get_text(self.page.get_by_role("alert").first, "获取结果")
        self.asserts_result(result, "=", "操作成功")

    def batch_addition_pt(self, one, two, three):
        """
               批量新增点表配置点位信息
               Args:
               """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="批量新增"), "批量新增按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请选择协议"), "请选择关联协议")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP"), "选择TCP协议")
        self.input_data(self.page.locator("div").filter(
            has_text=re.compile(r"^关联协议寄存器地址区0X1X3X4X数据类型Bool从站号起始位置个数$")).get_by_role(
            "textbox").nth(3), f"{one}", "从站号")
        self.input_data(self.page.locator("div").filter(
            has_text=re.compile(r"^关联协议寄存器地址区0X1X3X4X数据类型Bool从站号起始位置个数$")).get_by_role(
            "textbox").nth(4), f"{two}", "起始位置")
        self.input_data(self.page.locator("div").filter(
            has_text=re.compile(r"^关联协议寄存器地址区0X1X3X4X数据类型Bool从站号起始位置个数$")).get_by_role(
            "spinbutton"), f"{three}", "个数")
        self.click(self.page.get_by_role("button", name="生成预览"), "生成预览按钮")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取结果")
        self.asserts_result(result, "=", "批量新增成功，请及时下发点表")

    def batch_update_pt(self, one):
        """
          批量修改从站号
        Args:
            one: 从站号
        """
        self.list_row("1")
        self.click(self.page.get_by_role("button", name="批量修改从站号"), "批量修改从站号按钮")
        self.input_data(self.page.get_by_label("批量修改从站号").get_by_role("textbox"), f"{one}", "输入从站号")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取批量修改从站号结果")
        self.asserts_result(result, "=", "批量修改从站号成功")

    def save_as_template(self, name, miaoshu):
        """
        保存为模板
        Args:
            name: 模板名称
            miaoshu: 描述内容
        """
        self.list_row("1")
        self.click(self.page.get_by_role("button", name="保存为模板"), "保存为模板按钮")
        self.input_data(self.page.get_by_label("保存为模板").locator("input[type=\"text\"]"), f"{name}", "模板名称")
        self.input_data(self.page.locator("textarea"), f"{miaoshu}", "模板名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取保存为模板结果")
        self.asserts_result(result, "=", "点表保存为模板成功")

    def yinyong_template(self, name):
        """
        引用模板
        """
        self.click(self.page.get_by_role("button", name="引用模板"), "引用模板按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请选择协议"), "请选择协议")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP"), "选择Modbus TCP")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_label("选择模板").get_by_placeholder("请选择", exact=True), "请选择按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator("li").filter(has_text="0921"), f"{name}")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取保存为模板结果")
        self.asserts_result(result, "=", "引用模板成功")

    def template_download(self):
        """
        下载模板
        """
        self.interface_requests('/api/Project/DevPara/ParaTemplate')
        self.wait_for_timeouts(3000)
        self.click(self.page.get_by_role("button", name="模板下载"), "点表配置-模板下载按钮")
