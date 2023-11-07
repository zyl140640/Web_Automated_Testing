import allure
import logging

import yaml
from jsonpath import jsonpath
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
        try:
            with allure.step(f"访问网站:{url}"):
                self.page.goto(url, timeout=10000)
                self.logger.info(f"访问网站: [{url}]")
        except Exception as e:
            self.cut_out("网站未访问成功截图")
            self.logger.error(f"访问网站: [{url}]时，访问超时,报错内容{e}")
            raise e

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
            with allure.step(f"点击{text}"):
                self.locator.click()
                self.logger.info(f"点击[{text}]")
        except Exception as e:
            self.cut_out(f"{text}---报错截图")
            self.page.screenshot(path=f"auto/couout/{text}.png")
            self.logger.error(f"进行[{text}]操作时,元素未找到,报错内容{e}")
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
            with allure.step(f"在{text}内输入数据: {data}"):
                self.locator.fill(f"{data}")
                self.logger.info(f"在[{text}]内,输入数据: [{data}]")
        except Exception as e:
            self.page.screenshot(path=f"auto/couout/{text}.png")
            self.cut_out(f"{text}---报错截图")
            self.logger.error(f"进行[{text}]操作时,元素未找到,报错内容{e}")
            raise e

    def cut_out(self, image_name):
        """
        使用playwright截图功能，截取页面并存入缓存
        再通过使用allure获取缓存图片，上传至allure测试报告内
        :param image_name: 图片名称
        """
        with allure.step(f"截取{image_name}功能的结果图"):
            allure.attach(self.page.screenshot(timeout=3000), image_name, allure.attachment_type.PNG)

    def path_video(self, name):
        allure.attach(self.page.video.path(), name, attachment_type="WEBM")

    def wait_for_timeouts(self, time):
        """
         静态等待时间, 跟time.sleep一样
        :param time: 需要等待的时间  单位: 毫秒
        """
        with allure.step(f"等待{time}毫秒后执行下一步操作"):
            self.logger.info(f"等待[{time}]毫秒后执行下一步操作")
            self.page.wait_for_timeout(time)

    def asserts_result(self, result, pk, expected, bug_api="未调用提交接口"):
        results = self.read_yaml("auto/config.yaml", "$..asserts_switch")
        if results == "true":
            if pk == "=":
                with allure.step("结果验证"):
                    assert result == expected, f"验证失败实际结果与预期结果不符合,预期结果: [{expected}],实际结果: [{result}],禅道状态: {bug_api}"
                    self.logger.info(f"预期结果: [{expected}],实际结果: [{result}]")
            elif pk == "!=":
                with allure.step("结果验证"):
                    assert result != expected, f"验证失败实际结果与预期结果不符合,预期结果: [{expected}],实际结果: [{result}]"
                    self.logger.info(f"预期结果: [{expected}],实际结果: [{result}]")
        else:
            self.logger.info("未开启断言功能，不进行断言操作")

    def get_text(self, locator, text):
        self.locator = locator
        try:
            with allure.step(f"获取{text}元素文本内容"):
                texts = self.locator.inner_text()
                self.logger.info(f"获取[{text}]元素文本内容,内容是[{texts}]")
                return texts
        except Exception as e:
            with allure.step(f"获取{text}元素文本内容失败"):
                self.page.screenshot(path=f"auto/couout/{text}.png")
                self.cut_out(f"{text}---报错截图")
                self.logger.error(f"获取{text}元素文本内容操作时,元素未找到,报错内容{e}")
                return "{text}步骤元素未找到"

    def get_alert(self, text):

        result = self.read_yaml("auto/config.yaml", "$..get_alert_switch")
        if result == "true":
            try:
                with allure.step(f"获取{text}-alert弹窗文本内容"):
                    texts = self.page.get_by_role("alert").inner_text()
                    self.logger.info(f"获取{text}-alert弹窗文本内容,内容是[{texts}]")
                    return texts
            except Exception as e:
                with allure.step(f"获取{text}-alert弹窗文本内容"):
                    self.page.screenshot(path=f"auto/couout/{text}.png")
                    self.cut_out(f"{text}---报错截图")
                    self.logger.error(f"获取{text}-alert弹窗文本内容操作时,元素未找到,报错内容{e}")
                    return "{text}-弹窗内容未找到"
        else:
            self.logger.info("未开启获取弹窗功能，不进行断言操作")

    def list_row(self, row):
        """
        勾选row的行
        Args:
            row: 列表的行数 1 2 3  序号
        """
        self.click(self.page.get_by_role("row", name=f"{row}", exact=True).locator("label span").nth(1),
                   f"勾选第{row}列")

    def on_response(self, response, url):
        """
        拦截接口信息配置项
        Args:
            response:
            url: 接口地址 可模糊填写
        """
        # if f'{url}' in response.url and response.status == 200:
        if f'{url}' in response.url:
            with allure.step(f"【{url}】接口得到的响应结果为: [{response.json()}]"):
                self.logger.info(f"响应地址: [{response.url}]")
                self.logger.info("method:{}".format(response.request.method))
                self.logger.info(f"响应响应状态码: [{response.status}]")
                self.logger.info("timing:{} 毫秒".format(response.request.timing['responseEnd']))
                self.logger.info(f"响应求头: [{response.headers}]")
                self.logger.info(f"响应请求体: [{response.body}]")

    def interface_requests(self, url):
        """
        拦截接口并返回接口响应，并校验接口是否是200
        Args:
            url:
        """
        with allure.step(f"开始拦截: [{url}]接口信息"):
            self.logger.info(f"开始拦截: [{url}]接口信息")
            self.page.on('response', lambda response: self.on_response(response, url))

    def read_yaml(self, path, json_path="null"):
        """
        # 读取YAML文件

        Args:
            path:
            json_path:

        Returns:

        """
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        # 返回读取到的全部内容
        if json_path == "null":
            self.logger.info(f"读取文件名: [{path}] , 返回全部内容: [{data}]")
            return data
        else:
            result = jsonpath(data, json_path)
            cleaned_result = result[0]
            self.logger.info(f"读取文件名:[{path}] , 使用jsonpath读取[{json_path}]下的内容: [{cleaned_result}]")
            return cleaned_result
