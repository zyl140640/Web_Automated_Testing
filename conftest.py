import os
from typing import Any, Dict, Generator, List

import allure
import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Error,
    Page,
)
from slugify import slugify

from common.BasePages import BasePage


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1800,
            "height": 1024,
        },
    }


def _build_artifact_test_folder(
        pytestconfig: Any, request: pytest.FixtureRequest, folder_or_file_name: str
) -> str:
    output_dir = pytestconfig.getoption("--output")
    return os.path.join(output_dir, slugify(request.node.nodeid), folder_or_file_name)


@pytest.fixture(scope="function")
def context(
        browser: Browser,
        browser_context_args: Dict,
        pytestconfig: Any,
        request: pytest.FixtureRequest,
) -> Generator[BrowserContext, None, None]:
    pages: List[Page] = []
    context = browser.new_context(**browser_context_args, storage_state="./auto/cookies.json")
    # 设置全局超时40秒
    context.set_default_navigation_timeout(40000)
    # context = browser.new_context(**browser_context_args)

    context.on("page", lambda page: pages.append(page))
    # 开启跟踪器
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    tracing_option = pytestconfig.getoption("--tracing")
    capture_trace = tracing_option in ["on", "retain-on-failure"]
    if capture_trace:
        context.tracing.start(
            name=slugify(request.node.nodeid),
            screenshots=True,
            snapshots=True,
            sources=True,
        )

    yield context
    # If requst.node is missing rep_call, then some error happened during execution
    # that prevented teardown, but should still be counted as a failure
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else True
    if capture_trace:
        retain_trace = tracing_option == "on" or (
                failed and tracing_option == "retain-on-failure"
        )
        if retain_trace:
            # tracing_path = os.path.join(pytestconfig, request.node.name, "trace.zip")
            trace_path = _build_artifact_test_folder(pytestconfig, request, "trace.zip")
            context.tracing.stop(path=trace_path)
            allure.attach.file(trace_path, "trace.playwright.dev", extension="zip")
        else:
            context.tracing.stop(path="trace.zip")

    screenshot_option = pytestconfig.getoption("--screenshot")
    capture_screenshot = screenshot_option == "on" or (
            failed and screenshot_option == "only-on-failure"
    )
    if capture_screenshot:
        for index, page in enumerate(pages):
            human_readable_status = "failed" if failed else "finished"
            screenshot_path = _build_artifact_test_folder(
                pytestconfig, request, f"test-{human_readable_status}-{index + 1}.png"
            )
            try:
                page.screenshot(timeout=5000, path=screenshot_path)
                allure.attach.file(screenshot_path, "最终截图", allure.attachment_type.PNG)
            except Error:
                pass

    context.close()

    video_option = pytestconfig.getoption("--video")
    preserve_video = video_option == "on" or (
            failed and video_option == "retain-on-failure"
    )
    if preserve_video:
        for page in pages:
            video = page.video
            if not video:
                continue
            try:
                video_path = video.path()
                file_name = os.path.basename(video_path)
                video.save_as(
                    path=_build_artifact_test_folder(pytestconfig, request, file_name)
                )
                # 将视频文件放入allure报告
                allure.attach.file(page.video.path(), "用例录制文件", attachment_type=allure.attachment_type.WEBM)

            except Error:
                # Silent catch empty videos.
                pass


@pytest.fixture(scope="function", autouse=True)
def init(page):
    bs_init = BasePage(page)
    bs_init.go_url(bs_init.read_yaml("auto/config.yaml", "$..case_login.url"))
    bs_init.wait_for_timeouts(3000)
    title = str(bs_init.page.context.pages)
    if title.find("login") != -1:
        bs_init.logger.info("cookies无效,进入登录步骤")
        bs_init.input_data(page.get_by_placeholder("请输入用户名"),
                           bs_init.read_yaml("auto/config.yaml", "$..case_login.username"),
                           "输入账号信息")
        bs_init.input_data(page.get_by_placeholder("请输入登录密码"),
                           bs_init.read_yaml("auto/config.yaml", "$..case_login.password"),
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
        bs_init.click(page.get_by_role("button", name="登 录"), "登录按钮")
        bs_init.wait_for_timeouts(3000)
        page.context.storage_state(path="auto/cookies.json")
        bs_init.click(page.get_by_label("Close", exact=True), "关闭首页弹窗")
    else:
        bs_init.logger.info("cookies有效,跳过登录步骤")
        bs_init.wait_for_timeouts(1000)
