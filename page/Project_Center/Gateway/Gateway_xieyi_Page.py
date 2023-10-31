import re

from common.BasePages import BasePage


class GatewayXieYiPage(BasePage):

    def add_xieyi(self, ip):
        """
       新增协议配置-网关
        Args:
            ip: ip地址
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name=" 网口协议添加"), "网口协议添加按钮")
        self.click(self.page.get_by_placeholder("请选择").nth(1), "")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP").locator("span"), "")
        self.click(self.page.get_by_placeholder("请输入设备IP"), "")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), f"{ip}", "")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.asserts_result(self.get_alert("网关管理-协议配置-新增网口"), "=", "协议添加成功")

    def add_chuangkou(self):
        """
         新增协议配置-串口
        """
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name=" 串口协议添加"), "添加串口")
        self.click(self.page.locator("div").filter(has_text=re.compile(
            r"^协议类别标准西门子三菱台达协议协议Modbus RTU网关I/ORFID协议协议别名$")).get_by_placeholder("请选择").nth(
            1), "选择协议")
        self.click(self.page.locator("li").filter(has_text="Modbus RTU"), "选择RTU协议")
        self.click(self.page.locator(
            "#app > div > div.main-container.hasTagsView > section > div.tab-container > div > div:nth-child(4) > div > div.el-dialog__body > div.containerYK > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > input"),
            "COM口")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")
        self.asserts_result(self.get_alert("网关管理-协议配置-新增串口"), "=", "协议添加成功")

    def update_chuankou(self):
        """
               修改串口
              """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="编辑").first, "点击编辑")
        self.click(self.page.get_by_role("button", name="确 定"), "保存协议")
        self.asserts_result(self.get_alert("网关管理-协议配置-修改串口"), "=", "协议添加成功")

    def update_wangkou(self):
        """
               修改网口
              """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="编辑").first, "点击编辑")
        self.click(self.page.get_by_role("button", name="确 定"), "保存协议")
        self.asserts_result(self.get_alert("网关管理-协议配置-修改网口"), "=", "协议添加成功")

    def delete_xieyi(self):
        """
        删除俩协议
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="删除").nth(1), "删除按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认按钮删除")

    def wangkou_lianjie(self, ip):
        """
        网口连接测试
        Args:
            ip: ip地址
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name=" 网口协议添加"), "网口协议添加按钮")
        self.click(self.page.get_by_placeholder("请选择").nth(1), "")
        self.click(self.page.locator("li").filter(has_text="Modbus TCP").locator("span"), "")
        self.click(self.page.get_by_placeholder("请输入设备IP"), "")
        self.input_data(self.page.get_by_placeholder("请输入设备IP"), f"{ip}", "")
        self.click(self.page.get_by_role("button", name="网口连接测试"), "网口连接测试")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="确认"), "确认下发测试")
        self.asserts_result(self.get_alert("网关管理-协议配置-网口连接测试"), "=", "网口连接测试成功")
