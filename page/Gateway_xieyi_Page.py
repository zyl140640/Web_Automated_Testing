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
        self.get_text(self.page.get_by_role("alert"), "网口协议添加成功提示")

    def add_chuangkou(self):
        """
         新增协议配置-串口
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name=" 串口协议添加"), "添加串口")
        self.click(self.page.locator("div").filter(has_text=re.compile(
            r"^协议类别标准西门子三菱台达协议协议Modbus RTU网关I/ORFID协议协议别名$")).get_by_placeholder("请选择").nth(
            1), "选择协议")
        self.click(self.page.locator("li").filter(has_text="Modbus RTU"), "选择RTU协议")
        self.click(self.page.get_by_label("串口协议添加").locator("form div").filter(
            has_text="COM口com0(485)com1(232)波特率1200180024004800720096001440019200384005760011520012800").get_by_placeholder(
            "请选择").first, "COM口")
        self.click(self.page.locator("li").filter(has_text="com0(485)"), "选择COM口")
        self.click(self.page.get_by_role("button", name="确 定"), "确定按钮")

    def update_chuankou(self):
        """
               修改串口
              """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="编辑").first, "点击编辑")
        self.click(self.page.get_by_label("串口协议编辑").get_by_placeholder("请输入超时时间"), "编辑")
        self.input_data(self.page.get_by_label("串口协议编辑").get_by_placeholder("请输入超时时间"), "1110",
                        "输入超时时间")
        self.click(self.page.get_by_role("button", name="确 定"), "保存协议")
        self.get_text(self.page.get_by_role("alert"), "网口协议修改成功提示")

    def delete_xieyi(self):
        """
        删除俩协议
        """
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="删除").nth(1), "删除串口按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认按钮删除")
        self.wait_for_timeouts(1000)
        self.click(self.page.get_by_role("button", name="删除").nth(1), "删除网关按钮")
        self.click(self.page.get_by_role("button", name="确认"), "确认网关删除")

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
        self.get_text(self.page.get_by_role("alert"), "网口协议添加成功提示")
