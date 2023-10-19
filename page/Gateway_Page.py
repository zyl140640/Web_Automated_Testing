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

    def get_project_gateway(self, project):
        """
         根据项目查询网关信息
        Args:
            project: 项目名称
        """
        self.click(self.page.get_by_role("textbox", name="请输入项目名称"), "项目名称查询弹框")
        self.input_data(self.page.get_by_role("textbox", name="请输入项目名称"), project, "输入项目名称")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")
        self.get_text(self.page.locator(
            "#pane-first > div.containerYK > div.basicTableBox > div.pagination-container > div > span.el-pagination__total"),
            "查询w网关数量")

    def get_sn_gateway(self, sn):
        """
        根据网关sn查询
        Args:
            sn:714005F36924F9C7
        """
        self.click(self.page.get_by_role("button", name=" 展开"), "展开查询条件")
        self.click(self.page.get_by_role("textbox", name="请输入网关SN"), "网关SN查询框")
        self.input_data(self.page.get_by_role("textbox", name="请输入网关SN"), f"{sn}", "输入网关sn")
        self.click(self.page.get_by_role("button", name=" 收起"), "收起查询框")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询网关sn")

    def parm_read(self):
        """
        网关管理-参数读取
        Args:
            sn: 网关的sn
        """

        self.click(self.page.locator(
            ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first,
                   "点击网关...")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator("li:has-text('参数读取')").last, "网关点表读取提醒")
        self.click(self.page.get_by_role("button", name="确定"), "确定读取")
        self.wait_for_timeouts(2000)
        bs = self.get_text(self.page.get_by_text("操作成功"), "读取操作成功弹窗")
        assert bs == "操作成功", "与预期结果不符"
        self.click(self.page.get_by_role("button", name="同步到平台"), "同步到平台")
        self.click(self.page.get_by_role("button", name="确定"), "确定同步到平台")
        self.wait_for_timeouts(2000)
        cs = self.get_text(self.page.get_by_text("同步成功"), "读取同步成功弹窗")
        assert cs == "同步成功", "与预期结果不符"

    def issue_device_id(self):
        self.click(self.page.locator(
            ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first,
                   "点击网关...")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator("li:has-text('点表下发')").last, "网关点表读取提醒")
        self.click(self.page.get_by_role("button", name="确认"), "确认下发按钮")
        result = self.get_text(self.page.get_by_text("操作成功"), "读取下发弹窗结果")
        assert result == "操作成功", "下发点表与预期结果不符合"

    def get_clock_gate(self, year):
        self.click(self.page.locator(
            ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first,
                   "点击网关...")
        self.wait_for_timeouts(1000)
        self.click(self.page.locator("li:has-text('获取网关时间')").last, "获取网关时间")
        bs = self.get_text(self.page.locator(
            "#app > div > div.main-container.hasTagsView > section > div.tab-container > div:nth-child(6) > div > div.el-dialog__body"),
            "读取网关时钟弹窗结果")
        assert bs.find(f"{year}") != -1, "未获取到网关时间"
