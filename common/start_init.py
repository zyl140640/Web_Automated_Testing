from playwright.sync_api import sync_playwright


# 驱动封装
class WebStart:
    context = None
    playwright = None
    browser = None

    @classmethod
    def start_chromium(cls):
        # 创建浏览器对象
        cls.playwright = sync_playwright().start()
        # 选择启动浏览器,开启GUI模式，浏览器窗口变大
        cls.browser = cls.playwright.chromium.launch(headless=False, args=['--start-maximized'])
        # 禁用浏览器窗口大小，直接让他最大化
        cls.context = cls.browser.new_context(no_viewport=True, record_video_dir="./case_video/")
        return cls.context.new_page()

    @classmethod
    def close(cls):
        # 退出浏览器
        cls.context.close()
        cls.browser.close()
