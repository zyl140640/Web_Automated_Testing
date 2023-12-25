import re

from playwright.sync_api import Playwright, sync_playwright

from common.BasePages import BasePage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    bs_init = BasePage(page)
    bs_init.go_url("http://192.168.110.210:9016/login")
    bs_init.input_data(page.get_by_placeholder("请输入用户名"), "zhangyuanlong", "输入账号信息")
    bs_init.input_data(page.get_by_placeholder("请输入登录密码"), "123456", "输入密码信息")
    drop_button = page.get_by_role("article").locator("form div").filter(
        has_text="请按住滑块拖动 登 录").locator("div").nth(4)
    box = drop_button.bounding_box()
    page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
    page.mouse.down()
    mov_x = box['x'] + box['width'] / 2 + 260
    page.mouse.move(mov_x, box['y'] + box['height'] / 2)
    page.mouse.up()
    bs_init.click(page.get_by_role("button", name="登 录"), "登录按钮")
    page.pause()
    value = page.locator("#pane-first > div.containerYK > div.basicTableBox > div.pagination-container > div > span.el-pagination__total").inner_text()
    print(value)
    # if count == 0:
    #     page.get_by_text("快速接入平台指引说明").wait_for()
    #     bs_init.logger.info("当前页面加载完毕,获取到项目式引导框，点击并关闭")
    # else:
    #     bs_init.logger.info("----检测到弹窗资源----")
    #     bs_init.logger.info(f"----获取弹窗结果: {alert}----")
    #     assert alert == "弹窗内容未找到", f"登录失败,失败信息为: {alert}"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

#
# if __name__ == '__main__':
#     dict = {"packageName": "com.woodleaves.read", "appName": "常读免费小说", "versionName": "5.9.9.32",
#             "description": "隐藏图标，启动广告，去广告，去直播 去阅读广告",
#             "configs": "[{\"className\":\"com.dragon.read.user.b\",\"methodName\":\"d\",\"resultValues\":\"true\"},{\"className\":\"com.dragon.read.component.biz.impl.h.e\",\"methodName\":\"isVip\",\"resultValues\":\"true\"},{\"className\":\"com.dragon.read.polaris.d\",\"methodName\":\"e\",\"resultValues\":\"false\"},{\"className\":\"com.dragon.read.component.audio.impl.ui.c.a\",\"methodName\":\"a\",\"params\":\"android.content.Context,java.lang.String,java.lang.String\",\"resultValues\":\"null\"},{\"className\":\"com.dragon.read.base.ad.a\",\"methodName\":\"a\",\"params\":\"java.lang.String,java.lang.String\",\"resultValues\":\"false\"},{\"className\":\"com.ss.android.update.ad\",\"methodName\":\"k\",\"resultValues\":\"false\"},{\"className\":\"com.dragon.read.social.e.a.d\",\"methodName\":\"*\",\"resultValues\":\"*\"},{\"className\":\"com.dragon.read.widget.m\",\"methodName\":\"a\",\"resultValues\":\"*\"},{\"className\":\"com.dragon.read.reader.ad.readflow\",\"methodName\":\"*\",\"resultValues\":\"*\"},{\"className\":\"com.dragon.read.polaris.userimport.f\",\"methodName\":\"b\",\"resultValues\":\"true\"}]",
#             "id": 6}
#     print(dict.get("packageName"))
#     print(dict.get("appName"))
#     print(dict.get("versionName"))
#     print(dict.get("description"))
#     print(dict.get("configs"))
