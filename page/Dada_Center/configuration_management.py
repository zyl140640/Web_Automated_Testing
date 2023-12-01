from common.BasePages import BasePage


class ConfigurationManagement(BasePage):

    def add_configuration(self, name, project_name):
        """
        可视化中心-组态管理-新增组态
        Args:
            project_name: 项目名称
            name: 组态名称
        """
        self.click(self.page.get_by_role("button", name="新增"), "新增组态")
        self.click(self.page.get_by_placeholder("请选择项目名称"), "选择项目")
        self.click(self.page.locator("li").filter(has_text=f"{project_name}"), f"选择{project_name}")
        self.input_data(self.page.get_by_placeholder("请输入流程图名称"), f"{name}", "流程图名称")
        self.click(self.page.get_by_role("button", name="确 定"), "确定保存组态")
        self.asserts_result(self.page.get_by_role("alert").inner_text(), "=", "添加流程图成功")

    def get_configuration(self, project_name):
        """
        根据项目名称-查询组态
        Args:
            project_name: 项目名称
        """
        self.click(self.page.get_by_placeholder("请输入项目名称"), "组态-项目名称查询框")
        self.input_data(self.page.get_by_placeholder("请输入项目名称"), f"{project_name}",
                        f"输入项目名称：{project_name}")
        self.click(self.page.get_by_role("button", name=" 查询"), "组态-查询按钮")

    def delete_configuration(self):
        """
        组态管理-删除组态
        """
        self.wait_for_timeouts(1000)
        self.click(
            self.page.locator("tr:nth-child(1) > .el-table_1_column_1 > .cell > .basicTableBtnBox > .el-icon-delete"),
            "删除-组态按钮")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确定"), "确定-删除组态")
