import allure
# from playwright.async_api import Page
import logging

from playwright.sync_api import Page

"""
封装常用API
"""


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging

    def go_url(self, url):
        with allure.step(f"访问网站:{url}"):
            self.page.goto(url, wait_until='networkidle')
            self.logger.info(f"访问网站:{url}")

    def all_text(self, locator, text):
        return self.page.get_attribute(locator, text)  # 获取元素文本

    def find_element(self, locator, content):
        """
        封装定位元素
        :param locator: 选择定位的方式，如:css  xpath  id text 等
        :param content: 元素路径
        :return: 返回元素内容
        """
        try:
            el = None
            if locator == "locator":
                el = self.page.locator(content)
            elif locator == "get_by_role":
                el = self.page.get_by_role(content)  # 通过显式和隐式可访问性属性进行定位。
            elif locator == "get_by_text":
                el = self.page.get_by_text(content)  # 通过文本内容定位。
            elif locator == "get_by_label":
                el = self.page.get_by_label(content)  # 通过关联标签的文本定位表单控件。
            elif locator == "get_by_placeholder":
                el = self.page.get_by_placeholder(content)  # 按占位符定位输入。
            elif locator == "get_by_alt_text":
                el = self.page.get_by_alt_text(content)  # 通过替代文本定位元素，通常是图像。
            elif locator == "get_by_test_id":
                el = self.page.get_by_test_id(content)  # 根据data-test-id属性定位元素（可以配置其他属性）。
            elif locator == "get_by_title":
                el = self.page.get_by_title(content)  # 通过标题属性定位元素。
            if el is not None:
                return el
            self.logger.info("<{}>,元素<{}>定位成功")
        except Exception as e:
            self.logger.error("<{}>元素<{}>定位失败！")
            raise e

    def click(self, locator, content, text):
        try:
            with allure.step(f"点击页面{text}"):
                self.page.wait_for_load_state("networkidle")
                self.find_element(locator, content).click()
                self.logger.info(f"使用{locator}元素定位方法点击{text},元素路径{content}")
        except Exception as e:
            self.logger.error(f"进行{text}操作时,元素{content}未找到")
            raise e

    def input_data(self, locator, content, data, text):
        try:
            with allure.step(f"在{text}输入{data}"):
                self.page.wait_for_load_state("networkidle")
                self.find_element(locator, content).fill(data)
                self.logger.info(f"使用{locator}元素定位方法点击{text},输入{data},元素路径是: {content}")
        except Exception as e:
            self.logger.error(f"进行{text}操作时,元素{content}未找到")
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

    def pp(self):
        self.page.close()
