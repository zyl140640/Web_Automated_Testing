import re

from common.BasePages import BasePage


class DeviceIdPage(BasePage):

    def add_device_one(self):
        self.click(self.page.get_by_role("button", name="新增", exact=True), "新增点表按钮")
        self.click(self.page.get_by_role("dialog").locator("form").filter(
            has_text="所属租户xing0011009child1012qitest11009qi0921newa0921child0921qi09210010905qi荏原电产（青岛").get_by_placeholder(
            "请选择", exact=True), "选择租户")
        self.click(self.page.locator("li").filter(has_text="xing001").nth(1), "")
        self.click(self.page.get_by_role("dialog", name="新增点位").get_by_placeholder("请选择", exact=True).nth(2), "")
        self.click(self.page.locator("ul").filter(has_text="Modbus TCPOPC").locator("span").first, "")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), "189.123.22.11", "")
        self.click(self.page.get_by_role("button", name="下一步"), "")

    def add_device_id(self, name):
        self.click(self.page.get_by_role("button", name="添加点表"), "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox"),
                        f"{name}", "")
        self.input_data(self.page.locator(
            "div:nth-child(2) > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"),
            "1", "")
        self.click(self.page.get_by_role("button", name="确 定"), "")
        self.click(self.page.get_by_role("button", name="保存", exact=True), "")
        self.asserts_result(self.get_alert("点表管理-新增点表功能"), "=", "新增点位成功")

    def update_device_id(self):
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("cell", name="   ").locator("i").nth(1), "编辑按钮")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), "192.180.1.1", "输入ip地址")
        self.input_data(self.page.get_by_placeholder("请输入端口"), "501", "输入端口号")
        self.click(self.page.get_by_role("button", name="下一步"), "下一步按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="保存", exact=True), "保存按钮")
        self.asserts_result(self.get_alert("点表管理-修改点表功能"), "=", "保存成功")

    def get_device_id(self, name):
        self.click(self.page.get_by_role("textbox", name="请输入参数名称"), "参数名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入参数名称"), f"{name}", "输入点表参数名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def delete_device_id(self):
        self.list_row(1)
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="删除"), "删除按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        self.asserts_result(self.get_alert("点表管理-删除点表功能"), "=", "删除成功")

    def device_save_as_template(self, name, miaoshu):
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
        self.asserts_result(self.get_alert("点表管理-保存为模板"), "=", "点表保存为模板成功")

    def bind_gateway(self):
        self.list_row("1")
        self.click(self.page.get_by_role("button", name="绑定网关"), "绑定网关按钮")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.asserts_result(self.get_alert("点表管理-绑定网关"), "=", "绑定网关成功")

    def bind_device(self):
        self.wait_for_timeouts(1000)
        self.list_row("1")
        self.click(self.page.get_by_role("button", name="绑定设备"), "绑定设备按钮")
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        self.wait_for_timeouts(1000)
        self.asserts_result(self.get_alert("点表管理-绑定设备"), "=", "绑定设备成功")

    def add_device_dianwei(self, name):
        self.click(self.page.get_by_role("button", name="添加点表"), "")
        self.input_data(self.page.locator("div").filter(has_text=re.compile(r"^名称从站号$")).get_by_role("textbox"),
                        f"{name}", "")
        self.input_data(self.page.locator(
            "div:nth-child(2) > div:nth-child(2) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"),
            "1", "")
        self.click(self.page.get_by_role("button", name="确 定"), "")
        self.asserts_result(self.get_alert("点表管理-新增点表功能"), "=", "新增点位成功")

    def device_addition_pt(self, zhanhao, path, one):
        self.click(self.page.get_by_role("button", name="批量新增"), "批量新增")
        self.input_data(
            self.page.locator(".el-col > .el-form-item > .el-form-item__content > .el-input > .el-input__inner").first,
            f"{zhanhao}", "从站号")
        self.input_data(self.page.locator(
            "div:nth-child(5) > .el-form-item > .el-form-item__content > .el-input > .el-input__inner"), f"{path}",
            "点位地址")
        self.input_data(self.page.get_by_role("spinbutton").nth(1), f"{one}", "个数")
        self.click(self.page.get_by_role("button", name="确 定"), "确定")

    def device_pt_yinyong(self):
        self.click(self.page.get_by_role("button", name="引用模板"), "引用模板")
        self.click(self.page.get_by_role("dialog", name="选择模板").get_by_placeholder("请选择", exact=True), "请选择")
        self.click(self.page.locator("li").filter(has_text=re.compile(r"^0921$")), "选择")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")

    def device_xiazai_moban(self):
        self.click(self.page.get_by_role("button", name="下载模板"), "下载模板")
