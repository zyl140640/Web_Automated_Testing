import allure

from common.BasePages import BasePage


class GatewayPage(BasePage):

    def add_gateway(self, project, gateway, gateway_id):
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
        self.wait_for_timeouts(5000)
        self.page.get_by_role("row", name="1", exact=True).locator("label span").nth(1).click()
        self.page.get_by_role("button", name="删除").click()
        allure.attach(self.page.screenshot(), "用例执行结果图", allure.attachment_type.PNG)
        self.page.get_by_role("button", name="确认").click()
