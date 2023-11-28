import allure
import pytest

from common.BasePages import BasePage
from common.tools import login_yaml

yaml = login_yaml("auto/data.json")


@allure.epic("御控工业云平台")
class TestMain:

    @pytest.mark.parametrize('args', yaml['rows'])
    @allure.feature("登录")
    def test_mimu_api(self, page,args):
        bs_init = BasePage(page)
        bs_init.logger.info(
            f"------当前企业编码信息: [{args['Code']}], 登录账号信息: [{args['UserNO']}]------")
        allure.dynamic.title("测试登录功能,当前测试信息: 企业编码信息: [{}], 登录账号信息: [{}]".format(args['Code'],args['UserNO']))
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
            Dialog = page.get_by_text("快速接入平台指引说明").count()
            if Dialog == 1:
                bs_init.logger.info("----存在首页弹窗----")
                page.get_by_label("Close", exact=True).click()
            else:
                bs_init.logger.info("----未存在弹窗直接跳过----")
        else:
            bs_init.logger.info("当前企业编码为空，走默认登录页面")
            bs_init.go_url("http://192.168.110.210:9016/")
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
            Dialog = page.get_by_text("快速接入平台指引说明").count()
            if Dialog == 1:
                bs_init.logger.info("----存在首页弹窗----")
                page.get_by_label("Close", exact=True).click()
            else:
                bs_init.logger.info("----未存在弹窗直接跳过----")


