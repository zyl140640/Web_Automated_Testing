import re
from common.BasePages import BasePage


class ProjectPage(BasePage):

    def add_project(self, project, project_id, gateway_name, gateway_sn):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="新增"), "新增项目按钮")
        self.click(self.page.get_by_label("新增项目").get_by_placeholder("请选择", exact=True), "所属租户")
        self.wait_for_timeouts(2000)
        self.click(self.page.locator("li").filter(has_text="1115qi").nth(1), "选择所属租户")

        self.input_data(self.page.get_by_label("新增项目").get_by_placeholder("请输入项目名称"), f"{project}",
                        "输入项目名称")
        self.input_data(self.page.get_by_placeholder("请输入项目编码"), f"{project_id}",
                        "输入项目编码")
        self.click(self.page.get_by_placeholder("请点击地图选择位置"), "打开地图")
        self.wait_for_timeouts(3000)
        self.click(self.page.locator(".BMap_mask"), "地图位置")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator(".BMap_mask"), "地图位置")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.input_data(self.page.get_by_placeholder("请输入负责人"), "张三", "负责人输入框")
        self.input_data(self.page.get_by_placeholder("请输入电话"), "15533065391", "电话输入框")
        self.click(self.page.get_by_role("button", name="下一步"), "下一步按钮")
        self.input_data(self.page.get_by_placeholder("请输入网关别名"), f"{gateway_name}", "网关别名输入框")
        self.input_data(self.page.get_by_placeholder("请输入网关SN"), f"{gateway_sn}", "网关SN输入框")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请选择网关类型"), "请选择网关类型")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_text("YC-5300N"), "选择YC-5300N")
        self.click(self.page.get_by_text("添加网口"), "添加网口按钮")
        self.click(self.page.get_by_role("textbox", name="请选择", exact=True).nth(2), "请选择")
        self.click(self.page.get_by_text("Modbus TCP"), "协议")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), "192.168.30.152", "设备IP输入框")
        self.click(self.page.get_by_role("button", name="下一步"), "下一步按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="下一步"), "下一步按钮")
        self.wait_for_timeouts(1000)
        # self.click(self.page.locator("label").filter(has_text="0905自定义模板").locator("span").nth(1), "选择模板")
        self.click(self.page.get_by_role("button", name="保 存"), "保存按钮")
        self.asserts_result(self.get_text(self.page.get_by_text("项目创建成功"), "项目管理-新增"), "=",
                            "项目创建成功")
        self.click(self.page.get_by_role("button", name="关闭"), "关闭按钮")

    def update_project(self, project):
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), f"{project}", "输入项目名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
        self.click(self.page.get_by_role("cell", name="   ").locator("i").nth(1), "编辑按钮")
        self.input_data(self.page.get_by_placeholder("请输入负责人"), "李四", "负责人输入框")
        self.input_data(self.page.get_by_placeholder("请输入电话"), "15533065392", "电话输入框")
        self.click(self.page.get_by_role("button", name="结束并保存"), "结束并保存按钮")
        self.click(self.page.get_by_role("button", name="确定"), "确定按钮")
        self.asserts_result(self.get_text(self.page.get_by_text("项目编辑成功"), "项目管理-编辑"), "=",
                            "项目编辑成功")

    def detect_project(self, project):
        self.wait_for_timeouts(5000)
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), f"{project}", "输入项目名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
        self.click(self.page.get_by_role("cell", name="   ").locator("i").nth(2), "删除按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认按钮")
        self.asserts_result(self.get_alert("项目管理-删除项目"), "=",
                            "删除项目成功")

    def copy_project(self, project, gate):
        self.wait_for_timeouts(3000)
        self.click(self.page.get_by_placeholder("请输入项目名称，40字内"), "项目名称")
        self.input_data(self.page.get_by_placeholder("请输入项目名称，40字内"), f"{project}", "输入项目名称")
        self.click(self.page.get_by_role("button", name="下一步"), "基础信息下一步")
        self.click(self.page.get_by_role("cell", name="0/16").get_by_role("textbox"), "网关sn")
        self.input_data(self.page.get_by_role("cell", name="0/16").get_by_role("textbox"), f"{gate}", "输入网关sn")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="下一步"), "映射网关下一步")
        # self.click(self.page.get_by_label("项目复制").get_by_role("textbox"), "输入设备名称")
        self.click(self.page.get_by_role("button", name="下一步"), "映射设备下一步")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="下一步"), "点表复查下一步")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="提交"), "提交")
        self.asserts_result(self.get_alert("项目管理-复制"), "=", "复制成功")

    def update_date(self):
        """
        项目管理-上传材料
        """
        self.click(self.page.locator("div").filter(has_text=re.compile(r"^点击上传$")).nth(1), "上传资料li")

        # page.locator(".el-upload-dragger").click()
        # page.locator(".el-upload").set_input_files("微信截图_20231011104056.png")
        # page.locator("div").filter(has_text="资料上传成功").click()

    def update_relevant_date(self):
        """
        相关材料
        """
        self.wait_for_timeouts(2000)
        # page.locator(".el-upload-dragger").click()
        # page.locator(".el-upload").set_input_files("微信截图_20231011104056.png")
        # page.locator("div").filter(has_text="资料上传成功").click()
