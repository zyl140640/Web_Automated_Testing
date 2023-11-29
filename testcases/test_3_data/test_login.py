import allure
import pytest

from common.BasePages import BasePage
from common.tools import login_yaml

yaml = login_yaml("auto/data.json")


@allure.epic("御控工业云平台")
@allure.feature("登录")
class TestMain:

    @pytest.mark.parametrize('args', yaml['rows'])
    def test_mimu_api(self, page, args):
        bs_init = BasePage(page)
        bs_init.logger.info(
            f"------当前企业编码信息: [{args['Code']}], 登录账号信息: [{args['UserNO']}]------")
        if args['Code'] != "":
            bs_init.logger.info("当前企业编码不为空，走当前账号企业登录页面")
            bs_init.logger.info(f"http://192.168.110.210:9016/login?id={args['Code']}")
            bs_init.go_url(f"http://192.168.110.210:9016/login?id={args['Code']}")
            bs_init.input_data(page.get_by_placeholder("请输入用户名"), args['Code'], "输入账号信息")
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
            alert = bs_init.login_alert()
            if alert == "弹窗内容未找到":
                allure.dynamic.title(
                    "测试登录功能是否正常,当前企业编码: {} 当前测试账号: {} 测试结果: 登录成功".format(
                        args['Code'], args['UserNO']))
                page.get_by_text("快速接入平台指引说明").wait_for()
                bs_init.logger.info("当前页面加载完毕,获取到项目式引导框，点击并关闭")
            else:
                bs_init.logger.info("----检测到弹窗资源----")
                bs_init.logger.info(f"----获取弹窗结果: {alert}----")
                allure.dynamic.title(
                    "测试登录功能是否正常,当前企业编码: {} 当前测试账号: {} 测试结果: 登录失败-报错内容:{}".format(
                        args['Code'], args['UserNO'],
                        alert))
                assert alert == "弹窗内容未找到", f"登录失败,失败信息为: {alert}"

        else:
            bs_init.logger.info("当前企业编码为空，走默认登录页面")
            bs_init.go_url("http://192.168.110.210:9016/")
            bs_init.input_data(page.get_by_placeholder("请输入用户名"), args['UserNO'], "输入账号信息")
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
            alert = bs_init.login_alert()
            if alert == "弹窗内容未找到":
                allure.dynamic.title(
                    "测试登录功能是否正常,当前企业编码: {} 当前测试账号: {} 测试结果: 登录成功".format(
                        args['Code'], args['UserNO']))
                page.get_by_text("快速接入平台指引说明").wait_for()
                bs_init.logger.info("当前页面加载完毕,获取到项目式引导框，点击并关闭")
            else:
                bs_init.logger.info("----检测到弹窗资源----")
                bs_init.logger.info(f"----获取弹窗结果: {alert}----")
                allure.dynamic.title(
                    "测试登录功能是否正常,当前企业编码: {} 当前测试账号: {} 测试结果: 登录失败-报错内容:{}".format(
                        args['Code'], args['UserNO'],
                        alert))
                assert alert == "弹窗内容未找到", f"登录失败,失败信息为: {alert}"
