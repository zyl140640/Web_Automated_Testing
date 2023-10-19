from playwright.sync_api import Playwright, sync_playwright

from common.BasePages import BasePage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    bs_init = BasePage(page)
    page.goto("http://192.168.110.210:9016/login")
    bs_init.page.get_by_placeholder("请输入用户名").wait_for()
    bs_init.input_data(page.get_by_placeholder("请输入用户名"), "zhangyuanlong",
                       "输入账号信息")
    bs_init.input_data(page.get_by_placeholder("请输入登录密码"), "123456",
                       "输入密码信息")
    drop_button = page.get_by_role("article").locator("form div").filter(
        has_text="请按住滑块拖动 登 录").locator(
        "div").nth(
        4)
    box = drop_button.bounding_box()
    page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
    page.mouse.down()
    mov_x = box['x'] + box['width'] / 2 + 260
    page.mouse.move(mov_x, box['y'] + box['height'] / 2)
    page.mouse.up()
    page.get_by_role("button", name="登 录").click()
    bs_init.click(page.get_by_role("button", name="登 录"), "登录按钮")
    bs_init.wait_for_timeouts(8000)
    bs_init.click(page.get_by_label("Close", exact=True), "关闭首页弹窗")
    page.pause()
    bs_init.click(page.get_by_role("button", name=" 展开"), "展开查询条件")
    bs_init.click(page.get_by_placeholder("请输入网关别名"), "网关别名查询框")
    bs_init.input_data(page.get_by_placeholder("请输入网关别名"), "714005F36924F9C7", "输入网关sn")
    bs_init.click(page.get_by_role("button", name=" 收起"), "收起查询框")
    bs_init.click(page.get_by_role("button", name=" 查询"), "查询网关sn")
    bs_init.click(page.locator(
        ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first,
                  "点击网关...")
    bs_init.wait_for_timeouts(1000)
    bs_init.click(page.locator("li:has-text('获取网关时间')").last, "网关点表读取提醒")
    bs_init.click(page.get_by_role("button", name="确认"), "确认下发按钮")
    bs_init.get_text(page.get_by_text("操作成功"), "读取下发弹窗结果")
    print("你好")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
