# import time
#
# import allure
# import pytest
# from playwright.sync_api import sync_playwright
#
#
# @pytest.fixture(scope="class")
# def page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False, slow_mo=1300, args=['--start-maximized'])
#         context = browser.new_context(storage_state="./auto/cookies.json", no_viewport=True,
#                                       record_video_dir="./case_video/")
#         page = context.new_page()
#         page.goto("http://36.134.46.91:7070/dashboard")
#         time.sleep(8)
#         # page.pause()
#         title = str(context.pages)
#         if title.find("login") != -1:
#             page.get_by_placeholder("请输入用户名").wait_for()
#             page.get_by_placeholder("请输入用户名").fill("zhangyuanlong")
#             page.get_by_placeholder("请输入登录密码").fill("123456")
#             dropbutton = page.get_by_role("article").locator("form div").filter(
#                 has_text="请按住滑块拖动 登 录").locator(
#                 "div").nth(
#                 4)
#             box = dropbutton.bounding_box()
#             page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
#             page.mouse.down()
#             mov_x = box['x'] + box['width'] / 2 + 260
#             page.mouse.move(mov_x, box['y'] + box['height'] / 2)
#             page.mouse.up()
#             page.get_by_role("button", name="登 录").click()
#             page.context.storage_state(path="auto/cookies.json")
#             time.sleep(10)
#             page.get_by_label("Close", exact=True).click()
#         else:
#             time.sleep(10)
#             page.get_by_label("Close", exact=True).click()
#
#         yield page
#
#         context.close()
#         allure.attach.file(page.video.path(), "用例录制文件", attachment_type=allure.attachment_type.WEBM)
#         page.close()
#
#
