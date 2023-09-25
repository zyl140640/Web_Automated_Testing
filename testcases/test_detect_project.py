# import allure
#
#
# @allure.feature("御控工业云平台")
# class TestDetectProject:
#
#     def test_detect_project(self, init, page):
#         page.get_by_role("textbox", name="请输入项目名称").click()
#         page.get_by_role("textbox", name="请输入项目名称").fill("测试dome")
#         page.get_by_role("button", name=" 查询").click()
#         page.get_by_role("cell", name="   ").locator("i").nth(2).click()
#         page.get_by_role("button", name="确认").click()
