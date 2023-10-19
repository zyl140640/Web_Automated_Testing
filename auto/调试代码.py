import re

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://36.134.46.91:7070/login")
    page.pause()
    page.locator(
        ".el-table__fixed-right > .el-table__fixed-body-wrapper > .el-table__body > tbody > tr > .el-table_1_column_3 > .cell > .basicTableBtnBox > .el-dropdown > .el-dropdown-link").first.click()
    page.get_by_role("button", name="").click()
    page.get_by_text("上传资料").click()
    page.locator("div").filter(has_text=re.compile(r"^点击上传$")).first.set_input_files("email.html")
    page.locator("div").filter(has_text="资料上传成功").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
