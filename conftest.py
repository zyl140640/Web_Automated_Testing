import os
import time
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


@pytest.fixture(scope="class")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page


def _build_artifact_test_folder(
        pytestconfig: Any, request: pytest.FixtureRequest, folder_or_file_name: str
) -> str:
    output_dir = pytestconfig.getoption("--output")
    return os.path.join(output_dir, slugify(request.node.nodeid), folder_or_file_name)


@pytest.fixture(scope="class")
def context(
        browser: Browser,
        browser_context_args: Dict,
        pytestconfig: Any,
        request: pytest.FixtureRequest,
) -> Generator[BrowserContext, None, None]:
    pages: List[Page] = []
    context = browser.new_context(**browser_context_args, storage_state="./auto/cookies.json")
    context.on("page", lambda page: pages.append(page))
    # 开启跟踪器
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
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
            context.tracing.stop(path="trace.zip")
        else:
            context.tracing.stop()

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


@pytest.fixture(scope="class")
def init(page):
    page.goto("http://36.134.46.91:7070/dashboard")
    time.sleep(8)
    # page.pause()
    title = str(page.context.pages)
    if title.find("login") != -1:
        page.get_by_placeholder("请输入用户名").wait_for()
        page.get_by_placeholder("请输入用户名").fill("zhangyuanlong")
        page.get_by_placeholder("请输入登录密码").fill("123456")
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
        page.context.storage_state(path="auto/cookies.json")
        page.wait_for_timeout(9000)
        page.get_by_label("Close", exact=True).click()
    else:
        page.wait_for_timeout(9000)
        page.get_by_label("Close", exact=True).click()
