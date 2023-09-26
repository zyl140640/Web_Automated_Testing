import allure
# from playwright.async_api import Page
import logging

from playwright.sync_api import Page

"""
封装常用API
"""


class BasePage:
    def __init__(self, page: Page):
        self.locator = None
        self.page = page
        self.logger = logging

    def go_url(self, url):
        with allure.step(f"访问网站:{url}"):
            self.page.goto(url, wait_until='networkidle')
            self.logger.info(f"访问网站:{url}")

    def all_text(self, locator, text):
        return self.page.get_attribute(locator, text)  # 获取元素文本

    def click(self, locator, text):
        """
         封装点击方法
        :param locator: 定位方法
        :param text:   步骤名字，在Allure内显示
        """
        self.locator = locator
        try:
            with allure.step(f"点击页面{text}"):
                self.locator.click()
                self.logger.info(f"使用{locator}元素定位方法点击{text},元素路径{locator}")
        except Exception as e:
            self.logger.error(f"进行{text}操作时,元素{locator}未找到")
            raise e

    def input_data(self, locator, data, text):
        """
        封装输入方法
        :param locator: 定位方法 比如 get_by_placeholder("请输入用户名")  get_by_role("button", name="登 录")  这种都可以 百搭
        :param data: 要输入的内容
        :param text: 步骤名字，在Allure内显示, 效果：在[姓名输入框]内输入[张院龙]
        """
        self.locator = locator
        try:
            with allure.step(f"在{text}内输入{data}"):
                self.locator.fill(f"{data}")
                self.logger.info(f"使用{locator}元素定位方法点击{text},输入{data},元素路径是: {locator}")
        except Exception as e:
            self.logger.error(f"进行{text}操作时,元素{locator}未找到")
            raise e

    def cut_out(self, image_name):
        """
        使用playwright截图功能，截取页面并存入缓存
        再通过使用allure获取缓存图片，上传至allure测试报告内
        :param image_name: 图片名称
        """
        allure.attach(self.page.screenshot(timeout=2000), image_name, allure.attachment_type.PNG)

    def path_video(self, name):
        allure.attach(self.page.video.path(), name, attachment_type="WEBM")
