from playwright.sync_api import Playwright, sync_playwright, expect

from common.BasePages import BasePage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("http://36.134.46.91:7070/login")
    page.pause()
    bs = BasePage(page)
    bs.go_url("http://36.134.46.91:7070/login")
    ces = page.get_by_placeholder("请输入用户名")
    print(page.get_by_placeholder("请输入用户名"))
    print(type(page.get_by_placeholder("请输入用户名")))
    ces.click()









    bs.input_data(page.get_by_placeholder("请输入用户名"), "测试", "用户输入框内")
    bs.click(page.get_by_role("button", name="登 录"), "登录按钮")
    page.get_by_placeholder("请输入用户名").fill("zhangyuanlong")
    page.get_by_placeholder("请输入登录密码").click()
    page.get_by_placeholder("请输入登录密码").fill("123456")
    page.get_by_role("button", name="登 录").click()
    context.close()
    browser.close()


if __name__ == '__main__':
    # ---------------------

    with sync_playwright() as playwright:
        run(playwright)
