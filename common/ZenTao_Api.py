import requests
import logging

from common.tools import read_yaml_json

# 登录url
login_host = "http://192.168.110.129:81/zentao/index.php?m=user&f=login"
# 新增-BUG-url
add_bug_host = "http://192.168.110.129:81/zentao/index.php?m=bug&f=create&productID=5&branch=0&extra=moduleID=0"
# 提交图片地址
url1 = "http://192.168.110.129:81/zentao/file-ajaxUpload-5a26aca290b59.html?dir=image"


def add_bug(title, assigned_to, severity, pri, steps, image_path):
    """
    请求禅道地址-登录-填写Bug信息-指派-提交
    如使用此方法进行上传图片等附件时    请先使用该方法去存储page.screenshot(path="logs/shouye.png", type="png")
    去保存图片信息
    :param image_path: 附件图片地址
    :param title: Bug标题
    :param assigned_to: Bug指派人
    :param severity:  Bug严重程度
    :param pri:  Bug优先级
    :param steps:  Bug内容(步骤图片等等)
    示例：add_bug("自动化标题", "fangna", "4", "4", "111", "logs/shouye.png")
    """
    result = read_yaml_json("auto/config.yaml", "$..add_bug")
    if result == "true":
        header = {'Content-Type': "application/x-www-form-urlencoded; charset=utf-8"}  # 设置请求头
        datas = {"account": "zhangyuanlong", "password": "zylZYL140640..0"}  # 定义请求的数据
        s = requests.session()  # 实例化一个session对象
        response = s.post(login_host, headers=header, data=datas)  # 使用session发起请求

        print(response.content)

        f = {
            "localUrl": (None, "1.png"),
            "imgFile": ("name.png", open(f"{image_path}", "rb"), "image/png")
        }
        r = s.post(url1, files=f)
        try:
            jpgurl = "http://192.168.110.129:81/" + r.json()["url"]
            print(u"上传图片后的url地址：%s" % jpgurl)
        except Exception as msg:
            print(u"返回值不是json格式：%s" % str(msg))
            print(r.content)
        data = {
            "product": "5",  # int 所属产品 * 必填
            "openedBuild": "trunk",  # int | trunk 影响版本 * 必填
            "branch": "2",  # int 分支 / 平台
            "module": "31",  # int 所属模块
            "project": "17",  # int 所属项目
            "assignedTo": f"{assigned_to}",  # string 指派给
            "deadline": "2020-07-28",  # date 截止日期 日期格式：YY - mm - dd，如：2019 - 01 - 01
            # Bug类型(codeerror 代码错误 | config 配置相关 | install 安装部署 | security 安全相关 | performance 性能问题 |
            # standard 标准规范 | automation |测试脚本 | designdefect 设计缺陷 | others 其他)
            "type": "codeerror",
            "severity": f"{severity}",  # int 严重程度 取值范围：1 | 2 | 3 | 4
            "pri": f"{pri}",  # int 优先级 取值范围：0 | 1 | 2 | 3 | 4
            "keywords": "",  # string 关键词
            "title": f"{title}",  # 标题
            "story": "",  # 需求
            "steps": "<p>[步骤]{} </p><p>[结果]<p><img src='{}' /></p></p><p>[期望]</p>".format(steps, r.json()["url"])
            # string 重现步骤
        }

        responses = s.post(add_bug_host, data=data)
        print(responses.content.decode("utf-8"))
        logging.info(f"读取配置文件结果: {result} ,报错时触发禅道提交Bug功能")
        return "提交成功"
    else:
        logging.info(f"读取配置文件结果: {result} ,报错时不触发禅道提交Bug功能")
        print("不执行")
        return "未开启禅道提交BUG配置项"


if __name__ == '__main__':
    add_bug("自动化标题", "zhangyuanlong", "4", "4", "你好呀步骤", "Allure.png")
