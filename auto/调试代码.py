from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://36.134.46.91:7070/login")
    page.pause()
    page.get_by_label("Close", exact=True).click()
    page.get_by_text("项目中心").click()
    page.get_by_role("link", name="网关管理").click()
    page.goto("http://36.134.46.91:7070/projectManagement/pointGatewayList")
    page.locator("#dropdown-menu-7278").get_by_text("点表配置").click()
    page.get_by_role("button", name="新增", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
