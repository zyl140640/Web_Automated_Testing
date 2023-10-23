from common.BasePages import BasePage


class GatewayPage(BasePage):

    def add_gateway(self, project, gateway, gateway_id):
        """
       新增网关
        Args:
            project:
            gateway:
            gateway_id:
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="新增"), "新增网关按钮")
        self.click(self.page.get_by_role("textbox", name="请选择项目名称"), "项目名称")
        self.input_data(self.page.get_by_label("选择项目").get_by_placeholder("请选择项目名称"), f"{project}",
                        "输入项目名称")
        self.click(self.page.get_by_label("选择项目").get_by_role("button", name=" 查询"), "查询按钮")
        self.page.wait_for_timeout(3000)
        self.click(self.page.get_by_role("radio"), "勾选项目")
        self.click(self.page.get_by_label("选择项目").get_by_role("button", name="确 定"), "确定选择")
        self.input_data(self.page.get_by_placeholder("请输入网关别名"), f"{gateway}", "网关别名输入框")
        self.wait_for_timeouts(1000)
        self.input_data(self.page.get_by_role("textbox", name="请输入网关SN"), f"{gateway_id}", "网关SN输入框")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_placeholder("请选择网关类型"), "请选择网关类型")
        self.input_data(self.page.get_by_placeholder("请输入负责人"), "小张", "负责任输入框")
        self.input_data(self.page.get_by_placeholder("请输入地址"), "山东省青岛市李沧区九水东路东李新苑", "地址输入框")
        self.click(self.page.get_by_placeholder("请选择状态"), "请选择状态")
        self.click(self.page.get_by_role("button", name="确 定"), "保存按钮")
        self.cut_out("结果图")

    def update_gateway(self, project):
        """
        根据项目名称修改项目信息
        Args:
            project: 项目名称
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("link", name="网关管理"), "网关管理")
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称查询框")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), f"{project}", "项目名称查询框")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
        self.click(self.page.locator(
            '//*[@id="app"]/div/div[2]/section/div[1]/div[2]/div[5]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[15]/div/div/i[2]').first,
                   "编辑按钮")
        self.page.get_by_placeholder("请输入网关别名").fill("修改测试网关")
        self.page.get_by_label("网关编辑窗口").get_by_role("spinbutton").fill("6")
        self.page.get_by_role("button", name="确 定").click()
        self.cut_out("修改网关结果")

    def delete_gateway(self):
        """
        删除网关信息
        """
        self.wait_for_timeouts(5000)
        self.click(self.page.get_by_role("row", name="1", exact=True).locator("label span").nth(1), "勾选网关")
        self.click(self.page.get_by_role("button", name="删除"), "删除按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认删除按钮")
        self.cut_out("删除网关结果")

    def parm_read(self):
        """
        网关管理-参数读取
        Args:
        """
        self.click(self.page.get_by_role("button", name="确定"), "确定读取")
        self.wait_for_timeouts(2000)
        bs = self.get_text(self.page.get_by_role("alert").first, "读取操作成功弹窗")
        assert bs == "操作成功", "与预期结果不符"
        self.click(self.page.get_by_role("button", name="同步到平台"), "同步到平台")
        self.click(self.page.get_by_role("button", name="确定"), "确定同步到平台")
        self.wait_for_timeouts(2000)
        cs = self.get_text(self.page.get_by_role("alert").last, "读取同步成功弹窗")
        assert cs == "同步成功", "与预期结果不符"

    def issue_device_id(self):
        """
        点表下发
        """
        self.click(self.page.get_by_role("button", name="确认"), "确认下发按钮")
        result = self.get_text(self.page.get_by_role("alert"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def message_send(self):
        """
        基础信息下发
        """
        self.click(self.page.get_by_role("button", name="确认"), "确认下发按钮")
        result = self.get_text(self.page.get_by_role("alert"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def network_send(self):
        """
        网络信息下发
        """
        self.click(self.page.get_by_role("button", name="确认"), "确认下发按钮")
        result = self.get_text(self.page.get_by_role("alert"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def lock_in_time(self):
        """
        同步时钟
        """

        self.click(self.page.get_by_role("button", name="确认"), "确认同步按钮")
        result = self.get_text(self.page.get_by_role("alert"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def debug_switch(self):
        """
        远程调试开关
        """
        self.click(self.page.get_by_role("button", name="提 交"), "提交按钮")
        result = self.get_text(self.page.get_by_role("alert"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def get_clock_gate(self, year):
        bs = self.get_text(self.page.locator(
            "#app > div > div.main-container.hasTagsView > section > div.tab-container > div:nth-child(6) > div > div.el-dialog__body"),
            "读取网关时钟弹窗结果")
        assert bs.find(f"{year}") != -1, "未获取到网关时间"

    def gateway_share(self, project):
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_label("分享").get_by_placeholder("请输入项目名称"), "项目名称输入框")
        self.input_data(self.page.get_by_label("分享").get_by_placeholder("请输入项目名称"), f"{project}", "项目名称")
        self.click(self.page.get_by_label("分享").get_by_role("button", name=" 查询"), "查询按钮")
        self.click(
            self.page.get_by_role("row", name="d161b660-14ea-4efe-9eca-51702aa2bc31 设备3").locator("span").nth(1),
            "勾选项目")
        self.click(self.page.get_by_role("row", name="项目Id 项目名称").locator("span").nth(1), "勾选项目")
        self.click(self.page.get_by_role("button", name="提 交"), "提交按钮")
        result = self.get_text(self.page.get_by_role("alert"), "获取弹框结果")
        self.asserts_result(result, "=", "操作成功")
