from common.BasePages import BasePage


class ScreenMonitoring(BasePage):

    def add_screen_monitoring(self, name):
        with self.page.expect_popup() as page1_info:
            self.click(self.page.get_by_role("button", name="新增"), "新增大屏监控")
        page1 = page1_info.value
        self.click(page1.get_by_placeholder("请输入 大屏名称"), "大屏监控名称")
        self.input_data(page1.get_by_placeholder("请输入 大屏名称"), f"{name}", "大屏监控名称")
        self.click(page1.get_by_role("button", name=" 创建大屏"), "创建大屏")
        self.click(page1.get_by_role("menuitem", name=" ").locator("div").first.first, "新增翻牌器")
        self.click(page1.get_by_role("menuitem", name="翻牌器").get_by_role("img"), "选择翻牌器")
        self.click(page1.locator("div:nth-child(3) > div > .el-tooltip").first, "点击保存")
        self.asserts_result(page1.get_by_role("alert").inner_text(), "=", "大屏配置保存成功")

    def get_screen_monitoring(self, name):
        self.click(self.page.get_by_placeholder("请输入", exact=True), "选择大屏名称查询条件")
        self.input_data(self.page.get_by_placeholder("请输入", exact=True), f"{name}", f"输入大屏名称:{name}")
        self.click(self.page.get_by_role("button", name=" 查询"), "查询按钮")

    def delete_screen_monitoring(self):
        self.list_row(1)
        self.wait_for_timeouts(2000)
        self.click(self.page.get_by_role("button", name="删除"), "删除大屏监控")
        self.click(self.page.get_by_role("button", name="确认"), "确认删除大屏监控")

    def case_zutai(self):
        for m in range(1, 92):
            self.click(self.page.locator("#app").get_by_text(f"{m}", exact=True), f"点击第[{m}]页")
            self.wait_for_timeouts(3000)
            for i in range(1, 20):
                self.logger.info(f"当前页数: [{m}],当前点击组态行数: [{i}]")
                update = self.page.locator(
                    ".el-table__fixed-body-wrapper > .el-table__body > tbody > tr:nth-child({}) > .el-table_1_column_1 > .cell > .basicTableBtnBox > .el-icon-edit-outline".format(
                        i))
                if update.count() != 0:
                    with self.page.expect_popup() as page_info:
                        # 记录日志
                        update = self.page.locator(
                            ".el-table__fixed-body-wrapper > .el-table__body > tbody > tr:nth-child({}) > .el-table_1_column_1 > .cell > .basicTableBtnBox > .el-icon-edit-outline".format(
                                i))
                        self.logger.info(f"当前组态[{i}]有编辑按钮，开始进行编辑保存操作")
                        update.click()
                        to_page = page_info.value
                        to_page.wait_for_timeout(3000)
                        to_page.get_by_role("button", name=" 发布").click()
                        to_page.close()
                        self.logger.info(f"发布成功,关闭页面")
                else:
                    self.logger.info(f"当前组态序列 {i}没有编辑按钮，进行跳过处理")
