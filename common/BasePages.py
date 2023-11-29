import allure
import logging

import yaml
from jsonpath import jsonpath
from playwright.sync_api import Page
from common.ZenTao_Api import add_bug

"""
封装常用API
"""


class BasePage:
    # 初始化函数，传入参数为Page类型
    def __init__(self, page: Page):
        # 初始化locator为None
        self.locator = None
        # 将传入的page赋值给self.page
        self.page = page
        # 将logging赋值给self.logger
        self.logger = logging

    # 定义go_url函数，用于访问指定url
    def go_url(self, url):
        try:
            with allure.step(f"访问网站:{url}"):
                self.logger.info(f"访问网站: [{url}]")
                self.page.goto(url, wait_until='networkidle', timeout=60000)
        except Exception as e:
            self.cut_out("网站未访问成功截图")
            self.logger.error(f"访问网站: [{url}]时，访问超时,报错内容{e}")
            raise e

    def click(self, locator, text):

        """
         封装点击方法
        :param locator: 定位方法
        :param text:   步骤名字，在Allure内显示
        """
        self.locator = locator
        try:
            with allure.step(f"点击{text}"):
                self.logger.info(f"点击[{text}]")
                self.locator.click()
        except Exception as e:
            # self.cut_out(f"{text}---报错截图")
            # self.page.screenshot(path=f"auto/couout/{text}.png")
            # add_bug(f"Web自动化定位错误-报错操作: [点击] , 报错功能：{text}", "zhangyuanlong", "4", "4", "步骤暂无",
            #         f"auto/couout/{text}.png")
            self.logger.error(f"进行[{text}]操作时,元素未找到,报错内容{e}")
            raise e

    def input_data(self, locator, data, text):
        """
        封装输入方法
        :param locator: 定位方法 比如 get_by_placeholder("请输入用户名")  get_by_role("button", name="登 录")  这种都可以 百搭
        :param data: 要输入的内容
        :param text: 步骤名字，在Allure内显示, 效果：在[姓名输入框]内输入[张院龙]
        """
        # 设置locator
        self.locator = locator
        try:
            # 记录日志
            with allure.step(f"在{text}内输入数据: {data}"):
                self.logger.info(f"在[{text}]内,输入数据: [{data}]")
                # 输入数据
                self.locator.fill(f"{data}")
        except Exception as e:
            # 截图
            self.page.screenshot(path=f"auto/couout/{text}.png")
            # 记录日志
            self.logger.error(f"进行[{text}]操作时,元素未找到,报错内容{e}")
            # 抛出异常
            raise e

    def cut_out(self, image_name):
        """
        使用playwright截图功能，截取页面并存入缓存
        再通过使用allure获取缓存图片，上传至allure测试报告内
        :param image_name: 图片名称
        """
        with allure.step(f"截取{image_name}功能的结果图"):
            allure.attach(self.page.screenshot(timeout=3000), image_name, allure.attachment_type.PNG)

    # 定义一个函数，用于静态等待时间
    def wait_for_timeouts(self, time):
        """
         静态等待时间, 跟time.sleep一样
        :param time: 需要等待的时间  单位: 毫秒
        """
        with allure.step(f"等待{time}毫秒后执行下一步操作"):
            self.logger.info(f"等待[{time}]毫秒后执行下一步操作")
            self.page.wait_for_timeout(time)

    # 定义一个断言结果的函数，用于断言结果是否符合预期
    # 参数：self：表示当前对象；result：表示实际结果；pk：表示断言的方式；expected：表示预期结果；bug_api：表示禅道状态
    def asserts_result(self, result, pk, expected, bug_api="未调用提交接口"):
        """
        断言结果是否符合预期
        :param self: 当前对象
        :param result: 实际结果
        :param pk: 断言的方式
        :param expected: 预期结果
        :param bug_api: 禅道状态
        :return:
        """
        # 读取auto/config.yaml文件中的断言开关
        results = self.read_yaml("auto/config.yaml", "$..asserts_switch")
        # 如果开关为true，则进行断言
        if results == "true":
            # 如果pk为=，则断言结果是否与预期结果一致
            if pk == "=":
                with allure.step("结果验证"):
                    assert result == expected, f"验证失败实际结果与预期结果不符合,预期结果: [{expected}],实际结果: [{result}],禅道状态: {bug_api}"
                    self.logger.info(f"预期结果: [{expected}],实际结果: [{result}]")
            # 如果pk为!=，则断言结果是否与预期结果不一致
            elif pk == "!=":
                with allure.step("结果验证"):
                    assert result != expected, f"验证失败实际结果与预期结果不符合,预期结果: [{expected}],实际结果: [{result}]"
                    self.logger.info(f"预期结果: [{expected}],实际结果: [{result}]")
        # 如果开关为false，则不进行断言
        else:
            self.logger.info("未开启断言功能，不进行断言操作")

    # 定义一个函数，用于获取指定元素的文本内容
    def get_text(self, locator, text):
        # 设置locator
        self.locator = locator
        try:
            # 使用allure.step函数，获取指定元素的文本内容
            with allure.step(f"获取{text}元素文本内容"):
                texts = self.locator.inner_text()
                # 打印获取的文本内容
                self.logger.info(f"获取[{text}]元素文本内容,内容是[{texts}]")
                # 返回获取的文本内容
                return texts
        except Exception as e:
            # 使用allure.step函数，获取指定元素的文本内容失败
            with allure.step(f"获取{text}元素文本内容失败"):
                # 截图
                self.page.screenshot(path=f"auto/couout/{text}.png")
                # 截图
                self.cut_out(f"{text}---报错截图")
                # 打印获取文本内容操作时，元素未找到的报错信息
                self.logger.error(f"获取{text}元素文本内容操作时,元素未找到,报错内容{e}")
                # 返回报错信息
                return "{text}步骤元素未找到"

    # 定义一个函数，用于获取弹窗文本内容
    def get_alert(self, text):

        # 读取auto/config.yaml文件中的get_alert_switch值
        result = self.read_yaml("auto/config.yaml", "$..get_alert_switch")
        # 如果get_alert_switch值为true
        if result == "true":
            try:
                # 获取弹窗文本内容
                with allure.step(f"获取{text}-alert弹窗文本内容"):
                    self.page.get_by_role("alert").wait_for()
                    texts = self.page.get_by_role("alert").first.inner_text()
                    self.logger.info(f"获取{text}-alert弹窗文本内容,内容是[{texts}]")
                    return texts
            except Exception as e:
                # 如果获取弹窗文本内容操作时，元素未找到
                with allure.step(f"获取{text}-alert弹窗文本内容"):
                    self.page.screenshot(path=f"auto/couout/{text}.png")
                    self.cut_out(f"{text}---报错截图")
                    self.page.screenshot(path=f"auto/couout/{text}.png")
                    # 添加错误信息
                    add_bug(f"Web自动化定位错误-报错操作: [弹窗] , 报错功能：{text}", "zhangyuanlong", "4", "4",
                            "步骤暂无",
                            f"auto/couout/{text}.png")
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
        self.wait_for_timeouts(1000)
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

    # 读取yaml文件，并返回json格式数据
    def read_yaml(self, path, json_path="null"):
        # 打开文件
        with open(path, 'r') as f:
            # 读取文件内容
            data = yaml.safe_load(f)
        # 如果json_path为null
        if json_path == "null":
            # 打印读取文件信息
            self.logger.info(f"读取文件名: [{path}] , 返回全部内容: [{data}]")
            # 返回文件内容
            return data
        else:
            # 使用jsonpath读取文件内容
            result = jsonpath(data, json_path)
            # 获取读取的内容
            cleaned_result = result[0]
            # 打印读取文件信息
            self.logger.info(f"读取文件名:[{path}] , 使用jsonpath读取[{json_path}]下的内容: [{cleaned_result}]")
            # 返回读取的内容
            return cleaned_result

    # 定义一个函数chandao，参数为self,text,steps
    def chandao(self, text, steps):
        # 截图，并将图片保存到指定路径
        self.page.screenshot(path=f"auto/couout/{text}.png")
        # 调用add_bug函数，传入参数
        add_bug(text, "zhangyuanlong", "3", "2",
                steps,
                f"auto/couout/{text}.png")

    def login_alert(self):
        try:
            texts = self.page.get_by_role("alert").inner_text(timeout=3000)
            return texts
        except Exception as e:
            print(e)
            return "弹窗内容未找到"
