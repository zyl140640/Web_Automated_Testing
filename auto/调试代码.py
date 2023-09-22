from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://36.134.46.91:7070/")
    page.goto("http://36.134.46.91:7070/login")
    page.pause()
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("zhangyuanlong")
    page.get_by_placeholder("请输入登录密码").click()
    page.get_by_placeholder("请输入登录密码").fill("123456")
    page.get_by_role("button", name="登 录").click()
    page.locator("form").filter(
        has_text="用户平台登录USER PLATFORM LOGIN 请按住滑块拖动 登 录自动登录重置密码二维码已失效 点击刷新请使用微信扫码登录仅支持已绑定微信的账户进行快速").click(
        button="right")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
